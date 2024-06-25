pipeline {
    agent any

    environment {
        BUILD_DIR = 'build'
        BIN_DIR = "${BUILD_DIR}/bin"
        SRC_DIR = 'HelloWorld/src'
        EXECUTABLE = 'HelloWorld'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building the C++ project...'
                sh '''
                    mkdir -p ${BUILD_DIR}
                    mkdir -p ${BIN_DIR}
                    g++ -o ${BIN_DIR}/${EXECUTABLE} ${SRC_DIR}/*.cpp
                '''
            }
            post {
                success {
                    archiveArtifacts artifacts: "${BIN_DIR}/${EXECUTABLE}", fingerprint: true
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running the executable...'
                sh "${BIN_DIR}/${EXECUTABLE}"
            }
        }
    }
}
