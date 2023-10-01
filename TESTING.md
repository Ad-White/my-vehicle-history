# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate my HTML.
Inital results through testing by URI and by testing by Direct Input are as follows...

Testing By URI:

| Testing URI | W3C URL | Screenshot |
| --- | --- | --- |
| By URI | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmy-vehicle-history-451330bb3a9a.herokuapp.com%2F) | ![screenshot](documentation/html_validation/html_validation_by_url.png) |

Testing by Direct Input:

| Page | Screenshot |
| --- | --- |
| Registration | ![screenshot](documentation/html_validation/registration_page.png) |
| Sign-In | ![screenshot](documentation/html_validation/sign_in_page.png) |
| Profile | ![screenshot](documentation/html_validation/profile_page.png) |
| Show Vehicles | ![screenshot](documentation/html_validation/show_vehicles_page.png) |
| Add New Vehicle | ![screenshot](documentation/html_validation/add_new_vehicle_page.png) |
| Edit Vehicle (results - page 1) | ![screenshot](documentation/html_validation/edit_vehicle_page1.png) |
| Edit Vehicle (results - page 2) | ![screenshot](documentation/html_validation/edit_vehicle_page2.png) |
| Manage Vehicle Types | ![screenshot](documentation/html_validation/manage_vehicle_types_page.png) |
| Add New Vehicle Type | ![screenshot](documentation/html_validation/add_new_vehicle_type.png) |
| Edit Vehicle Type | ![screenshot](documentation/html_validation/edit_vehicle_type_page.png) |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
I tested the my css code by copying and testing by Direct Input.

| File | Screenshot | Notes |
| --- | --- | --- |
| style.css | ![screenshot](documentation/css_validation/mvh_css_validation.png) | Pass - No Errors Found |
|  related css warning | ![screenshot](documentation/css_validation/css_warning.png) | 1 Warning: Imported style sheets are not checked in direct input and file upload modes |

### Python and Jinja Syntax

I have used the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) application in order to test my Python and Jinja syntax.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| app.py - Inital Test Result | --- | ![screenshot](documentation/python_linter_results/ci_python_linter_first_test.png) | 1 case of trailing whitespace. No newline at end of file |
| app.py - Final Test Result | [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ad-White/my-vehicle-history/main/app.py) | ![screenshot](documentation/python_linter_results/ci_python_linter_result.png) | All clear, no errors found |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Register | Sign-In | Profile | Show Vehicles | Add New Vehicle | Edit Vehicle | Manage Vehicle Types | Add Vehicle Type | Edit Vehicle Type | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/desktop_chrome/register_chrome.png) | ![screenshot](documentation/desktop_chrome/sign_in_chrome.png) | ![screenshot](documentation/desktop_chrome/profile_chrome.png) | ![screenshot](documentation/desktop_chrome/show_vehicles_chrome.png) | ![screenshot](documentation/desktop_chrome/add_new_vehicle_chrome.png) | ![screenshot](documentation/desktop_chrome/edit_vehicle_chrome.png) | ![screenshot](documentation/desktop_chrome/manage_vehicle_types_chrome.png) | ![screenshot](documentation/desktop_chrome/add_vehicle_type_chrome.png) | ![screenshot](documentation/desktop_chrome/edit_vehicle_type_chrome.png) | Works as expected |
| Safari | ![screenshot](documentation/mobile_safari/register_mobile.png) | ![screenshot](documentation/mobile_safari/sign_in_mobile.png) | ![screenshot](documentation/mobile_safari/profile_mobile.png) | ![screenshot](documentation/mobile_safari/show_vehicles_mobile.png) | ![screenshot](documentation/mobile_safari/add_new_vehicle_mobile.png) | ![screenshot](documentation/mobile_safari/edit_vehicle_mobile.png) | ![screenshot](documentation/mobile_safari/manage_vehicle_types_mobile.png) |  ![screenshot](documentation/mobile_safari/add_vehicle_type_mobile.png) | ![screenshot](documentation/mobile_safari/edit_vehicle_type_mobile.png) | Minor CSS difference with logo font not being italic |
| Firefox | ![screenshot](documentation/desktop_firefox/register_firefox.png) | ![screenshot](documentation/desktop_firefox/sign_in_firefox.png) | ![screenshot](documentation/desktop_firefox/profile_firefox.png) | ![screenshot](documentation/desktop_firefox/show_vehicles_firefox.png) | ![screenshot](documentation/desktop_firefox/add_new_vehicle_firefox.png) | ![screenshot](documentation/desktop_firefox/edit_vehicle_firefox.png) | ![screenshot](documentation/desktop_firefox/manage_vehicle_types_firefox.png) | ![screenshot](documentation/desktop_firefox/add_vehicle_type_firefox.png) | ![screenshot](documentation/desktop_firefox/edit_vehicle_type_firefox.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Browser | Register | Sign-In | Profile | Show Vehicles | Add New Vehicle | Edit Vehicle | Manage Vehicle Types | Add Vehicle Type | Edit Vehicle Type | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile |  ![screenshot](documentation/mobile_safari/register_mobile.png) | ![screenshot](documentation/mobile_safari/sign_in_mobile.png) | ![screenshot](documentation/mobile_safari/profile_mobile.png) | ![screenshot](documentation/mobile_safari/show_vehicles_mobile.png) | ![screenshot](documentation/mobile_safari/add_new_vehicle_mobile.png) | ![screenshot](documentation/mobile_safari/edit_vehicle_mobile.png) | ![screenshot](documentation/mobile_safari/manage_vehicle_types_mobile.png) |  ![screenshot](documentation/mobile_safari/add_vehicle_type_mobile.png) | ![screenshot](documentation/mobile_safari/edit_vehicle_type_mobile.png) | Works as expected |
| Tablet |  ![screenshot](documentation/tablet_chrome/register_tablet.png) | ![screenshot](documentation/tablet_chrome/sign_in_tablet.png) | ![screenshot](documentation/tablet_chrome/profile_tablet.png) | ![screenshot](documentation/tablet_chrome/show_vehicles_tablet.png) | ![screenshot](documentation/tablet_chrome/add_new_vehicle_tablet.png) | ![screenshot](documentation/tablet_chrome/edit_vehicle_tablet.png) | ![screenshot](documentation/tablet_chrome/manage_vehicle_types_tablet.png) |  ![screenshot](documentation/tablet_chrome/add_vehicle_type_tablet.png) | ![screenshot](documentation/tablet_chrome/edit_vehicle_type_tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/desktop_chrome/register_chrome.png) | ![screenshot](documentation/desktop_chrome/sign_in_chrome.png) | ![screenshot](documentation/desktop_chrome/profile_chrome.png) | ![screenshot](documentation/desktop_chrome/show_vehicles_chrome.png) | ![screenshot](documentation/desktop_chrome/add_new_vehicle_chrome.png) | ![screenshot](documentation/desktop_chrome/edit_vehicle_chrome.png) | ![screenshot](documentation/desktop_chrome/manage_vehicle_types_chrome.png) | ![screenshot](documentation/desktop_chrome/add_vehicle_type_chrome.png) | ![screenshot](documentation/desktop_chrome/edit_vehicle_type_chrome.png) | Works as expected |
