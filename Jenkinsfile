pipeline {
    agent any

    stages {
        stage('Clean workspace')
        {
            steps
            {
                cleanWs()
            }
        }
        stage('Build') {
            steps {
               git credentialsId: 'c57d4c63-17ee-4f39-b0b3-5e21b6394b9d', url: 'https://github.com/satishkumar96/OrangeHRM_Automation.git'
            }
        }
        stage('Test')
        {
            steps
            {
                bat 'pip install -r requirements.txt'
                bat 'pytest -v -s -n=4'
            }
        }
            }
        }
