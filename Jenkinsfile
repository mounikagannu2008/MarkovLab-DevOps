
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Tests') {
            steps {
                sh '''
                    cd engine
                    python3 -m pip install -r requirements.txt
                    python3 -m pytest -q
                '''
            }
        }

        stage('Java Build') {
            steps {
                sh 'cd api && mvn -B clean package'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker compose build'
            }
        }
    }

    post {
        success {
            echo 'MarkovLab CI Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the failed stage.'
        }
    }
}
