# Jenkins Setup Guide

1. Run the Docker in Docker container:
```docker run --name jenkins-docker --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind --storage-driver overlay2```

2. Build the Dockerfile for Jenkins (Located in the init/ directory)
```docker build -t myjenkins-blueocean:1.1 .```

3. Run Jenkins (including Blue ocean)
```docker run --name jenkins-blueocean --detach --privileged --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --publish 8080:8080 --publish 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --volume "$HOME":/home myjenkins-blueocean:1.1```

4. Go to the webinterface located at [host]:8080
5. Go to 'Manage Jenkins' to auto update Jenkins
6. TODO: Credentials aanmaken...
7. Create a pipeline
8. Go the the configuration panel of the pipeline
9. Go to the pipeline tab and change the definition to 'Pipeline script from SCM'
10. Fill in the URL of this private repository
11. TODO: ....

# PS: Running a python container with .py file
```docker run -it --rm --detach --priviliged --network jenkins --name tello-code-exe --volume jenkins-data:/var/jenkins_home -w /var/jenkins_home/tello-code-exe python:3 python ready-files/group_10.py```
