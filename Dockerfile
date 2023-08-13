# Select the base image
FROM  python:3.10

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Copy the source code
COPY ./api /code/api
COPY ./cifar.h5 /code/cifar.h5
COPY ./api/ /code/api/
COPY ./cifar10/ /code/cifar10/


# Install ffmpeg
RUN apt-get update -y
RUN apt-get install ffmpeg libsm6 libxext6 libxext6 -y 

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# Expose the port
EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]