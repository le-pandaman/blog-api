# Pull base image
FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

# Set Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 11
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# SET WORKING DIRECTORY

WORKDIR /django_project_blog_api

# Install dependencies

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .