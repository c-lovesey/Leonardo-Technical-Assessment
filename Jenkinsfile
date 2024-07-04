pipeline {
	agent any //allows any available agent to do the task
    

	stages { //Compiling Stage
        stage('Build') {
            steps {
                echo 'Compiling the C++ program...'
                sh 'g++ -o HelloWorld/src/HelloWorld HelloWorld/src/HelloWorld.cpp'
            }
        }
		stage('Archive') { //Archives the program
            steps {
                echo 'Archiving the artifacts...'
                archiveArtifacts artifacts: 'HelloWorld/src/HelloWorld', allowEmptyArchive: true
            }
		}
    }
}
