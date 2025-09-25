# Hello World Flask App with Azure DevOps CI/CD

This repository contains a minimal Flask web application with:  
- CI/CD pipeline (`azure-pipelines.yml`)  
- Infrastructure as Code (`main.tf`)  
- Deployment to Azure App Service  

The goal is to demonstrate CI/CD, IaC, and systematic thinking around deployments.

---

## How to Run/Deploy

### Local Development
```bash
git clone https://github.com/Rautcode/azure-devops-assignment.git
cd azure-devops-assignment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

App runs at:
- http://localhost:5000
- Health check: http://localhost:5000/health
- Info endpoint: http://localhost:5000/info

### Azure DevOps Pipeline
1. Import this repo into Azure DevOps.
2. Create a service connection to Azure Resource Manager.
3. Configure pipeline variables (appName, resourceGroupName).
4. Run the pipeline (azure-pipelines.yml) → builds, tests, and deploys to Azure App Service.

### Infrastructure with Terraform
```bash
terraform init
terraform apply
```
Provisions an App Service and supporting resources in Azure.

## Assumptions
- A valid Azure subscription and permissions are available.
- App Service name must be globally unique.
- Python 3.11 on Linux is the runtime stack.
- Single environment (production only) is used for this task.

## Improvements for Production
- Use Azure Key Vault for secrets and configs.
- Add monitoring/logging via Application Insights.
- Introduce staging → production environments.
- Enable HTTPS enforcement and WAF.
- Add rollback or canary deployment strategy in the pipeline.