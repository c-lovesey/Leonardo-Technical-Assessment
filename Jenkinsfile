pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Check if make and g++ are installed
                sh 'make --version'
                sh 'g++ --version'
                
                // Debug: List files in vendor/bin/premake
                sh 'ls -l vendor/bin/premake'
                
                // Debug: List files in the project directory
                sh 'ls -l'
                
                // Build
                sh 'echo "Building..."'
                sh 'chmod +x scripts/Linux-Build.sh'
                sh 'scripts/Linux-Build.sh'
                archiveArtifacts artifacts: 'bin/Debug/*', fingerprint: true
            }
        }
        stage('Test'){
            steps {
                sh 'echo "Running..."'
                sh 'chmod +x scripts/Linux-Run.sh'
                sh 'scripts/Linux-Run.sh'
            }
        }
    }
}
