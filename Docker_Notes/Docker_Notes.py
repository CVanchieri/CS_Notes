''' Docker Notes '''
# alternative to VIM 
# Docker is a platform for packaging, deploying, and running applications that uses containerization
# Docker applications run in containers that can be used on any system
# Docker packages applications as images that contain everything needed to run them: code, runtime environment, libraries, and configuration
# The images run in containers, which are discrete processes that take up only as many resources as any other executable
# Containers use less memory and less CPU
# Docker containers share a Linux kernel and dont run their own virtual machine
# Linux runtime is required 


''' benefits of containerization '''
# Consistent test environment for development and QA
# Cross-platform packages called images
# Isolation and encapsulation of application dependencies
# Ability to scale efficiently, easily, and in real time
# Enhances efficiency via easy reuse of images


''' Docker images '''
# All Docker images are referenced by their names 
# The image name is made up of 3 parts: repository name, image name, and an image tag 
# The image tag (or version) can be omitted, however, any image without a tag gets the default tag called the latest


''' Docker commands '''
# docker for computer must be running 
# A Docker image is a collection of layers (one command in the Dockerfile = a layer in the image). The layers are stacked one on top of the other and they are all read-only, with the exception of a topmost, writeable layer
### run a new container ###
docker run hello-world # looks for image on local system, if not found downloads from docker hub
docker run -it ubuntu bash # using the -it flag allows us to interact with the shell 
### run a container already local ### 
docker start –attach <container name> 
### stop a container running locally ### 
docker stop <container name> 
### remove a local container ### 
docker rm <container name> 
### check local containers ### 
docker ps -a # lists the containers on the local system
# status UP shows a docker container is running 
### looks inside the container ### 
docker top <container name> # see what the container is running 
### list image on the local system ###
docker image ls # produces a listing of images on our system
### remove image from local system ###
docker image rm <image name> 


''' build and run '''
### docker image for a web application ### 
### creating the virtual environment ### 
# same set up as VIM, create directory, requirements.txt 
# add requirements.txt through Dockerfile
### build from the local docker file ### 
docker build -t python-fastapi . 
docker run python-imdb
### run the docker image with port + host, necessary for web app 
docker run -p 8000:8000 python-fastapi


''' Docker file notes '''
### create/copy a new image ### 
# similar command style to SQL
# docker files are a set of instructions 
### copy an image to a local path ###
FROM nginx # where to copy from
COPY html/usr/share/nginx/html # where to copy too, path local
### 
FROM ubuntu:18.04 # where to copy from
WORKDIR /app # working directory in image 
COPY hello.sh /app # copying from host computer to image directory
RUN chmod +x hello.sh
RUN apt-get update 
RUN apt-get install curl -y
CMD ["./hello.sh"] # sets the default command for the container, run to execute




