This project is inspired by Django polls app. We will create a polls api using following stack:

- Chalice
- API Gateway
- AWS Lambda
- Aurora
- Peewee

## Execute

Build Docker image:

    docker build -t chalice-polls .

Run with docker

    docker run -p 8000:8000 --env-file env.list chalice-polls

Navigate to http://localhost:8000/polls/questions/.
