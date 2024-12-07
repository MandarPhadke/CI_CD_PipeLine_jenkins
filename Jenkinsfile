pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        AWS_DEFAULT_REGION = 'us-west-2' // Replace with your region
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Cleaning the workspace...'
                deleteDir()  // Ensure the workspace is cleared
                sh 'ls -la /var/jenkins_home/workspace/pk1-assignment-pipeline'  // Verify the cleanup
                sh '''
                    bash -c "
                    python3 -m venv myenv &&
                    source myenv/bin/activate &&
                    pip install pytest flask django &&
                    pip install -r requirements.txt
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
