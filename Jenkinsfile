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
                    nohup python -m flask run
                    "
                    '''
                echo 'Flask app is running in the background...'
            }
        }
    }
}
