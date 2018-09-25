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
<code>$ docker build -t project_name/sub_project_name:0.0.1 . </code>


when successfully finish, check your docker with
<code>$ docker images</code>
then run build container
<code>$ docker run -d --name container_name -p 80:80 project_name/sub_project_name</code>
then run check container is running
<code>$ docker ps</code>
to stop docker

<code>
$ docker stop container_name <br />
$ docker rm container_name <br />
$ docker rmi -f project_name/sub_project_name <br />
</code>
