# Dockerfile, blueprint for building the images 
# Image, is a template for the running containers 
# Container, is the running process with ther packaged projects 
# order is important 

### set the image to use ### 
FROM python:3.9
### add the file to the container ### 
ADD main.py .
### must install dependecies used ###
RUN pip install requests beautifulsoup4 
### set the command to run the file ### 
CMD [ "python", "./main.py"] 
