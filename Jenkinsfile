pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sharuk19/employee-management-system"
    }

    stages {
        stage('Checkout from git') {
            steps {
                git branch: 'main', url: 'https://github.com/sharuk19/employee-management-system.git'
            }
        }
    
        stage('Build docker image'){
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Push to Docker Hub'){
            steps {
                script {
                    docker.withRegistry('https://registry-1.docker.io', 'dockerhub-creds') {
                    docker.image("${DOCKER_IMAGE}:latest").push()
                    }

                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built and pushed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}