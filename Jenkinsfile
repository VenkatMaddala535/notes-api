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