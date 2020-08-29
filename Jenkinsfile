pipeline{
    agent any
    stages{
        stage("Make Scripts Executable"){
            steps{
                sh 'chmod +x ./scripts/*'
            }
        }
        stage("Docker deployment via stack."){
            steps{
                sh './scripts/docker.sh'
            }
        }
    }
}