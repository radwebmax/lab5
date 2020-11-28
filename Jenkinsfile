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
                    agent { docker{ image 'alpine'
                                args '-u=\"root\"'
                    }
                    }
                    steps{
                        //sh 'apk add -update python3 py-pip'
                        //sh 'pip install Flask'
                        //sh 'pip install xmlrunner
                         timeout(time: 1, unit: 'MINUTES') {
                                 sh '''#!/bin/sh
                                         echo "Hello World"
                                    '''
                              // sh ' echo "Hello World" '
                }
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
