# Jenkins Setup Guide

2. Build the Dockerfile for Jenkins (Located in the init/ directory)
```docker build -t jenkins .```

3. Run Jenkins (including Blue ocean)
```docker run --name jenkins -d --privileged -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins-data:/var/jenkins_home -v "$HOME":/home jenkins```

4. Go to the webinterface located at [host]:8080
5. When you first access a new Jenkins instance, you are asked to unlock it using an automatically-generated password.
6. Display the Jenkins console log with the command:

    ```docker logs jenkins```

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
```docker run -it --rm --detach --priviliged --network jenkins --name tello-code-exe --volume jenkins-data:/var/jenkins_home -w /var/jenkins_home/tello-code-exe python:3 python ready-files/group_10.py```
