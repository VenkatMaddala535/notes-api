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
                    . .venv/bin/activate
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
                pwd
                ls -la
                ls -la .venv
                ls -la .venv/bin

                . .venv/bin/activate

                echo "PATH=$PATH"
                echo "VIRTUAL_ENV=$VIRTUAL_ENV"

                which python
                which python3

                ls -l .venv/bin/python*
                python --version
                python3 --version
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