#!groovy

node('docker') {

    docker.image('python:3.6-stretch').inside('-u root') {
        stage 'Cleanup workspace'
        sh 'chmod 777 -R .'
        sh 'rm -rf *'

        stage 'Checkout SCM'
            checkout([
                $class: 'GitSCM',
                branches: [[name: "refs/heads/${env.BRANCH_NAME}"]],
                extensions: [[$class: 'LocalBranch']],
                userRemoteConfigs: scm.userRemoteConfigs,
                doGenerateSubmoduleConfigurations: false,
                submoduleCfg: []
            ])

        stage 'Install & Unit Tests'
            timestamps {
                timeout(time: 30, unit: 'MINUTES') {
                    try {
                        sh 'pip install . -U --pre'
                        sh 'python setup.py nosetests --with-xunit'
                    } finally {
                        step([$class: 'JUnitResultArchiver', testResults: 'nosetests.xml'])
                    }
		}
	    }
    }
}
	    
// node {
//	stage ('Setup') {
//		createVirtualEnv 'env'
//		executeIn 'env', 'pip install -U -r requirements.txt'
//	}
//	stage ('Run Tests') {
//		executeIn 'env', 'python -m pytest -v tests'
//	}
//	stage ('Notify') {
//		mail bcc: '', body: '${subject} (${env.BUILD_URL})', cc: '', from: 'jenkins@openshift.com', replyTo: '', subject: '${buildStatus}: Job \'${env.JOB_NAME} [${env.BUILD_NUMBER}]\'', to: 'najjarammar@gmail.com'
// 	}
// }


def createVirtualEnv(String name) {
	sh "python -m venv ${name}"
}

def executeIn(String environment, String script) {
	sh "${environment}/bin/activate && " + script
}

