# :floppy_disk: Jenkins Setup Guide (as a Docker container)

## Running Jenkins

- Open a terminal and go to the init directory located in this repository (tello-code-execution-config)
- Build the Dockerfile for Jenkins:

  ```
  docker build -t jenkins .
  ```
- Run Jenkins:

  ```
  docker run --name jenkins -d --privileged -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins-data:/var /jenkins_home -v "$HOME":/home jenkins
  ```

## Setting up Jenkins

- Go to the webinterface located at [host]:8080
- When you first access a new Jenkins instance, you are asked to unlock it using an automatically-generated password.
- Display the Jenkins console log with the command:

  ```
  docker logs jenkins
  ```
- From your terminal/command prompt window again, copy the automatically-generated alphanumeric password (between the 2 sets of asterisks).
- On the Unlock Jenkins page, paste this password into the Administrator password field and click Continue.
- The automatically-generated password can be used to login the Jenkins (the username is: 'admin').
- U can also create a custom user but it is not necesarry.
- Go to 'Manage Jenkins' to update Jenkins to a newer version and check the auto-restart box

### Setting up an anonymous guest user for students to log in

- Go to 'Manage Jenkins' -> 'Manage plugins' -> 'Available' search for the 'Role-based Authorization Strategy'
- Check the box in the row of the plugin and click the button 'Download now and install after restart'
- After the restart, go to 'Manage Jenkins' -> 'Manage and Assign Roles' -> 'Manage Roles'
- Add a new role named 'anonymous' and assign 'global' -> 'read', 'job' -> 'read' and 'view' -> 'read'
- Now restart Jenkins, to do this go to the following url: [host]:8080/restart

### Setting up the pipeline

- Go to 'New Item' and create a pipeline project
- Go the the configuration panel of the pipeline
- Go to the pipeline tab and change the definition to 'Pipeline script from SCM'
- Fill in the URL of this private repository
- TODO: ....

### PS: Running a python container with .py file
```
docker run -it --rm --detach --priviliged --network jenkins --name tello-code-exe --volume jenkins-data:/var/jenkins_home -w /var/jenkins_home/tello-code-exe python:3 python ready-files/group_10.py
```
