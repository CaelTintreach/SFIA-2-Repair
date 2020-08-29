pipeline{
    agent any
    environment{
        DATABASE_URI = credentials('mysql+pymysql://root:root@database:3306/prizedb')
        MYSQL_ROOT_PASSWORD = credentials('root')
    }
    stages{
        stage("Make Scripts Executable"){
            steps{
                sh 'chmod +x ./scripts/*'
            }
        }
}