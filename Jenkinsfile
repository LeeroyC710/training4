pipeline{
        agent any
        stages{ 
		    stage('---First Test---'){
                        steps{
			    sh '''
			    ssh leeroychiweshe@pythontest1 << EOF 
                            python3 -m pytest test/factorial_test.py
			    EOF
			    '''
                        }
                }
        }
}
