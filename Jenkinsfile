pipeline{
    agent any
    stages{
        stage("Make Scripts Executable"){
            steps{
                sh 'chmod +x ./scripts/*'
            }
        }
        stage("Install Ansible and Run Playbook."){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage("Docker deployment via stack."){
            steps{
                sh './scripts/docker.sh'
            }
        }
    }
}