pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv myenv'
                sh 'source myenv/bin/activate'
                sh 'pip install pytest flask django '
            }
        }

        stage('Run Script') {
            steps {
                sh 'python -m flask run'
            }
        }
    }
}
