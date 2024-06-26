pipeline {
	agent any
    

	stages {
        stage('Build') {
            steps {
                echo 'Compiling the C++ program...'
                sh 'g++ -o HelloWorld/src/HelloWorld HelloWorld/src/HelloWorld.cpp'
            }
        }

        stage('Test') {
            steps {
                echo 'Running the program...'
                sh './HelloWorld/src/HelloWorld'
            }
        }

		stage('Archive') {
            steps {
                echo 'Archiving the artifacts...'
                archiveArtifacts artifacts: 'HelloWorld/src/HelloWorld', allowEmptyArchive: true
            }
		}
    }
}
