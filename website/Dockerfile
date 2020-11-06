# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /website

# Install dependencies
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
COPY Pipfile Pipfile.lock /website/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /website/
