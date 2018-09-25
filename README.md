# Flask-Docker

Install flask within docker with

Alpine
Nginx
uWSGI
pyodbc

Setup :

Copy your project to folder app
Dont (remove) main.py, cause it used for wsgi call check wsgi.ini

Build docker with command :
<code>docker build -t project_name/sub_project_name:0.0.1 . </code>


when successfully finish, check your docker with
$ docker images
then run build container
$ docker run -d --name container_name -p 80:80 project_name/sub_project_name
then run check container is running
$ docker ps
to stop docker

$ docker stop container_name
$ docker rm container_name
$ docker rmi -f project_name/sub_project_name
