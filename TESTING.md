# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| home | [index.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/home/templates/home/index.html) | [W3C Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmp4-ecommerce-390faaa8fcde.herokuapp.com%2F) | ![screenshot](documentation/validation/html-home-index.png) | |
| services | [services.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/templates/services/services.html) | N/A | ![screenshot](documentation/validation/html-services-services.png) | Validated by direct input - No link, Includes service-modal.html and delete-modal.html |
| services | [service_detail.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/templates/services/service_detail.html) | [W3C Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmp4-ecommerce-390faaa8fcde.herokuapp.com%2Fservices%2F8%2F) | ![screenshot](documentation/validation/html-services-service_detail.png) | |
| bag | [bag.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/bag/templates/bag/bag.html) | [W3C Link](https://validator.w3.org/nu/?doc=https://mp4-ecommerce-390faaa8fcde.herokuapp.com/bag/&out=html) | ![screenshot](documentation/validation/html-bag-bag.png) | |
| checkout | [checkout.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/templates/checkout/checkout.html) | N/A | ![screenshot](documentation/validation/html-checkout-checkout.png) | Validated by direct input - No link |
| checkout | [checkout_success.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/templates/checkout/checkout_success.html) | N/A | ![screenshot](documentation/validation/html-checkout-checkout_success.png) | Validated by direct input - No link |
| contact | [contact.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/templates/contact/contact.html) | [W3C Link](https://validator.w3.org/nu/?doc=https://mp4-ecommerce-390faaa8fcde.herokuapp.com/contact/&out=html) | ![screenshot](documentation/validation/html-contact-contact.png) | |
| profiles | [profile.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/templates/profiles/profile.html) | N/A | ![screenshot](documentation/validation/html-profiles-profile.png) | Validated by direct input - No link, includes edit-contact-modal.html |
| templates | [400.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/templates/errors/400.html) | N/A | ![screenshot](documentation/validation/html-templates-400.png) | Validated by direct input - No link |
| templates | [403.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/templates/errors/403.html) | N/A | ![screenshot](documentation/validation/html-templates-403.png) | Validated by direct input - No link |
| templates | [404.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/templates/errors/404.html) | N/A | ![screenshot](documentation/validation/html-templates-404.png) | Validated by direct input - No link |
| templates | [500.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/templates/errors/500.html) | N/A | ![screenshot](documentation/validation/html-templates-500.png) | Validated by direct input - No link |
| templates | [signup.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/templates/account/signup.html) | [W3C Link](https://validator.w3.org/nu/?doc=https://mp4-ecommerce-390faaa8fcde.herokuapp.com/accounts/signup/&out=html) | ![screenshot](documentation/validation/html-templates-signup.png) | |
| templates | [login.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/templates/account/login.html) | [W3C Link](https://validator.w3.org/nu/?doc=https://mp4-ecommerce-390faaa8fcde.herokuapp.com/accounts/login/&out=html) | ![screenshot](documentation/validation/html-templates-login.png) | |
| templates | [logout.html](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/templates/account/logout.html) | N/A | ![screenshot](documentation/validation/html-templates-logout.png) | Validated by direct input - No link |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [base.css](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/static/css/base.css) | [W3C link](https://jigsaw.w3.org/css-validator/validator?uri=https://mp4-ecommerce-390faaa8fcde.herokuapp.com/static/css/base.css&output=html) | ![screenshot](documentation/validation/css-static-base.png) | |
| home | [home.css](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/home/static/home/css/home.css) | [W3C link](https://jigsaw.w3.org/css-validator/validator?uri=https://mp4-ecommerce-390faaa8fcde.herokuapp.com/static/home/css/home.css&output=html#warnings) | ![screenshot](documentation/validation/css-home-home.png) | |
| checkout | [checkout.css](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/static/checkout/css/checkout.css) | N/A | ![screenshot](documentation/validation/css-checkout-checkout.png) | Validated by direct input |
| services | [services.css](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/static/services/css/services.css) | N/A | ![screenshot](documentation/validation/css-services-services.png) | Validated by direct input |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [stripe_elements.js](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/static/checkout/js/stripe_elements.js) |  | ![screenshot](documentation/validation/js-checkout-stripe_elements.png) | Only warnings that show are from external libraries |
| profiles | [profile.js](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/static/profiles/js/profile.js) |  | ![screenshot](documentation/validation/js-profiles-profile.png) | |
| services | [services.js](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/static/services/js/services.js) |  | ![screenshot](documentation/validation/js-services-services.png) | Only warnings that show are from external libraries |
| static | [base.js](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/static/js/base.js) |  | ![screenshot](documentation/validation/js-static-base.png) | Only warnings that show are from external libraries |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
| bag | [contexts.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/bag/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/bag/contexts.py) | ![screenshot](documentation/validation/py-bag-contexts.png) |
| bag | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/bag/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/bag/urls.py) | ![screenshot](documentation/validation/py-bag-urls.png) |
| bag | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/bag/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/bag/views.py) | ![screenshot](documentation/validation/py-bag-views.png) |
| checkout | [admin.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/admin.py) | ![screenshot](documentation/validation/py-checkout-admin.png) |
| checkout | [forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/forms.py) | ![screenshot](documentation/validation/py-checkout-forms.png) |
| checkout | [models.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/models.py) | ![screenshot](documentation/validation/py-checkout-models.png) |
| checkout | [signals.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/signals.py) | ![screenshot](documentation/validation/py-checkout-signals.png) |
| checkout | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/urls.py) | ![screenshot](documentation/validation/py-checkout-urls.png) |
| checkout | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/views.py) | ![screenshot](documentation/validation/py-checkout-views.png) |
| checkout | [webhook_handler.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/py-checkout-webhook_handler.png) |
| checkout | [webhooks.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/webhooks.py) | ![screenshot](documentation/validation/py-checkout-webhooks.png) |
| contact | [admin.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/admin.py) | ![screenshot](documentation/validation/py-contact-admin.png) |
| contact | [forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/forms.py) | ![screenshot](documentation/validation/py-contact-forms.png) |
| contact | [models.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/models.py) | ![screenshot](documentation/validation/py-contact-models.png) |
| contact | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/urls.py) | ![screenshot](documentation/validation/py-contact-urls.png) |
| contact | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/views.py) | ![screenshot](documentation/validation/py-contact-views.png) |
| home | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) |
| home | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) |
| main | [settings.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/main/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/main/settings.py) | ![screenshot](documentation/validation/py-main-settings.png) |
| main | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/main/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/main/urls.py) | ![screenshot](documentation/validation/py-main-urls.png) |
| main | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/main/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/main/views.py) | ![screenshot](documentation/validation/py-main-views.png) |
|  | [manage.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) |
| profiles | [forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/profiles/forms.py) | ![screenshot](documentation/validation/py-profiles-forms.png) |
| profiles | [models.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/profiles/models.py) | ![screenshot](documentation/validation/py-profiles-models.png) |
| profiles | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/profiles/urls.py) | ![screenshot](documentation/validation/py-profiles-urls.png) |
| profiles | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/profiles/views.py) | ![screenshot](documentation/validation/py-profiles-views.png) |
| services | [admin.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/admin.py) | ![screenshot](documentation/validation/py-services-admin.png) |
| services | [forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/forms.py) | ![screenshot](documentation/validation/py-services-forms.png) |
| services | [models.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/models.py) | ![screenshot](documentation/validation/py-services-models.png) |
| services | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/urls.py) | ![screenshot](documentation/validation/py-services-urls.png) |
| services | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/views.py) | ![screenshot](documentation/validation/py-services-views.png) |


## Responsiveness

I've tested my deployed project to check for responsiveness issues. To carry out these tests I used Google Chrome's device emulator. The three devices I chose to use were:

| Device              | CSS Viewport (Width × Height) | Notes                              |
|---------------------|-------------------------------|------------------------------------|
| iPhone 14 Pro Max   | 430 × 932                     | Chrome DevTools preset             |
| iPad Mini           | 768 × 1024                    | Chrome DevTools preset             |
| MacBook Air (full screen) | ~1470 × 956              | Actual viewport in Chrome window   |


| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Services | ![screenshot](documentation/responsiveness/mobile-services.png) | ![screenshot](documentation/responsiveness/tablet-services.png) | ![screenshot](documentation/responsiveness/desktop-services.png) | Works as expected |
| Service Details | ![screenshot](documentation/responsiveness/mobile-service-detail.png) | ![screenshot](documentation/responsiveness/tablet-service-detail.png) | ![screenshot](documentation/responsiveness/desktop-service-detail.png) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/desktop-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Add Service Modal | ![screenshot](documentation/responsiveness/mobile-add-service.png) | ![screenshot](documentation/responsiveness/tablet-add-service.png) | ![screenshot](documentation/responsiveness/desktop-add-service.png) | Works as expected |
| Edit Service Modal | ![screenshot](documentation/responsiveness/mobile-edit-service.png) | ![screenshot](documentation/responsiveness/tablet-edit-service.png) | ![screenshot](documentation/responsiveness/desktop-edit-service.png) | Works as expected |Service
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Logout | ![screenshot](documentation/responsiveness/mobile-logout.png) | ![screenshot](documentation/responsiveness/tablet-logout.png) | ![screenshot](documentation/responsiveness/desktop-logout.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

For testing the live/deployed site, I used three different browsers: Google Chrome, Safari, and Mozilla Firefox. The goal was to ensure consistent functionality, layout, and performance across multiple environments.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Services | ![screenshot](documentation/browsers/chrome-services.png) | ![screenshot](documentation/browsers/firefox-services.png) | ![screenshot](documentation/browsers/safari-services.png) | Works as expected |
| Service Details | ![screenshot](documentation/browsers/chrome-service-detail.png) | ![screenshot](documentation/browsers/firefox-service-detail.png) | ![screenshot](documentation/browsers/safari-service-detail.png) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/firefox-checkout.png) | ![screenshot](documentation/browsers/safari-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/safari-checkout-success.png) | Works as expected |
| Add Service Modal | ![screenshot](documentation/browsers/chrome-add-service.png) | ![screenshot](documentation/browsers/firefox-add-service.png) | ![screenshot](documentation/browsers/safari-add-service.png) | Works as expected |
| Edit Service Modal | ![screenshot](documentation/browsers/chrome-edit-service.png) | ![screenshot](documentation/browsers/firefox-edit-service.png) | ![screenshot](documentation/browsers/safari-edit-service.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/safari-profile.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/firefox-contact.png) | ![screenshot](documentation/browsers/safari-contact.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Logout | ![screenshot](documentation/browsers/chrome-logout.png) | ![screenshot](documentation/browsers/firefox-logout.png) | ![screenshot](documentation/browsers/safari-logout.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Overall, the audit helped me catch performance, accessibility, and SEO improvements to make the app more reliable and user-friendly.

Some lower scores, such as the Best Practices metric, were caused by third-party resources like Stripe and Cloudinary, which are outside of my control.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Services | ![screenshot](documentation/lighthouse/mobile-services.png) [!IMPORTANT] CRUD Modals are included within the services page| ![screenshot](documentation/lighthouse/desktop-services.png) [!IMPORTANT] CRUD Modals are included within the services page|
| Service Details | ![screenshot](documentation/lighthouse/mobile-service-detail.png) | ![screenshot](documentation/lighthouse/desktop-service-detail.png) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop-bag.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/products.png) |
| | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.png) |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.png) |
| | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.png) |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.png) |
| | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-product.png) |
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-product.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-product.png) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders.png) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email addresses for newsletter registration. | Email addresses were successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/features/feature01.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/feature02.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](documentation/features/feature03.png) |
| As a customer | I would like to browse various product categories (clothing, toys, jewelry, kitchen gadgets, etc.) | so that I can easily find what I'm looking for. | ![screenshot](documentation/features/feature04.png) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/features/feature05.png) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](documentation/features/feature06.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/feature07.png) |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. | ![screenshot](documentation/features/feature08.png) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/features/feature09.png) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/features/feature10.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/features/feature11.png) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/features/feature12.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/feature13.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/feature14.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/feature15.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/features/feature16.png) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/features/feature17.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/features/feature18.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/features/feature19.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/feature20.png) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/features/feature21.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/features/feature22.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/feature23.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/AlexThoma5/MP4_ecommerce/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/AlexThoma5/MP4_ecommerce?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/AlexThoma5/MP4_ecommerce/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issue custom search](https://img.shields.io/github/issues-search/AlexThoma5/MP4_ecommerce?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/checkout-success.png) |
| If a product is in your bag/cart, but then gets deleted from the database, it throws errors from the session storage memory. | ![screenshot](documentation/issues/session-storage.png) |
| The `-`/`+` quantity buttons work well on "product_details.html", but not on "bag.html". | ![screenshot](documentation/issues/quantity-buttons.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

