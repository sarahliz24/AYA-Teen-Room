#  AYA Teen Room

![Welcome image](#)

## Site Link: <a href="" target="_blank">#</a>

1. [Introduction](#introduction)
2. [User Experience](#user-experience)
3. [Design](#design)
4. [Features](#features)
5. [Future Features](#future-features)
6. [Testing](#testing)
    1. [Validator Testing](#validator-testing)
    2. [Manual Testing](#manual-testing)
7. [Bugs](#bugs)
    1. [Known Bugs](#known-bugs)
    2. [Solved Bugs](#solved-bugs)
8. [Deployment](#deployment)
    1. [Github](#github)
    2. [Heroku](#heroku)
9. [Credits](#credits)
    1. [Code Used](#code-used)
    2. [Content](#content)
    3. [Technologies Used](#technologies-used)
10. [Acknowledgements](#acknowledgements)

## Site Link: (https://#)


# INTRODUCTION

Intro text goes here

# User Experience

## Target Audience
Describe the target audience

## User Stories

### As a user I want to:

uSer stories go here

## As the site owner I want:

site owner goals go here

# DESIGN

## Colour scheme

<details><summary>Colour scheme</summary>
    <img src="#">
</details>

The colour scheme was chosen to....  A bright, contrasting colour palatte was selected, and then the yellow colour was manually edited to match the yellow from the background image, for a cohesive look.

The colours chosen were:
* Palatinate Blue #0043DE 
* Poppy #DF2935
* Sunglow #FDCA40
* Platinum #E6E8E6

## Typograhy

The primary font, used for the site heading, buttons and warnings, is ###. This is a fun pop-art style font that reflects the site ethos. A default font of cursive was set as this will still reflect the fun ethos of the site in case Bangers cannot be loaded.

The secondary font used is...

## Imagery

<details><summary>#</summary>
    <img src="#">
</details>

The background is set to a simple black and yellow image of repeating question marks.  This helps the user to quickly identify the purpose of the site (i.e. a quiz), and fits with the bright pop-art theme.  A background colour of Sunglow #FDCA40 (from the above colour palette) was added as the default background in case the image does not load, in order to maintain the colour scheme of the site, if needed.

## Wireframes

Wireframes for the project are below.  Mobile and desktop wireframes were produced using Balsamiq.  Final product is consistent with the intention and design of the wireframe designs.

 <details><summary>Home Page Mobile</summary>
    <img src="#">
</details>

<details><summary>Home Page Desktop</summary>
    <img src="#">
</details>

<details><summary>Feedback Page Mobile</summary>
    <img src="#">
</details>

<details><summary>Feedback Page Desktop</summary>
    <img src="#">
</details>

<details><summary>About Mobile</summary>
    <img src="#">
</details>

<details><summary>About Desktop</summary>
    <img src="#">
</details>
---
# Technical Design

## Flowchart

Designed at planning stage of application, the chart was used to guide the development process while building the application.  The initial flowchart closely reflects the structure of the finished application.
<details><summary>#  Flowchart</summary>
    <img src="#">
</details>

## Data Models

....

# Features

## Welcome page & Description
Introduction: display logo, explain purpose of application, give menu option to enter application.
* User story #

<details><summary>Welcome page</summary>
    <img src="#">
</details>

## Menu options
* User story #

There are two main menus, allowing the user to select options to proceed, or return to main menu. Menu options and headings are displayed in blue for consistency and to highlight purpose to user. 
* User story 15
<details><summary>Main menu</summary>
    <img src="#">
</details>
<details><summary>Search menu</summary>
    <img src="#">
</details>

## Add new staff member
User can enter a new staff member, adding first name, last name, and position (with prompts for position). User cannot enter a duplicate staff member.
* User story 5

<details><summary>#</summary>
    <img src="#">
</details>

## Update staff skills
* User story #
* User story #

User can search for an existing staff member, and when successfully found, can enter a new skill for that staff member. Staff members current skill status is displayed to user, along with a list of available skills to add. After skill entry user is prompted to enter another skill or return to main menu.  User cannot enter duplicate skills for the staff member.
<details><summary>Enter skills</summary>
    <img src="#">
</details>

## Search by staff member
* User story #
* User story #
* User story #

User can search for a staff member and see a list of their assigned skills.  User given option to search for another staff member or update that staff member's skills. 
<details><summary>#</summary>
    <img src="#">
</details>

## Search by skill
* User story #
* User story #
* User story #

User can search by skill.  User is presented with a list of skill to choose from.  Then presented with a list of staff assigned that skill. Staff position is displayed in this list as it can assist with decision making in rostering situations to ensure correct skill mix. User then given option to search for another skill or search by staff member. User cannot search for a skill that is not on the list.
<details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>

## Warnings
* User story #
* User story #
* User story #
* User story #

Throughout the application the user is given warnings for incorrect entries such as entering numbers out of range, entering letters instead of numbers (and vice versa), failed searches (e.g. no staff found by name entered), entering duplicate information.  Warnings are displayed in red to highlight to user.  After each warning a new input is requested or a menu selection is provided.
<details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>

## User feedback
* User story #
* User story #
* User story #
* User story #

User is given feedback through the application.  Feedback is displayed in green for user experience.  User is informed when information is successfully stored (with a short time delay added to give the impression the system is doing "work"). User entries are displayed to user at all times to check user is satisfied with their input before further action.
<details><summary>#</summary>
    <img src="#">
</details>
    <details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>

## Google Sheets
* User story #

Google sheets showing data entry.  Can be used for reference if testing the application (i.e. to find existing users or skills etc).
<details><summary>#/summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>
<details><summary>#</summary>
    <img src="#">
</details>




# Future Features

* ...
* ...
* ...



# TESTING

## Validator Testing

The code was regularly tested using the Code Institute PEP Validator substitute
<a href="https://pep8ci.herokuapp.com/" target="_blank">CI Python Linter</a>.  All tests passed with no warnings or errors.

<details><summary>CI Python Linter Results</summary>
    <img src="#">
</details>

## Manual Testing

# Example...
| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Main Menu | Select 0 to exit | Exits program | Works as expected |
| Main Menu |  Select  1 to enter new staff member | Sends user to: Enter new staff member section  | Works as expected |
| Main Menu |  Select  2 to update skills for  a staff member | Sends user to: Find staff member section | Works as expected |
| Main Menu | Select 3 to search records by  skill or staff member | Sends user to: Search menu options section | Works as expected |
| Main Menu | Select number other than 0-3 | Warning message to user:  "Please choose number 0 -3 from the menu" | Works as expected |
| Main Menu | Select non-number input e.g. 'g' | Warning message to user: "Please choose a number (only) from the menu" | Works as expected |



# BUGS

## Known Bugs
...

 ## Solved Bugs
...

# DEPLOYMENT

This site can be forked using Github as follows (to make a copy in your own repo)

## Github

2. Go to **Fork** button on the right-side ribbon menu (between **Unwatch** and **Star**)
3. Click the button to make a copy automatically into your own respository
4. **Owner** will default to your own github name
5. Add a repository name and an optional  
5. Add a repository name and an optional description 
6. Select **Create Fork** button

This site can be cloned using Github as follows (to make a copy on your own machine):

1. Enter the relevant Github repository
2. Click the green **Code** from the menu (to the left of the green **Gitpod** button)
2. Click the green **Code** button from the menu (to the left of the green **Gitpod** button)
3. Copy the link under https (to copy using HTTPS)
4. Open git bash on your own machine, and select the directory you want to save into
5. Type 'git clone' then copy in your link
The site github link is here: 

## Heroku

### In Github
1. Ensure all input methods have a new line at the end of the text (due to software behaviour of the mock terminal)
2. Create requirements.txt file so Heroku can load required dependancies
    - in workspace terminal, type 'Pip3 freeze > requirements.txt' to automatically update the requirements.txt file
    - push to GitHub

### In Heroku
1. In Heroku dashboard click **Create New App** button
2. Give app a unique name
3. Select region e.g. **Europe**
4. Click **Create App**
5. Go to **Settings** tab
6. Add **Config Vars**:
    1. Click on **Reveal Config Vars** button
    2. Type **CREDS** in the **KEY** field
    3. Copy & paste the contents of the **creds.json** file from github workspace into the **VALUE** field
    4. Click **Add* button
    5. In the next config var row, type **PORT** in the **KEY** field, and add **8000** to the **VALUE** field
7. Add **Buildpacks**:
    1. Click **Add Buildpack** button
    2. Click **Python** in pop-up window and click **Save changes**
    3. Click **Add Buildpack** button again
    4. Click **nodejs** in pop-up window and click **Save changes**
    5. Ensure python buildpack is first in the list (click and drag to re-order if needed)
8. Go to **Deploy** tab
    1. Click on **Github** icon
    2. Click on **Connect to Github** button
    3. In search field, search for repo name and click **Search**
    4. Click **Connect** button
    5. Scroll to bottom of page to select deployment method
        * Click **Deploy Branch** to manually deploy, ensuring desired branch is selected
        * Click **Enable Automatic Deploys** to enable automatic deployment based on every git push (ensuring desired branch is selected)
        6. Click **View** to go to deployed link

# CREDITS

## Code

- Guidance on the use of colorama was from <a href="https://www.pythonpool.com/python-colorama/" target="_blank">pythonpool</a>

- Idea for truth value testing to solve 'Solved Bug #5' from <a href="https://flexiple.com/python/check-if-list-is-empty-python/#section2" target="_blank">flexiple</a>

- Working with lists and dictionaries was initally guided by <a href="https://blog.finxter.com/python-list-of-lists/" target="_blank">finxter</a>

- List to dictionary conversions were informed by <a href="https://builtin.com/software-engineering-perspectives/convert-list-to-dictionary-python" target="_blank">builtin</a>

- Code Institute Love Sandwiches walk-through - API set-up, scoping, creds

## Contents
All written content was created by the site author based on professional knowledge.  All code was written by the site author.

## Technologies Used

Languages
- <a href="https://www.python.org/" target="_blank">Python</a>

Libraries
- <a href="https://docs.python.org/3/library/os.html" target="_blank">OS</a> Gives functions for interacting with the operating system.  Allows use of clear screen function (used to improve user experience to declutter screen).
- <a href="https://docs.python.org/3/library/sys.html" target="_blank">Sys</a> Interacts with the runtime environment. Allows program exit function to run.
- <a href="https://docs.python.org/3/library/datetime.html" target="_blank">Datetime</a> For getting & manipulation dates & time.  The date is added to the database when user adds a skill.  The date display (attached to a skill & user) will be implemented in user display in future versions of the applicationn.
- <a href="https://docs.python.org/3/library/time.html" target="_blank">Time </a> Sleep was imported from Time to give a delay when sending information to worksheets, to enhance user experience (gives impression program is doing "work".)
- <a href="https://docs.gspread.org/en/v5.7.2/" target="_blank">Gspread</a> An API for google sheets, used to enable interaction between sheet and application.
- <a href="https://pypi.org/project/colorama/" target="_blank">Colorama</a> Used to enhance user experience & expectations by colouring warnings red, menus and important information in blue, and input sections in green.
- <a href="https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html" target="_blank">google-auth</a> Enables service account between application and google service.


During the creation of this site I used the following technologies:

- <a href="https://github.com/" target="_blank">Git Hub</a> used for online programming, change tracking and storage respository for this project.
- <a href="https://www.heroku.com/" target="_blank">Heroku</a> cloud platform service to deploy, use & manage the application.
- <a href="https://www.google.com/sheets/about/" target="_blank">Google Sheets</a> used as online spreadsheet editor to store application data.
- <a href="https://console.cloud.google.com/" target="_blank">Google Cloud Services</a> used as public cloud service.
-  <a href="https://app.diagrams.net/">Draw.io</a> for flowchart creation during devlopment phase.
- <a href="https://tablesgenerator.com/markdown_tables" target="_blank">Tables Generator</a> used to create tables in manual testing section for README.


# Acknowledgements
Thanks to my mentor Spencer Barrilball for his advice and support, and my fellow students on Slack for advice and colleagiality.

<a href="" target="_blank">#</a>