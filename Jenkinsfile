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
                        
                         timeout(time: 1, unit: 'MINUTES') {
                                 $ 'apk add -update python3 py-pip'
                                 $ 'pip install Flask'
                                 $ 'pip install xmlrunner'
                                   
                              
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
