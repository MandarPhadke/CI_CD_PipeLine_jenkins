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
                    python -m flask run &
                    "
                    '''
            }
        }
    }
}
