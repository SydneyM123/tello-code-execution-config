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
                            url: 'https://github.com/SydneyM123/p-tff_ci_public'
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
                echo 'Checking code ...'
                
                sh  '''                    
                    . venv/bin/activate
                    python src/validate_changes.py
                    deactivate
                '''
            }
        }
        stage('Detect')
        {
            steps
            {
                echo 'Detecting changes...'
                
                sh  '''                    
                    . venv/bin/activate
                    python src/detect_changes.py
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
