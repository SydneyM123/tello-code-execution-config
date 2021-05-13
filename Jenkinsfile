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
            echoBanner("Initialise", ["Clones the tello-code-execution repo if it does not exist already.", "Creates venv and install flake8"])
            
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
            echoBanner("Validate", ["Validates all Python files in the tello-code-execution directory."])
            
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
                    flake8 ./public_tmp
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

def echoBanner(def ... msgs) {
   echo createBanner(msgs)
}

def errorBanner(def ... msgs) {
   error(createBanner(msgs))
}

def createBanner(def ... msgs) {
   return """
       ===========================================

       ${msgFlatten(null, msgs).join("\n        ")}

       ===========================================
   """
}

// flatten function hack included in case Jenkins security
// is set to preclude calling Groovy flatten() static method
// NOTE: works well on all nested collections except a Map
def msgFlatten(def list, def msgs) {
   list = list ?: []
   if (!(msgs instanceof String) && !(msgs instanceof GString)) {
       msgs.each { msg ->
           list = msgFlatten(list, msg)
       }
   }
   else {
       list += msgs
   }

   return  list
}
