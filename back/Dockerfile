FROM python:3.10.4-slim-buster
WORKDIR /home/user/back
COPY requirements.txt requirements.txt
RUN apt-get update && \ 
    apt-get install -y libpq-dev && \
    pip3 install -U pip && \ 
    pip3 install -r requirements.txt

COPY . .
# Ativa o debug mode e o reload on save
ENV FLASK_ENV=development

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]