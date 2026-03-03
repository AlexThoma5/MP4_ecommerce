# [MP4_ecommerce](https://mp4-ecommerce-390faaa8fcde.herokuapp.com)

Developer: Alex Thomas ([AlexThoma5](https://www.github.com/AlexThoma5))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/AlexThoma5/MP4_ecommerce)](https://www.github.com/AlexThoma5/MP4_ecommerce/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/AlexThoma5/MP4_ecommerce)](https://www.github.com/AlexThoma5/MP4_ecommerce/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/AlexThoma5/MP4_ecommerce)](https://www.github.com/AlexThoma5/MP4_ecommerce)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://mp4-ecommerce-390faaa8fcde.herokuapp.com)

For my Milestone Project 4, I decided to build an e-commerce store based around a business called Motion Lab. Motion Lab is a fictional physiotherapy business that is aiming to sell its services to the local community and drive traffic to its business through this modern, intuitive, responsive website.

The goal of the project is primarily to advertise services and provide users with a seamless purchasing experience. Customers can browse available physiotherapy services, interact with a fully functional store, and securely purchase the services they require.

Site administrators have full control over company details and service listings, with full CRUD functionality implemented on the front end for superusers. This ensures complete ownership and flexibility in managing the business content.

I chose to develop Motion Lab for my MS4 project because my partner is an NHS physiotherapist. It gave me the ability to simulate a real-world client–developer scenario, treating the project as if I were building a live commercial product for an actual business. Approaching the project in this way helped me design a more purposeful and industry-specific application. It also gave me valuable experience not only in building a complex e-commerce system, but in delivering a tailored solution for a specific professional sector.

![screenshot](documentation/mockup.png)

source: [MP4_ecommerce amiresponsive](https://ui.dev/amiresponsive?url=https://mp4-ecommerce-390faaa8fcde.herokuapp.com)

Live site can be found [here](https://mp4-ecommerce-390faaa8fcde.herokuapp.com).

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide a seamless and intuitive e-commerce experience for customers to browse and purchase physiotherapy services
or treatment packages.
- Enable site administrators to efficiently manage service listings, pricing, company details and customer orders.

**Primary User Needs**
- Guest users need to browse available physiotherapy services, view descriptions and pricing, and complete purchases easily.
- Registered users need a streamlined checkout experience, access to order history, and the ability to manage their accounts.
- site owners need tools to manage service listings, update pricing, and monitor customer orders.

**Business Goals**
- Drive traffic and increase revenue by offering a clear and simple online purchasing experience for physiotherapy services.
- Encourage repeat purchases through user accounts and order history tracking.
- Maintain accurate and up-to-date service listings, pricing and company details.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Service details, including name, price, description, service type, duration, and images.
- Clear navigation and calls-to-action to guide users through browsing and purchasing services.
- A simple and intuitive checkout process.
- Discount code functionality allowing users to apply promotional codes at checkout.
- Order summary and confirmation pages.
- Order history functionality for registered users.
- Automated payment confirmation emails sent to customers.
- Secure payment processing using Stripe.
- Custom 404 page to guide lost users back to relevant pages.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Services, Contact, Bag, and Account sections.
  - Logged in users get additional Profile link.
- **Hierarchy**:
  - Landing Page: Introduces the clinic and builds trust through professional messaging, visuals, and highlighted sections such as “Why Choose Us” and “What Our Patients Say”. Prominent calls-to-action, like “View Services”, guide users toward purchasing physiotherapy services.
  - Services Page: Displays all available physiotherapy services in a clear card-based layout. Each service card includes the service name, duration, truncated description, and pricing information to allow users to compare options quickly.
  - Service Detail Page: Provides the full service description, duration, and pricing information, along with an “Add to Bag” button to enable users to proceed with their purchase.
  - Cart & Checkout: Easily accessible from the navigation bar, allowing users to review their selected services, apply discount codes, and complete secure payment via Stripe.
  - Account Area (Registered Users): Enables users to view order history and manage account details.

**User Flow**
1. Guest user browses the landing page → see an overview of the clinic and reasons to choose the service, and patient testimonials to build trust and credibility.
2. Guest user clicks a clear call-to-action (“View Services”) → Is directed to the Services page.
3. Guest browses available physiotherapy services → Views descriptions and pricing.
4. Guest user selects a service → Navigates to the service detail page for more information.
5. Guest adds service to bag → Reviews bag contents on bag page.
6. Guest proceeds to checkout → Is prompted to log in or create an account if not already authenticated.
7. User Applies a discount code (if applicable) → completes secure payment via Stripe.
8. User is redirected to an order confirmation page → Receives a confirmation email with purchase details.
9. Returning customers log in → View past orders and track purchase history within their account.
10. Site administrators manage discount codes via the Django admin panel → Create and update discount codes.
11. Site administrators manage services via the frontend services page → Create, update, and delete services directly on the site.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

The website uses a light, professional theme with splashes of colour used strategically to highlight buttons. Keeping the site colours modern, professional and highly readable was the core principle for this project, emulating what you would expect from a business in the health sector. This led me to use simple colours and shades for most of the site, while keeping the website attractive by implementing the brand colours for CTAs across the site.

I used [coolors.co](https://coolors.co/000000-f9fafb-f4f6f8-652cff) to generate my color palette.

- `#000000` primary text.
- `#652cff` primary highlights.
- `rgba(33, 37, 41, 0.75)` Bootstraps muted text.

![screenshot](documentation/coolors.png)

### Typography

While maintaining a modern, Apple-esque aesthetic, I chose fonts that emphasise clarity, simplicity, and readability. My goal was to create a clean, professional look that reflects the nature of the business.

- Headings and titles use a system font stack (-apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif), ensuring San Francisco on Apple devices and appropriate native fonts on other platforms..
- [Roboto](https://fonts.google.com/specimen/Roboto) was used for all other body text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer and category icons.

## Wireframes

⚠️ INSTRUCTIONS ⚠️

If you've created wireframes or mock-ups, use this section to display screenshots of your wireframes. The example table below uses sample pages from the walkthrough project to give you some inspiration for your own project, so please adjust accordingly.

⚠️ --- END --- ⚠️

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Services | ![screenshot](documentation/wireframes/mobile-services.png) | ![screenshot](documentation/wireframes/tablet-services.png) | ![screenshot](documentation/wireframes/desktop-services.png) |
| Service Details | ![screenshot](documentation/wireframes/mobile-services-details.png) | ![screenshot](documentation/wireframes/tablet-service-details.png) | ![screenshot](documentation/wireframes/desktop-service-details.png) |
| Bag | ![screenshot](documentation/wireframes/mobile-bag.png) | ![screenshot](documentation/wireframes/tablet-bag.png) | ![screenshot](documentation/wireframes/desktop-bag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile-checkout.png) | ![screenshot](documentation/wireframes/tablet-checkout.png) | ![screenshot](documentation/wireframes/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile-checkout-success.png) | ![screenshot](documentation/wireframes/tablet-checkout-success.png) | ![screenshot](documentation/wireframes/desktop-checkout-success.png) |
| Add service | ![screenshot](documentation/wireframes/mobile-add-service.png) | ![screenshot](documentation/wireframes/tablet-add-service.png) | ![screenshot](documentation/wireframes/desktop-add-service.png) |
| Edit Service | ![screenshot](documentation/wireframes/mobile-edit-service.png) | ![screenshot](documentation/wireframes/tablet-edit-service.png) | ![screenshot](documentation/wireframes/desktop-edit-service.png) |
| Newsletter | ![screenshot](documentation/wireframes/mobile-newsletter.png) | ![screenshot](documentation/wireframes/tablet-newsletter.png) | ![screenshot](documentation/wireframes/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact.png) | ![screenshot](documentation/wireframes/tablet-contact.png) | ![screenshot](documentation/wireframes/desktop-contact.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I would like to browse physiotherapy services without needing to register | so that I can explore available treatments before deciding to create an account. |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and access my service purchase history. |
| As a customer | I would like to both in-person and virtual service options | so that I can have flexibility with my treatments. |
| As a customer | I would like to click on an individual service to view more details (description, duration, price) | so that I can make an informed decision before purchasing. |
| As a customer | I would like to view and manage my shopping cart | so that I can review my selected services before proceeding to checkout. |
| As a customer | I would like to remove services from my cart | so that I can change my mind before completing payment. |
| As a customer | I would like to proceed to checkout where I can see my selected services, total cost, and enter my personal and payment details | so that I can complete my purchase securely. |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident that my payment information is protected. |
| As a customer | I would like to receive a confirmation email after my purchase | so that I have a record of my transaction and service details. |
| As a customer | I would like to see an order confirmation page with an order number after completing my purchase | so that I know my transaction was successful. |
| As a returning customer | I would like to log in and view my past service purchases | so that I can keep track of my treatment history. |
| As a returning customer | I would like my personal details to be remembered at checkout | so that future purchases are quicker and more convenient. |
| As a site owner | I would like to create new physiotherapy services with a name, description, price, duration, images and service type | so that I can expand the services offered by the clinic. |
| As a site owner | I would like to update service details (name, price, description, duration, image, service type) at any time | so that I can keep listings accurate and up to date. |
| As a site owner | I would like to delete services that are no longer offered | so that I can maintain a clear and relevant service list. |
| As a site owner | I would like to manage the clinic’s company details (e.g., address, email, opening hours, and phone number) | so that customers always have access to accurate and up-to-date information. |
| As a site owner | I would like to view all customer orders | so that I can track and manage service purchases. |
| As a site owner | I would like to offer promotional codes | so that customers are more likely to purchase services. |
| As a user | I would like to see a custom 404 error page if I navigate to a non-existent page | so that I clearly understand the page cannot be found and can return to the site easily. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Service List | Users can view all available physiotherapy services presented in a clean card layout. Services are visually ordered by service type, with each card displaying pricing, session duration, and a short description to help users quickly compare options before viewing full details. | ![screenshot](documentation/features/service-list.png) |
| Service Details | Displays detailed information about a selected service, including its name, full description, session count, duration and price. | ![screenshot](documentation/features/service-detail.png) |
| Add to Bag | Users can add services to their shopping bag | ![screenshot](documentation/features/add-to-bag.png) |
| View Bag | Users can view the contents of their shopping bag, and remove services | ![screenshot](documentation/features/view-bag.png) |
| Checkout | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe integration. | ![screenshot](documentation/features/checkout.png) |
| Order Confirmation | Users receive an on-screen and email confirmation with details of their purchase. | ![screenshot](documentation/features/order-confirmation.png) |
| Profile Management | Users can manage their profile information, including their default delivery address and order history. | ![screenshot](documentation/features/profile-management.png) |
| Order History | Users can view their past orders and access details of each order, including services purchased and the delivery status. | ![screenshot](documentation/features/order-history.png) |
| Service Management | Superusers can add, edit, and delete services from the site via a CRUD interface. | ![screenshot](documentation/features/service-management.png) |
| Discounts | Users can apply discount codes in the bag page to save money at checkout.| ![screenshot](documentation/features/discount.png) |
| Contact | Users can submit a message via the contact form, which stores their name, email, and message in the database. | ![screenshot](documentation/features/contact.png) |
| Company Details | Admins can manage company details easily in admin panel | ![screenshot](documentation/features/company-details.png) |
| User Feedback | Clear and concise Django messages are used to provide feedback to users when interacting with various features (e.g., adding services to the bag, checking out, etc.). | ![screenshot](documentation/features/user-feedback.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/heroku.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

- **Booking Dystem**: Integrate a functional booking system that allows users to select dates, times and which physiotherapist they want to see. The booking system would update dynamically to ensure that users have no overlapping appointments.
- **Personal Injury Information**: Allow users secure access to their own private information about their injury.
- **Profile – My Exercise Programme**: Customers can securely access personalised exercise videos provided by their physiotherapist, helping them follow structured rehabilitation programmes between clinic visits.
- **Secure Patient Messaging**: Enable customers to message their physiotherapist securely through their account to ask follow-up questions about exercises or recovery.
- **Progress Tracking Dashboard**: Allow patients to track recovery and log pain levels to help aid future physio sessions.
- **Service Reviews & Ratings**: Allow customers to leave reviews and rate services, with admin moderation. Display average ratings and review counts on service pages.
- **Live Chat Support**: Provide real-time customer support through an integrated live chat or chatbot.
- **Abandoned Cart Recovery**: Automatically send emails to users who add items to their cart but don't complete the purchase, offering discounts or reminders.
- **Advanced Analytics Dashboard for Admin**: Offer an in-depth dashboard that displays sales trends, popular services, customer behavior, and more.
- **Mobile App**: Develop a mobile app for iOS and Android, providing users with a more optimized shopping experience on mobile devices.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/favicon.io-grey?logo=fi&logoColor=209CEE)](https://favicon.io) | Generating the favicon. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram

    AUTH_USER {
        int id PK
        string username
        string email
        string password
        boolean is_staff
        boolean is_active
        datetime date_joined
    }

    USER_PROFILE {
        int id PK
        int user_id FK
        string default_full_name
        string default_phone_number
    }

    SERVICE {
        int id PK
        int service_type
        string name
        text description
        decimal price
        int duration
        int session_count
        string featured_image
    }

    CONTACT_MESSAGE {
        int id PK
        string full_name
        string email
        string phone_number
        int subject
        text message
        datetime date
        boolean read
    }

    COMPANY_DETAILS {
        int id PK
        string email
        string phone_number
        text address
        datetime updated_on
    }

    ORDER {
        int id PK
        string order_number
        int user_profile_id FK
        string full_name
        string email
        string phone_number
        datetime date
        decimal order_total
        decimal grand_total
        text original_bag
        string stripe_pid
        int discount_id FK
        decimal discount_amount
    }

    ORDER_LINE_ITEM {
        int id PK
        int order_id FK
        int service_id FK
        int quantity
        decimal lineitem_total
    }

    DISCOUNT {
        int id PK
        string code
        int percentage
        boolean active
        datetime created_on
    }

    %% Relationships
    AUTH_USER ||--|| USER_PROFILE : has_one
    USER_PROFILE ||--o{ ORDER : places
    ORDER ||--o{ ORDER_LINE_ITEM : contains
    SERVICE ||--o{ ORDER_LINE_ITEM : included_in
    DISCOUNT ||--o{ ORDER : applied_to
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqtVW1v2jAQ_iuRpX6jVXkJL_mGIJ1QC1RAJ21Cskx8gDfHzhy7KqP89zmBAElAY9LyJfad7Xvu_DznLQokBeQhUH1GVoqEczEXjv2m_uTroOc72_00-ZjQDqPO63PeFIN6ZwFgvYng5Im1YmLlCBKeGTV8aIdCHCgWaSbFyUMhYCHhTqTsUfnzqVEkv3gfNY6tEQfSCF0KuwSijQKK7aGrw3m7LLU3mxt-nYyfBi-35Gdsgtjan55LYSgsieEaLw3nOJ9qYUW0lgKwMOECVAFObzyadXszPPSn0-6XvyHKErwaEULCeMlajn8spFn8gEAXLim05T1WLr0gokGzENLBybyQkgMRjgJCS3kNX7ujb7jvz7qDl-ltef0L-hQooVRZrBeAmigZUpwx5whsPOn7k9vgSEXt5V8qW8qKSMkl43CFHf_njq4UPhPMHqGWmvCy0wpa0KIzLZtUbMUE4XhBViUgyS8CHDFaUCKLU7kV883CHf0kPKkyX3b8Mhj5eDDzhzcob59bIdh5y7ng-mWI0Exvyug4E8A0hOf1OILrD6a98dtodhstkqaZXxeBCkDonGQybZBAs_dLUgqsai4y9O7OmQBPu168ZlF8oW99ft7fy-2By54TcRJAfM7v8wVnVfcseIuTiTjf568uZyLghiattFiqAgQSRZxBQjdUQSvFKPK0MlBBISjLdztFaXHnSK_BigJ5dkiJ-jlHc7GzeyIivksZZtuUNKs18paEx3a2V_PhkTpaidFyuhFBtscegbwt-kCe6z60Gi231u40Gx3XrXYqaIO8uvvQfnTbVbdZf2zWao1ac1dBv9Ogjw-deqvaaTWsq11v19y6hQDCMrCXkNnurTYqCCjTUg33j2b6du7-AP_pM7w)

## Agile Development Process

### GitHub Projects

⚠️ TIP ⚠️

Consider adding screenshots of your Projects Board(s), Issues (open and closed), and Milestone tasks.

⚠️ --- END ---⚠️

[GitHub Projects](https://www.github.com/AlexThoma5/MP4_ecommerce/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/AlexThoma5/MP4_ecommerce/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/AlexThoma5/MP4_ecommerce?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/AlexThoma5/MP4_ecommerce?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://mp4-ecommerce-390faaa8fcde.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |
| `STRIPE_WH_SECRET` | user-inserts-own-stripe-webhook-secret |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://mp4-ecommerce-390faaa8fcde.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `MP4_ecommerce`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")  # only if using Stripe Webhooks

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/AlexThoma5/MP4_ecommerce).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/AlexThoma5/MP4_ecommerce.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/AlexThoma5/MP4_ecommerce)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/AlexThoma5/MP4_ecommerce).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary](https://cloudinary.com/) | Cloud storage for media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Freepik](https://www.freepik.com/free-photo/young-hispanic-physioterapist-woman-make-arm-rehab-treatment-man-clinic_39512608.htm#fromView=search&page=1&position=0&uuid=a5004960-db26-4067-8740-3849e77a64aa&query=physio) | Hero image |
| [Flaticon](https://www.flaticon.com) | Icon images used for services |
| [ChatGPT](https://chatgpt.com/) | Used to generate logo |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [Squoosh](https://squoosh.app/) | Resize, compress and convert images to `.webp` |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.