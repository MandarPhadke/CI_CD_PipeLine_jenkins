pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python my_script.py'
            }
        }
    }
}
