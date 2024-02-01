FROM docker.io/python:3.8-buster


LABEL maintainer="Bobby Dhanoolal <>bobbydhanoolal@gmail.com>" tag="Tiger Pay Carde"


WORKDIR /app
ADD ./ /app
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 22

WORKDIR /app/

CMD ["python3", "app.py"]