pipeline {
    agent {
        docker {
            image 'cpp-jenkins:latest'
            args '-u root:root' // Run as root to avoid permission issues
        }
    }

    stages {
        stage('Build') {
            steps {
				echo 'Compiling the C++ program...'
                sh 'g++ -o HelloWorld HelloWorld.cpp'
            }
        }

        stage('Test') {
            steps {
                echo 'Running the program...'
                sh './HelloWorld'
            }
        }
		stage('Archive') {
            steps {
                echo 'Archiving the artifacts...'
                archiveArtifacts artifacts: 'HelloWorld', allowEmptyArchive: true
            }
		}
    }
}
