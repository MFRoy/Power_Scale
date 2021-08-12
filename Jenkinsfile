pipeline{
        agent any
   environment{
        DATABASE_URI=credentials("DATABASE_URI")
        DOCKERHUB_CREDENTIALS=credentials("DOCKERHUB_CREDENTIALS")
    }
    stages{
        stage('Setup'){
            steps{
                sh "bash scripts/setup.sh"
            }
        }
        stage('Test app'){
            steps{
                sh "bash scripts/test.sh"
            }
        }
        stage('Builds images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }
        stage('configure VMs'){
            steps{
                sh "bash scripts/config.sh"
            }
        }
        stage('Deploy stack'){
            steps{
                sh "bash scripts/deploy.sh"
            }
        }
        
    }   
}