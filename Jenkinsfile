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
                    
                    sh 'ls -a'
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
                    pip3 install gitpython
                    deactivate
                '''
            }
        }
        stage('Check')
        {
            steps
            {
                echo 'Checking code ...'
            }
        }
        stage('Detect')
        {
            steps
            {
                echo 'Detecting changes...'
                
                sh  '''
                    ls public -a
                    ls -a
                    . venv/bin/activate
                    python src/detect_changes.py
                    deactivate
                '''
            }
        }
    }
}
