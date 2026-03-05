pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the latest code from GitHub
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker Image...'
                sh 'docker build -t devops-task-api:latest .'
            }
        }
        
        stage('Deploy Container') {
            steps {
                echo 'Deploying the new container...'
                // The '|| true' ensures the pipeline doesn't fail if the container isn't running yet
                sh 'docker stop my-task-container || true'
                sh 'docker rm my-task-container || true'
                
                // Run the newly built image
                sh 'docker run -d -p 8000:8000 --name my-task-container devops-task-api:latest'
            }
        }
    }
}