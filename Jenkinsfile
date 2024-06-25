pipeline {
    agent any

    stages {
        stage('Build') {
            steps {              
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
