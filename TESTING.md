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
| checkout | [test_forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/test_forms.py) | ![screenshot](documentation/validation/py-checkout-test_forms.png) |
| checkout | [signals.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/signals.py) | ![screenshot](documentation/validation/py-checkout-signals.png) |
| checkout | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/urls.py) | ![screenshot](documentation/validation/py-checkout-urls.png) |
| checkout | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/views.py) | ![screenshot](documentation/validation/py-checkout-views.png) |
| checkout | [webhook_handler.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/py-checkout-webhook_handler.png) |
| checkout | [webhooks.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/checkout/webhooks.py) | ![screenshot](documentation/validation/py-checkout-webhooks.png) |
| contact | [admin.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/admin.py) | ![screenshot](documentation/validation/py-contact-admin.png) |
| contact | [forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/forms.py) | ![screenshot](documentation/validation/py-contact-forms.png) |
| contact | [models.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/models.py) | ![screenshot](documentation/validation/py-contact-models.png) |
| contact | [test_forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/contact/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/contact/test_forms.py) | ![screenshot](documentation/validation/py-contact-test_forms.png) |
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
| profiles | [test_forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/profiles/test_forms.py) | ![screenshot](documentation/validation/py-profiles-test_forms.png) |
| profiles | [urls.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/profiles/urls.py) | ![screenshot](documentation/validation/py-profiles-urls.png) |
| profiles | [views.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/profiles/views.py) | ![screenshot](documentation/validation/py-profiles-views.png) |
| services | [admin.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/admin.py) | ![screenshot](documentation/validation/py-services-admin.png) |
| services | [forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/forms.py) | ![screenshot](documentation/validation/py-services-forms.png) |
| services | [models.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/models.py) | ![screenshot](documentation/validation/py-services-models.png) |
| services | [test_forms.py](https://github.com/AlexThoma5/MP4_ecommerce/blob/main/services/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlexThoma5/MP4_ecommerce/main/services/test_forms.py) | ![screenshot](documentation/validation/py-services-test_forms.png) |
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

Defensive programming focuses on ensuring data integrity, user access control, and secure input validation across the Motion Lab site. All forms and CRUD operations were manually tested to confirm that unauthorised or invalid actions are correctly restricted.

When developing Motion Lab, multiple layers of defensive programming were implemented — including the use of the @login_required decorator to protect authorised pages, validation checks within views to ensure user == request.user, and conditional logic in Django templates using if request.user.is_superuser to restrict access to superuser-only functionality.

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| services | Feature is expected to allow users to browse services without registration. | Opened service pages as a guest user. | services were fully accessible without requiring registration. | ![screenshot](documentation/defensive/services.gif) |
| | Feature is expected to show detailed service information. | Clicked on individual services to view details. | service details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/service-details.gif) |
| Shopping bag | Feature is expected to allow customers to add items to the bag. | Added services to the bag. | Services were added successfully. | ![screenshot](documentation/defensive/add-to-bag.gif) |
| | Feature is expected to allow customers to view and manage their bag. | Opened the bag page and edited bag contents. | Bag contents were displayed and removed correctly. | ![screenshot](documentation/defensive/manage-cart.gif) |
| | Feature is expected to allow customers to apply a discount to their bag. | Added discount on bag page. | Discount is displayed and grand total is updated. | ![screenshot](documentation/defensive/discount.gif) |
| Checkout | Feature is expected to display bag items, grand total, and input fields for checkout. | Proceeded to checkout with items in the bag. | Checkout page displayed bag items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.gif) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.gif) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/email-confirmation.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.gif) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.gif) |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.gif) |
| | Feature is expected to allow users to edit their account details on profile page. | Changed account details on profile page. | Account details section reflected chnages. | ![screenshot](documentation/defensive/edit-account-details.gif) |
| Admin Features | Feature is expected to allow the site owner to create new services. | Created new services with valid data (name, price, description, image, category). | services were added successfully and displayed on the site. | ![screenshot](documentation/defensive/add-service.gif) |
| | Feature is expected to allow the site owner to update service details. | Edited service details as an admin user. | service updates were saved and displayed correctly. | ![screenshot](documentation/defensive/edit-service.gif) |
| | Feature is expected to allow the site owner to delete services. | Deleted a service from the inventory. | service was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-service.gif) |
| | Feature is expected to admins to edit company details. | Changed company details via admin panel. | New changes were updated on site. | ![screenshot](documentation/defensive/company-details.gif) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/orders.gif) |
| Contact | Feature is expected to allow users to send a contact message to site owners | Completed contact form and submitted it. | Message was successfully sent and success toast shows | ![screenshot](documentation/defensive/contact.gif) |
| | Feature is expected to send a confirmation email after contact message is sent. | Completed a contact message and checked email inbox. | Confirmation email was received. | ![screenshot](documentation/defensive/contact-email.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.gif) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse physiotherapy services without needing to register | so that I can explore available treatments before deciding to create an account. | ![screenshot](documentation/defensive/services.gif) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and access my service purchase history. | ![screenshot](documentation/features/user-story-2.gif) |
| As a customer | I would like to both in-person and virtual service options | so that I can have flexibility with my treatments. | ![screenshot](documentation/features/user-story-3.png) |
| As a customer | I would like to click on an individual service to view more details (description, duration, price) | so that I can make an informed decision before purchasing. | ![screenshot](documentation/defensive/service-details.gif) |
| As a customer | I would like to remove services from my bag | so that I can change my mind before completing payment. | ![screenshot](documentation/defensive/manage-cart.gif) |
| As a customer | I would like to proceed to checkout where I can see my selected services, total cost, and enter my personal and payment details | so that I can complete my purchase securely. | ![screenshot](documentation/defensive/checkout.gif) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident that my payment information is protected. | ![screenshot](documentation/features/user-story-7.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I have a record of my transaction and service details. | ![screenshot](documentation/defensive/email-confirmation.png) |
| As a customer | I would like to see an order confirmation page with an order number after completing my purchase | so that I know my transaction was successful. | ![screenshot](documentation/defensive/order-confirmation.gif) |
| As a returning customer | I would like to log in and view my past service purchases | so that I can keep track of my treatment history. | ![screenshot](documentation/defensive/order-history.gif) |
| As a returning customer | I would like my personal details to be remembered at checkout | so that future purchases are quicker and more convenient. | ![screenshot](documentation/features/checkout-data.gif) |
| As a site owner | I would like to create new physiotherapy services with a name, description, price, duration, images and service type | so that I can expand the services offered by the clinic. | ![screenshot](documentation/defensive/add-service.gif) |
| As a site owner | I would like to update service details (name, price, description, duration, image, service type) at any time | so that I can keep listings accurate and up to date. | ![screenshot](documentation/defensive/edit-service.gif) |
| As a site owner | I would like to delete services that are no longer offered | so that I can maintain a clear and relevant service list. | ![screenshot](documentation/defensive/delete-service.gif) |
| As a site owner | I would like to manage the clinic’s company details (e.g., address, email, opening hours, and phone number) | so that customers always have access to accurate and up-to-date information. | ![screenshot](documentation/defensive/company-details.gif) |
| As a site owner | I would like to view all customer orders | so that I can track and manage service purchases. | ![screenshot](documentation/defensive/orders.gif) |
| As a site owner | I would like to offer promotional codes | so that customers are more likely to purchase services. | ![screenshot](documentation/features/user-story-17.png) |
| As a user | I would like to see a custom 404 error page if I navigate to a non-existent page | so that I clearly understand the page cannot be found and can return to the site easily. | ![screenshot](documentation/defensive/404.gif) |
| As a user | I would like to fill out a contact form to send a message to the clinic | so that I can easily make enquiries or request further information. | ![screenshot](documentation/defensive/contact-form.gif) |
## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

A series of 17 automated tests have been conducted on the application, covering:

Forms: All forms in the `checkout`, `contact`, `profiles` and `services` apps.

Due to time constraints and the complexity of some views, this project focuses automated testing on forms, ensuring that required and optional fields are validated correctly.

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal:

- `python3 manage.py test`

All form validation behaves as expected. All tests ran 'OK'.

![screenshot](documentation/automation/test-result.png)

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`
- I then filtered for `forms`

Coverage results for the application, filtered to the forms module only:

![screenshot](documentation/automation/html-coverage.png)

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/AlexThoma5/MP4_ecommerce?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/AlexThoma5/MP4_ecommerce/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/AlexThoma5/MP4_ecommerce?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/AlexThoma5/MP4_ecommerce/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

### Known Issues

| Issue | Screenshot |
| --- | --- |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/brute-force.gif) |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsive.png) |
| If a service is in your bag/cart, but then gets deleted from the database, it throws errors from the session storage memory. | ![screenshot](documentation/issues/session-storage.png) |
| Occasionally, when logging into different accounts using Safari on iPhone, a CSRF token error may occur. This is due to how Safari on iOS handles cookies and cached session data. Refreshing the page resolves the issue. | N/A |
