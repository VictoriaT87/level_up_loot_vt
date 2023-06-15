from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import View, UpdateView, DetailView, DeleteView
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        # used in toast template
        "on_profile_page": True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        # used in toast template
        "from_profile": True,
    }

    return render(request, template, context)


class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes the currently signed-in user and all associated data.
    """

    model = UserProfile
    template_name = "profiles/profile_delete.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, request, *args, **kwargs):
        """
        Delete Profile for logged in user
        """
        user = self.get_object().user
        user.delete()
        messages.success(self.request, "Profile successfully deleted")
        return HttpResponseRedirect(self.success_url)
