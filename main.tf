terraform {
  required_version = ">= 1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    Environment = var.environment
    Project     = "HelloWorld"
  }
}

resource "azurerm_service_plan" "main" {
  name                = "${var.app_name}-plan"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  os_type             = "Linux"
  sku_name            = var.app_service_sku

  tags = {
    Environment = var.environment
    Project     = "HelloWorld"
  }
}

resource "azurerm_linux_web_app" "main" {
  name                = var.app_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_service_plan.main.location
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      python_version = "3.11"
    }
    always_on = false
  }

  app_settings = {
    "ENVIRONMENT"                    = var.environment
    "SCM_DO_BUILD_DURING_DEPLOYMENT" = "true"
  }

  tags = {
    Environment = var.environment
    Project     = "HelloWorld"
  }
}

output "web_app_url" {
  value = "https://${azurerm_linux_web_app.main.name}.azurewebsites.net"
}

output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "app_service_name" {
  value = azurerm_linux_web_app.main.name
}
