pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'integracion-continua-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/janaldana2025/integracion-continua.git',
            branch: 'main',
            credentialsId: 'github-jenkins'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t integracion-continua-app .'
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    sh 'docker compose down || true'
                    sh 'docker compose up -d'
                }
            }
        }

        stage('Smoke Test') {
            steps {
                script {
                    echo 'Probando que la aplicación responde...'
                    sh 'sleep 5'
                    sh 'curl -I http://localhost:5000 || true'
                }
            }
        }

        stage('Logs') {
            steps {
                sh 'docker compose logs --tail=50'
            }
        }
    }

    post {
        always {
            echo 'Limpiando contenedores...'
            sh 'docker compose down'
        }
    }
}
