pipeline{
        agent any
   environment{
        DATABASE_URI=credentials("DATABASE_URI")
    }
    stages{
        stage('Setup'){
            steps{
                sh "cd Power_Scale && bash scripts/setup.sh"
            }
        }
        stage('Test app'){
            steps{
                sh "cd Power_Scale && bash scripts/tests.sh"
            }
        }
        stage('Builds images'){
            steps{
                sh "cd Power_Scale && bash scripts/build.sh"
            }
        }
        stage('configure VMs'){
            steps{
                sh "cd Power_Scale && bash scripts/config.sh"
            }
        }
        stage('Deploy stack'){
            steps{
                sh "cd Power_Scale && bash scripts/deploy.sh"
            }
        }
        
    }   
}