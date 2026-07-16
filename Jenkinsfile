pipeline
{
    agent any

    stage('Checkout') 
    {
        steps 
        {
            checkout scm

        }
    }

    stage('Verify Tools')
    {
        steps 
        {
            sh '''
            echo "TOOL VERSIONS"
            python --version
            git --version
            docker --version
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
    
Post 
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