# Milestone Project 4 - Handmade By Ellie

[![Build Status](https://travis-ci.com/Tmuat/handmade-by-ellie.svg?branch=master)](https://travis-ci.com/Tmuat/handmade-by-ellie)

![Desktop Demo](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/readme_images/site-view.png "Desktop Demo")

## View live project [here](https://handmade-by-ellie.herokuapp.com/).

## Description

**Handmande By Ellie** is an e-commerce store selling wax melts. The website allows the company owner to list their range of products for the purpose of site visitors being able to search, view and purchase through the use of Stripe.

The site allows the store admin to add, edit and delete products as well as being able to view all orders and use automated emails to update purchasers on the status of their order.

---

## Contents

- [UX](#ux)
  - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [User Stories](#user-stories)
  - [The Scope Plane](#the-scope-plane)
  - [The Structure Plane](#the-structure-plane)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Security](#security)
  - [The Surface Plane](#the-surface-plane)
    - [Landing Imagery](#landing-imagery)
    - [Colour Scheme](#colour-scheme)
    - [Fonts](#fonts)
    - [Information Architecture](#information-architecture)
    - [Differences To Design](#differences-to-design)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks and External Resources](#frameworks-and-external-resources)
- [Testing](#testing)
  - [Google Dev Tools](#google-dev-tools)
  - [Responsivley](#responsivley)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [User Story Testing](#user-story-testing)
  - [Fixed Bugs](#fixed-bugs)
  - [Known Bugs](#known-bugs)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Misc](#misc)
    - [Content](#content)
    - [Images](#images)
  - [Acknowledgements](#acknowledgements)
  - [Disclaimer](#disclaimer)

---

## UX

---

### **The Strategy Plane**

Handamde by Ellie is the current business of client Ellie; having started the business during the COVID-19 lockdown in 2020, Ellie has primarily run the business through social media and word of mouth. With the success of her business, Ellie is looking to move her business on to an e-commerce store.

Ellie would like an e-commerce store styled to match her current social media colours & branding. She would like the ability for site users to view information on products, add them to a shopping and finally purchase these items. Ellie would like the ability to add, edit and delete products as an when needed.

The aim is to build Ellie an e-commerce store which will allow registering of users, purchasing of products, viewing of order history/profile information and if needed the ability to contact the store owner. A seperate admin section (different from the Django Admin) will be created and secured from non site owners. This area will allow the site owner to manage products and orders.

#### Site Goals

- Create a site using HTML, CSS, Javascript, Python (Django) and SQL working together.
- Create an e-commerce store that is appealing to view and easy to navigate.
- Create a site that allows viewing and purchasing of products.
- Create a fully responsive site for use on all devices.
- Allow store owner to fulfill the other 3 variables of CRUD (CREATE, UPDATE & DELETE) for products.
- Allow the store owner to view and manage orders

#### User Stories

**Annonymous User:**

- As a **annonymous user**, I want to visit a responsive site.
- As a **annonymous user**, I want it to be clear the purpose of the site and what the site is intending to sell.
- As a **annonymous user**, I want to be easily able to navigate through the site.
- As a **annonymous user**, I want to be able to register an account for the site.
- As a **annonymous user**, I want to be able to search and filter through the different products on sale.
- As a **annonymous user**, I want to be able to create a shopping bag of one or more items to purchase in one checkout process.
- As a **annonymous user**, I want to be able to add, change and delete products in my shopping bag.
- As a **annonymous user**, I want to be able to checkout annonymously.
- As a **annonymous user**, I want to recieve an email notification of my order.

**Registered User:**

Some if not all the annoymous user stories carry over to registered users.

- As a **registered user**, I want to be able to login to the site.
- As a **registered user**, I want to be able to reset my password if I had forgotten it.
- As a **registered user**, I want to be able to save my default information for quicker checkout processes of future purchases.
- As a **registered user**, I want to be able to view my previous orders and their status.

**Admin User:**

- As a **admin user**, I want to be able to create, update and delete products in the store.
- As a **admin user**, I want to be able to monitor and adjust product stock quantities.
- As a **admin user**, I want to be able to view all orders being made on the site.
- As a **admin user**, I want to be able to adjust order status' and send corresponding.emails to users who have made purchases.

---

### **The Scope Plane**

**Features Planned:**

- Responsive Design - site should be fully responsive across screen sizes/devices.
- Cross browser functionality - the site should work no matter the browser of choice.
- Mobile, tablet and desktop optimised navigation.
- Website information and relevant landing imagery on landing page.
- Registered user functionality - able to create a user, login as said user and update default information.
- Product information - description and stock information.
- Search and Filter functionality.
- Shopping bag - functionality to add one or more different products and quantities to a shopping bag.
- Secure card checkout - utilising stripe.
- Contact form for all users to be able to contact the site owner.
- Admin section for 'staff' - area for 'staff' to manage sections of the site.

---

### **The Structure Plane**

#### User Story:

> As a **annonymous user**, I want to visit a responsive site.

**Acceptance Criteria**

- The website will feature a grid layout, incorporating breakpoints and media queries to respond to the users screen size & platform.

**Implementation**

- The website will be built using [Bootstrap](https://getbootstrap.com/); this will entail the use of their grid system and thus the wide browser compatibility.

#### User Story:

> As a **annonymous user**, I want it to be clear the purpose of the site and what the site is intending to sell.

**Acceptance Criteria**

- The landing page will feature information regarding the site aim with headings and imagery styled to the same aim.

**Implementation**

- The landing page will contain the name of the site along with a short sentence for a to the point description of the site.

- Below the landing imagery is an 'About Us' section with more detail about the site and the products.

#### User Story:

> As a **annonymous user**, I want to be easily able to navigate through the site.

**Acceptance Criteria**

- A navigation bar responsive to all screen sizes.
- All links should navigate to the correct pages.
- The current page should be highlighted as active to indicate to the user which page they are on.

**Implementation**

- A navigation bar will be implemented for all screen sizes with different views for mobile, tablet and desktop. The navigation bar will collapse on both tablet and mobile for a better user experience.

- Dependent on whether the user is authenticated, the menu options will differ for logging in/registering and viewing a authenticated users profile.

- A bag item will be used with a font awesome icon; the bag will change colour once an item is in the bag.

#### User Story:

> As a **annonymous user**, I want to be able to register an account for the site.

**Acceptance Criteria**

- A user is able to register for an account, using a site form. They will be required to complete email verification. Subsequently the user is then able to login to their account.

**Implementation**

- The site will use the [All Auth](https://django-allauth.readthedocs.io/en/latest/#) package which takes care of authentication & social authentication.

#### User Story:

> As a **annonymous user**, I want to be able to search and filter through the different products on sale.

**Acceptance Criteria**

- A user will be able to view all products, as well as the ability to search for an item or use page filters to see only certain categories, prices etc. The filters and search fields must show the condensed product lists and not all products.

**Implementation**

- A search bar will be placed in the navigation menu, thus allowing users to search for specific names of products.

- A filter section on the products page will allow users to filter to any specific category they would like.

#### User Story:

> As a **annonymous user**, I want to be able to create a shopping bag of one or more items to purchase in one checkout process.

**Acceptance Criteria**

- The user will be able to add one or more products to a viewable shopping bag; the items in the shopping bag must accept varying quantities.

**Implementation**

- The users session will be used to hold shopping bag details.

- When a user adds a product to the shopping bag, the product sku and quantity will be added or updated in the users session.

- When viewing the bag, all items and quantities in the bag will be displayed for the user.

#### User Story:

> As a **annonymous user**, I want to be able to add, change and delete products in my shopping bag.

**Acceptance Criteria**

- When in the shopping bag, the user is able to adjust quantities and delete products from their bag. When doing so, the user should see their bag refreshed with the updated bag shown.

**Implementation**

- In the shopping bag the user will see a form to update the quantity of individual items.

- On each table row for each item, there will be a remove button. This will remove the item from the bag before reloading the current page without the item in.

#### User Story:

> As a **annonymous user**, I want to be able to checkout annonymously.

**Acceptance Criteria**

- A user is able to go through the full process of purchasing an item as an unauthenticated user.

**Implementation**

- Users will be able to checkout without an account; they must still fill in details regarding name, email, delivery address etc but will not need to be authenticated.

- When checking out they will be informed that they cannot view a full order history if not authenticated on the site.

#### User Story:

> As a **annonymous user**, I want to recieve an email notification of my order.

**Acceptance Criteria**

- Any user making a purchase must recieve email notification their order.

**Implementation**

- Stripe webhooks will be used to send emails; this will ensure the order has been processed and money taken by stripe before the order email is sent out.

#### User Story:

> As a **registered user**, I want to be able to login to the site.

**Acceptance Criteria**

- A registered user is able to navigate to a login page and authenticate with the site.

**Implementation**

- Using the previously mentioned [All Auth](https://django-allauth.readthedocs.io/en/latest/#) and the inbuilt django authentication; the user will be able to login as a registered user.

#### User Story:

> As a **registered user**, I want to be able to reset my password if I had forgotten it.

**Acceptance Criteria**

- Users are able to recieve a forgotten password email should they be unathenticated on the site. They are then able to change their password.

- Users already authenticated are taken to a form to change their password; once changed they are able to login using the new password.

**Implementation**

- Using the previously mentioned [All Auth](https://django-allauth.readthedocs.io/en/latest/#), both scenarios will be handled with their templates.

- The All Auth templates will be styled to follow the styling of the site.

#### User Story:

> As a **registered user**, I want to be able to save my default information for quicker checkout processes of future purchases.

**Acceptance Criteria**

- Users information is stored in their profile; if it has been saved and they move to checkout the information is pre-filled.

**Implementation**

- The user can either input their default information on their profile page to be used when checking out or they have the option to save this information from the checkout page on their order.

#### User Story:

> As a **registered user**, I want to be able to view my previous orders and their status.

**Acceptance Criteria**

- Users must be able to view all previous orders on their profile page along with the up to date status of said order/s.

**Implementation**

- All a authenticated users orders are linked to their profile; thus when viewing their profile a table of orders will be rendered on the same page.

- The orders rendered into the table will include information, including the status. The user can view more detail when clicking on the order to see the order detail.

#### User Story:

> As a **admin user**, I want to be able to create, update and delete products in the store.

**Acceptance Criteria**

- The admin user is able to view the admin site and subsequently perform CRUD operations on all products within the store.

**Implementation**

- A seperate admin site will be created for admin users to access; once here they have the ability to perform CRUD operations on the sites products.

#### User Story:

> As a **admin user**, I want to be able to monitor and adjust product stock quantities.

**Acceptance Criteria**

- When viewing product detail, the admin user can see up to date product stock. They are also able to add/delete stock for individual products.

**Implementation**

- A stock model will be used for all products; this will be updated as orders are placed.

- The admin user will be able to see the stock of all products and adjust the stock accordingly.

#### User Story:

> As a **admin user**, I want to be able to view all orders being made on the site.

**Acceptance Criteria**

- When on the admin site, the admin user is able to see all orders that have been placed (including order detail).

**Implementation**

- Once on the admin site, the admin user will have options to view all orders and also search for specific order numbers.

- The admin user will be able to view all the order details of each order.

#### User Story:

> As a **admin user**, I want to be able to adjust order status' and send corresponding emails to users who have made purchases.

**Acceptance Criteria**

- The admin user is able to select one or more orders and change the order status. This must trigger an email to be sent out to the email address linked to each order.

**Implementation**

- A form will be used to change order status' and send orders. This will allow admin users to select multiple orders at once and mark as dispatched/completed.

---

### **The Skeleton Plane**

#### Wireframes

The wireframes for phone, tablet and desktop can be found by clicking [here](https://github.com/Tmuat/handmade-by-ellie/tree/master/assets/wireframes).

[Desktop](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/wireframes/desktop.pdf)

[Tablet](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/wireframes/tablet.pdf)

[Mobile](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/wireframes/mobile.pdf)

#### Security

In order to keep the site secure, all potentially sensitive information have been kept in an env.py file which is not commited to github and on Heroku config variables have been used.

Sections of the site have been decorated to ensure users are only able to access sections of the site they have been given permissions to access.

### **The Surface Plane**

#### Landing Imagery

The landing imagery has changed from wireframes; this was down to a request from Ellie having taken so updated pictures.

The landing imagery was used to conincide with the landing text, as a way to allow the user to quickly identify the purpose of the site and the type of products being sold. The imagery is styled to match the existing social media posts from 'Handmade By Ellie'.

#### Colour Scheme

Entering into the build process of the site, 'Handmade By Ellie' is already a functioning business. As such the colour schemes have been dictated by the company media already out in the public domain.

The overall site features a light colour scheme in keeping with the already utilised colour schemes. The two main colours used on the site come from the company logo and are:

![Main Colours](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/readme_images/colours.png "Main Colours")

- Colour 1 #BDA1A1
- Colour 2 #FFEDED

#### Fonts

The site features two main fonts taken from the logo; the main font across the site comes from the 'Handmade' aspect of the company logo, whilst the 'By Ellie' font is used sparingly across the site. The fonts used are:

- Main Font - Baskerville
- Secondary Font - Starlight

#### Information Architecture

![Information Architecture](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/readme_images/information_architecture.png "Information Architecture")

To access the Information Architecture click [here](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/readme_images/information_architecture.png).

#### Differences To Design

There were two main differences to the wireframes; the landing imagery and the admin section.

The landing imagery was changed from the wireframes as the client supplied their own imagery to be used in the background.

The admin section of the site was created utilising a bootstrap example; this was used to give a better experience to the store owner.

---

[Return to Contents](#contents)

---

## Features

### Existing Features

#### Navbar

The site features a consistent navbar across the store. The navbar changes colour when moving away from the landing page to improve the user experience. The navbar features filter links to all products; when on the products page these filters are not displayed as they are displayed elsewhere on the page. Also on the navbar is an account section for access for the user to resgister, login, logout, change password and access their profile. It also includes a link to the users 'shopping bag', with a colour change when one or more items are in the bag. The navbar is full responsive; moving to a dropdown on smaller screens. There is a difference on the admin site but this is detailed below.

#### Footer

Much like the navbar, the site features a consistently themed footer across all pages. The footer includes links to popular pages on the site as well as a short description of the website. The colour of the footer matches the overall theme of the site.

#### Landing Page

The landing page features imagery consistent with the Handmade By Ellie brand. The landing page features very little text; the page includes a call to action 'Shop Now' and the user will be able to glimpse another section below. When the users scrolls they are able to see a short section detailing the Handmade By Ellie brand along with a few select testimonials.

#### Products

In order to get to the products page, the user can either search for a particular term in the search bar or use some of the dropdowns to filter or sort all the active products.

Once on the products page, the user will be presented with all the products they have either searched or filtered for (no filtering takes place if they select all products). They can then see each products image, name, price and any categories they fall into.

To give the user information, a white row is displayed underneath the navbar to display the current number of products displayed, the number when filtered and a link to the products home and finally if the products have been searched it will show the number of products and search term. In the middle it will show any categories if the user has filtered by these. Lastly it gives a select box for the user to sort the items in different ways.

On the left hand side of the screen for small screen sizes and up is a sidebar including more advanced filtering options for the user to sort and filter the products on screen. On smaller screen sizes the filter is hidden off screen with a fixed filter button appearing in the bottom right of the screen.

The user can view product detail by simply clicking on the product image or on the product name.

#### Product Detail

On the product detail page, the user is able to see a short description of the product along with any categories it falls into. Below this the user can add a quantity of the product to their bag and also see product stock. The user cannot put more than the max stock level of the product into their bag. The site features a number of checks to ensure that this is not possible.

#### Shopping Bag

The user can navigate to the shopping bag. If the shopping bag is empty they are informed of this and offered a link back to all products. If they have any products in their bag they will be able to see all the products and corresponding quantities they wish to purchase. The user can adjust the quantity of individual items from here or remove the item entirely from the bag. 

The shopping bag features some defensive programming; on loading the bag page, the view performs a check to ensure any products in the bag are still in stock and active. This counters the problem with someone putting an item into their bag and it being added to the value in their session; them leaving the site coming back a week later when it is out of stock and still being able to proceed to checkout. The checkout button will be disabled if any of the products aren't in stock or active.

Also on this page the user is required to enter a delivery option; without this they cannot proceed to the checkout page. The delivery method is then set into the session and the grand total is updated.

Another feature on this page is the ability to add a discount code (these are set by the store owner). This is not required to proceed to checkout but should you have a discount you enter it here and it will calculate your discount (a percentage). Only one discount code can be added at any time.

Once you have in stock and active product and set your delivery method you can proceed to the checkout page.

#### Checkout

Like the shopping bag, on loading the checkout all products in the shopping bag are checked for stock and to see if they are still active. The view also checks if any discount code is included and if it is valid as the code can have either an expiry or quantity set on it. This stops a user being in the bag for a while and coming back and proceeding straight to checkout.

The user is required to add some basic order information such as name, email and phone number along with billing/delivery address. The checkout then utilises stripe to form a card element and handle the payment process. The user can then proceed with an order. A store user can checkout without being authenticated; but if they are they have the option to save their info to a profile model which can auto filled out when they next proceed to checkout.

#### Checkout Success

Should the store process the order, the user is displayed with a summary of the order along with receiving an order email.

#### Profile

An authenticated user is able to view their profile; here they can see details of all previous orders and also update/change any of their default information for the next time they checkout. If a user selects an order to see, they see the same screen as the checkout success without a duplicate order email being sent.

#### Site Admin

The store features a seperate admin area, with a UX more in keeping with manageing stock and orders. The store owner can set orders as dispatched which sends an automated email to the customers email address. The admin site also allows users to search for a particular order in case of queries from a customer. 

The admin site features a side navigation bar to allow the the store owner to edit and add products, edit discount codes and edit delivery options. The discount codes and delivery options are created using formsets to allow for multiple instances to be edited on the same page; creating a quicker user experience.

#### Django Admin

The site uses the [Django Admin Honeypot](https://pypi.org/project/django-admin-honeypot/) package to change the admin url of the site. This stops web crawlers from trying to force their way into the admin section.

### Features Left To Implement

#### Contact Page

At the moment the store doesn't contain a standalone contact page; this is something that would improve the users site experience in case they wanted to contact the sites owner.

#### Editing Products

Whilst the site features a nice admin site to manage the store, the store owner currently doesn't have a way to edit the store products from the normal store. Implementing this would allow the store owner to make small changes quickly as they find them.

#### Discount Codes & Product Names

As the site uses the product skug for product detail, it requires them all to be unique. At the moment this is enforced on the backend; however to improve UX, it would be good to have an ajax call to check for uniqueness on the front end so the user doesn't need to submit the form to find out.

#### Store Emails

Currently when a store user makes a purchase, they are sent an email summarising their order. However, an automated email to the store owner would allow to owner to start acting on orders without having to access the site.

---

[Return to Contents](#contents)

---

## Technologies Used

### Languages

---

Across the site 4 languages were used:

- HTML5
  - This was used to form the structure of each page
- CSS3
  - This was used to add syling to all html elements
- JavaScript
  - This was was to add classes and validate forms.
- Python 3.8.7
  - Python provided the backend language of the project.

---

### Frameworks and External Resources

---

A number of external frameworks, code libraries and programs were incorportated into the Visit Kingston site. These are listed below with code attribution within each segment of the live site and in the credits section towards the end of this README.

- [Django](https://www.djangoproject.com/)
    - Django was the python framework used to build the application - version 3.1.8 was used on this project.

- [Bootstrap 4.5.3](https://getbootstrap.com/)
    - Bootstrap formed the skeleton of the website; the bootstrap grid system and classes formed the underlying structure of the site

- [Font Awesome 5.12.2](https://fontawesome.com/)
    - Font Awesome was used to add icons across the site for a more intuitive user experience

- [JQuery 3.5.1](https://jquery.com/)
    - JQuery was used across the different pages of the site to create interactive elements without the need for huge volumes of Javascript coding

- [Popper.js 1.16.0](https://popper.js.org/)
    - Popper was used with Bootstrap to create a responsive navbar element

- [argon2-cffi](https://argon2.online/)
    - Argon2 was used as the password validator as reccommended by Two Scoops of Django.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
    - Allauth was used to handle the complete sign up process on the site.

- [Black](https://pypi.org/project/black/)
    - Black was used as a python code formatter.

- [Boto3](https://pypi.org/project/boto3/)
    - Boto3 was used to intergrate with AWS

- [Coverage](https://pypi.org/project/coverage/)
    - Coverage was used to assess the overall testing coverage

- [Django Admin Env Notice](https://pypi.org/project/django-admin-env-notice/)
    - This was used to put a simple banner at the top of the admin site to visually display which environment the user is working in

- [Django Cleanup](https://pypi.org/project/django-cleanup/)
    - This was used to automatically delete user uploaded images etc
  
- [Django Admin Honeypot](https://pypi.org/project/django-admin-honeypot/)
    - As previosuly stated, this package was used to change the admin url and create a honeypot which can alert the superuser of malicious attempts to access the admin.

- [Django Cleanup](https://pypi.org/project/django-countries/)
    - This was used to set the countries recognised country code

- [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/)
    - This was used to easily format all forms on the site

- [Django Debug Toolbar](https://pypi.org/project/django-debug-toolbar/)
    - This was used in development to provide additional information about each page, database queries etc

- [Django Environ](https://pypi.org/project/django-environ/)
    - As reccomended by the Twelve Factor App, django environ was used to store all env varibales in an env file.

- [Django SES](https://pypi.org/project/django-ses3/)
    - Django SES was used to connect to the AWS SES service for the production sites email backend

- [Django Storages](https://pypi.org/project/django-storages/)
    - Django Storages was used alongside Boto3 to utilise AWS S3 as the sites static files provider

- [Pillow](https://pypi.org/project/Pillow/)
    - Pillow was used to allow image upload for the product model

- [Pytest](https://pypi.org/project/pytest/)
    - Pytest was used as the testing library for the site

- [Stripe](https://pypi.org/project/stripe/)
    - Stripe was used to form a connection to the stripe api for payments

- [Gitpod](https://gitpod.io/)
    - Gitpod was the development environment used to code this site, gitpods terminal was used to synchronise with Github

- [Github](https://github.com/)
    - Github was used to store all components of this site during and after the build

- [Git](https://git-scm.com/)
    - Git was the version control system utilised for the build of this project

- [Figma](https://www.figma.com/)
    - Figma was used to create the wireframes prior to the build commencing

- [Google Fonts](https://fonts.google.com/)
    - Google Fonts was used to find and import the selected font for the site

- [Heroku](https://www.heroku.com)
    - Heroku was used to host the website online.

- WC3 [HTML](https://validator.w3.org/) & [CSS](https://jigsaw.w3.org/css-validator/) Validator
    - Both the CSS & HTML validators were used to check code for compliance with recognised standards

- [JSHint](https://jshint.com/)
    - Was used to validate all Javascript codes

- [Pep8Online](http://pep8online.com/checkresult)
    - Along with the fact that Pep8 compliance is built into the coding environment, this external site was also used to
        check the python code

- [Responsivley](https://responsively.app/)
    - Responsivley was used to check the responsiveness of the site (see testing below)

Click [here](https://github.com/Tmuat/handmade-by-ellie/blob/master/requirements.txt) to view the sites requirements.txt.

---

[Return to Contents](#contents)

---

## Testing

### JSHint

---

All Javascript codes were passed through the [JSHint](https://jshint.com/) validator with all corrections made.

---

### Google Dev Tools

---

Chrome DevTools was used from start to finish when building and testing this site. Throughout the build it served several purposes:

- Throughout the build it was used to quickly test responsiveness for all elements and design

- When constructing pages and elements, it was used to quickly and visually check for any padding and margin issues. Unicorn Revealer also provided a lot of help with this.

- Dev tools was used to identify and errors and warnings; I was reminded to utilise a favicon. Once created a link tag was added into the head of the base template.

- It was used vigorously to adjust css for hover, focus and active classes. 

---

### Responsivley

---

During development, the respondivley app was used to easily show how the front end reacts to multiple screen sizes. This sped up development as multiple views could be seen at once.

---

### Manual Testing

---

Along with the autmated testing below, manual tests were conducted by completing user stories and processes which would take place should the site move to production such as adding products to the shopping bag, completing orders and editing/adding products.

- Each page has been tested individually to check that:
    - Images load properly and are the correct sizes
    - Navigation buttons work and also link to the correct pages on the site
    - Any external links on the site (footer & products page) are set to target="_blank" to open on a new page
    - On top of this testing, with the number of forms on the site they were also checked for:
        - Client side & server side validation works
        - Any messages back to the user are clearly displayed in appropriatley coloured toasts
    - Checked the navbar is visible on all pages. 
        - The navbar has a different background on the landing page to all other pages.

---

### Automated Testing

---

The site features a number of automated tests. During development TDD principles were attempted; by writing failing tests before creating the view, model etc. 

The site uses pytest as its testing framework; this was used for the simpler style of writing tests. The site is intergrated with TravisCI to ensure all pushes to github pass the tests.

---

### User Story Testing

---

Testing the user stories from the [UX Section](#ux).

#### First Time User:

#### User Story:

> As a **annonymous user**, I want to visit a responsive site.

**Acceptance Criteria**

- The website will feature a grid layout, incorporating breakpoints and media queries to respond to the users screen size & platform.

**Pass/Fail**

- The website was built entirely within the bootstrap framework and is responsive to all screen sizes.

#### User Story:

> As a **annonymous user**, I want it to be clear the purpose of the site and what the site is intending to sell.

**Acceptance Criteria**

- The landing page will feature information regarding the site aim with headings and imagery styled to the same aim.

**Pass/Fail**

- The landing page contains a brief sentence describing the site. Underneath this is an about section providing an overview of the site as well as testimonials from happy customers.

#### User Story:

> As a **annonymous user**, I want to be easily able to navigate through the site.

**Acceptance Criteria**

- A navigation bar responsive to all screen sizes.
- All links should navigate to the correct pages.
- The current page should be highlighted as active to indicate to the user which page they are on.

**Pass/Fail**

- A navbar and footer is visible on all pages across all screen sizes. The navbar and footer are responsive to allow for a good UX on smaller screen sizes.

- The navbar updates dependent on whether the user is logged in and if they are a staff member/superuse.

- The shopping bag changes colour dependent on whether there is items in it.

#### User Story:

> As a **annonymous user**, I want to be able to register an account for the site.

**Acceptance Criteria**

- A user is able to register for an account, using a site form. They will be required to complete email verification. Subsequently the user is then able to login to their account.

**Pass/Fail**

- The site takes advantage of the allauth package and allows for user registration, email verification along with forgotten passwords and changing passwords.

#### User Story:

> As a **annonymous user**, I want to be able to search and filter through the different products on sale.

**Pass/Fail**

- At the top of the page in the navbar there is a search bar for the user to input a query; this is collpased into a search dropdown on smaller screen sizes. On top of this the user has the option to filter to different styles and types of products from a number of dropdowns. 

- Once on the product page they have a filter bar appear on the left hand side of the page or if on smaller device appear through clicking a fixed button in the bottom right corner.

#### User Story:

> As a **annonymous user**, I want to be able to create a shopping bag of one or more items to purchase in one checkout process.

**Acceptance Criteria**

- The user will be able to add one or more products to a viewable shopping bag; the items in the shopping bag must accept varying quantities.

**Pass/Fail**

- The user is able to add varying quantities of numerous products to their shopping bag; this is dependent on the stock levels available for each product. Once in the bag the user can see each product and the quantity in their bag. The shopping bag, delivery option and discount code are stored in the users session.

#### User Story:

> As a **annonymous user**, I want to be able to add, change and delete products in my shopping bag.

**Acceptance Criteria**

- When in the shopping bag, the user is able to adjust quantities and delete products from their bag. When doing so, the user should see their bag refreshed with the updated bag shown.

**Pass/Fail**

- The user is able to adjust/remove items in their bag. Stock is checked when editing their bag to ensure they cannot add a higher quantity than available stock.

#### User Story:

> As a **annonymous user**, I want to be able to checkout annonymously.

**Acceptance Criteria**

- A user is able to go through the full process of purchasing an item as an unauthenticated user.

**Pass/Fail**

- Users are able to complete the whole purchase process as an unauthenticated user; they are given the option to sign in or create an account.

#### User Story:

> As a **annonymous user**, I want to recieve an email notification of my order.

**Acceptance Criteria**

- Any user making a purchase must recieve email notification their order.

**Pass/Fail**

-  Amazon SES has been implemented as the email service; once an order is processed either by the site or through the webhook an email is sent to the user.


#### Registered User:

#### User Story:

> As a **registered user**, I want to be able to login to the site.

**Acceptance Criteria**

- A registered user is able to navigate to a login page and authenticate with the site.

**Pass/Fail**

- Using the previously mentioned [All Auth](https://django-allauth.readthedocs.io/en/latest/#) and the inbuilt django authentication; the user can login as a registered user.

#### User Story:

> As a **registered user**, I want to be able to reset my password if I had forgotten it.

**Acceptance Criteria**

- Users are able to recieve a forgotten password email should they be unathenticated on the site. They are then able to change their password.

- Users already authenticated are taken to a form to change their password; once changed they are able to login using the new password.

**Pass/Fail**

- Should the user be able to login, they can change their password using the allauth templates. 

- If the user cannot login, they can receive an change password email and be redirected to a password change form.

#### User Story:

> As a **registered user**, I want to be able to save my default information for quicker checkout processes of future purchases.

**Acceptance Criteria**

- Users information is stored in their profile; if it has been saved and they move to checkout the information is pre-filled.

**Pass/Fail**

- The user is able to select a checkbox to save their information on the checkout page, this will save their information and prefill it once the user proceeds to checkout a second time.

- The user is also able to edit and update their default information from their profile page.

#### User Story:

> As a **registered user**, I want to be able to view my previous orders and their status.

**Acceptance Criteria**

- Users must be able to view all previous orders on their profile page along with the up to date status of said order/s.

**Pass/Fail**

- The user can view all orders made from their profile and the status of the orders.

- When the order has been marked as dispatched by the store owner, the purchaser will recieve a dispatch email.


#### Admin User:

#### User Story:

> As a **admin user**, I want to be able to create, update and delete products in the store.

**Acceptance Criteria**

- The admin user is able to view the admin site and subsequently perform CRUD operations on all products within the store.

**Pass/Fail**

- The site includes a seperate admin area for the store owner, where they can see all orders, perform CRUD operations on products, delivery options and discount codes.

#### User Story:

> As a **admin user**, I want to be able to monitor and adjust product stock quantities.

**Acceptance Criteria**

- When viewing product detail, the admin user can see up to date product stock. They are also able to add/delete stock for individual products.

**Pass/Fail**

- A product stock model has been implemented with a one to one link to the product model. The owner can edit stock through the edit product page.

#### User Story:

> As a **admin user**, I want to be able to view all orders being made on the site.

**Acceptance Criteria**

- When on the admin site, the admin user is able to see all orders that have been placed (including order detail).

**Pass/Fail**

- On the admin site, the store owner is shown the most recent orders. They can also naviagte to an all orders page and from here search for orders should they need to.

#### User Story:

> As a **admin user**, I want to be able to adjust order status' and send corresponding emails to users who have made purchases.

**Acceptance Criteria**

- The admin user is able to select one or more orders and change the order status. This must trigger an email to be sent out to the email address linked to each order.

**Pass/Fail**

- The store owner can select a checkobox next to the order and mark the order as dispatched or completed. If the order/s is marked as dispatched the send_mass_mail function is used to send out all the dispatch emails.

---

### Fixed Bugs

---

---

### Known Bugs

---

---

[Return to Contents](#contents)

---

## Deployment

### Local Deployment

---

[Return to Contents](#contents)

---

## Credits

### Code

---

- To create the user model, the following tutorial was followed [here](https://testdriven.io/blog/django-custom-user-model/)

---

### Media

---

- #### Misc

---

- #### Content

---

- #### Images & Video

---

### Acknowledgements

---

---

### Disclaimer

---

This project was created for educational use only.

[Return to Contents](#contents)
