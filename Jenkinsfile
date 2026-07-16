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
                    python3 --versionhttp://localhost:8081/job/student-app/4/
                    pip3 --version
                    git --version
                    docker --version
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