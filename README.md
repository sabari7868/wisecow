🐄 Wisecow App

A Wisdom server that returns random quotes using fortune and cowsay.
This project demonstrates Docker, Kubernetes, CI/CD (GitHub Actions), and temporary public access via ngrok.

📑 Table of Contents

Project Overview

Why server.js Instead of Shell Script

Prerequisites

Local Setup

Docker Deployment

Kubernetes Deployment

Temporary Public Access via ngrok

Kubernetes Self-Healing Demo

CI/CD Workflow

Secrets Required

🌟 Project Overview

Runs a small HTTP server on port 4499

Returns wisdom quotes formatted by cowsay

Deployable in Docker containers or Kubernetes clusters

Provides a temporary public URL via ngrok for demonstration

💡 Why server.js Instead of Shell Script

Originally, a shell script (wisecow.sh) was used:

❌ Limitations:

Not fully HTTP-compliant → browsers could not render correctly

Cannot handle multiple connections efficiently

Difficult to integrate with Docker/Kubernetes probes

✅ Benefits of Node.js HTTP server (server.js):

Works perfectly in browsers

Compatible with readinessProbe & livenessProbe

Simple, extendable, and maintainable

🛠 Prerequisites

Node.js & npm

Docker

kubectl

kind (local Kubernetes cluster)

ngrok (temporary public URL)

GitHub account (for CI/CD)

💻 Local Setup
<details> <summary>Click to expand</summary>
# Clone the repository
git clone https://github.com/<username>/wisecow.git
cd wisecow

# Install dependencies
sudo apt update
sudo apt install nodejs npm fortune cowsay -y

# Run the server
node server.js

# Open browser
http://localhost:4499

</details>
🐳 Docker Deployment
<details> <summary>Click to expand</summary>
# Build Docker image
docker build -t wisecow-app .

# Run Docker container
docker run -p 4499:4499 wisecow-app

# Open browser
http://localhost:4499

</details>
☸️ Kubernetes Deployment
<details> <summary>Click to expand</summary>
# Create kind cluster
kind create cluster --name wisecow-cluster

# Load Docker image into cluster
kind load docker-image wisecow-app:latest --name wisecow-cluster

# Deploy manifests
kubectl apply -f wisecow-deployment.yaml
kubectl apply -f wisecow-service.yaml

# Forward port to local machine
kubectl port-forward service/wisecow-service 4499:4499

# Open browser
http://localhost:4499

</details>
🌐 Temporary Public Access via ngrok
<details> <summary>Click to expand</summary>
# Install ngrok
sudo apt install ngrok -y

# Add auth token
ngrok config add-authtoken <YOUR_NGROK_AUTH_TOKEN>

# Start tunnel
ngrok http 4499


ngrok will provide a temporary public URL, e.g.:
https://abcd1234.ngrok-free.app

Anyone can access your server temporarily.

</details>
🔄 Kubernetes Self-Healing Demo
<details> <summary>Click to expand</summary>
# List pods
kubectl get pods -l app=wisecow

# Delete a pod manually
kubectl delete pod <pod-name>

# Observe automatic recreation
kubectl get pods -l app=wisecow -w


Kubernetes ensures pods are restarted automatically (restartPolicy: Always).

</details>
⚙️ CI/CD Workflow

Workflow file: .github/workflows/build-and-deploy.yml

Steps:

Checkout repository

Build Docker image

Push image to Docker Hub

Install kubectl & kind

Create local kind cluster

Load Docker image into cluster

Deploy Kubernetes manifests (Deployment + Service)

Start ngrok tunnel and print temporary URL

Note: GitHub Actions runners are ephemeral, so pods and ngrok URLs exist only during workflow execution.

🔑 Secrets Required
Secret Name	Purpose
DOCKER_USERNAME	Docker Hub login
DOCKER_PASSWORD	Docker Hub password/token
NGROK_AUTH_TOKEN	ngrok public tunnel
