#!groovy
	    
node {
	stage ('Setup') {
		echo 'This is setup stage'
	}
	stage ('Run Tests') {
		echo 'This is run tests stage'
		sh 'which python'
	}
	stage ('Notify') {
		echo 'This is notification stage (smtp should be configured correctly)'
 	}
}
