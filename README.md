# FullStack milestone Unicorn attractor

[![Build Status](https://travis-ci.org/rtreagus/Final-project-unicorn-attractor-DONT-DELETE.svg?branch=master)](https://travis-ci.org/rtreagus/Final-project-unicorn-attractor-DONT-DELETE)

## FullStack Milestone Project

Developers website 


[View Developers Webpage](https://unicornapp-milestone-project.herokuapp.com/)

Developers was created so a company was able to post bugs or new features that have been created by users or are experiencing problems. Bugs are listed by there status, which are Todo, Doing and Done. Bugs and Features can easily be added by simply filling out the forms through there profile page. Users that feel they can help fix the bugs can assign the bug to themselves and once completed can change the status to Done. Bugs can be upvoted so they are listed first before other other bugs. Users can comment on bugs and features about there thoughts and give free advise.  Features that have been created can be purchased through the online payment system which is supported by stripe.  
 
## Website Functionality

How does Developers work : 

 1. Register a new user or login using your existing user.

 2. Once logged in you are brought to the main webpage where all the Bugs and Features that have been created by users are displayed. Bugs are displayed by status tags, Todo, Doing and Done. Bugs and Feautres are displayed by small sample cards but can be viewed larger by previewing. If a feature you wish to purchase simply add to cart and follow the payment procedure.

* Click View - Bugs and Features have this button for previewing the complete description and comments for each post.

* Click Add - Adding a bug will assign this bug to you, once complete you can change the status to Done.

 3. Features can be purchased through the webpage by simply adding to basket and processing the order through the steps.

    * Once the Feature has been added to your basket you can proceed to checkout.

    * Once your personal details have been added you can process a working payment by entering :

    |  |Credit card Number |  CVV | Expiry Date   |
    |--| ------------------ |:----:|--------------:|
    | Visa | 4242424242424242   | 111  | Any valid Date|
    | Visa Debit | 4000056655665556   | 222  | Any valid Date|
    | Mastercard | 5555555555554444   | 333  | Any valid Date|

   

 4. Once you have finished with a Bug or Feature you can delete this by simply clicking on a delete button on your profile page.

 5. Searching for a Bugs or Features is done on the main display page by filling in the searchbar which will automatically search through features and bugs for a match. Any matches will be displayed below also displaying how many matches where found.


## Technologies Used


- [JQuery / Javascript](https://jquery.com)
    - The project uses **JQuery / Javascript** for initialization on Bootstrap elements functionality to make the users have more of an experience using the website. 

- [Python / Django](https://www.python.org/)
    -  **Python** and **Django**  where chosen languages used to write the Developers webpage. Python and Django are powerful programming language with many builtin functions and extensions. 

- [Visual Studio Code](https://code.visualstudio.com/)
    - **Visual Studio Code** was the chosen text editor. Very easy to use with create built in debugging and extensions.

- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap**, a modern responsive front end framework. Bootstrap is similar to bootstrap making the webpage responsive from being in a mobile view to a large screen or tablet.

- [Heroku Postgres](https://www.heroku.com/postgres)
    -  **Heroku Postgres** PostgreSQL is a relational database management systems. 

- [Heroku](https://id.heroku.com/login)
    -  **Heroku** is used for my webpage deployment. My code is committed to Heroku and add a requirements text file and procfile so Heroku knows which software has to be installed and what program my code is running.

- [Amazon Web Services](https://aws.amazon.com/)
    -  **Amazon Web Services** is used for storing all the static files for Developers. Css and javascript for the page running and styling and profile photos are stored online.

- [Chart Js](https://www.chartjs.org/)
    -  **Chart JS** Chart Js is used for diplaying statistics for Bugs status and Current Users.

## Testing Developers Webpage

1. Google Chrome - HTML / Javascript / Jquery / CSS where all tested through the google chrome developer tool. Error message would appear in the console if anything was detected. Errors where displayed with a file location and which line the fault was on. Google chrome developer tools has a responsive section in which my webpage could be tested on many different screen sizes to make sure everything was working correctly for any users screen. 

2. Webpage scenario testing was carried out on the login page, register page, bug and feature adding tested making sure the user was alerted if an input had been left blank or incorrectly filled in.



## Deployment

My webpage is deployed through Heroku. I created a Heroku app to which I created a Github repository thorough the command line. i added a requirements text file and a Procfile so Heroku knows what to install and what program my code is running. Once created I added all my code to Heroku and committed my work ready to be pushed to the Heroku branch. 