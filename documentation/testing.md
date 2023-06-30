
# Manual Testing

This table shows all the manual testing done for the website, and whether it worked as expected or not.

## Features

### General

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
NavBar responsiveness | NavBar becomes logo menu on page resize | As expected | Pass
Images resize on mobile | Images resize on mobile | As expected | Pass
Layout becomes linear on mobile | Layout becomes linear on mobile | As expected | Pass
Buttons change colour on hover | Buttons change colour on hover | As expected | Pass
Messages are displayed for user feedback | All messages shown as expected | As expected | Pass
Page title changes for each product page | Page title changes for each product page | As expected | Pass
Footer links all work when clicked | Footer links all work when clicked | As expected | Pass
Button on home page links to featured product | Button links to Ezio Statue | As expected | Pass
Contact form renders on Contact page | contact.html renders | As expected | Pass
Contact form saves to admin panel | admin panel shows message, name and email | As expected | Pass
User gets feedback on contact form submission | Message "Your message was sent! We'll be in touch shortly." shows | As expected | Pass
Wishlist link is hidden until a user is logged in | Only show when logged in | As expected | Pass
Each Category dropdown links to the correct category page | Categories are sorted as expected | As expected | Pass
Each Brand dropdown links to the correct brand page | Brands are sorted as expected | As expected | Pass
Each Product dropdown links to the correct sorting page | Products are sorted as expected | As expected | Pass
Selector box works as expected | Selector box sorts | As expected | Pass
Sale link only shows products on sale | Products marked as on sale are shown | As expected | Pass
Clicking a product renders the correct product page | product-detail page with the correct Product ID renders | As expected | Pass
Clicking add to wishlist as logged in user | message "-product name- has been added to your wishlist" | As expected | Pass
Clicking add to wishlist as logged in user | Product viewable in wishlist page | As expected | Pass
Viewing Wishlist link as logged in user | Site redirects to Wishlist page | As expected | Pass
Clicking View icon on Wishlist page | Site redirects to product details page | As expected | Pass
Clicking Remove icon on Wishlist page | Message "-product- has been removed from your Wishlist!" | As expected | Pass
Clicking Wishlist icon on Product Detail page a 2nd time | Message "-product- has been removed from your Wishlist!" | As expected | Pass
Clicking Review This Product as logged in user | Review form opens | As expected | Pass
Submitting a review as logged in user | Message "Your review has been successfully added!" | As expected | Pass
Updating a review as logged in user | Review Update form opens | As expected | Pass
Deleting a review as logged in user | Delete review confirmation page opens | As expected | Pass
Review page when not logged in user | Message "Please Register or Login to leave a review." | As expected | Pass
My Profile link renders Profile page | profile.html is shown | As expected | Pass
User information is displayed on Profile page | Name and Address fields shown | As expected | Pass
Update Address button saves updated form | Message "Profile updated successfully" shown | As expected | Pass
User order history shown on Profile Orders tab | Orders tab shows all past orders | As expected | Pass
Delete Account tab opens account delete message | message "Warning! Account deletion is permanent. Proceed?" shown | As expected | Pass
Delete Account button opens account delete confirmation page | user-delete with user id in url shown | As expected | Pass
Return button on user_delete page redirects back to profile | profile.html renders | As expected | Pass
Confirm button on user_delete page redirects back to index.html | index.html renders | As expected | Pass
Confirmation message on user_delete shows | message "Profile successfully deleted" shown | As expected | Pass
All of a users orders are deleted on profile deletion | orders removed from database | As expected | Pass
Add Product redirects to add_product.html form | add_product.html form renders | As expected | Pass
Edit Product redirects to update form | edit_product form renders | As expected | Pass
Delete Product link renders delete confirmation modal | Modal renders | As expected | Pass
Delete Product cancel button closes Modal | Modal is closed | As expected | Pass
Delete Product delete button redirects to Products page | products.html renders | As expected | Pass
Product deleted from database on confirmation | Product deleted | As expected | Pass
User redirected to logout confirmation when Logout is clicked | account/logout.html renders | As expected | Pass
User redirected when Profile Logout is cancelled | index.html renders | As expected | Pass
User redirected to Index page when logged out | index.html renders | As expected | Pass
User shown log out message feedback | message "You have signed out." shown | As expected | Pass

<br>

### Checkout

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Add to cart button shows success message | Success message and product image shown | As expected | Pass
Cart button redirects to cart | cart.html renders | As expected | Pass
Product details shown in cart | Products render in cart as table | As expected | Pass
Sale price of product shown in cart | Products on sale show their sale price | As expected | Pass
Update quantity button updates subtotal | Subtotal calculated correctly | As expected | Pass
Delete product button deletes product | Cart is updated without that product | As expected | Pass
Secure Checkout button shows checkout page | checkout.html renders | As expected | Pass
User information is prepoulated if saved in profile | Fields are automatically filled | As expected | Pass
Coupon code field renders | Coupon form is shown | As expected | Pass
Correct coupon is entered | Sucess popup message "Coupon code: -code- applied" | As expected | Pass
Correct coupon is entered | Text "Applied coupon -code- for -amount-% off!" | As expected | Pass
Correct coupon is entered | Discount applied to Grand Total | As expected | Pass
Remove coupon link clicked | Discount removed from Grand Total | As expected | Pass
Stripe validation works on incorrect/incomplete card number | Stripe validation error shown | As expected | Pass
Successful checkout | Checkout loading overlay shown | As expected | Pass
Successful checkout | Checkout Success page shown | As expected | Pass
Successful checkout | Confirmation email sent | As expected | Pass
Checkout other products button clicked | Products page shown | As expected | Pass

<br>

## Errors

Error Tested | Expected Result | Actual Result | Pass/Fail
-------------|-----------------|---------------|----------
Registration page validates each input for empty or whitespaces | message "Please fill in this field is shown" | As expected | Pass
Registration page validates email address | message "A user is already registered with this e-mail address." | As expected | Pass
Registration page validates username | message "A user with that username already exists." | As expected | Pass
Clicking add to wishlist as not logged in user | message "Sorry you need be logged in to add to your wishlist" | As expected | Pass
Clicking add to wishlist as not logged in user | Site redirects to login page | As expected | Pass
Submitting an empty review as logged in user | Message "Your review has not been submitted" | As expected | Pass
Add Product form has validation | Product won't add without title, price, SKU | As expected | Pass
Contact form validates for whitespaces | message "Please fill in this field" shows | As expected | Pass
Item Quantity can't be less than 1 or more than 99 | Buttons disabled on 1 and 99 | As expected | Pass
Incorrect coupon is entered | Message "Sorry, -code- is not a valid code" | As expected | Pass
User tried to render profile URL when not logged in | user redirected to log in page | As expected | Pass
User tried to render wishlist URL when not logged in | user redirected to log in page | As expected | Pass
User tried to render delete_profile URL when not logged in | user redirected to login page | As expected | Pass
User tried to render profile URL for another user | user redirected to 403 page | As expected | Pass
User tried to render delete_profile URL for another user | user redirected to 403 page | As expected | Pass