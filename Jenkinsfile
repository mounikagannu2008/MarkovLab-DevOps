
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
         bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r engine/requirements.txt'
         bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest engine -q'
       }
     }

        stage('Java Maven Build') {
            steps {
                bat 'cd api && mvn -B clean package'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Docker Run') {
            steps {
                bat 'docker compose up -d'
            }
        }
    }

    post {
        success {
            echo 'MARKOVLAB PIPELINE SUCCESS'
        }
        failure {
            echo 'PIPELINE FAILED - CHECK CONSOLE'
        }
    }
}
