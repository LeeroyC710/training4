pipeline{
        agent any
        stages{ 
		    stage('---First Test---'){
                        steps{
			    sh '''
			    ssh leeroychiweshe@pythontest1 << EOF 
			    sudo apt-get install git -y
			    git clone https://github.com/LeeroyC710/training4.git
			    cd ./training4
                            python3 -m pytest ./test/factorial_test.py
			    '''
                        }
                }
        }
}
