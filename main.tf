# main.tf
# -----------------------------------------------------------------------------
# Infrastructure-as-Code definition for a fictional company's cloud environment.
#
# IMPORTANT: This file is intentionally misconfigured for audit/training
# purposes. It is never deployed (no `terraform apply` is run). It exists
# only to be scanned by a static analysis tool (Checkov) to demonstrate
# "Shift Left" security auditing, catching misconfigurations before
# infrastructure is ever provisioned.
# -----------------------------------------------------------------------------

provider "aws" {
  region = "us-east-1"
}

# -----------------------------------------------------------------------------
# VIOLATION 1: S3 bucket with public read access.
# This bucket is meant to store internal employee documents but is
# misconfigured to allow public read access, exposing it to anyone on
# the internet.
# -----------------------------------------------------------------------------
resource "aws_s3_bucket" "employee_documents" {
  bucket = "meridian-employee-documents"
}

resource "aws_s3_bucket_acl" "employee_documents_acl" {
  bucket = aws_s3_bucket.employee_documents.id
  acl    = "public-read"
}

resource "aws_s3_bucket_public_access_block" "employee_documents_block" {
  bucket                  = aws_s3_bucket.employee_documents.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# -----------------------------------------------------------------------------
# VIOLATION 2: S3 bucket without encryption configured.
# No server-side encryption block is defined, meaning data at rest is
# stored unencrypted.
# -----------------------------------------------------------------------------
resource "aws_s3_bucket" "backup_storage" {
  bucket = "meridian-backup-storage"
}

# -----------------------------------------------------------------------------
# VIOLATION 3: Security group with SSH open to the entire internet.
# Port 22 (SSH) is open to 0.0.0.0/0, meaning anyone on the internet
# can attempt to connect, rather than restricting it to known IP ranges.
# -----------------------------------------------------------------------------
resource "aws_security_group" "app_server_sg" {
  name        = "app-server-sg"
  description = "Security group for the application server"

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# -----------------------------------------------------------------------------
# VIOLATION 4: IAM policy with overly broad permissions.
# This policy grants full administrative access ("*") instead of scoping
# permissions to only what's needed (least privilege).
# -----------------------------------------------------------------------------
resource "aws_iam_policy" "overly_broad_policy" {
  name        = "app-admin-policy"
  description = "Policy for application server access"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}
