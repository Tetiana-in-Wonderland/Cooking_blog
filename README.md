# Cooking blog

## Getting started

This is the project setup base for the website project "Coocking blob".

Make sure you have [docker](https://docs.docker.com/engine/install/) installed on your computer.

Clone the project locally & run docker :

```
git clone git@gitlab.liip.ch:apprentice-and-interns/exercises/cooking-blog/base.git cooking-blog
cd cooking-blog
docker compose up
```

Try to run the project in your browser at :

http://localhost:8000/

You should see the django page "The install worked successfully!"

## Create the "blog" application

In Django, the project structure looks like this :
* Main folder
  * 1 main project configuration folder (cookingblog)
  * N applications folders (containing the business logic)
  * ./manage.py the django command script

In your project folder run the following :
```
mkdir -p apps/blog
docker compose exec backend ./manage.py startapp blog apps/blog
```