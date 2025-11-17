output "vpc_id" {
  description = "The ID of the created VPC."
  value       = module.vpc.vpc_id
}

output "eks_cluster_name" {
  description = "The name of the EKS cluster."
  value       = module.eks.cluster_name
}

output "rds_instance_endpoint" {
  description = "The endpoint of the RDS instance."
  value       = module.rds.db_instance_endpoint
}
