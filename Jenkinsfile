wpipeline
{
    agent none
    stages
    {
        stage('Initialise')
        {
            agent
            {
                docker
                {
                    image 'python:3'
                    args '-v /root/.m2:/root/.m2'
                }
            }
            steps
            {
                echo '#####################################'
                echo 'Initialising...'
                
                script
                {                    
                    if (!fileExists('public'))
                    {
                        sh 'mkdir public'
                        
                        dir ('public')
                        {
                            git branch: 'master',
                            url: 'https://github.com/SydneyM123/tello-code-execution'
                        }
                    }
                }
                
                sh  '''
                    python -m pip install --upgrade pip
                    python -m pip install virtualenv
                    virtualenv venv
                    . venv/bin/activate
                    pip3 install flake8
                    deactivate
                '''
                
                echo 'Initialisation complete.'
                echo '#####################################'
            }
        }
        stage('Validate')
        {
            agent
            {
                docker
                {
                    image 'python:3'
                    args '-v /root/.m2:/root/.m2'
                }
            }
            steps
            {
                echo '#####################################'
                echo 'Validating...'
                
                script
                {
                    sh 'mkdir public_tmp'

                    dir ('public_tmp')
                    {
                        git branch: 'master',
                        url: 'https://github.com/SydneyM123/tello-code-execution'
                    }
                }
                
                sh  '''                    
                    . venv/bin/activate
                    flake8 ./public_tmp --extend-ignore W1,W2,W3,W5,W6,E302,E111,E722,F401,F821
                    deactivate
                '''
                
                echo 'Validation succesful.'
                echo '#####################################'
            }
            post
            {
                always
                {
                    sh 'rm -r public_tmp'
                }
            }
        }
        stage('Schedule')
        {
            agent
            {
                docker
                {
                    image 'python:3'
                    args '-v /root/.m2:/root/.m2'
                }
            }
            steps
            {
                echo '#####################################'
                echo 'Scheduling...'
                
                script
                {                    
                    if (!fileExists('ready-files'))
                    {
                        sh 'mkdir ready-files'
                    }
                }
                
                sh  '''                    
                    . venv/bin/activate
                    python private/schedule.py
                    deactivate
                '''
                
                echo 'Scheduling complete.'
                echo '#####################################'
            }
        }
        stage('Prepare')
        {
            agent any
            steps
            {
                echo '#####################################'
                echo 'Preparing'
                
                script
                {
                    if (!fileExists('./tello_code_execution.py'))
                    {
                        if (fileExists('private/tello_code_execution.py'))
                        {
                            sh 'cp -f ./private/tello_code_execution.py ./tello_code_execution.py'
                        }
                        else
                        {
                            error 'The tello_code_execution library is missing...'
                        }
                    }
                    
                    if (!fileExists('config/tello_code_execonfig.json'))
                    {
                        if (fileExists('private/tello_code_execonfig.json'))
                        {
                            
                            sh 'mv ./private/tello_code_execonfig.json ./config/tello_code_execonfig.json'
                        }
                        else
                        {
                            error 'The tello execution configuration is missing...'
                        }
                    }
                }
                
                echo 'Done preparing.'
                echo '#####################################'
            }
        }
        stage('Execute')
        {
            agent any
            steps
            {
                echo '#####################################'
                echo 'Executing'
                
                script
                {                    
                    if (fileExists('exe.py'))
                    {                        
                        try
                        {
                            echo 'Executing...'
                            
                            sh '''
                                docker run --rm --name tello-code-exe \
                                --volume jenkins-data:/var/jenkins_home \
                                --volume tello_code_execonfig:/var/jenkins_home/workspace/tello-code-execution-pipeline/config \
                                -w /var/jenkins_home/workspace/tello-code-execution-pipeline python:3 python exe.py
                            '''
                            
                            sh 'rm exe.py'
                        }
                        catch (ex)
                        {
                            echo 'Another script is already running or there are errors in the executed file.'
                        }
                    }
                    else
                    {
                        echo 'Nothing to execute.'
                    }
                }
                
                echo 'Execution completed.'
                echo '#####################################'
            }
        }
    }
}
