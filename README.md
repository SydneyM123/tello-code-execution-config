# :floppy_disk: Jenkins Setup Guide
#### Private repository which contains code for Docker, Jenkins (as a Docker container) and the scheduler.
##### In this setup guide we expect you to have Docker already installed. ![This link](https://docs.docker.com/engine/install/debian/) contains the docs for installing Docker on a Debian (Raspbian) based system.

## Running the Jenkins container

1. Open a terminal and go to the init directory located in this repository (tello-code-execution-config)
2. Build the Dockerfile for Jenkins:
```
docker build -t jenkins .
```
3. Run Jenkins:
```
docker run --name jenkins --detach --privileged --publish 8080:8080 --publish 50000:50000 --volume /var/run/docker.sock:/var/run/docker.sock --volume jenkins-data:/var/jenkins_home --volume "$HOME":/home jenkins
```

## Setting up Jenkins

1. Go to the webinterface located at [host]:8080
2. When you first access a new Jenkins instance, you are asked to unlock it using an automatically-generated password.
3. Display the Jenkins console log with the command:
```
docker logs jenkins
```
4. From your terminal/command prompt window again, copy the automatically-generated alphanumeric password (between the 2 sets of asterisks).
5. On the Unlock Jenkins page, paste this password into the Administrator password field and click Continue.
6. The automatically-generated password can be used to login the Jenkins (the username is: 'admin').
7. U can also create a custom user but it is not necesarry.
8. Go to 'Manage Jenkins' to update Jenkins to a newer version and check the auto-restart box

### Setting up an anonymous guest user for students to log in

1. Go to 'Manage Jenkins' -> 'Manage plugins' -> 'Available' search for the 'Role-based Authorization Strategy'
2. Check the box in the row of the plugin and click the button 'Download now and install after restart'
3. After the restart, go to 'Manage Jenkins' -> 'Manage and Assign Roles' -> 'Manage Roles'
4. Add a new role named 'anonymous' and assign 'global' -> 'read', 'job' -> 'read' and 'view' -> 'read'
5. Now restart Jenkins, to do this go to the following url: [host]:8080/restart

### Setting up the pipeline

6. Go to 'New Item' and create a pipeline project
7. Go the the configuration panel of the pipeline
8. Go to the pipeline tab and change the definition to 'Pipeline script from SCM'
9. Fill in the URL of this private repository
10. TODO: ....
