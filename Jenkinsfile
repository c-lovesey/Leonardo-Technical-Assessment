pipeline {
	agent any
    

    stages {
        stage('Build') {
            steps {
				echo 'Compiling the C++ program...'
				dir('HelloWorld/src') {
					sh 'g++ -o HelloWorld HelloWorld\src\HelloWorld.cpp'
				}
            }
        }

        stage('Test') {
            steps {
                echo 'Running the program...'
                dir('HelloWorld/src') {
                    sh './HelloWorld'
				}
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
