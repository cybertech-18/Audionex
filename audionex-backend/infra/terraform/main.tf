terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  backend "s3" {
    # This will be configured in the CI/CD pipeline
    # bucket         = "your-terraform-state-bucket"
    # key            = "audionex/terraform.tfstate"
    # region         = "us-east-1"
    # encrypt        = true
    # dynamodb_table = "your-terraform-lock-table"
  }
}

provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source = "./modules/vpc"

  project_name = var.project_name
  env          = var.env
  aws_region   = var.aws_region
}

module "eks" {
  source = "./modules/eks"

  project_name      = var.project_name
  env               = var.env
  vpc_id            = module.vpc.vpc_id
  private_subnets   = module.vpc.private_subnets
  cluster_version   = "1.28"
}

module "rds" {
  source = "./modules/rds"

  project_name      = var.project_name
  env               = var.env
  vpc_id            = module.vpc.vpc_id
  db_subnets        = module.vpc.private_subnets # Use private subnets for DB
  db_instance_class = "db.t3.micro"
  db_name           = "audionex"
  db_username       = "admin"
}
