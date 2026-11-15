# MarkovLab — Probabilistic Text Generation Web Application

A small educational web app demonstrating Markov-chain text generation.
- Streamlit UI (`ui/`)
- Java Spring Boot API built with Maven (`api/`)
- Python FastAPI Markov engine (`engine/`)

## Features
- Paste or upload a text corpus (paste supported in this starter)
- Generate with first-order or second-order Markov chains
- Set output length and random seed
- Health endpoints for all services

## Run locally with Docker Compose
Prerequisite: Docker Desktop with Compose.
```bash
docker compose up --build
```
Open UI at http://localhost:8501. API health: http://localhost:8080/health. Engine health: http://localhost:8000/health.
Stop with `docker compose down`.

## DevOps pipeline
Git/GitHub stores source; Jenkins checks out, runs Python tests and Maven tests/build, builds Docker images, pushes them, and deploys Kubernetes manifests.

Configure Jenkins credentials:
- `docker-registry-url` (Secret text): registry namespace, e.g. `docker.io/yourusername`
- `docker-registry` (Username/Password): registry credentials
- `kubeconfig` (Secret file): cluster kubeconfig

Ensure the Jenkins agent has Docker, Python/pip, Maven, and kubectl. Edit registry/image names for your account.

## Kubernetes
The Jenkinsfile renders `k8s/deployments.template.yaml` with registry and build tag. For manual deployment, substitute `IMAGE_REGISTRY` and `IMAGE_TAG` in that template, then apply namespace, deployments, and services. Port-forward:
```bash
kubectl port-forward -n markovlab svc/markov-ui 8501:8501
```
Then visit http://localhost:8501.

## Viva concepts
- Markov chain: next-token probability depends on a limited history.
- Order 1 uses one previous token; order 2 uses two.
- Maven builds/tests the Java API.
- Jenkins automates build, test, image creation, and deployment.
- Docker packages each service and dependencies.
- Kubernetes manages pods, replicas, and service discovery.

## Important limitations
Educational prototype; no authentication/database. Generation is probabilistic, not semantic AI. Test the full pipeline on the actual lab cluster before submission.
