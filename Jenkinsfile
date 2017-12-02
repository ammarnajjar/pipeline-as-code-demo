#!groovy

node {
	stage 'Setup' {
		createVirtualEnv 'env'
		executeIn 'env', 'pip install -U -r requirements.txt'
	}
	stage 'Run Tests' {
		executeIn 'env', 'python -m pytest -v tests'
	}
	stage 'Notify' {
		mail bcc: '', body: '${subject} (${env.BUILD_URL})', cc: '', from: 'jenkins@openshift.com', replyTo: '', subject: '${buildStatus}: Job \'${env.JOB_NAME} [${env.BUILD_NUMBER}]\'', to: 'najjarammar@gmail.com'
	}
}


def createVirtualEnv(String name) {
	sh 'python3 -m venv ${name}'
}

def executeIn(String environment, String script) {
	sh "${environment}/bin/activate && " + script
}

