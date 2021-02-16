''' Docker Notes '''
# Docker is a platform for packaging, deploying, and running applications that uses containerization
# alternative to VIM 
# Docker applications run in containers that can be used on any system
# Docker packages applications as images that contain everything needed to run them: code, runtime environment, libraries, and configuration
# The images run in containers, which are discrete processes that take up only as many resources as any other executable
# Containers use less memory and less CPU
# Docker containers share a Linux kernel and dont run their own virtual machine

### steps ### 
# set up a directory
# add/creae your files 
# set up environment if needed
# add dependencies or requirments.txt 
# create Dockerfile process 
# build docker package 
# run docker package


''' benefits of containerization '''
# Consistent test environment for development and QA
# Cross-platform packages called 'images'
# Isolation and encapsulation of application dependencies
# Ability to scale efficiently, easily, and in real-time
# Enhances efficiency via easy reuse of images


''' Docker images '''
# All Docker images are referenced by their names 
# The image name is made up of 3 parts: repository name, image name, and an image tag 
# The image tag (or version) can be omitted, however, any image without a tag gets the default tag called the latest
# A Docker image is a collection of layers (one command in the Dockerfile = a layer in the image) 
# The layers are stacked one on top of the other and they are all read-only, with the exception of a topmost, writeable layer


''' build and run '''
# from the root directory
### build the doctor image, name the image, specify location . for current directory ###
docker build -t python-imdb . 
### run the image with given name ###
docker run python-imdb .
# if file is changed run docker build again 
# if interactive input from user is needed use -t -i
docker run -t -i python-imdb # check docker_pythonscript folder 
# if a web app a port and host number are needed
docker run -p 8000:8000 python-fastapi # check docker_webapp folder


''' Docker commands '''
# Docker for computer must be running 
### run a container ### 
docker run hello-world # looks for image on local system, if not found downloads from docker hub, will create a new container 
docker run -it ubuntu bash # using the -it flag allows us to interact
### run a container already local ### 
docker start –attach <container name> # will use a container specified and not create a new one
### stop a container running locally ### 
docker stop <container name> # this will stop containers that run continuously
### remove a local container ### 
docker rm <container name> # remove a local container, must be stopped first
### check local containers ### 
docker ps -a # lists the containers that are local 
# status UP shows a docker container is running 
### look inside the container ### 
docker top <container name> # see what the container is running 
### list image on the local system ###
docker image ls # produces a listing of images on our system
### remove image from local system ###
docker image rm <image name> # remove the image locally 


''' build and run '''
### docker image for a web application ### 
# create a virtual environment
# same set up as VIM, create directory, working file, requirements.txt 
# add requirements.txt through Dockerfile
### build from the local docker file ### 
docker build -t python-fastapi . # . represents the current directory
docker run python-imdb # run the Dockerfile and set a name
docker run -p 8000:8000 python-fastapi # a web app needs to specify the port and host numbers 


''' Docker file notes '''
### create/copy a new image ### 
# similar command style to SQL
FROM <docker image name> # creates a layer from the Docker image
ADD  <file to image> # copy files/dorectories to a Docker image, capable of tar and remote URL handling
COPY <add files to image> # copy files/dorectories to a Docker image, basic
WORKDIR # set the diretory to work form 
RUN # run a command
CMD # specifies what command to run within the container
# docker files are a set of instructions 





