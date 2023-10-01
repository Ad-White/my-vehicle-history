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

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.
These are the results after inital testing. Testing conducted for both Navigation and Snapshots on mobile and desktop.

| Test Used | Page | Size | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Navigation | --- | Mobile | ![screenshot](documentation/lighthouse_reports/navigation_reports/lighthouse_navigation_report_mobile.png) | Performance related issues regarding handling of images. ARIA IDs are not unique (modal related). Issues were logged in the Issues panel in Chrome Devtools, related to cloudinary images used. |
| Navigation | --- | Desktop | ![screenshot](documentation/lighthouse_reports/navigation_reports/lighthouse_navigation_report_desktop.png) | Performance related issues regarding handling of images. ARIA IDs are not unique (modal related). Issues were logged in the Issues panel in Chrome Devtools, related to cloudinary images used. |

| Test Used | Page | Size | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Snapshot | Registration | Mobile| ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_register.png) | --- |
| Snapshot | Sign-In | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_sign_in.png) | --- |
| Snapshot | Profile | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_profile.png) | --- |
| Snapshot | Show Vehicles | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_show_vehicles.png) | --- |
| Snapshot | Add New Vehicle | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_add_new_vehicle.png) | --- |
| Snapshot | Edit Vehicle | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_edit_vehicle.png) | --- |
| Snapshot | Manage Vehicle Types | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_manage_vehicle_types.png) | --- |
| Snapshot | Add Vehicle Type | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_add_vehicle_type.png) | --- |
| Snapshot | Edit Vehicle Type | Mobile |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_mobile/lighthouse_snapshot_edit_vehicle_type.png) | --- |
| Snapshot | Registration | Desktop | ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_register.png) | --- |
| Snapshot | Sign-In | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_sign_in.png) | --- |
| Snapshot | Profile | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_profile.png) | --- |
| Snapshot | Show Vehicles | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_show_vehicles.png) | --- |
| Snapshot | Add New Vehicle | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_add_new_vehicle.png) | --- |
| Snapshot | Edit Vehicle | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_edit_vehicle.png) | --- |
| Snapshot | Manage Vehicle Types | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_manage_vehicle_types.png) | --- |
| Snapshot | Add Vehicle Type | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_add_vehicle_type.png) | --- |
| Snapshot | Edit Vehicle Type | Desktop |  ![screenshot](documentation/lighthouse_reports/snapshot_reports_desktop/lighthouse_snapshot_edit_vehicle_type.png) | --- |

### WAVE Reports

I have tested the website using WAVE, [Web Accessibility Evaluation](https://my-vehicle-history-451330bb3a9a.herokuapp.com/) to check for any major issues.
These are the results after inital testing.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Registration | ![screenshot](documentation/wave_reports/wave_register.png) | No Errors. 2 alerts related to `<h1>` tag not present and Arai-Current Page Selection |
| Sign_In | ![screenshot](documentation/wave_reports/wave_sign_in.png) | No errors. 3 alerts related to `<h1>` tag not present and Arai-Current Page Selection. Register Account link - Adjacent links go to the same URL. |
| Profile | --- | Would not allow testing |
| Show Vehicles | ![screenshot](documentation/wave_reports/wave_show_vehicles.png) | No Errors. 2 alerts related to `<h1>` tag not present and Arai-Current Page Selection |
| Add Vehicle | ![screenshot](documentation/wave_reports/wave_add_vehicle.png) | No errors. 2 alerts related to `<h1>` tag not present and Arai-Current Page Selection |
| Edit Vehicle | ![screenshot](documentation/wave_reports/wave_edit_vehicle.png) | 2 errors, related to radio selectors having same ID. 4 alerts, `<h1>` tag not present and Arai-Current Page Selection. The other 2 related to the radio selectors |
| Manage Vehicle Types | ![screenshot](documentation/wave_reports/wave_manage_vehicle_types.png) | No errors. 7 alerts related to heading tag hierachy |
| Add Vehicle Type | ![screenshot](documentation/wave_reports/wave_add_vehicle_type.png) | 2 errors, related to radio selectors having same ID. 3 alerts, `<h1>` tag not present and Arai-Current Page Selection. |
| Edit Vehicle Type | ![screenshot](documentation/wave_reports/wave_edit_vehicle_type.png) | No errors. 2 alerts related to `<h1>` tag not present and Arai-Current Page Selection |

I have since attempted to reduce and eliminate any remaining errors and alerts. See the Bugs and Issues section for more information.

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to view a selection of vehicles consisting of those presented by the existing member's of the website. | ![screenshot](documentation/show_vehicles.png) |
| As a new site user,  I would like to be able to preform a search through the vehicles on the Show Vehicles page by either, make, model or vehicle type. | ![screenshot](documentation/search_bar.png) |
| As a new site user, I would like to be able to have a way to easily navigate my way around the site. | ![screenshot](documentation/navigation_system.png)  |
| As a new site user,  I would like to register as a new site member, and have access to my own profile area. With the ability to be able to upload details of my vehicle, including an image of my vehicle. | ![screenshot](documentation/user_story_profile.png) |
| As a new site user, I would like to be able to edit the details and image of my vehicle, and to save those changes. | ![screenshot](documentation/crud.png) |
| As a new site user, I would like the ability to add my own vehicle to the Show Vehicles page, alongside other site member's vehicles. | ![screenshot](documentation/show_vehicle.png) |
| As a new site user, I would like the ability to not add my own vehicle to the Show Vehicles page, alongside other site member's vehicles. I would prefer if it were kept private to myself. | ![screenshot](documentation/not_show_vehicle.png) |
| As a new site user, I would like to be able to delete any of my vehicles from my collection if I choose.
 | ![screenshot](documentation/deletion_confirmation.png) |
| As a new site user, I would like the ability to sign out of the website. | ![screenshot](documentation/sign_out.png) |
