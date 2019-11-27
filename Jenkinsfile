pipeline{
        agent any
        stages{
		stage('---Environment Set-Up---'){
			steps{
			    sh '''
			    ssh leeroychiweshe@pythontest1 << EOF 
			    sudo apt-get install git -y
			    rm -rf ./training4
			    git clone https://github.com/LeeroyC710/training4.git
			    '''
                        }
                }
		stage('---Testing---'){
			steps{
			   sh '''
			   ssh leeroychiweshe@pythontest1 << EOF
			   cd ./training4
			   python3 -m pytest ./test/factorial_test.py
			   '''
			}
		}
        }
}
