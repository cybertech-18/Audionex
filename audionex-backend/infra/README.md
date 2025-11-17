# Audionex Infrastructure

This directory contains all the Infrastructure as Code (IaC) for deploying the Audionex platform to AWS. It uses a combination of Terraform and Helm.

##  Terraform

Terraform is used to provision the core cloud infrastructure.

### Structure

- **`main.tf`**: The root Terraform file that defines the providers and modules.
- **`variables.tf`**: Input variables for the Terraform configuration.
- **`outputs.tf`**: Outputs from the Terraform configuration.
- **`modules/`**: Reusable Terraform modules for different parts of the infrastructure:
  - **`vpc/`**: Creates a Virtual Private Cloud (VPC).
  - **`eks/`**: Creates an Elastic Kubernetes Service (EKS) cluster.
  - **`rds/`**: Creates a Relational Database Service (RDS) instance for PostgreSQL.

### Usage

1.  **Initialize Terraform:**

    ```bash
    cd audionex-backend/infra/terraform
    terraform init
    ```

2.  **Plan the deployment:**

    ```bash
    terraform plan
    ```

3.  **Apply the changes:**

    ```bash
    terraform apply
    ```

## Helm

Helm is used to package and deploy the Audionex application to the Kubernetes cluster created by Terraform.

### Structure

- **`charts/audionex/`**: The Helm chart for the Audionex application.
  - **`Chart.yaml`**: Metadata about the chart.
  - **`values.yaml`**: The default configuration values for the chart.
  - **`templates/`**: The Kubernetes manifest templates.

### Usage

1.  **Configure `kubectl`:**

    After running `terraform apply`, you will need to configure `kubectl` to connect to your new EKS cluster. You can do this using the AWS CLI:

    ```bash
    aws eks --region $(terraform output -raw aws_region) update-kubeconfig --name $(terraform output -raw eks_cluster_name)
    ```

2.  **Deploy the Helm chart:**

    You can deploy the application using `helm install`. You will need to override the default values in `values.yaml` with the outputs from Terraform (e.g., the RDS endpoint).

    ```bash
    helm install my-release audionex-backend/infra/helm/charts/audionex \
      --set secrets.databaseUrl="postgresql://<user>:<password>@$(terraform output -raw rds_instance_endpoint)/audionex"
    ```
