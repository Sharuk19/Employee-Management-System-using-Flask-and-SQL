pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sharuk19/employee-management-system"
    }

    stages {

        stage('Get Version Tag') {
            steps {
                script {
                    def rawOutput = bat(
                        script: 'git describe --tags --abbrev=0',
                        returnStdout: true
                    ).trim()

                    def versionTag = rawOutput
                        .split("\\r?\\n")
                        .findAll { it?.trim() }
                        .last()
                        .trim()
                    env.VERSION_TAG = versionTag
                    echo "Clean Version Tag: ${env.VERSION_TAG}"
                }
            }
        }


        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.VERSION_TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
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