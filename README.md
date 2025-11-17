# 🔊 Audionex — Build Intelligent Voice Agents From a Single Prompt

Audionex is a next-generation platform for creating, testing, and deploying AI-powered voice agents—without complex engineering. This repository contains the source code for the Audionex platform, including the backend API, infrastructure as code, and frontend landing page.

## 🚀 Project Structure

The repository is organized into the following main components:

- **`index.html`**: The static frontend landing page.
- **`audionex-backend/`**: The core of the project, containing the backend service and all infrastructure code.

### Backend & Infrastructure (`audionex-backend/`)

- **`app/`**: A production-grade FastAPI application that serves the main API. It includes a structured layout for API endpoints, database models, data schemas, and configuration.
- **`infra/`**: All Infrastructure as Code (IaC) for deploying Audionex to a cloud environment.
  - **`terraform/`**: Terraform code to provision cloud resources, including a VPC, an EKS (Kubernetes) cluster, and an RDS (PostgreSQL) database.
  - **`helm/`**: A Helm chart for deploying the Audionex FastAPI application to the Kubernetes cluster.
- **`requirements.txt`**: A list of Python dependencies required for the backend application.

For detailed instructions on the backend and infrastructure, please see the `README.md` files within those directories.

## 🏁 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Python 3.9+](https://www.python.org/downloads/)
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- [Helm](https://helm.sh/docs/intro/install/)
- An AWS account with credentials configured for Terraform.

### 1. Running the Backend Locally

For instructions on how to run the FastAPI application on your local machine for development, please see the [backend README](./audionex-backend/README.md).

### 2. Deploying the Infrastructure

The infrastructure is managed with Terraform and Helm. For detailed steps on how to provision the cloud resources and deploy the application, please see the [infrastructure README](./audionex-backend/infra/README.md).

---

*This project was bootstrapped with the help of GitHub Copilot.*
