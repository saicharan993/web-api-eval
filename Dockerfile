# start by pulling the python image
FROM python:3.11.5-slim

# copy source files to container
COPY . /flask-app

# switch working directory
WORKDIR /flask-app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]