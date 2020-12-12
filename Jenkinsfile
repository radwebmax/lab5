pipeline
{
    environment {
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
	options
	{
		timestamps()
	}
	agent none
	stages
	{
		stage('Check scm')
		{
			agent any
			steps
			{
				checkout scm
			}
		} // stage Build
		stage('Build')
		{
			steps
			{
				echo "Building ...${BUILD_NUMBER}"
				echo "Build completed"
			}
		} // stage Build
		stage('Test')
		{
			agent
			{
				docker
				{
					image 'python:3.8.6-slim'
					args '-u=\"root\"'
				}
			}
			steps
			{
				sh 'pip install --no-cache-dir -r ./requirements.txt'
				sh 'python3 unitTest.py'
			}
			post
			{
				always
				{
					junit 'test-reports/*.xml'
				}
				success
				{
					echo "Application testing successfully completed "
				}
				failure
				{
					echo "Oooppss!!! Tests failed!"
				}
			} // post
		} // stage Test
		stage('Docker Publish')
		{
            agent any
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo "Application Publishing"
                checkout scm
                script {
                    def customImage = docker.build("utilka/docker-test:${env.BUILD_ID}")
                    docker.withRegistry('',registryCredential )
                    {
                        customImage.push()}
                    }

            }
		} // stage Docker Publish
	} // stages
}
/*pipeline{
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
                   agent {docker { image 'alpine'
                           args '-u=\"root\"'
        
                               // args '-u=\"root\"'
                    }
                    }
                    steps{
                        
                        // timeout(time: 1, unit: 'MINUTES') {
                                 sh """#!/bin/sh echo "hello world!""""
                                 //sh 'apk add -update python3 py-pip'
                                 //sh 'pip install Flask'
                                 //sh 'pip install xmlrunner'
                                 //sh 'python3 lab5.2.py'
                                   
                              
               //}
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
*/
