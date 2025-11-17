# A basic RDS module. In a real-world scenario, you'd use the official AWS RDS module.
resource "aws_db_instance" "main" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "14.5"
  instance_class       = var.db_instance_class
  db_name              = var.db_name
  username             = var.db_username
  password             = random_password.password.result
  db_subnet_group_name = aws_db_subnet_group.default.name
  skip_final_snapshot  = true
}

resource "aws_db_subnet_group" "default" {
  name       = "${var.project_name}-sng-${var.env}"
  subnet_ids = var.db_subnets
}

resource "random_password" "password" {
  length           = 16
  special          = true
  override_special = "_%@"
}
