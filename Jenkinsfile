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
			    sh "chmod +x -R ${env.WORKSPACE}/../${env.JOB_NAME}@script"
				sh "${env.WORKSPACE}/../${env.JOB_NAME}@script/script.sh"
			    	 sh 'bash apk add -update python3 py-pip'
                                 sh 'bash pip install Flask'
                                 sh 'bash pip install xmlrunner'
			    	 sh 'bash python3 lab5.2.py'			    	//}
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
