output "db_instance_endpoint" {
  value = aws_db_instance.main.endpoint
}

output "db_instance_password" {
  value     = random_password.password.result
  sensitive = true
}
