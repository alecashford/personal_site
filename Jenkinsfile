pipeline {
  agent any
  stages {
    stage('Build'){
      steps {
        sh 'whoami'
        sh 'pwd'
        sh 'ls'
        sh 'docker-compose up -d'
      }
    }
    stage('Deploy') {
      steps { 
        sh 'ls'
      }
    }
  }
}