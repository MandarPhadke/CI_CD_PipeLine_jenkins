pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh 'source myenv/bin/activate'
                sh 'source myenv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python -m flask run'
            }
        }
    }
}
