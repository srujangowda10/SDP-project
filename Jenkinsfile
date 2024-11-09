pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'lib-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                
                git url: 'https://github.com/srujangowda10/SDP-project.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'C:\\Users\\sruja_p93z\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // def imageName = "${DOCKER_IMAGE}".toLowerCase()
                    bat "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                     def imageName = "${DOCKER_IMAGE}".toLowerCase()
                     bat "docker run -d -p 5009:5000 ${imageName}"
                }
            }
        }
        stage('Deploy Image') {
            steps {
                script {
                    // Use Jenkins credentials for Docker Hub login
                    withCredentials([usernamePassword(credentialsId: 'dockercredentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%"
 
                        // Push the image
                        bat "docker tag ${DOCKER_IMAGE}:latest %DOCKER_USERNAME%/${DOCKER_IMAGE}:latest"
                        bat "docker push %DOCKER_USERNAME%/${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
    }
}