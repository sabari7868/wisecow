🐄 Wisecow App

A simple Wisdom server that returns random quotes using fortune and cowsay.
This project demonstrates Docker, Kubernetes, CI/CD (GitHub Actions), and temporary public access via ngrok.

Table of Contents

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

Project Overview

Runs a small HTTP server on port 4499.

Returns wisdom quotes formatted by cowsay.

Can be deployed in Docker containers.

Can run in Kubernetes clusters (local kind or cloud).

Exposes a temporary public URL via ngrok for demonstration.

Why server.js Instead of Shell Script

Originally, a shell script was used to serve wisdom quotes. However, it had limitations:

Not fully HTTP-compliant, so browsers could not render the output correctly.

Cannot handle multiple connections efficiently.

Difficult to integrate with Docker or Kubernetes probes.

The project now uses a Node.js HTTP server which:

Works correctly in browsers.

Integrates seamlessly with Docker and Kubernetes probes.

Is simple, extendable, and maintainable.

Prerequisites

Node.js & npm

Docker (for containerized deployment)

kubectl (for Kubernetes)

kind (for local Kubernetes cluster)

ngrok (for temporary public URL)

GitHub account (for CI/CD workflow)

Local Setup

Clone the repository:

git clone https://github.com/<username>/wisecow.git
cd wisecow


Install dependencies:

sudo apt update
sudo apt install nodejs npm fortune cowsay -y


Run the server:

node server.js


Open browser:

http://localhost:4499

Docker Deployment

Build Docker image:

docker build -t wisecow-app .


Run container:

docker run -p 4499:4499 wisecow-app


Open browser:

http://localhost:4499

Kubernetes Deployment

Create local kind cluster:

kind create cluster --name wisecow-cluster


Load Docker image into cluster:

kind load docker-image wisecow-app:latest --name wisecow-cluster


Deploy Kubernetes manifests:

kubectl apply -f wisecow-deployment.yaml
kubectl apply -f wisecow-service.yaml


Forward port to local machine:

kubectl port-forward service/wisecow-service 4499:4499


Open browser:

http://localhost:4499

Temporary Public Access via ngrok

Install ngrok:

sudo apt install ngrok -y


Add your auth token:

ngrok config add-authtoken <YOUR_NGROK_AUTH_TOKEN>


Start tunnel:

ngrok http 4499


ngrok gives a temporary public URL like:

https://abcd1234.ngrok-free.app


Anyone can access the server using this URL temporarily.

Kubernetes Self-Healing Demo

List pods:

kubectl get pods -l app=wisecow


Delete a pod manually:

kubectl delete pod <pod-name>


Observe Kubernetes automatically recreates the pod:

kubectl get pods -l app=wisecow -w


Kubernetes ensures pods are restarted automatically (restartPolicy: Always).

CI/CD Workflow

Workflow file: .github/workflows/build-and-deploy.yml

Workflow Steps:

Checkout repository

Build Docker image

Push image to Docker Hub

Install kubectl & kind

Create a local kind cluster

Load Docker image into the cluster

Deploy Kubernetes manifests (Deployment + Service)

Start ngrok tunnel and print temporary URL

Note: GitHub Actions runners are ephemeral, so pods and ngrok URLs exist only during workflow execution.

Secrets Required
Secret Name	Purpose
DOCKER_USERNAME	Docker Hub login
DOCKER_PASSWORD	Docker Hub password/token
NGROK_AUTH_TOKEN	ngrok public tunnel
