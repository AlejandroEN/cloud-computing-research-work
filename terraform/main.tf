# Configuración del proveedor de AWS
provider "aws" {
  region = "us-east-1"
}

# 1. Crear grupo de seguridad (Security Group)
resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Permitir SSH y HTTP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
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

# 2. Crear instancia EC2
resource "aws_instance" "web_instance" {
  ami           = "ami-0aa28dab1f2852040"  # Cambia con la AMI que desees
  instance_type = "t3.micro"
  key_name      = "vockey"  # Asegúrate de que el par de claves SSH esté disponible

  security_groups = [aws_security_group.web_sg.name]

  root_block_device {
    volume_size = 20  # Tamaño del disco (20 GB)
  }

  tags = {
    Name = "MV-MVD-Terraform"
  }
}

# 3. Exportar la IP pública de la instancia
output "public_ip" {
  value = aws_instance.web_instance.public_ip
}
