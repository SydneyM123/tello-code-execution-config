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
        stage('Checkout')
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
            }
        }
        stage('Init')
        {
            steps
            {
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
        stage('Check')
        {
            steps
            {
                sh  '''                    
                    . venv/bin/activate
                    flake8 ./public
                    deactivate
                '''
            }
        }
        stage('Detect')
        {
            steps
            {                
                sh  '''                    
                    . venv/bin/activate
                    python private/src/detect_changes.py
                    deactivate
                '''
                
                echo '--------------------------------------'
                
                sh  '''                    
                    ls ready-files
                '''
            }
        }
    }
}
