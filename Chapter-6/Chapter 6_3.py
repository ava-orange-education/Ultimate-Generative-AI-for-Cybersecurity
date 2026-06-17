# adaptive_security_group.tf
resource "aws_security_group" "genai_adaptive" {
  name_prefix = "genai-adaptive-"
  
  dynamic "ingress" {
    for_each = var.threat_level == "HIGH" ? [1] : []
    content {
      from_port   = 443
      to_port     = 443
      protocol    = "tcp"
      cidr_blocks = ["10.0.0.0/8"]  # Lock to internal only
      description = "HIGH threat lockdown"
    }
  }
  
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = var.threat_level == "LOW" ? ["0.0.0.0/0"] : ["10.0.0.0/8"]
    description = "Adaptive HTTPS access"
  }
  
  lifecycle {
    create_before_destroy = true
  }
}

variable "threat_level" {
  description = "Current threat level: LOW, MEDIUM, HIGH"
  type        = string
  default     = "LOW"
}