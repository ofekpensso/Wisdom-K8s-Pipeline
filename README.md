# 🚀 Wisdom K8s Platform - End-to-End DevOps Project

A fully automated Kubernetes platform deployed on AWS, featuring a complete CI/CD pipeline, monitoring stack, and ingress networking.

## 🏗 Architecture
* **Cloud Provider:** AWS (EC2 Instances)
* **Orchestration:** Kubernetes (Kubeadm cluster)
* **CI/CD:** Jenkins (Pipeline as Code), GitHub, Docker Hub
* **Configuration Management:** Ansible (Automated server setup)
* **Monitoring:** Prometheus & Grafana (Full cluster observability)
* **Networking:** NGINX Ingress Controller

## 🔄 The CI/CD Pipeline
1.  **Code Commit:** Developer pushes code to GitHub.
2.  **Trigger:** Jenkins detects the change via Webhook.
3.  **Build:** Docker image is built and tagged with the build number.
4.  **Push:** Image is pushed to Docker Hub registry.
5.  **Deploy:** Jenkins updates the Kubernetes deployment (Zero Downtime).

## 🛠 Tech Stack
* **Infrastructure:** AWS, Linux (Ubuntu)
* **Containerization:** Docker, Kubernetes
* **Automation:** Ansible, Jenkins, Helm
* **Observability:** Prometheus, Grafana
* **Language:** Python (Flask App)
