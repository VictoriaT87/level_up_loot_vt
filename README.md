# LevelUp! Loot

![Website responsiveness on multiple screen sizes](documentation/images/responsiveness.png)

Welcome to LevelUp! Loot. This website was built using Django, with custom Python, HTML and CSS for Code Institute P5 E-commerce Applications. This website is a B2C e-commerce application that allows users to purchase premium and exclusive collectible figures from across the realm of Pop Culture - including gaming, anime, TV show and movies.

The site has some features available exclusively to registered users, including viewing their order history, saving items to a wishlist and add product reviews.

Users have the ability to search products and view product details, add products to a cart and checkout. There is also a contact page for queries, a privacy policy and a page of FAQs.

[Live link to LevelUp! Loot](https://levelup-loot-vt.herokuapp.com/)


<br>

# Table of Contents

1. [UX](#ux)
  
2. [The Strategy Plane](#the-strategy-plane)
    * [Targeted Users](#targeted-users)
    * [Site Goals](#site-goals)
    * [Project Goals](#project-goals)
3. [Agile Planning](#agile-planning)
    * [User Stories](#user-stories)
    * [Epic Breakdowns](#epic-breakdowns)
4. [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
5. [The Scope Plane](#the-scope-plane)
6. [The Structure Plane](#the-structure-plane)
    * [Features](#features)
    * [Home Page](#home-page)
      * [Wellness Section](#wellness-section)
      * [Benefits Section](#benefits-section)
      * [Instructors Section](#instructors-section)
    * [About Page](#about-page)
    * [Contact Page](#contact-page)
    * [Pages Restricted to Login](#restricted-pages)
      * [Booking](#booking-page)
      * [My Profile](#profile-page)
      * [Register](#register-page)
      * [Log Out](#log-out-page)
      * [Admin Page](#admin-page)
    * [Future Features](#future-features)
7. [The Surface Plane](#the-surface-plane)
    * [Design](#design)
      * [Colour Scheme](#colour-scheme)
      * [Typography](#typography)
      * [Images](#images)
8. [Technologies](#technologies)
    * [Languages Used](#languages-used)
    * [Libraries And Frameworks](#libraries-and-frameworks)
    * [Tools and Resources](#tools-and-resources)
9. [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Other Testing](#other-testing)
10. [Bugs Found and Fixed](#bugs-found-and-fixed)
    * [Bugs Not Fixed](#bugs-not-fixed)
11. [Credits And Sources](#credits-and-sources)
12. [Deployment](#deployment)
13. [Acknowledgements](#acknowledgements)

<br>

# UX

## The Strategy Plane

### Targeted Users

- A user that wants to view and buy collectible statues.
- A user that wants to see the latest statues released from major brands.
- A user that is interested in all things Pop Culture.

### Site Goals

- For users to be able to search products quickly and easily.
- For users to be able to purchase products quickly and easily.
- For users to be able to create an account to store their Wishlist and see their order history.
- For users to be able to edit their saved address for easier purchasing.
- For users to be able to contact the business online.

### Project Goals

- Create a fully working e-commerce application that would look and feel like a professionally designed online store. Taking all of my knowledge from the 4 projects before, I wasnted this website to be as comprehensive and complete as I could possibly make it.
- In my previous projects, I had yet to write anything like a wishlist or user reviews so these were something I wanted to incorporate to further expand my knowledge of CRUD functionality.

<br>

[Back to Top](#table-of-contents)

<br>

## **Agile Planning**

My Project was developed with agile planning. This meant that each individual feature was split first into User Stories for what the user of the website would expect. Each User Story was thought about and planned out, which allowed me to create multiple tasks which would be developed to implement certain features and these Tasks were then grouped together into Epics.

Everything was labeled as Must Have, Should Have, Could Have and Won't Have to help prioritise which were most important to implement.

As the main priority of the website, the products section was started first and given the most time for completion. After that, as the project evolved, some more tasks were added or updated, based on the changing needs of a User within the website.

The Project board can be found [here](https://github.com/users/VictoriaT87/projects/6/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D).


![Project Kanban](documentation/images/project-board.png)

[Back to Top](#table-of-contents)

<br>

## User Stories

* Users will:

  * Have the ability to view and purchase products quickly and easily.
  * Be able to use the website across all devices with responsive design.
  * Be able to create an account, update their profile information, leave reviews and create a wishlist.

* Users expect:

  * An easy to use e-commerce store, with purchasing of products going smoothly.
  * A website that looks well across all devices.
  * A website that works well, with minimum errors encountered.

<br>

[Back to Top](#table-of-contents)

<br>

## Epic Breakdowns
## **Epic 1: [Initial Install](https://github.com/VictoriaT87/level_up_loot_vt/issues/1)**
> Create the base Django application on which to build the project.

Broken down into these tasks:
- **Task: [Install Libraries and Frameworks](https://github.com/VictoriaT87/level_up_loot_vt/issues/10)**
>Install: Django, gunicorn, dj-database, psycopg2
- **Task: [Hide sensitive information](https://github.com/VictoriaT87/level_up_loot_vt/issues/11)**
> Hide sensitive information by creating an env.py file
- **Task: [Create Products app](https://github.com/VictoriaT87/level_up_loot_vt/issues/12)**
>  Create a products app to install the fixtures file
- **Task: [Create Fixtures File](https://github.com/VictoriaT87/level_up_loot_vt/issues/46)**
>  Create custom fixtures file for adding products

This Epic was the inital install of Django, gunicorn, dj-database and psycopg2 and the Products app. The custom fixtures file needed to add products into the store was then installed into this app. This was the base platform on which the entire website would be built.

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 2: [Initial Deployment](https://github.com/VictoriaT87/level_up_loot_vt/issues/2)**
> First deployment to the Heroku app once basic framework for the project is in place

Broken down into these tasks:
- **Task: [Heroku Deployment](https://github.com/VictoriaT87/level_up_loot_vt/issues/13)**
> Create App in Heroku, Create Config Var files, Deploy from main branch
- **Task: [ElephantSQL Set up](https://github.com/VictoriaT87/level_up_loot_vt/issues/14)**
>  Create Database URL in Elephant SQL, Add the Database URL to env.py and Heroku Config Vars

This Epic was for the inital deployment of the website to Heroku. This was undertaken as soon as the base packages, App and env.py file was set up and working correctly. Config Var files were created on Heroku for any sensitive information contained in the env.py file, as well as Port access needed.

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 3: [Databases](https://github.com/VictoriaT87/level_up_loot_vt/issues/3)**
> Create database models in project app and migrate them

Broken down into the following task:
- **Task: [Create and Migrate Database](https://github.com/VictoriaT87/level_up_loot_vt/issues/15)**
> Create and Migrate Database of products


The initial database was created for the products app and the installed products from the fixtures file. The database is hosted on ElephantSQL, so a project was started there to host it.

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 4: [Admin Panel](https://github.com/VictoriaT87/level_up_loot_vt/issues/4)**
> Add an admin panel to the project app to allow the admin to manage products

This was from the User Story:
#### **User Story: [Admin Panel](https://github.com/VictoriaT87/level_up_loot_vt/issues/16)**
> As a Site Admin I can use an admin panel so that I can create, update, manage and delete products and orders


The Admin panel allows the site admin to manage products - add, delete, update, set them to be on sale with discount prices or have them featured on the homepage. The admin panel also stores all contact form submissions and user profiles. All information for these can be seen, updated and removed from the database through the admin panel. Each App's admin.py file was also given some sort of display or search parameter, to make it easier for the site admin to find and sort information on the backend. 

[Back to Top](#table-of-contents)

<br>

---


## **Epic 5: [User Profiles](https://github.com/VictoriaT87/level_up_loot_vt/issues/5)**
> Allow Users to create/update/manage and delete user profiles

This was from the User Story:
#### **User Story: [Create a Profile](https://github.com/VictoriaT87/level_up_loot_vt/issues/17)**
> As a Site User I can create an account so that I can save my information for easier repeat purchases and to view my order history

Which was down broken down into these tasks:
- **Task: [Create Account](https://github.com/VictoriaT87/level_up_loot_vt/issues/18)**
> As a Site User I can create an account so that I can save my information for easier repeat purchases and to view my order history
- **Task: [Update Account](https://github.com/VictoriaT87/level_up_loot_vt/issues/19)**
> Allow a user to update all their profile information within their account and update database accordingly
- **Task: [Delete Account](https://github.com/VictoriaT87/level_up_loot_vt/issues/20)**
> Allow a user to delete their account, add authorisation so this isn't done by accident

<br>

This User Story was implemented with the use of the AllAuth package, as well as a Profile Model, Form and Template. The information the user enters in this is stored in the Admin panel, for SuperUsers/Staff to see and manage. Each User is assigned a User ID which allows for orders to be assigned properly to each individual. Users can edit their profiles and delete them and this is all reflected in the database.

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 6: [Adding Products to Cart](https://github.com/VictoriaT87/level_up_loot_vt/issues/6)**

> Create an app to allow users to view products and add them to a cart


This was from these User Stories:
#### **User Story: [View Products](https://github.com/VictoriaT87/level_up_loot_vt/issues/37)**
> As a user I can view products so that I can decide which items I want to purchase

#### **User Story: [Search Products](https://github.com/VictoriaT87/level_up_loot_vt/issues/38)**
> As a user I can search all products and view categories so that I can see only the products I'm interested in

#### **User Story: [View Product Details](https://github.com/VictoriaT87/level_up_loot_vt/issues/39)**
> As a user I can view individual product details so that I can identify the price, description, rating, image and price.

#### **User Story: [Identify Deals](https://github.com/VictoriaT87/level_up_loot_vt/issues/40)**
> As a user I can easily view deals and sales so that I can take advantage of savings on products I want to purchase

Which was down broken down into these tasks:
- **Task: [Create Products app](https://github.com/VictoriaT87/level_up_loot_vt/issues/12)**
>  Create a products app to install the fixtures file
- **Task: [Manage Products](https://github.com/VictoriaT87/level_up_loot_vt/issues/23)**
> Allow admins/superusers to add products to the store through the frontend or admin panel
- **Task: [Add/View Products](https://github.com/VictoriaT87/level_up_loot_vt/issues/24)**
> Create a Product app which will show all available products, with prices and ratings.
- **Task: [Update/Delete Products](https://github.com/VictoriaT87/level_up_loot_vt/issues/25)**
> Allow Site Admins to update and delete products available on the site
- **Task: [Add Sale Feature](https://github.com/VictoriaT87/level_up_loot_vt/issues/47)**
> Add the ability for an admin/superuser to add products to a sale list, with calculated discount, for users to view

These User Stories are the basis of the website. This adds the product app which allows Admins/Superusers to add products to the store, update or delete them, and publish them for Site Users to view. It also adds the Sale section which will allow Users to quickly view products that are on sale, which will entice more sales for discount prices. All products can be managed on both the frontend and the admin section, with everything reflected in the database.

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 7: [Purchasing Items](https://github.com/VictoriaT87/level_up_loot_vt/issues/7)**

> Allow users to purchase items in their cart

This was from these User Stories:
#### **User Story: [View Total Spending](https://github.com/VictoriaT87/level_up_loot_vt/issues/41)**
As a user I can easily see how much my total purchase will be so that I can avoid spending too much

#### **User Story: [View Items in Cart](https://github.com/VictoriaT87/level_up_loot_vt/issues/43)**
As a user I can view items in my bag to be purchased so that I can identify the total cost of my purchase and all the items I will receive

#### **User Story: [Safe and Secure Payment](https://github.com/VictoriaT87/level_up_loot_vt/issues/42)**
As a user I can feel that my payment is safe and secure so that I can confidently provide the needed information to make a purchase

Which was down broken down into these tasks:
- **Task: [Create Cart App](https://github.com/VictoriaT87/level_up_loot_vt/issues/48)**
> Create a cart app which will allow site users to view their cart, update it as they wish and see their current subtotal
- **Task: [Set up Stripe Payments](https://github.com/VictoriaT87/level_up_loot_vt/issues/49)**
> Set up webhooks to connect and allow Stripe payments on the website

This Epic was the breakdown of User Stories that will allow Site Users to add products to a cart, view the subtotals and checkout securely. Stripe was used for the Webhooks to handle payments. 

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 8: [Front End Design](https://github.com/VictoriaT87/level_up_loot_vt/issues/8)**

>Create templates, a colour scheme, navigation and responsiveness for the website

This was from the User Story:
#### **User Story: [Responsive Design](https://github.com/VictoriaT87/level_up_loot_vt/issues/21)**
> As a Site User I expect responsive elements so that I can view the website across multiple devices

Which was down broken down into these tasks:
- **Task: [Create Templates](https://github.com/VictoriaT87/level_up_loot_vt/issues/26)**
> Create templates for each page needed within the site, including the home page, a booking page, a login/create account page and pages for further information.
- **Task: [UI Design](https://github.com/VictoriaT87/level_up_loot_vt/issues/27)**
> Design a website fitting of the theme with appropriate colours, easy to navigate, easily accessible information and has full screen reader capabilities.

One of the most important parts of a website, the look and layout bring out emotions in the user. The website needs to be easy to navigate, while not feeling too cluttered with the many options for products to buy. The responsiveness of the website has been extensively tested, as documented in the testing section.

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 9: [Error Pages](https://github.com/VictoriaT87/level_up_loot_vt/issues/9)**

> Create custom error page templates for 404, 403 and 500 errors.

This was from the User Story:
#### **User Story: [Error Pages](https://github.com/VictoriaT87/level_up_loot_vt/issues/50)**
> As a user I can see custom error pages so that I can see exactly what my issue was and report it to the site admin if needed

Which was down broken down into these tasks:
- **Task: [404 Error Page](https://github.com/VictoriaT87/level_up_loot_vt/issues/29)**
> Add a custom 404 Page to show the user which error they encountered while keeping the base template and css of the website.
- **Task: [403 Error Page](https://github.com/VictoriaT87/level_up_loot_vt/issues/30)**
> Add a custom 403 Page to show the user which error they encountered while keeping the base template and css of the website.
- **Task: [500 Error Page](https://github.com/VictoriaT87/level_up_loot_vt/issues/31)**
> Add a custom 500 Page to show the user which error they encountered while keeping the base template and css of the website.

Creating custom error page templates makes the website feel more fleshed out. Before their implementation, they were provided as a basic white page with black text. Hopefully the user never sees these pages but in the event that they do, it's important that the page still looks individual to the website.

[Back to Top](#table-of-contents)

<br>

---

<br>

## **Epic 10: [Create Documentation](https://github.com/VictoriaT87/level_up_loot_vt/issues/51)**

>Create both a README.md file and a Testing.md file to show the process of creating the project

Which was down broken down into these tasks:
- **Task: [Create README.md](https://github.com/VictoriaT87/level_up_loot_vt/issues/34)**
> Create an app inside the Django project to allow users to book a yoga session
- **Task: [Create Testing.md](https://github.com/VictoriaT87/level_up_loot_vt/issues/35)**
> Create a full Testing.md document with all necessary information on how the project was manually/automatically tested.

Document everything needed for the process of developing and testing the website.

[Back to Top](#table-of-contents)

<br>

---

#### **Others**
- **Task: [Testing](https://github.com/VictoriaT87/level_up_loot_vt/issues/52)**
> Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies

Automatic tests were written using TestCase from Django, as well as manual testing of code and resposivness. Covered in the Testing section.

- **Task: [Allow Email and Password Changing](https://github.com/VictoriaT87/level_up_loot_vt/issues/28)**
> Allow the User to reset both their passwords and their email addresses if they've forgotten either.

This is all handled through the AllAuth authentication system. Users who have forgotten their password have the option to have it emailed to them.

- **User Story: [Wishlists](https://github.com/VictoriaT87/level_up_loot_vt/issues/44)**
> As a user I can add products to a wishlist so that I can easily see which items I would like to buy eventually
- **Task: [Wishlist](https://github.com/VictoriaT87/level_up_loot_vt/issues/45)**
> Add an app with views/models/URLs to allow users to store a wishlist of products

These 2 tasks were added on later in the planning when I realised that the majority of e-commerce stores have some sort of wishlist/favourites section and as a user of those sites myself, I find this function very useful. Instead of having to return to the "All Products" section to find a certain product, allowing users to store their favourites in one place will make it more likely for them to return to purchase these items quickly.

<br>

[Back to Top](#table-of-contents)

<br>

## Skeleton Plane

### Wireframes

- My starting point for this project was to decide on a layout using a wireframe. I went for a Hero Image for the front page, to quickly show the user what the business was about at first view. The products page each has a card, showing all details quickly so users can easily see the product, the price and a quick description.

<img src="documentation/images/index-wireframe.png" alt="front page wireframe" width="600"/>

<br>

<img src="documentation/images/products-wireframe.png" alt="products wireframe" width="600"/>

<br>

### Database Schema

- Both the AllAuth User and the Products Database are the main ones in the schema, connecting all products and profiles.
- The Products Database allows for a connection to the Checkout Databases, including the orders, order items and coupons.
- The Products Database also allows us to create a Wishlist for users. This is a ManyToMany database, which allows us to have 1 user wishlist as many products as they want.
- The Profile Database is separate from the User, so that users to the site don't need to have created an account to make an order but if they do, they can save their profile information for quicker checkout next time. 
- The Review Database is connected to the Profile Database - this means that registered users can leave a review for a product, as well as update and delete those reviews.
- The Contact Database is used purely for creating and storing Contact Form submissions on the admin panel for staff to view.

![Database Schema](documentation/images/database.png)

[Back to Top](#table-of-contents)

<br>

## The Scope Plane
- Home page with hero image that immediately tells the user what the site is for.
- Account registration which will allow for restricted viewing on Editing and Deleting reviews, wishlists and saving their information for quicker checkout next time.
- Fully responsive website, tested across all screen sizes, with navigation for mobile.
- Ability to create, view, update and delete reviews for users and products for superusers.

<br>

[Back to Top](#table-of-contents)

<br>

## The Structure Plane

# Features 

## Existing Features

### Home Page
![Hero Image](documentation/images/hero.png)
- The home page features a hero image, with some text that show a product for sale. This lets the user know immediately what type of items are available.
- The index page is split into multiple sections, with the information easy to read and eye catching to a visitor.
- There is a button that links to the product details page.

![Hero Mobile Image](documentation/images/hero-mobile.png)

<br>

[Back to Top](#table-of-contents)

<br>

### Brands Section
![Brand Section Image](documentation/images/brands.png)
- The Brands section is a section of images which links to a search for each brand name.
- There is a hover effect on each image for larger screen sizes, which shows text with the name of each Brand. On mobile, this hover effect is the default.

![Brand Mobile Image](documentation/images/brand-mobile.png)

<br>

[Back to Top](#table-of-contents)

<br>

### Categories Section
![Categories Section Image](documentation/images/categories.png)
- The categories section is used to add more colour to the page. Each panel links to a search of categories. On mobile this section is condensed to a vertical view.

![Categories Mobile Image](documentation/images/categories-mobile.png)

<br>

### Featured Products Section
![Featured Products Section Image](documentation/images/featured.png)
- The Featured Products section will take a random list of 5 products that have been marked as "Is_Featured" on the admin panel.
- Each product has a card with it's details, price and if it's also on sale.

<br>

[Back to Top](#table-of-contents)

<br>

### Why Shop With Us Section
![Featured Products Section Image](documentation/images/why-shop.png)
- The "Why Shop With Us" section gives users a quick summary of reasons to shop with this store.
- There are icons and a single line of text giving 3 quick reasons why a user would want to shop online - quick shipping, weekly rotation of products and no import fees are reasons why users would want to shop with an online store and also come back to shop again.

<br>

[Back to Top](#table-of-contents)

### Footer
![Footer Image](documentation/images/footer.png)
- The footer is used across all pages, with links to Contact, FAQs, Privacy Policies and an email address.
- The footer also has our newsletter signup, generated through MailChimp. This makes it available across every page to maximise the chance of someone signing up.

<br>

[Back to Top](#table-of-contents)

<br>

### FAQs Page
![FAQs Page Image](documentation/images/faqs.png)
- The FAQs page gives the user information about shipping, cancellations, order modifications and payment options.
- There is a link system at the top of the page to allow users to quickly get to the section they need.

<br>

[Back to Top](#table-of-contents)

<br>

### Contact Page
![Contact Page Image](documentation/images/contact.png)
- The contact page features small icons with quick and easy to read information with a phone number, address and email.
- The page also hold a form for users to get in contact with the business. This form stores the posted information in the Admin panel, for staff to read easily.

<br>

[Back to Top](#table-of-contents)

<br>

### Restricted Pages
![Logged in Nav Image](documentation/images/logged-in-nav.png)
![Logged out Nav Image](documentation/images/logged-out-nav.png)
- Some pages are restricted to logged in users only. Links to these pages are only show in the Navbar when a user logged in.
- The Wishlist is exclusively for users who register an account.

<br>

[Back to Top](#table-of-contents)

<br>

### Products Page
![Products Page Image](documentation/images/booking-page.png)
- The Products Page lists all products initially.
- This can be changed by choosing a category or a brand from the drop down navbar menu or by using the Selector Box to sort items.
- Each individual product has a card with all details listed (rating, price, brand, category) and each card also has a hover effect.
- Clicking on the "View Product" button will bring the user to the product detail page for that item.

<br>

[Back to Top](#table-of-contents)

<br>

### Product Details Page
![Product Detail Image](documentation/images/product-detail.png)
- The product detail page shows a larger product image, a description for the product, as well as allowing the user to add this product to their cart for the amount they want.
- The page also shows user left reviews, with the option for logged in users to leave their own.
- Reviews are able to be updated or deleted by the User who left them or by admin/superusers. This is all CRUD functionality.

![Review Image](documentation/images/reviews.png)
![Review Image](documentation/images/update-review.png)
![Review Image](documentation/images/delete-review.png)

<br>

[Back to Top](#table-of-contents)

<br>

### Wishlist Page
![Wishlist Image](documentation/images/wishlist.png)
- The Wishlist page allows users to have a list of all the products they have added to their Wishlist, by clicking the heart icon on each product.
- On the Wishlist page, there is ashort summary of the product, as well as a link to the product detail page, which allows users to add it to their cart.
- The page also has a remove option, which allows users to remove product from their Wishlist - again this is done through CRUD functionality.

<br>

[Back to Top](#table-of-contents)

<br>

### Profile Page
![Profile Image](documentation/images/account-dashboard.png)
- The Account Profile page has a tabbed dashboard which allows users to update their information - name and shipping address - which can be used for a quicker checkout process.
- This Profile page also shows the users Order History, which allows them to see the summary of all past purchases.
- On this dashboard, the user also has the option to delete their profile. This deletes all associated order histories and information. There is a separate page for deletion confirmation.

![Order History Image](documentation/images/account-orders.png)
![Delete Profile Image](documentation/images/account-delete.png)
![Delete Profile Image](documentation/images/profile-delete.png)

<br>

[Back to Top](#table-of-contents)

<br>

### Admin Page
![Admin Dashboard Image](documentation/images/admin-dashboard.png)
- The admin dashboard is restricted to Super Users and anyone the Super User designates as staff. The dashboard is populated with the information from the Models in each app.
- There is a section for products, wishlists, users, contact form submissions and orders.
![Admin Products Image](documentation/images/admin-products.png)
- The Products section of the admin, allows for adding, removing and updating all products.
- There are also checkboxes to allow admins to update products as on_sale (with a default 10% off) and to be featured on the home page.
![Admin Contact Image](documentation/images/admin-contact.png)
- The Contact form submissions are saved to the admin panel. The name, email and message from the contact form is shown to the admin, to allow them to reply to the User easily.

[Back to Top](#table-of-contents)

<br>

## Future Features

- There are a few features I would like to add to the website, given more time. Currently the product ratings are just random numbers entered when the product is being added (initally with a fixtures file) but I would like for users to also be able to add a product rating too which is caluclated as an average. 
- The coupons currently can be added any number of times - there is no limit for one use per customer. I trid to implemenet that to no sucess. More information about it can be found in the [Bugs Section](#bugs-not-fixed)

<br>

[Back to Top](#table-of-contents)


## The Surface Plane
## Design
### Colour Scheme
 -  The colour scheme was designed so that while it stands out as a bright interface, the colours also don't distract from the product images, as these are the main point of the website.
 - For this I chose a blue to stand out on the white background - they compliment each other well enough without one being overly distracting from the other.

![Color Scheme](documentation/images/colours.png)

### Typography
 -   The font chosen for the website is a font called Fjalla One. This was picked because it is very easy to read with a medium contrast but it also has a somewhat fantasy feel to it, in fitting with the expected user base of people who like Pop Culture. I wanted the typography to compliment the website, not overpower what it was saying. The font was found on [Google Font](https://fonts.google.com/specimen/Fjalla+One) and imported to the website with a CSS import.

### Images
- All product images were taken from their respective brands websites, as well as some from [Gamestop](https://www.gamestop.com/).

<br>

[Back to Top](#table-of-contents)

<br>

# Technologies

## Languages Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks Used

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://blog.getbootstrap.com/) 

## Libraries And Installed Packages

* [coverage](https://pypi.org/project/django-coverage/) - Used for running automated tests.
* [pytest](https://docs.pytest.org/en/7.2.x/) - Used for running automated tests.
* [pytest-cov](https://pypi.org/project/pytest-cov/) - Used for running automated tests.
* [crispy-bootstrap4](https://pypi.org/project/crispy-bootstrap4/) - Template pack used for django-crispy-forms
* [django-crispy-forms](https://pypi.org/project/crispy-bootstrap4/) - Used to render forms throughout the project.
* [dj-database-url](https://pypi.org/project/dj-database-url/) - A package used to utilize DATABASE_URL environment variable.
* [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Facilitates integration with Cloudinary by implementing Django Storage API.  
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - Allows authentication, registration and account management in Django.
* [django-countries, v7.2.1](https://pypi.org/project/django-countries/7.2.1/) - Django application used to provide country choices for use with forms, and a country field for models.
* [gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX.
* [psycopg2](https://pypi.org/project/psycopg2/) - A PostgreSQL database adapter.
* [boto3==1.26.27](https://pypi.org/project/boto3/) - An Amazon Web Services (AWS) software development kit (SDK) used to connect to the S3 bucket
* [Black](https://pypi.org/project/black/) - A Python code formatter.
* [django storages](https://django-storages.readthedocs.io/en/latest/) - Collection of custom storage backends for Django.
* [Css Minifier](https://www.toptal.com/developers/cssminifier) - Minify CSS for better response time.

<br>

[Back to Top](#table-of-contents)

<br>

## Tools And Resources
* [GitPod](https://www.gitpod.io/)
* [GitHub](https://github.com/)
* [Heroku](https://heroku.com)
* [ElephantSQL](https://www.elephantsql.com/)
* [Cloudinary](https://cloudinary.com/)
* [ReadMe Template](https://github.com/Code-Institute-Solutions/readme-template)
* [Stack Overflow](https://stackoverflow.com/)
* [Coolors](https://coolors.co/)
* [AmIResponsive](https://ui.dev/amiresponsive)
* [Real Python](https://realpython.com/)
* [Online Convert](https://image.online-convert.com/convert-to-webp)
* [Pic Resize](https://picresize.com/)
* [Sideshow](https://www.sideshow.com/)
* [Hasbro](https://shop.hasbro.com/)
* [Darkhorse](https://www.darkhorsedirect.com/)
* [Gamestop](https://www.gamestop.com/)

<br>

[Back to Top](#table-of-contents)

<br>

# Testing 
### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
  - The only warnings that were given were because of the nature of Django Template Syntax.
![W3 Errors](documentation/images/w3-validation.png)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
  ![W3 Errors](documentation/images/css-validation.png)
- Python
  - No errors were returned when passing through [CI Python Linter](https://pep8ci.herokuapp.com/)
  - The only issue that was brought up by the Linter were some lines too long. As these were less than 5 characters and that code had already been formatted by the Black plugin, I left these alone.

<br>

### Lighthouse Testing
![Lighthouse Metrics](documentation/images/lighthouse-desktop.png)
  - Testing on desktop originally gave a low Accesibility score with an 87. The reason for this was because the contrast on the blue colour I had originally chosen did not have a suffiecient contrast ratio.
  - By using the linked colour contrast checker in Lighthouse, I was able to see I neeeded to change this blue to a darker colour.
  - I then checked the rest of the colours on the page - specifically the Categories section and realised I needed to change the contrast on these too. My fix for that was to add a drop shadow on the text.
  - After these fixes, my metrics were as shown in the top image. 99 Performance, 98 Accessibility, 92 Best Practices, 100 SEO.

- ![Lighthouse Metrics](documentation/images/lighthouse-desktop-accessibility.png)
- ![Lighthouse Metrics](documentation/images/lighthouse-contrast.png)

<br>

 - On mobile, the performace is 86. This was originally lower because of a cumulative layout shift of 0.219. Recommendations for this were to add width and height to images and change the images to .webp format.
 - To change images from .jpg to .webp I used the website [WEBP Converter](https://cloudconvert.com/webp-converter).
 - I also changed the background image on the Hero section of the index page to a smaller version to try and help with the CLS.
 - The main issues with this low rating is because Lighthouse recommends to use HTTP2, which I am unable to change because the website is hosted on Heroku.
 - There is also an issue with "Reduced unused JavaScript" which then lists Stripe, AWS, Mailchimp and jQuery. These are all included in the base template, so unless I split them out to use only with each app they're associated with (and this would be massively time consuming for me to figure out), I have decided to leave it as is and include screenshots.

![Lighthouse Metrics](documentation/images/lighthouse-mobile.png)
![Lighthouse Metrics](documentation/images/lighthouse-mobile-perf.png)
![Lighthouse Metrics](documentation/images/lighthouse-mobile-js.png)

| Page | Device | Category | Result |
|------|--------|----------|--------|
|Index | Mobile | Performance | 86% |
|||Accessibility| 98% |
|||Best Practice | 92% |
|||SEO | 100% |
|| Desktop | Performance | 100% |
||| Accessibility | 98% |
||| Best Practice | 92% |
||| SEO | 100% |
 <br>

 [Back to Top](#table-of-contents)

<br>

### Automated Testing
- I wrote tests for each app and for every view.py, model.py and form.py I have in the project. Below is the coverage report. Since my last project I have taken a keen interest in learning more about automated testing. Linked below are some of the resources I used to help me learn. Although the test still aren't comprehensive as I'd like and there are unfortunately some apps that I didn't even know how to begin to tackle (or if I should), I still managed to write 81 tests that all pass.

- For the SetUp methods, based on the video linked below from Adam Johnson, I used the class method. However, as I had previously learned to use the SetUp method, I reverted back to that as I didn't know the difference between the 2 versions and didn't want t confuse the code by having multiple ways for the same thing. 

#### Resources Used For Testing
- [DjangoCon 2021 | Speed up your tests with setUpTestData | Adam Johnson](https://www.youtube.com/watch?v=_8qLxaWMdzE)
- [Mozilla | Django Tutorial Part 10: Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
- [https://machinelearningmastery.com/ | A Gentle Introduction to Unit Testing in Python](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/)
- [Real Python | Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [DataQuest | A Beginner’s Guide to Unit Tests in Python (2023)](https://www.dataquest.io/blog/unit-tests-python/)

<br>

![Coverage Report](documentation/images/coverage-report.png)
![Pytest Report](documentation/images/pytest.png) 

<br>

### Manual Testing
- Manual testing has been done extensively and has been shown in separate file, located [here.](documentation/testing.md)

### Other Testing
 - The website has been tested across various screen sizes, using the Chrome DevTools responsive device section, [Responsive Design Checker](https://responsivedesignchecker.com/) and by opening the website on Firefox, Chrome, 3 various sized Android phones (Huawei P20 Lite, OnePlus 9 Pro, Samsung Galaxy S20) and an Android tablet (Samsung Galaxy Tab 10). 
 - Here is a link to a separate [Markdown file](documentation/tested-devices.md) of device screenshots.

<br>

[Back to Top](#table-of-contents)

<br>

# Bugs

 Below is a description of bugs encountered and how I was able to fix them or why I couldn't.

### Adding an incorrect SKU throws a server error

  - #### Issue:

    - When Adding or Updating Products, the SKU could be any combination of letters or numbers and any length - resulting an error on form submission

  - #### Fix:

    - My inital thought was to add help-text to the model so that the form would tell the user what to write in the code. However, this didn't solve the issue that someone could intentionally or unintentionally still add an incorrect SKU and cause the same failure.
    - I then decided to have a SKU automatically generated when a new product was being added. This field pre-populates with a 6 digit code and is always unique. On top of that, I also made the field Read-Only on the Product Form, therefore it doesn't need to be touched by the admin and can't cause an issue.

![SKU](documentation/images/sku-readonly.png) 

<br>

[Back to Top](#table-of-contents)

<br>

  ### Delete Modal Not Deleting Correct Product ID

  - #### Issue:

    - When clicking on "Delete" on the all products page, the product ID for deletion would only point to the first product ID.

  - #### Fix:

    - This fix was actually quite easy in the end but it wasn't spotted for a long time, so thank you to [Sean Finn](https://github.com/seanf316/) my classmate for finding it.
    - The product cards on the product page were being rendered with a loop - {% for product in products %}, however I originally had the modal for deletion outside the loop. Therefore it rendered for the first product only. Moving the deletion modal into the loop, made sure that when clicking Delete, it was for the correct Product ID.

![Delete Modal](documentation/images/delete-product.png) 

<br>

[Back to Top](#table-of-contents)

<br>

### User Editing and Deletion

  - #### Issue:

    - Any logged in user was able to delete another users profile by changing the URL PK number to another.

  - #### Fix:

    - This was a bug pointed out to me by a fellow student [Sean Johnston](https://github.com/seanj06/). I wouldn't have known to look for it myself so I'm very thankful.
    - I had LoginRequired Mixins on my edit and delete views for both appointments and profiles, however I didn't realise that would allow _any_ logged in user access to a different users account just by changing the PK in the URL for edit/delete.
    - Sean pointed me towards the UserPassesTestMixin and I was successfully able to implement this into my Views. Users now need to pass an ID check before they're allowed to access the Edit or Delete views for their own profile and they get a 403 Forbidden page if they try to access a different users profile.

<br>

[Back to Top](#table-of-contents)

<br>

### Reviews Can Be Updated By Any User, Multiple Reviews Allowed 

  - #### Issue:

    - Any user can update any other users review by changing the review ID in the update URL. Also, multiple reviews could be submitted by a user for the same product.

  - #### Fix:

    - I used CBVs for my Review forms - to allow updating and deleting. However, I originally only had the LoginRequiredMixin on these.
    - I needed to add the UserPassesTestMixin to these CBVs, so that only the original auther of the reviews could update or delete their own review.
    - For the reviews being 1 per user - I found this article on [StackOverflow](https://stackoverflow.com/questions/68135234/how-to-allow-users-to-rate-a-product-only-once), which allowed me to a UnqiueContraint to the review model.

<br>

[Back to Top](#table-of-contents)

<br>

### Wishlists

  - #### Issue:

    - The Wishlist would only allow 1 product to be added per user.

  - #### Fix:

    - The most trouble I had with this project seemed to be with the Wishlist. This particular issue was more to do with a misunderstanding of my models.
    - The original model I created for the wishlist used a ForiegnKey for both the user and the product. This meant that I could add 1 product to 1 user's Wishlist.
    - I also had an issue where a newly registered user would not have a Wishlist automatically created on account creation - so when that user tried to add a product to a wishlist, this would throw an error as a wishlist didn't exist. I originally thought to create a signal that would create the Wishlist, the same way the UserProfile would be deleted, however this seemed like it was an overcomplication of the issue.
    - To fix everything, I had a complete re-write of the Wishlist app. I changed the model from ForeignKeys to a ManyToManyField key for Products and a OneToOneField for the User.
    - For the views, I found these articles - [Django Docs](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#get-or-create) and [https://www.queworx.com/django/django-get_or_create/](https://www.queworx.com/django/django-get_or_create/) - which would allow me to get_or_create a Wishlist for a user. Alongside the Try and Except statements, this would handle any error that might be created if a user did not currently have a Wishlist associated with their account ID.
    - However, on the actual template then, this was giving me the error "AttributeError::: 'tuple' object has no attribute 'products'" when trying to iterate over the Wishlist with {% if wishlist %} and {% for product in wishlist %}. Researching this wasn't easy, it took me a few days to try and understand what was happening and why.
    - I finally realised the the get_or_create was creating a tuple, so I couldn't iterate over it with just the {% if wishlist %} syntax - I needed to check if the wishlist exists with products first and then I needed to access the products on the wishlist. This lead me to try {% if wishlist.products.exists %} and {% for product in wishlist.products.all %} which worked. This - to my knowledge - was because the Wishlist itself was only a type of holder for many products. The wishlist itelf was 1 item - the products were what we needed to access.
    - I feel there was probably an easier way to achieve the same outcome - but this solution worked for me, it's being saved properly to the database and so was fit for purpose here.


<br>

[Back to Top](#table-of-contents)

<br>

# Bugs Not Fixed

### Email System

  - #### Issue:

    - Emails would not send, despite having the correct credentials.

  - #### What I Tried:

    - I wanted to add an email system to have the user verify their account before being able to access restricted pages.
    - Initially, I tried to implement this with EmailJS but even after following the tutorial and the walkthrough, when deployed to the live server, the EmailJS dashboard would show my emails were failing to sent with a service error.
    - I then looked into Google STMP with some tutorials - [1](https://www.geeksforgeeks.org/setup-sending-email-in-django-project/), [2](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab), but again, this didn't work. 
    - Researching this made me believe that the port for sending emails was blocked.
    - I do know that there must be a way to send them but given time contraints, I had to leave it unfixed and remove any mention of password resetting or email verification.

### Submit button on contact form

- #### Issue:

    - Have the Submit button dissapear from the contact form once submitted.
  
 - I would like the contact form to completely disappear on submission, instead of just the Submit button being left behind. This is something I looked into but adding an onclick through HTML/CSS wouldn't work because the button would still disappear if the form failed to send. This would mean the user needs to refresh the page to get the submit button to reappear.
 - I then tried to add javascript for a button click event but this prevented the submission message from being displayed after the successful submission. Adding javascript to hide the button on submission, would hide it when the form was invalid but still show it when the page rendered the success message.
 - To counter this and make for a better UX, I decided to create a new view which renders the "contact_thank_you.html" page. This redirects a user to a page with a success message upon a valif form submission.

<br>

### Whitespace Validation on Contact Form

- #### Issue:

    - Could not achieve full whitespace validation for forms.

- The contact form currently allows users to submit messages that aren't stripped, e.g "C C C". Looking into this, I found some answers which were to set the model fields to have "blank=False" and "null=False" but this didn't work. I then tried to clean the data on the field using the clean() method but again, this didn't work. [Trim whitespaces from charField](https://stackoverflow.com/questions/5043012/django-trim-whitespaces-from-charfield)
- The fields do all have to be filled in or the form will fail to send with an error message explaing all fields must be filled in, this was the best I could achieve for the form currently.

<br>

[Back to Top](#table-of-contents)

<br>

# Credits and Sources

### Booking System
- The booking system was based on reading and watching multiple walkthroughs of Django Booking systems.
  - [DevGenius - Django Tutorial On How To Create A Booking System For A Health Clinic](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)
  - [Codemy.com YouTube, Build Dental Website](https://www.youtube.com/watch?v=4b3yvjcPLnk)
  - [DarshanDev YouTube, Django Hotel Management System](https://www.youtube.com/watch?v=-9dhCQ7FdD0&list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY&index=2)
  - [Developer-Felix, Doctor-Patient-Scheduler](https://github.com/Developer-Felix/Doctor---Patient-Scheduler)
  - [Tyler Taewook, Tutor Scheduler Django](https://github.com/tylertaewook/tutor-scheduler-django) 
  - [Selmi Tech YouTube, Build A Doctor Website With Django](https://www.youtube.com/watch?v=3_3q_dE4_qs) 
  - [pynative.com, Python Create List Of Dates Within Range](https://pynative.com/python-create-list-of-dates-within-range/)
  - [Geeks For Geeks, Creating a list of range of dates in Python](https://www.geeksforgeeks.org/creating-a-list-of-range-of-dates-in-python/) 

<br>

### Testing Credits
- [Freecodecamp.org, An Introduction to Unit Testing in Python](https://www.freecodecamp.org/news/an-introduction-to-testing-in-python) 
- [Real Python.com, Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Real Python.com, Testing in Django (Part 1) – Best Practices and Examples](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/)
- [Real Python.com, Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [valentinog.com, Django Testing Cheat Sheet](https://www.valentinog.com/blog/testing-django/)
- [developer.mozilla.org, Django Tutorial Part 10: Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
- [adamj.eu, How to Unit Test a Django Form](https://adamj.eu/tech/2020/06/15/how-to-unit-test-a-django-form/)
- [Django Documentation, Advanced testing topics](https://docs.djangoproject.com/en/4.1/topics/testing/advanced)
- [Django Documentation, Testing tools](https://docs.djangoproject.com/en/4.1/topics/testing/tools/)
- [Stackoverflow.com, How to test django model method __str__()](https://stackoverflow.com/questions/29077509/how-to-test-django-model-method-str)
- [Stackoverflow.com, How can I unit test django messages?](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages)
- [Stackoverflow.com, Django how to test model functions with validator](https://stackoverflow.com/questions/67331863/django-how-to-test-model-functions-with-validator)
- [Stackoverflow.com, Is it possible exclude test directories from coverage.py reports?](https://stackoverflow.com/questions/1628996/is-it-possible-exclude-test-directories-from-coverage-py-reports)

<br>

### General Credits
- [PythonEatsTail, Adding extra fields to a Django custom user model](https://www.youtube.com/watch?v=sSKYEMEU-C8&list=PL3I1Ttg2koa7hPduw6NDOaiZImfTTgw0b&index=31) 
- [Stackoverflow.com, How to pass logged user's id to CreateView](https://stackoverflow.com/questions/63550890/how-to-pass-logged-users-id-to-createview)
- [Geeks For Geeks, UpdateView – Class Based Views Django](https://www.geeksforgeeks.org/updateview-class-based-views-django/)
- [Geeks For Geeks, Update View – Function based Views Django](https://www.geeksforgeeks.org/update-view-function-based-views-django/)
- [ordinarycoders.com, Build a Django Contact Form with Email Backend](https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend)
- [Stackoverflow.com, Edit view is not showing choice field data in django?](https://stackoverflow.com/questions/40946200/edit-view-is-not-showing-choice-field-data-in-django)
- [Stackoverflow.com, How to validate in UpdateView without validating through a form?](https://stackoverflow.com/questions/54319706/how-to-validate-in-updateview-without-validating-through-a-form)
- [Stackoverflow.com, How to remove an already selected option from options list to avoid double bookings](https://stackoverflow.com/questions/73270490/how-to-remove-an-already-selected-option-from-options-list-to-avoid-double-booki)
- [Stackoverflow.com, django form validation with parameters from view](https://stackoverflow.com/questions/19007990/django-form-validation-with-parameters-from-view)
- [Stackoverflow.com, Django validating time slot](https://stackoverflow.com/questions/67981109/django-validating-time-slot)
- [Stackoverflow.com, Django form field clean to check if entered date is in a stored range](https://stackoverflow.com/questions/13026689/django-form-field-clean-to-check-if-entered-date-is-in-a-stored-range)
- [Stackoverflow.com, Create User and UserProfile on user signup with django-allauth](https://stackoverflow.com/questions/69990075/create-user-and-userprofile-on-user-signup-with-django-allauth)
- [Simpleisbetterthancomplex.com, How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
- [Django Documentation, Using mixins with class-based views](https://docs.djangoproject.com/en/4.1/topics/class-based-views/mixins/)
- [Django Documentation, Using the Django authentication system](https://docs.djangoproject.com/en/4.1/topics/auth/default/)
- [Django Documentation, Form handling with class-based views](https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/)
- [codewithhugo.com, Disable a HTML link/anchor tag](https://codewithhugo.com/disable-html-anchor/)
- [Stackoverflow.com, Angular ngx-boostrap datepicker position issue on mobile screen](https://stackoverflow.com/questions/60906841/angular-ngx-boostrap-datepicker-position-issue-on-mobile-screen)
- [developer.mozilla.org, translate3d()](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/translate3d)
- [Stackoverflow.com, What is best practice when using ValidationError and Constraint (new in Django 2.2)?](https://stackoverflow.com/questions/59592746/what-is-best-practice-when-using-validationerror-and-constraint-new-in-django-2)
- [How to restrict date and time in django bootstrap datetimepicker plus?](https://stackoverflow.com/questions/51022722/how-to-restrict-date-and-time-in-django-bootstrap-datetimepicker-plus)
- [Trim whitespaces from charField](https://stackoverflow.com/questions/5043012/django-trim-whitespaces-from-charfield)
- [Pexels](https://www.pexels.com/)
- [ThemeWagon](https://themewagon.com/themes/free-responsive-bootstrap-5-html5-construction-company-website-template-upconsttruction/) Some elements for the Contact Page were built on the UpConstruction boostrap template.

<br>

[Back to Top](#table-of-contents)

<br>

# Deployment

The following are the steps I went through to deploy my live site:

- The site was deployed using Heroku. The steps to deploy are as follows: 
1. Go to [Heroku](https://dashboard.heroku.com/apps)
2. Go to 'New' and select 'Create a new app'
3. Input your app name and create app.
4. Navigate to 'Settings'
5. On the Config Vars section, enter the following values:
    - SECRET_KEY: The Secret Key for your project
    - DATABASE_URL: The URL from your ElephantSQL dashboard
    - CLOUNDINARY_URL: The URL from your Cloudinary dashboard
    - PORT: 8000
6. Navigate to the 'Deploy' section. 
7. Connect to GitHub, search for your repo and confirm. 
8. Choose branch to deploy.
9. Your app should now be available to see. You can choose whether to have your app automatically redeploy with every push or to keep it manual. 

- To Fork the repository:
  - On GitHub.com, navigate to the repository.
  - In the top-right corner of the page, click Fork.
  - Select an owner for the forked repository.
  - By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
  - Optionally, add a description of your fork.
  - Choose whether to copy only the default branch or all branches to the new fork.
  - Click Create fork.

- To Clone the repository:
  - On GitHub.com, navigate to the repository.
  - Above the list of files, click the Code button.
  - Copy the URL for the repository.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
  - Press Enter. Your local clone will be created.

<br>

The live link can be found here - [LevelUp! Loot](https://levelup-loot-vt.herokuapp.com/)

<br>

[Back to Top](#table-of-contents)

<br>

# Acknowledgements
- To my amazing boyfriend Thomas. For listening to me worry about this project for months, for keeping me sane, for helping me switch off after a long day with a cup of coffee and a bar of chocolate :)
- My family and my cats for keeping my stress levels under control!
- [Sean Johnston](https://github.com/seanj06/) and [Sean Finn](https://github.com/seanf316/), my fellow classmates on Slack. Your help with my many questions was super appreciated, thank you.

<br>

[Back to Top](#table-of-contents)