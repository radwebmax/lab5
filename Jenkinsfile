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
                    stage('test') {
        docker.image('r-base:3.1.2').inside() {
            sh(script: 'ping -c 2 jenkins.io')
        }
    }
               /* stage('Test'){
                    agent { docker{ image 'alpine'
                                args '-u=\"root\"'
                    }
                    }
                    steps{
                        
                         //timeout(time: 5, unit: 'MINUTES') {
                                 sh 'apk add -update python3 py-pip'
                                 sh 'pip install Flask'
                                 sh 'pip install xmlrunner'
                                 sh 'python3 lab5.2.py'
                                   
                              
               // }
                    }*/
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
