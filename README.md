Project READMEWelcome to the Django application! This document will guide you through the initial setup, database configuration, and API endpoints.
Installation Instructions###1. Install DependenciesEnsure you have a requirements.txt file in your project directory. To install the required packages, run the following command:bashpip install -r requirements.txt
###2. Run MigrationsAfter installing the dependencies, set up your database schema by executing the following commands:bashpython manage.py makemigrationspython manage.py migrate

API EndpointsThis Django application offers several API endpoints to interact with the news feature.
News Endpoints- List News To retrieve a list of news articles, use the following endpoint: ```http GET /api/news/
ruby

### Landing Page- The application can be accessed at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).- Features:  
- Search for articles using query parameters.  
- View the four most recently published news articles.  
- Click on tags or categories in the footer to explore related news.  

### New Page- The New page functions similarly to the Landing page, providing additional dedicated access to news articles.  

### Accounts Page and API- **Login** Access the login page at [http://127.0.0.1:8000/accounts/login](http://127.0.0.1:8000/accounts/login).  
- **Logout** To log out, navigate to [http://127.0.0.1:8000/accounts/logout](http://127.0.0.1:8000/accounts/logout).  

- **Signup** Create a new account at [http://127.0.0.1:8000/accounts/signup](http://127.0.0.1:8000/accounts/signup).  

### News Management- To manage news articles, use the following API endpoints:  
- **Create a New Article**: POST to [http://127.0.0.1:8000/api/news/create/](http://127.0.0.1:8000/api/news/create/)  
- **List All News Articles**: GET [http://127.0.0.1:8000/api/news/](http://127.0.0.1:8000/api/news/)  
- **Retrieve a Specific News Article**: GET [http://127.0.0.1:8000/api/news/detail/<int:pk>/](http://127.0.0.1:8000/api/news/detail/<int:pk>/)  
- **Delete a News Article**: DELETE [http://127.0.0.1:8000/api/news/delete/<int:pk>/](http://127.0.0.1:8000/api/news/delete/<int:pk>/)  
- **Update a News Article**: PUT [http://127.0.0.1:8000/api/news/update/<int:pk>/](http://127.0.0.1:8000/api/news/update/<int:pk>/)  

Feel free to reach out if you have any