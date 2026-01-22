pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ofekpensso/wisdom-app'
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    sh "docker build -t $DOCKER_IMAGE:$IMAGE_TAG ./wisdom-app"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing Image to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push $DOCKER_IMAGE:$IMAGE_TAG"
                    }
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    echo 'Updating Kubernetes Deployment...'
                    withCredentials([file(credentialsId: 'k8s-kubeconfig', variable: 'KUBECONFIG')]) {
                        sh "kubectl --kubeconfig $KUBECONFIG set image deployment/wisdom-deployment wisdom-container=$DOCKER_IMAGE:$IMAGE_TAG"
                        
                        sh "kubectl --kubeconfig $KUBECONFIG rollout status deployment/wisdom-deployment"
                    }
                }
            }
        }
    }
}
