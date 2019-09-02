### INSTAGRAM
This is a clone of the popular app, Instagram.

### By Emmanuel Muchiri

### Description
The application allows users to sign up, upload pictures,view other user's pictures,like them, comment on them and also follow the other users. Users can also search for other users using their user names.

### BDD SPECIFICATIONS
|   User Requirements     |           Input                                 |           Output                            |
|-------------------------|-------------------------------------------------|---------------------------------------------|
| Sign up/Login           | To sign up, click on the sign up link and fill  | If login is successful, user is navigated to|
|                         | in the form details. To log in, enter your      | the home page                               |
|                         | username and password                           |                                             |
| Comment on a post       | Click on the comment icon and add a comment     | The comment will be added to the post's     |
|                         |                                                 | comment section                             |
| Add a new post          | Click on the profile icon and the Upload Image  | The user will be navigated to a page where  |
|                         | button                                          | he/she can upload a new post                |
| Edit profile            | On the profile page, click on the Edit Profile  | Profile will be edited                      |
|                         | button                                          |                                             |
| View all your posts     | Click on the profile icon and navigate to the   | All the user's posts will be displayed      |
|                         | profile page                                    |                                             |
| View other people's     | Navigate to the home page to view posts from    | All the posts will be displayed             |
| posts                   | the users you follow                            |                                             |
| Log out                 | On the profile page, click on the settings      | You will be logged out                      |
|                         | button then select log out                      |                                             |


### Setup/Installation Requirements
<ul>
<li>Ensure you have Python 3.6</li>
<li>Clone the Instagram repository</li>
<li>Create your own virtual environment and activate it using these respective commands:python3.6 -m venv --without-pip virtual && source virtual/bin/activate</li>
<li>Install all the necessary dependencies necessarry for running the application using this command: pip install-r requirements.txt</li>
<li>Create a database: psql then create the databse using this command: CREATE DATABASE     database-name </li>
<li>Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate</li>
<li>Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser</li>
</ul>

### Technologies Used
<ul>
<li>Python 3.6</li>
<li>Django</li>
<li>Bootstrap</li>
<li>CSS</li>
<li>HTML</li>
</ul>

### Support and Contact Details
For more information, questions, or feedback, get in touch with me on - 
email: emmanuel.muchiri@outlook.com

### Licence
Copyright(c) 2019 Emmanuel Muchiri