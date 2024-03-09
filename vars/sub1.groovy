def call(){
pipeline {
    agent any
    environment {
        GIT_URL="${(env.BRANCH_NAME ==~ 'PR.+') ? env.GIT_URL_1 :  env.GIT_URL}"
        GIT_REPO_NAME = "$GIT_URL".replaceFirst(/^.*\/([^\/]+?).git$/, '$1')
        BRANCH_NAME="${env.BRANCH_NAME}"
  }
    stages {
        stage('Fetch ansible and common script code') {
            steps {
                script {
                sh "ls"
                 echo '!* sub1.. *!'
                }
            }
        } 
        stage('Build') {
            steps {
                sh "ls"
            }
        }
        stage('Test') {
            steps {
                // Perform all validation tests
                sh 'ls'

            }
        }

        stage('Check branch and load iaplatform file') {
            steps {
                sh "pwd"
                sh "ls -la"
                echo '!* Checking.. *!'
              
                script {
                  if (env.BRANCH_NAME == 'staging') {
                      VARIABLE_HOST='stage'
                  } else if(env.BRANCH_NAME == 'production') {
                      VARIABLE_HOST='prod'
                  } else if (env.BRANCH_NAME == 'development') {
                      VARIABLE_HOST='dev'
                  }
                   }
            }
        }
        stage('Deploy service package in dev server') {
          when {
              expression {
                return VARIABLE_HOST == 'dev'
                 }    
            }
          steps {
                echo "!* Running Ansible Playbook*!"

          }
        }

         stage('Deploy service package in stage servers') {
          when {
              expression {
                return VARIABLE_HOST == 'stage'
                 }    
            }
          steps {
                echo "!* Running Ansible Playbook stage"
           
          }
         }
        
}
}
}