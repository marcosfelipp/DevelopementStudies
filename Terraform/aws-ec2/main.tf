terraform {
  backend "s3" {
    bucket = "ec2-provider-tf-marcos"
    key = "terraform-ec2.tfstate"
    region = "us-east-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.47.0"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = var.region
}