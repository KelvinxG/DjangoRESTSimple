
<h1>Objectives are to learn about Web development using Django and Django-rest-framework to Build serializers objects</h1>

This project is about Django and Django Restful APIs

<p>CRUDs operations</p>

Methods allowed

<ul>
    <li> GET /   #index page</li>
    <li>GET /polls #All polls</li>
    <li>GET /polls/<int:pk> #get a poll by ID</li>
    <li>POST /polls/<int:pk> #post a new poll</li>
    <li>DELETE /polls/<int:pk> #delete a poll by ID</li>
</ul>

<b style='font-size:20px;'>Docker</b>

docker build -t my-django-project .

docker run -p 8000:8000 my-project-project

but if you run normally with just env

pip install -r requirements.txt

go to DjangoREST directory and run the following command

cd >DjangoREST

<code>Python manage.py runserver</code>


<img src="interface.png">

