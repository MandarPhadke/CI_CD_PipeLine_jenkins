pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                    bash -c "
                    python3 -m venv myenv &&
                    source myenv/bin/activate &&
                    pip install pytest flask django &&
                    "
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh 'source myenv/bin/activate && python -m flask run'
            }
        }
    }
}
