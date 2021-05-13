pipeline
{
    agent
    {
        docker
        {
            image 'python:3'
            args '-v /root/.m2:/root/.m2'
        }
    }
    stages
    {
        stage('Initialise')
        {
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
                    flake8 ./public_tmp --extend-ignore W1,W2,W3,W5,W6
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
            steps
            {                
                sh  '''                    
                    . venv/bin/activate
                    python private/src/schedule.py
                    deactivate
                '''
                
                echo '--------------------------------------'
                
                sh  '''                    
                    ls ready-files
                '''
                
                sh  '''                    
                    rm -r ready-files
                '''
                
                sh  '''                    
                    ls ready-files
                '''
            }
        }
        stage('Execute')
        {
            steps
            {                
                sh  '''                    
                    . venv/bin/activate
                    python private/src/execute.py
                    deactivate
                '''
            }
        }
    }
}
