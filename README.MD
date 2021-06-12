1.Create a virtual eniv and install django and any other requirement
2.Activate virtual envi path
3.cd into project folder.
4.create database in MySQL client as a Token.
5.In Token_Assignment/setting.py file change Database user, password as per mysql client username, passwors.  
6.Run command in cmd manage.py makemigrations.
7.Run command in cmd manage.py migrate.
8.Run Command in cmd manage.py runserver
9.Set the method 'POST' and hit the url http://localhost:8000/gnerate_token on the Postman.
10.Set the method 'PUT' and hit the url http://localhost:8000/assign in 1 minute to keep assign with generated token 
12 Set the method 'PUT' and hit the url http://localhost:8000/keep_alive/tid in 5 minute,take tid from in status code from
assign tid and 
13.Set the method 'PUT' and it Hit the url http://localhost:8000/keep_assign/tid to keep assign alive token   
14.Set the method 'PUT' and hit Hit the url http://localhost:8000/unassign to unassign the token.
15.Set the method 'DELETE' and hit Hit the url http://localhost:8000/delete/tid to delete the token from Pool.
16.Set the method 'GET' and Hit the url http://localhost:8000/get_all_token  
17.Use broswer instead of postman to test api and hit the url http://localhost:8000/swagger 
