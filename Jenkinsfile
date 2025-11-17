pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'integracion-continua-app'
        CONTAINER_NAME = 'integracion-continua-app'
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
                sh 'docker build -t integracion-continua-app .'
            }
        }

        stage('Deploy App Container') {
            steps {
                sh '''
                # detener y eliminar contenedor previo
                docker stop integracion-continua-app || true
                docker rm integracion-continua-app || true

                # ejecutar la aplicación
                docker run -d \
                    --name integracion-continua-app \
                    -p 5000:5000 \
                    integracion-continua-app
                '''
            }
        }

        stage('Smoke Test') {
            steps {
                sh '''
                echo "Esperando 5 segundos..."
                sleep 5
                curl -I http://localhost:5000 || true
                '''
            }
        }

        stage('Logs') {
            steps {
                sh 'docker logs --tail 50 integracion-continua-app'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado'
        }
    }
}
