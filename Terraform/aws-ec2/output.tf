output "vm-ip-address" {
  value = "${aws_instance.web}.public_ip"
}