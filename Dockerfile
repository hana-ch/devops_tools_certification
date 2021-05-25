FROM python:3.6-alpine 

RUN mkdir /app

WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . /app 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
