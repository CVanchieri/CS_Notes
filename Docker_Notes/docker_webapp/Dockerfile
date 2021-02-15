# Dockerfile, blueprint for building the images 
# Image, is a template for the running containers 
# Container, is the running process with ther packaged projects 
# order is important 

### set the image to use ### 
FROM python:3.9
### set the directory ### 
WORKDIR /docker_example2-app 
### copy the requirements.txt file 
COPY requirements.txt .
### must install dependecies from requirements.txt ###
RUN pip install -r requirements.txt
##$ copy the local app folder to the container
COPY ./app ./app 
### set the command to run the file ### 
CMD ["python", "./app/main.py"]