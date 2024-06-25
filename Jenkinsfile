pipeline {
    agent any

    stages {
        
        stage('Build') {
            steps {     
                sh 'make --version'
                sg 'g++ --version'
                sh 'echo "Building..."'
                sh 'g++ HelloWorld.cpp -o HelloWorld'
            }
        }
        stage('Test'){
            steps {
                sh 'echo "Running..."'
                sh 'HelloWorld'
            }
        }
    }
}
