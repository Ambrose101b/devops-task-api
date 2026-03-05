pipeline {
    // 'agent any' tells Jenkins to run this on any available environment
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                // This step automatically pulls your latest code from GitHub
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker Image...'
                // Running the exact Linux command we used manually
                sh 'docker build -t devops-task-api:latest .'
            }
        }
    }
}