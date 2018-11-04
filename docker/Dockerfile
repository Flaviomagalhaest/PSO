FROM python:3.6-slim-stretch

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
   git \
   wget \
   curl \ 
   python3-dev \
   && apt-get clean && rm -rf /tmp/* /var/tmp/*

# Set workd dir and copy requirements.txt to container
WORKDIR /app
# Copy requirements.txt to configured workdir (/app)
COPY docker/requirements.txt .

# Installs dependecies added in requirements.txt
RUN pip3 install -r requirements.txt

# This command copy all itens in your app directory to container in configured workdir (/ app)
COPY ./. .

# Setting volume
VOLUME .

# Indicate the port
EXPOSE 3001

