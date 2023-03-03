FROM python:3.10-slim-buster

#within container
WORKDIR /backend-flask

#outside container
# where libraries are stored
COPY requirements.txt requirements.txt

#runn commands are used to setup the environment/container
RUN pip3 install -r requirements.txt

COPY . .

#set en vars within container
ENV FLASK_ENV=development

EXPOSE ${PORT}
#used to execute within the container, after the container has been built
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]