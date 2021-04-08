# Milestone Project 4 - Handmade By Ellie

![Desktop Demo](link "Desktop Demo")

View live project [here](link).
---
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
        
        
        - [Colour Scheme](#colour-scheme)
        - [Fonts](#fonts)
        - [Information Architecture](#information-architecture)
    - [Wireframes](#wireframes)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks and External Resources](#frameworks-and-externalresources)
- [Testing](#testing)
    - [WC3 Validation](#wc3-validation)
    - [Lighthouse Accessibility](#lighthouse-accessibility)
    - [JSHint](#jshint)
    - [Google Dev Tools](#google-dev-tools)
    - [Responsivley](#responsivley)
    - [Manual Testing](#manual-testing)
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

---


#### User Story:

> As a **admin user**, I want to be able to create, update and delete products in the store.

**Acceptance Criteria**
- The admin user is able to view the admin site and subsequently perform CRUD operations on all products within the store.

**Implementation**

- A seperate admin site will be created for admin users to access; once here they have the ability to perform CRUD operations on the sites products.

- As well as being able to use the admin site for CRUD operations; admin users will be able to access a modal on the product pages to perform the same actions.


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

> As a **admin user**, I want to be able to adjust order status' and send corresponding.emails to users who have made purchases.

**Acceptance Criteria**
- The admin user is able to select one or more orders and change the order status. This must trigger an email to be sent out to the email address linked to each order.

**Implementation**

- A form will be used to change order status' and send orders. This will allow admin users to select multiple orders at once and mark as dispatched/completed.

---

### **The Skeleton Plane**

### Wireframes

The wireframes for phone, tablet and desktop can be found by clicking [here](https://github.com/Tmuat/handmade-by-ellie/tree/master/assets/wireframes).

[Desktop](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/wireframes/desktop.pdf)

[Tablet](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/wireframes/tablet.pdf)

[Mobile](https://github.com/Tmuat/handmade-by-ellie/blob/master/assets/wireframes/mobile.pdf)

---

#### Colour Scheme

---

#### Fonts


---

#### Landing Imagery


---
#### Information Architecture


---



[Return to Contents](#contents)

---

## Features

### Existing Features

---

#### Design

- Favicon

- Navbar 
    

- Footer

- Interaction

- Overall Design

#### Users
- User functionality


---

### Features Left to Implement

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




[Return to Contents](#contents)

---

## Testing

### WC3 Validation

---

---

### Lighthouse Accessibility

---


---

### JSHint

---

---

### Google Dev Tools

---

---

### Responsivley

---

---

### Manual Testing


---

### User Story Testing

---

Testing the user stories from the [UX Section](#ux).

#### First Time User:


#### Registered User:


#### Admin User:

---

### Fixed Bugs

---



---

### Known Bugs

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