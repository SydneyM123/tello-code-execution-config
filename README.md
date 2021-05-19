# Configuration file for the tello code execution
Private repository which contains code for Docker, Jenkins and the scheduler

## Jenkins Setup Guide

1. Run the Docker in Docker container:

    ```
    docker run --name jenkins-docker --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-       docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind --storage-driver overlay2
    ```

2. Build the Dockerfile for Jenkins (Located in the init/ directory)

    ```docker build -t myjenkins-blueocean:1.1 .```

3. Run Jenkins (including Blue ocean)

    ```docker run --name jenkins-blueocean --detach --privileged --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs            /client --env DOCKER_TLS_VERIFY=1 --publish 8080:8080 --publish 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock --volume jenkins-              data:/var /jenkins_home --volume jenkins-docker-certs:/certs/client:ro --volume "$HOME":/home myjenkins-blueocean:1.1```

4. Go to the webinterface located at [host]:8080
5. When you first access a new Jenkins instance, you are asked to unlock it using an automatically-generated password.
6. Display the Jenkins console log with the command:

    ```docker logs jenkins-blueocean```

7. From your terminal/command prompt window again, copy the automatically-generated alphanumeric password (between the 2 sets of asterisks).
8. On the Unlock Jenkins page, paste this password into the Administrator password field and click Continue.
9. Go to 'Manage Jenkins' to update Jenkins to a newer version and check the auto-restart box
10. Go to 'Manage Jenkins' -> 'Manage plugins' -> 'Available' search for the 'Role-based Authorization Strategy'
11. Check the box in the row of the plugin and click the button 'Download now and install after restart'
12. After the restart, go to 'Manage Jenkins' -> 'Manage and Assign Roles' -> 'Manage Roles'
13. Add a new role named 'anonymous' and assign 'global' -> 'read', 'job' -> 'read' and 'view' -> 'read'
14. Now restart Jenkins, to do this go to the following url: [host]:8080/restart
15. Go to 'New Item' and create a pipeline project
16. Go the the configuration panel of the pipeline
17. Go to the pipeline tab and change the definition to 'Pipeline script from SCM'
18. Fill in the URL of this private repository
19. TODO: ....

# PS: Running a python container with .py file

```docker run -it --rm --detach --priviliged --network jenkins --name tello-code-exe --volume jenkins-data:/var/jenkins_home -w /var/jenkins_home/tello-    code-exe python:3 python ready-files/group_10.py```
