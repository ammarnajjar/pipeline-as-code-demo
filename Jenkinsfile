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
		mail bcc: '', body: '${subject} (${env.BUILD_URL})', cc: '', from: 'jenkins@openshift.com', replyTo: '', subject: '${buildStatus}: Job \'${env.JOB_NAME} [${env.BUILD_NUMBER}]\'', to: 'najjarammar@gmail.com'
 	}
}
