# CCC Assignment 2


## Deadlines
Wednesday **27th May**.

## Schedule

| Date | Task |
| ---- | ---- |
| 29 April - 5 May | Phase 1 |
| 6 May - 12 May  | Phase 2 |
| 13 May - 22 May | Phase 3 |
| 22 May - 26 May | Phase 4 |

## HomePage

[http://172.26.130.129/](http://172.26.130.129/)

## Report 

[Google Docs](https://docs.google.com/document/d/1cmAZPMd_cMoZovoOQ9oAVQEcvcezhG1WOlRujWO3Qxw/edit?usp=sharing)

## Video

[Youtube](https://youtu.be/3EfNvGMjbSo)

## About instances

Four instances exist. Each one has 2 VCPU, 9 GB RAM and private IP address.
One instance for running program, which is 172.26.133.24(demo1)
And the rest instances are for storage.

#### How to connect to an instance

Move to the directory where ins1.pem is located, then use the following commands:  
```
Execute only once
chmod 600 ins1.pem
Execute every time you wanna connect to the instance
The IP could be changed to the corresponding one
<<<<<<< HEAD
ssh -i ins2.pem ubuntu@172.26.130.129
=======
ssh -i ins1.pem ubuntu@172.26.130.129
>>>>>>> bdaee24e15e670b01cccf8b83441eb48c1c2305f
 ```

## Technical Framework

- TBD  
- Ansible  
- Docker  
- CouchDB  
- Twitter API
- Python

## For Reference

#### LaTeX

[A short introduction to LaTeX](https://www.latex-project.org/help/documentation/usrguide.pdf)

#### Git Workflow

[Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) & [Pull Request](https://www.atlassian.com/git/tutorials/making-a-pull-request)

#### What is REST

- [First](https://www.ruanyifeng.com/blog/2011/09/restful.html)
- [Second](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
- [Third](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)


## Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers.it is possible to get far more apps running on the same old servers and it also makes it very easy to package and ship programs

### twitter_harvester-docker

twitter harvester is a python file that is used to collect tweets from twitter.

We use tweepy as our twitter API.

We use `tweepy.search` methods to collect tweets from last 7 days with keywords and geo-location settings.
We use `tweepy.Stream` from Twitter Streamer to create a stream session that collects real-time tweets.

#### Dockerize python files

to dockerize our twitter-harvester program (Python) in a single container, we need to create a image of this program. But first, we need to create a docker file named Dockerfile under the directory of our twitter application

Dockerfile is a file specified by docker that contains a list of instructions.

first the Dockerfile must contain a basic image. 

`FROM python:3.7.4-stretch`

Then add all the files in this directory into an app directory created by docker itself.

`ADD . /app`

Set the working directory to app

`WORKDIR /app`

run install command that all libraries needs to be installed.

`RUN pip install -r requirements.txt`

expose the container to port 8000

`EXPOSE 8000`

define the run command that start the app:

`CMD ["python3","my_havester"]`

With the Dokerfile, we'll be able to build the docker image by entering the same directory of our Dockerfile and run the command:

`docker build -t myimage .`

to view the existed docker images:

`docker images`

with out image build, to run the image in a container:

`docker run --name give_name_to_contaienr -d myimage`

if you want to see the process and bebug information in terminal then just ignore  `-d`

Python file does not need port to run, so in this case, the port could not be declared.

### Dockerize Nginx and Web frontend

Web front is build by JavaScript and HTML. 

Nginx is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server). The nginx project started with a strong focus on high concurrency, high performance and low memory usage. It is licensed under the 2-clause BSD-like license and it runs on Linux, BSD variants, Mac OS X, Solaris, AIX, HP-UX, as well as on other *nix flavors. It also has a proof of concept port for Microsoft Windows.

create a docker file under the directory

`FROM nginx`

Here we copy all our static js and html into nginx:

`COPY static-html-directory /usr/share/nginx/html`

`COPY static-js /usr/share/nginx/html` 

etc
 
with the Dockerfile, we could build the image by 

`docker build -t nginx-image .`

With push and pull the image to the cloud server,

then start the container:

`docker run --name give_name_to_nginx_container -d -p 80:8000 nginx-image`

`-p 80:8000` means map the internal port 8000 where our app runs to external 80 which is the default port used by tcp.

Go to [http://172.26.130.129/]() to view the page