# My Vehicle History

The purpose of this website is to provide users with somewhere to keep a log of their vehicles. Whether currently and/or previously owned.
With this application I hope to provide a solution to the real world case, I have experienced myself over the years. With regards to people I have met or know, who are enthusiastic about their own vehicles.
Typically during a discussion about vehicles we have owned, I find it would be nice to actually see a photograph of the vehicle in question. Only to remember it's tucked away in a drawer or on an old phone or a hard-drive, somewhere!
With the above in mind, I have decided to call this website, My Vehicle History.

You can view the site on Am I Responsive [here](https://ui.dev/amiresponsive?url=https://my-vehicle-history-451330bb3a9a.herokuapp.com/)

The live link can be found [here](https://my-vehicle-history-451330bb3a9a.herokuapp.com/)

## User Experience (UX)

My intended and expected audience will consist of friends and people I know, that have a passion for their vehicles. Also, generally anyone that would like to use the sites services to keep a log of their vehicles, or just for the pleasure of viewing a selection of other member's cars, motorcycles, etc.
My intention has been to design a website that is visually pleasing, easy to use, and one which I hope my audience will enjoy using. And will return to again in time, to add more content to their vehicle history.

## User Stories

### New Site Users

- As a new site user, I would like to view a selection of vehicles consisting of those presented by the existing member's of the website.

- As a new site user, I would like to be able to preform a search through the vehicles on the Show Vehicles page by either, make, model or vehicle type.

- As a new site user, I would like to be able to have a way to easily navigate my way around the site.

- As a new site user, I would like to register as a new site member, and have access to my own profile area. With the ability to be able to upload details of my vehicle, including an image of my vehicle.

- As a new site user, I would like to be able to edit the details and image of my vehicle, and to save those changes.

- As a new site user, I would like the ability to add my own vehicle to the Show Vehicles page, alongside other site member's vehicles.

- As a new site user, I would like the ability to not add my own vehicle to the Show Vehicles page, alongside other site member's vehicles. I would prefer if it were kept private to myself.

- As a new site user, I would like to be able to delete any of my vehicles from my collection if I choose.

- As a new site user, I would like the ability to sign out of the website.

### Returning Site Users

- As a returning site user, I would like to able to sign back in to the site so that I can see my own profile.

- As a returning site user, I would like all of the abilities of a new user, so that I can create, edit and delete vehicles from my vehicle history.

### Site Administrator

- As a site administrator, I should be able to sign-in to the website and have more priviledges than a general user.

- As a site administrator, I should be able to edit the names used for the vehicle types selection options.

- As a site administrator, I should be able to create new vehicle types to be used within the vehicle types selection options.

- As a site administrator, I should be able to delete any vehicle type.

## Design

### Colour Scheme

I have chosen a colour scheme that I hope gives the site a clean look, and one that is visually appealing to the user.
I have chosen British Racing Green as the main site colour used for the logo, the navbar and favicon. I hope it portraits a sense of history.
I opted to use an off white colour called, Seasalt for the background. In order to help emphasis the white colour of the card components on display. Seasalt is also used for any white based text within the site.
For the main text colour, I choose Oxford Blue in order to maintain a very good contrast to the background colours in use.
As for the buttons used throughout the site. I decided to use a discordant colour combination. Hopefully making it more intuitive for the user as to what kind of action each may perform. Penn Red and True Blue.

- `# 004225` - British Racing Green - Logo, favicon and navigation.
- `# 0A122A` - Oxford Blue - General text, headings, labels.
- `# FBFAF8` - Seasalt - Background colour, text used in logo and favicon.
- `# 3066BE` - True Blue - Button.
- `# A00005` - Penn Red - Button.

![screenshot](documentation/colours/mvh_colours.png/)

### Typography

I wanted to use two differing but complimenting typfaces. One to be used for the site logo, the other for general use. I wanted to use typefaces that look modern against the 'historical' green in the colour scheme.
I opted for Montserrat italic for the logo.

- ![screenshot](documentation/typography/montserrat_mvh.png/)
- [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montserrat)

 Dosis for all other text.

- ![screenshot](documentation/typography/dosis_mvh.png/)
- [Dosis](https://fonts.google.com/specimen/Dosis?query=dosis)

### Imagery

All images used throughout this site have been...

## Database Design

My project uses a non-relational database with MongoDB, and therefore the database architecture doesn't have actual relationships like a relational database would.

My database is called **my_vehicle_history**.

It contains 3 collections:

- **vehicle_types**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | vehicle_type | String | |

- **vehicles**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | vehicle_type | String | selected from *vehicle_types* collection |
    | make | String | |
    | model | String | |
    | capacity | String | |
    | year | String | |
    | colour | String | |
    | current_owner | String | |
    | show_my_vehicle | String | |
    | description | String | |
    | image_url | String | |
    | litres_cc | String | |
    | created_by | String | selected from the *users* collection |

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (SHA) |
