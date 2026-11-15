# HANDOFF — MarkovLab

## First run
1. Install Docker Desktop.
2. Extract the zip.
3. Run `docker compose up --build`.
4. Visit `http://localhost:8501`.

## Included
- Python Markov engine (FastAPI + pytest)
- Java Spring Boot API (Maven)
- Streamlit interface
- Dockerfiles + Compose
- Jenkins pipeline
- Kubernetes Namespace, Deployments, Services

## Before CI/CD deployment
- Push to GitHub and create Jenkins Pipeline job.
- Set Jenkins credentials: `docker-registry-url` (Secret text), `docker-registry` (username/password), `kubeconfig` (secret file).
- Jenkins agent requires Docker, Python/pip, Maven, and kubectl.
- Update registry account and verify Minikube/cluster access.
- Never commit credentials.

## Demo/viva flow
1. Explain Markov order and transition probabilities.
2. Generate text in Streamlit.
3. Push a Git commit.
4. Show Jenkins Python tests and Maven build.
5. Explain Docker images.
6. Show Kubernetes pods/services and access the app.

## Known simplifications
- No login or database; no persistent experiment history.
- This is an educational probabilistic generator, not semantic AI.
- Run and verify the full pipeline on the actual lab setup before submission.
