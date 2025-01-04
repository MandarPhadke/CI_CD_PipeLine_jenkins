pipeline {
    agent any



    stages {
        stage('Setup Environment') {
            steps {
                echo 'Cleaning the workspace...'
                deleteDir()  // Ensure the workspace is cleared
                sh '''
                    bash -c "
                    python3 -m venv myenv &&
                    source myenv/bin/activate &&
                    pip install pytest flask django pyotp
                    "
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                    bash -c "
                    source myenv/bin/activate && 
                    nohup python -m flask run
                    "
                    '''
                echo 'Flask app is running in the background...'
            }
        }
stage('Run Tests') {
            steps {
                script {
                    def result = sh(script: '''
                        . myenv/bin/activate
                        pytest
                    ''', returnStatus: true)
                    
                    if (result != 0) {
                        error("Pytest failed. Check logs for details.")
                    }
                }
            }
        }


    stage('Setup AWS CLI') {
        steps {
            sh '''
                aws s3 ls
            '''
        }
    }

        
    }
}
