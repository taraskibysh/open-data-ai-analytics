variable "resource_group_name" {
  type        = string
  description = "Назва Resource Group"
  default     = "rg-cloud-lab"
}

variable "location" {
  type        = string
  description = "Регіон Azure"
  default     = "East US"
}

variable "vm_size" {
  type        = string
  description = "Розмір віртуальної машини"
  default     = "Standard_B2s"
}

variable "admin_username" {
  type        = string
  description = "Ім'я адміністратора VM"
  default     = "azureuser"
}