pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        AWS_DEFAULT_REGION = 'us-west-2'
    }

    stages {
        stage('Setup AWS CLI') {
            steps {
                withEnv([
                    "AWS_ACCESS_KEY_ID=${env.AWS_ACCESS_KEY_ID}",
                    "AWS_SECRET_ACCESS_KEY=${env.AWS_SECRET_ACCESS_KEY}",
                    "AWS_DEFAULT_REGION=${env.AWS_DEFAULT_REGION}"
                ]) {
                    sh '''
                        echo "Testing AWS CLI..."
                        aws s3 ls
                    '''
                }
            }
        }
    }
}
