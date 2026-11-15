pipeline {
  agent any
  environment {
    REGISTRY = credentials('docker-registry-url')
    DOCKER_CREDS = 'docker-registry'
    IMAGE_TAG = "${BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Test Python Engine') {
      steps {
        sh 'python3 -m pip install -r engine/requirements.txt'
        sh 'cd engine && python3 -m pytest -q'
      }
    }
    stage('Build and Test Java API') {
      steps { sh 'cd api && mvn -B clean test package' }
    }
    stage('Build Docker Images') {
      steps {
        sh 'docker build -t $REGISTRY/markov-engine:$IMAGE_TAG ./engine'
        sh 'docker build -t $REGISTRY/markov-api:$IMAGE_TAG ./api'
        sh 'docker build -t $REGISTRY/markov-ui:$IMAGE_TAG ./ui'
      }
    }
    stage('Push Images') {
      steps {
        withCredentials([usernamePassword(credentialsId: DOCKER_CREDS, usernameVariable: 'D_USER', passwordVariable: 'D_PASS')]) {
          sh 'echo "$D_PASS" | docker login -u "$D_USER" --password-stdin'
          sh 'docker push $REGISTRY/markov-engine:$IMAGE_TAG'
          sh 'docker push $REGISTRY/markov-api:$IMAGE_TAG'
          sh 'docker push $REGISTRY/markov-ui:$IMAGE_TAG'
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
          sh 'sed "s|IMAGE_REGISTRY|$REGISTRY|g; s|IMAGE_TAG|$IMAGE_TAG|g" k8s/deployments.template.yaml > k8s/deployments.generated.yaml'
          sh 'kubectl apply -f k8s/namespace.yaml'
          sh 'kubectl apply -n markovlab -f k8s/deployments.generated.yaml'
          sh 'kubectl apply -n markovlab -f k8s/services.yaml'
        }
      }
    }
  }
  post { always { sh 'docker logout || true' } }
}
