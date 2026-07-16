pipeline
{
    agent any

    stages
    {
        stage('Checkout') 
        {
            steps 
            {
                checkout scm
            }
        }

        stage('Verify Tools') 
        {
            steps {
                sh '''
                    python3 --version
                    pip3 --version
                    git --version
                    docker --version
                '''
            }
        }

        stage('Verify Test Cases') 
            {
                steps {
                    sh '''
                    #!/bin/bash
                    source .venv/bin/activate
                    python -m pytest -v
                    '''
                }
            }


        stage('Build Docker Image') 
        {
            steps 
            {
                sh '''
                    docker build -t notes-api:${BUILD_NUMBER} -t notes-api:latest .
                '''
            }
        }

        stage('Finish') 
        {
            steps 
            {
                echo 'CI Pipeline Completed Successfully!'
            }
        }
    }

    post 
    {
        success 
        {
            echo 'Build SUCCESS'
        }

        failure 
        {
            echo 'Build FAILED'
        }
    }


}