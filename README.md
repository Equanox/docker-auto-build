<h1>Docker Auto Build/Run</h1>

    * cmd line tool for a better workflow building docker images
    * store run cmds inside Dockerfiles
    * speedup workflow in production and development
    * one image -> one container

This cmd line tool is great when working without a docker registry. All dockerfiles are stored inside a git repository in a special folder named docker. You can simply include  your private and public git repo using a ADD cmd inside your dockerfile

<h2>Requirements</h2>
The repo is tested on ubuntu 14.04 LTS. But should work on all UNIX systems 

    docker
    git


<h2>Installation</h2>
```
git clone https://github.com/Equanox/docker-auto-build
cd docker-auto-build
sudo chmod +x install dab
sudo ./install
```

<h2>Example</h2>
```
cd docker-auto-build
dab -i "webhook" -b -c
```
wait for webhook beeing built. Then c&p the run cmd
```
sudo docker run -i -t -p 127.0.0.1:8080:9001 --restart=always --name=webhook webhook /bin/bash
```
Open a new terminal and test the webhook inside the docker container using
(if curl is not installed type **sudo apt-get install curl**)
```
curl -X POST 127.0.0.1:8080/hook?text=HelloWorld
```
Everytime you do an update in your code (e.g. examples/server.py) you can just type..
```
dab -i "webhook" -b -r -c
```
to stop+remove the running container and rebuilt your image. This gives you a super fast workflow when testing your code in a local environment.


<h2>Get Started</h2>
Choose an existing git repo 

    * Create a folder named docker in the root folder of the repo
    * Create a folder named image (or any other name)  inside the docker folder
    * copy Dockerfile inside the folder named image

Now you can build your docker image from everywhere inside your git repo.
    
```
sudo dab -b -i "imagename"
```
or when inside the image folder
```
sudo dab -b
```
.

To include your repo in your docker image just add the line
```
ADD image somefolder
```
to your Dockerfile.

When you need to replace a running container with the one from a new build 
```
sudo dab -b -i "imagename" -r -c
```
*-r* stops and remove all running containers using the name *imagename*

*-c* shows typicall used run cmds for production and development

So you just have to copy & paste the run cmd to restart your container


<h2>Contribute</h2>
Please, only commit to the develop branch. The master branch  always contains a stable version.

<h2>License</h2>
This Software is released under the [MIT license](http://opensource.org/licenses/mit-license.php).








