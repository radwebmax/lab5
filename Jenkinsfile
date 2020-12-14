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
				   image 'python:3.8.6-slim'
                           args '-u=\"root\"'                           
                    }
                    }
                    steps{
                        
                         //timeout(time: 1, unit: 'MINUTES') {
                                 //sh 'apk add -update python3 py-pip'
                                 //sh 'pip install Flask'
                                 //sh '1pip install xmlrunner'
			    	 //sh 'pip install --no-cache-dir -r ./requirements.txt'			    	
                                 //sh 'python lab5.2.py'
			    echo "Hello world ${SHELL}"
                                   
                              
              // }
                    }
                    post{
                        always{
                            junit 'test-reports/*.xml'
                        success{
                            echo 'Application testing successfully completed'
                        }
                        failure{
                            echo 'Well, well, well... looks like u dont know python...'
                        }
                        }
                    }
                }

            }
        }
