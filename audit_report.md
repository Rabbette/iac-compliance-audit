# Infrastructure-as-Code Compliance Audit Report

**Scanned file:** `main.tf`
**Generated:** 2026-06-26 22:30
**Total findings:** 32

## Severity Breakdown

| Severity | Count |
|---|---|
| CRITICAL | 4 |
| HIGH | 2 |
| MEDIUM | 26 |
| LOW | 0 |

## Priority Findings (Critical & High Only)

These require remediation before this infrastructure should ever be deployed. Medium and Low findings are listed in full further below for technical reference, but should not block deployment on their own.

### [CRITICAL] Ensure S3 bucket has block public ACLS enabled
- **Check ID:** `CKV_AWS_53`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket public ACL blocking is disabled, allowing the bucket to be made publicly accessible.

### [CRITICAL] Ensure S3 bucket has block public policy enabled
- **Check ID:** `CKV_AWS_54`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket public policy blocking is disabled, allowing public bucket policies to take effect.

### [CRITICAL] Ensure no security groups allow ingress from 0.0.0.0:0 to port 22
- **Check ID:** `CKV_AWS_24`
- **Resource:** `aws_security_group.app_server_sg`
- **Location:** /main.tf (lines 53-71)
- **Why it matters:** SSH port open to the entire internet allows unrestricted remote access attempts from anywhere.

### [CRITICAL] S3 Bucket has an ACL defined which allows public READ access.
- **Check ID:** `CKV_AWS_20`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** S3 bucket ACL is explicitly set to allow public read access.

### [HIGH] Ensure S3 bucket has 'restrict_public_buckets' enabled
- **Check ID:** `CKV_AWS_56`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket does not restrict public bucket access, increasing risk of accidental public exposure.

### [HIGH] Ensure S3 bucket has ignore public ACLs enabled
- **Check ID:** `CKV_AWS_55`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket does not ignore public ACLs, increasing risk of accidental public exposure.

## Full Findings (All Severities)

### [CRITICAL] Ensure S3 bucket has block public ACLS enabled
- **Check ID:** `CKV_AWS_53`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket public ACL blocking is disabled, allowing the bucket to be made publicly accessible.

### [CRITICAL] Ensure S3 bucket has block public policy enabled
- **Check ID:** `CKV_AWS_54`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket public policy blocking is disabled, allowing public bucket policies to take effect.

### [CRITICAL] Ensure no security groups allow ingress from 0.0.0.0:0 to port 22
- **Check ID:** `CKV_AWS_24`
- **Resource:** `aws_security_group.app_server_sg`
- **Location:** /main.tf (lines 53-71)
- **Why it matters:** SSH port open to the entire internet allows unrestricted remote access attempts from anywhere.

### [CRITICAL] S3 Bucket has an ACL defined which allows public READ access.
- **Check ID:** `CKV_AWS_20`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** S3 bucket ACL is explicitly set to allow public read access.

### [HIGH] Ensure S3 bucket has 'restrict_public_buckets' enabled
- **Check ID:** `CKV_AWS_56`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket does not restrict public bucket access, increasing risk of accidental public exposure.

### [HIGH] Ensure S3 bucket has ignore public ACLs enabled
- **Check ID:** `CKV_AWS_55`
- **Resource:** `aws_s3_bucket_public_access_block.employee_documents_block`
- **Location:** /main.tf (lines 31-37)
- **Why it matters:** S3 bucket does not ignore public ACLs, increasing risk of accidental public exposure.

### [MEDIUM] Ensure no security groups allow egress from 0.0.0.0:0 to port -1
- **Check ID:** `CKV_AWS_382`
- **Resource:** `aws_security_group.app_server_sg`
- **Location:** /main.tf (lines 53-71)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure every security group and rule has a description
- **Check ID:** `CKV_AWS_23`
- **Resource:** `aws_security_group.app_server_sg`
- **Location:** /main.tf (lines 53-71)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure IAM policies does not allow privilege escalation
- **Check ID:** `CKV_AWS_286`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure IAM policies does not allow write access without constraints
- **Check ID:** `CKV_AWS_290`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure IAM policies does not allow data exfiltration
- **Check ID:** `CKV_AWS_288`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure IAM policies that allow full "*-*" administrative privileges are not created
- **Check ID:** `CKV_AWS_62`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure IAM policies does not allow permissions management / resource exposure without constraints
- **Check ID:** `CKV_AWS_289`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure IAM policies does not allow credentials exposure
- **Check ID:** `CKV_AWS_287`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure no IAM policies documents allow "*" as a statement's actions
- **Check ID:** `CKV_AWS_63`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure no IAM policies documents allow "*" as a statement's resource for restrictable actions
- **Check ID:** `CKV_AWS_355`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure S3 buckets should have event notifications enabled
- **Check ID:** `CKV2_AWS_62`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure S3 buckets should have event notifications enabled
- **Check ID:** `CKV2_AWS_62`
- **Resource:** `aws_s3_bucket.backup_storage`
- **Location:** /main.tf (lines 44-46)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that S3 bucket has a Public Access block
- **Check ID:** `CKV2_AWS_6`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that S3 bucket has a Public Access block
- **Check ID:** `CKV2_AWS_6`
- **Resource:** `aws_s3_bucket.backup_storage`
- **Location:** /main.tf (lines 44-46)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure the S3 bucket has access logging enabled
- **Check ID:** `CKV_AWS_18`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure the S3 bucket has access logging enabled
- **Check ID:** `CKV_AWS_18`
- **Resource:** `aws_s3_bucket.backup_storage`
- **Location:** /main.tf (lines 44-46)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that Security Groups are attached to another resource
- **Check ID:** `CKV2_AWS_5`
- **Resource:** `aws_security_group.app_server_sg`
- **Location:** /main.tf (lines 53-71)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that S3 bucket has cross-region replication enabled
- **Check ID:** `CKV_AWS_144`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that S3 bucket has cross-region replication enabled
- **Check ID:** `CKV_AWS_144`
- **Resource:** `aws_s3_bucket.backup_storage`
- **Location:** /main.tf (lines 44-46)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that an S3 bucket has a lifecycle configuration
- **Check ID:** `CKV2_AWS_61`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that an S3 bucket has a lifecycle configuration
- **Check ID:** `CKV2_AWS_61`
- **Resource:** `aws_s3_bucket.backup_storage`
- **Location:** /main.tf (lines 44-46)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure all data stored in the S3 bucket have versioning enabled
- **Check ID:** `CKV_AWS_21`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure all data stored in the S3 bucket have versioning enabled
- **Check ID:** `CKV_AWS_21`
- **Resource:** `aws_s3_bucket.backup_storage`
- **Location:** /main.tf (lines 44-46)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that S3 buckets are encrypted with KMS by default
- **Check ID:** `CKV_AWS_145`
- **Resource:** `aws_s3_bucket.employee_documents`
- **Location:** /main.tf (lines 22-24)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure that S3 buckets are encrypted with KMS by default
- **Check ID:** `CKV_AWS_145`
- **Resource:** `aws_s3_bucket.backup_storage`
- **Location:** /main.tf (lines 44-46)
- **Why it matters:** Deviates from security best practice; recommend review.

### [MEDIUM] Ensure AWS IAM policy does not allow full IAM privileges
- **Check ID:** `CKV2_AWS_40`
- **Resource:** `aws_iam_policy.overly_broad_policy`
- **Location:** /main.tf (lines 78-92)
- **Why it matters:** Deviates from security best practice; recommend review.
