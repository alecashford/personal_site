# pull official base image
FROM python:3.7-alpine

# set work directory
WORKDIR /home/appuser

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Tell docker that all future commands should run as the appuser user
USER appuser

# Create site wordking dir
WORKDIR /home/appuser/personal_site

# copy project
COPY . /home/appuser/personal_site

# set environment varibles
# RUN /bin/sh -c "source secrets.sh"
RUN /bin/sh -c "cat secrets.sh" >> ~/.bashrc
RUN /bin/sh -c "source ~/.bashrc"
RUN env