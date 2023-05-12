from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Brand, Reviews


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        # create tuple list of friendly namea
        friendly_names_categories = [
            (c.id, c.get_friendly_name()) for c in categories]
        friendly_names_brands = [(b.id, b.get_friendly_name()) for b in brands]

        # set each fields name as friendly name
        self.fields['category'].choices = friendly_names_categories
        self.fields['brand'].choices = friendly_names_brands
        # add class to each field name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'review']
