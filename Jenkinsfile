pipeline{
        options{timestamps()}
            agent none
            stages{
                stage('Check scm'){
                    agent any
                    steps{
                        checkout scm
                    }
                }
                stage('Build'){
                    steps{
                        echo "Building ... ${BUILD_NUMBER}"
                        echo "Build complete"
                    }
                } 
                stage('Test'){
                   agent {
			   docker {
				   image 'alpine'
                           args '-u=\"root\"'                           
                    }
                    }
                    steps{        
                         //timeout(time: 1, unit: 'MINUTES') {
			    	 //sh 'apk add -update python3 py-pip'
                                 //sh 'pip install Flask'
                                 //sh 'pip install xmlrunner'
			    	 //sh 'python3 lab5.2.py'
			    echo "Bla bla bla ${env.PATH}"
			    sh 'cd var/jenkins_home/workspace/Lab 5 v2.0'
			    echo "Bla bla bla ${env.PATH}"
			    sh 'python3 lab5.2.py'
			    //}
                    }
                    post{
                        always{
                            junit 'test-reports/*.xml'
                        success{
                            echo "Application testing successfully completed"
                        }
                        failure{
                            echo "Well, well, well... looks like u dont know python..."
                        }
                        }
                    }
                }
            }
        }
