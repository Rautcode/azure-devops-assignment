# Hello World Flask App with Azure DevOps CI/CD

A production-ready Flask web application demonstrating enterprise-level DevOps practices with automated deployment to Azure App Service using Azure DevOps pipelines, comprehensive testing, and Infrastructure as Code with Terraform.

## Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── azure-pipelines.yml    # Azure DevOps CI/CD pipeline
├── main.tf               # Terraform infrastructure configuration
├── variables.tf          # Terraform variables
├── Procfile              # Process file for deployment
├── .gitignore            # Git ignore rules
├── tests/                # Test suite
│   ├── __init__.py
│   └── test_app.py
└── README.md             # This file
```

## Features

- Health Check Endpoint: /health - Returns application status
- Info Endpoint: /info - Displays application information
- Main Route: / - Simple Hello World message
- Comprehensive test suite with pytest
- Automated CI/CD pipeline with build, test, and deploy stages
- Infrastructure as Code with Terraform

## Prerequisites

- Azure subscription
- Azure DevOps organization
- Terraform installed locally (for infrastructure provisioning)
- Python 3.11+ (for local development)

## How to Run/Deploy

### Option 1: Azure DevOps (Recommended)

1. Create Azure DevOps Project
   - Create a new project in your Azure DevOps organization
   - Import this repository or push code to Azure DevOps Git

2. Set up Azure Service Connection
   - Go to Project Settings > Service connections
   - Create new Azure Resource Manager connection
   - Name it azure-service-connection (matches pipeline variable)

3. Create Pipeline
   - Go to Pipelines > Create Pipeline
   - Select Azure Repos Git and choose your repository
   - Select existing Azure Pipelines YAML file: azure-pipelines.yml

4. Configure Variables
   - Update pipeline variables if needed:
     - appName: Must be globally unique
     - resourceGroupName: Azure resource group name

5. Run Pipeline
   - Pipeline will automatically trigger on push to main branch
   - Monitors build, test, and deployment stages

### Option 2: Local Development

1. Clone Repository
   ```
   git clone <repository-url>
   cd Azure_Devops_Assignment
   ```

2. Create Virtual Environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run Application
   ```
   python app.py
   ```

5. Access Application
   - Open browser to http://localhost:5000
   - Health check: http://localhost:5000/health
   - App info: http://localhost:5000/info

### Option 3: Infrastructure Deployment

1. Install Terraform
   - Download and install Terraform from terraform.io

2. Initialize Terraform
   ```
   terraform init
   ```

3. Plan Deployment
   ```
   terraform plan
   ```

4. Apply Infrastructure
   ```
   terraform apply
   ```

5. View Outputs
   ```
   terraform output
   ```

## Testing

### Run Tests Locally
```
# Install test dependencies
pip install pytest pytest-cov

# Run tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=app
```

### Test Coverage
The test suite includes:
- Basic endpoint testing
- JSON response validation  
- Environment variable handling
- Error handling scenarios
- CORS header verification
- Advanced test scenarios with fixtures

## Assumptions Made

1. Azure Subscription: Valid Azure subscription with sufficient permissions
2. Service Connection: Azure DevOps service connection is properly configured
3. Resource Naming: App Service names must be globally unique
4. Runtime Stack: Application uses Python 3.11 on Linux
5. Testing: Real pytest test implementation instead of dummy tests
6. Environment: Single production environment (no staging/dev separation)

## Production Improvements

### Security Enhancements
- Implement Azure Key Vault for sensitive configuration
- Add Azure AD authentication for admin endpoints
- Enable HTTPS redirect and HSTS headers
- Configure Web Application Firewall (WAF)
- Implement IP restrictions and network security groups

### Monitoring & Observability
- Integrate Application Insights for monitoring
- Add structured logging with correlation IDs
- Implement health check endpoints with detailed diagnostics
- Set up alerts for application errors and performance metrics
- Configure log retention and archival policies

### Infrastructure & Deployment
- Implement multi-environment setup (dev/staging/prod)
- Add blue-green or canary deployment strategies
- Use Azure Container Registry for containerized deployments
- Implement infrastructure drift detection
- Add backup and disaster recovery procedures

### Application Architecture
- Add proper error handling and exception management
- Implement database connectivity with connection pooling
- Add caching layer (Redis) for improved performance
- Implement API versioning and backward compatibility
- Add rate limiting and throttling

### CI/CD Pipeline Enhancements
- Add security scanning (SAST/DAST)
- Implement automated testing in multiple environments
- Add performance testing and load testing
- Implement approval gates for production deployments
- Add rollback mechanisms and deployment verification

### Scalability & Performance
- Configure auto-scaling based on metrics
- Implement CDN for static content delivery
- Add database read replicas for improved performance
- Implement microservices architecture for better scalability
- Add connection pooling and resource optimization

## Live Endpoints (After Deployment)

- Main App: https://{app-name}.azurewebsites.net/
- Health Check: https://{app-name}.azurewebsites.net/health  
- App Info: https://{app-name}.azurewebsites.net/info

## Pipeline Workflow

### Build Stage
- Python 3.11 environment setup
- Install dependencies via pip
- Run comprehensive test suite
- Create deployment artifacts

### Deploy Stage  
- Deploy to Azure App Service
- Configure Linux runtime with Python 3.11
- Start application with gunicorn WSGI server

## Infrastructure Components

### Azure Resources Created
- Resource Group: Container for all resources
- App Service Plan: Compute resources (Linux, F1 SKU)
- Linux Web App: Application hosting service
- Configured with Python 3.11 runtime stack

### Terraform Configuration
- Provider: AzureRM version 3.0+
- Resource dependencies properly configured
- Environment-specific variables
- Consistent resource tagging

## Troubleshooting

### Common Issues
1. App Name Conflicts: App Service names must be globally unique
2. Service Connection: Ensure Azure service connection is properly configured
3. Permissions: Verify Azure subscription has sufficient permissions
4. Dependencies: Ensure all Python dependencies are listed in requirements.txt

### Debugging Steps
1. Check pipeline logs in Azure DevOps
2. Verify Terraform state and configuration
3. Review application logs in Azure App Service
4. Test endpoints locally before deployment
