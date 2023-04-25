data "aws_ami" "ubuntu"{
  most_recent = true

  filter {
    name   = "name"
    values = ["IaaSWeek-${var.hash_commit}"]
  }
  owners = [""]
}

resource "aws_instance" "web" {
  ami           = "ami-02396cdd13e9a1257"
  instance_type = "t2.micro"
  tags = {
    Name = "web-instance"
  }
}