# start by pulling the python image
FROM python:3.11.5-slim

# copy app files to container
COPY . /flask-app

# set working directory to app directory
WORKDIR /flask-app

# install app dependencies
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]