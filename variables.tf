variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-hello-world"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "East US"
}

variable "app_name" {
  description = "Name of the App Service"
  type        = string
  default     = "hello-world-flask-app"
}

variable "app_service_sku" {
  description = "SKU for the App Service Plan"
  type        = string
  default     = "F1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}
