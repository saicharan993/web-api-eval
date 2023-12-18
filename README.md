# web-api-eval
python web api repo for demonstrating api pattern, documentation, build, deploy and maintenance

docker build -t flask-app .
docker run -d -p 5001:5000 --name flask-app-api flask-app