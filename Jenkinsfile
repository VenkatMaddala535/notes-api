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

        stage('Build Docker Image')
        {
                steps
                {
                    sh '''
                        docker build -t notes-api:v1.0 .
                        docker run -d --name notes-api -p 5005:5005 notes-api:v1.0
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