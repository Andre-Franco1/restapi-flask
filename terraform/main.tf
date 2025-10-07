module "kubernetes" {
  source       = "git@github.com:Andre-Franco1/terraform-eks.git?ref=restapi"
  #source = "/home/ondrej/Documents/terraform-eks"
  cidr_block   = "10.10.0.0/16"
  project_name = "restapi"
  region       = "us-east-1"
  tags = {
    Department = "DevOps"
  }
}