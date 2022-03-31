FROM python:3.8
WORKDIR /app
RUN apt-get update
#RUN apt install -y libgl1-mesa-glx
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "uwsgi", "uwsgi.ini"]
