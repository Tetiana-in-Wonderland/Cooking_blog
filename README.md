# Cooking blog

## Getting started

This is the project setup base for the website project "Coocking blob".

Make sure you have [docker](https://docs.docker.com/engine/install/) installed on your computer.

Clone the project locally & run docker :

```
git clone https://github.com/Tetiana-in-Wonderland/Cooking_blog.git cooking-blog
cd cooking-blog
```

### Optional
Run docker
```
docker compose up
```


## Run the project (no docker)
* In a terminal, go to the project folder
```
cd [...]/cooking-blog
```
* Run django
```./manage.py runserver```
* Open your browser at `localhost:8000`


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