pipeline
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
                    flake8 ./public_tmp --extend-ignore W1,W2,W3,W5,W6,E302,E111,E722
                    deactivate
                '''
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
                script
                {                    
                    if (!fileExists('ready-files'))
                    {
                        sh 'mkdir ready-files'
                    }
                }
                
                sh  '''                    
                    . venv/bin/activate
                    python private/src/schedule.py
                    deactivate
                '''
            }
        }
        stage('Execute')
        {
            agent any
            steps
            {
                echo 'Executing...'
                
                sh 'docker run --rm --privileged --name tello-code-exe --volume jenkins-data:/var/jenkins_home -w /var/jenkins_home/tello-code-exe python:3 python exe.py'
            }
        }
    }
}
