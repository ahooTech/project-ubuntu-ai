# Staff Canteen Management System

Generated: 09/02/2026 08:27:47

---

## Table of Contents

- .gitignore
- cicd\azure-devops\pipelines\deployment-pipeline.yml
- cicd\azure-devops\pipelines\infrastructure-pipeline.yml
- cicd\azure-devops\pipelines\mlops-pipeline.yml
- cicd\azure-devops\pipelines\README.md
- cicd\azure-devops\templates\build-template.yml
- cicd\azure-devops\templates\deploy-template.yml
- cicd\azure-devops\templates\README.md
- cicd\github-actions\actions\deploy-to-k8s\action.yml
- cicd\github-actions\actions\deploy-to-k8s\README.md
- cicd\github-actions\workflows\ci-credit-model-api.yml
- cicd\github-actions\workflows\ci-customer-rag.yml
- cicd\github-actions\workflows\ci-fraud-agent.yml
- cicd\github-actions\workflows\ci-genai-gateway.yml
- cicd\github-actions\workflows\kubernetes-deploy.yml
- cicd\github-actions\workflows\README.md
- cicd\github-actions\workflows\release.yml
- cicd\github-actions\workflows\security-scan.yml
- cicd\github-actions\workflows\terraform-plan-apply.yml
- cicd\jenkins\Jenkinsfile
- cicd\jenkins\jobs\legacy-batch-processing\jenkins-config.xml
- cicd\jenkins\jobs\legacy-batch-processing\README.md
- cost-optimization\budgets\aws-budgets.json
- cost-optimization\budgets\azure-budgets.json
- cost-optimization\budgets\README.md
- cost-optimization\cost-allocation-tags.md
- cost-optimization\recommendations\README.md
- cost-optimization\recommendations\reserved-capacity.md
- cost-optimization\recommendations\rightsizing.md
- cost-optimization\recommendations\spot-instances.md
- cost-optimization\reports\cost-trend-analysis.py
- cost-optimization\reports\monthly-cost-report.py
- cost-optimization\reports\README.md
- disaster-recovery\backup-scripts\backup-databases.sh
- disaster-recovery\backup-scripts\backup-etcd.sh
- disaster-recovery\backup-scripts\backup-k8s-resources.sh
- disaster-recovery\backup-scripts\README.md
- disaster-recovery\backup-strategy.md
- disaster-recovery\dr-runbook.md
- disaster-recovery\dr-tests\failover-test.md
- disaster-recovery\dr-tests\README.md
- disaster-recovery\dr-tests\restore-validation.md
- disaster-recovery\restore-scripts\README.md
- disaster-recovery\restore-scripts\restore-databases.sh
- disaster-recovery\restore-scripts\restore-k8s-resources.sh
- docs\architecture\diagrams\README.md
- docs\architecture\network-design.md
- docs\architecture\security-design.md
- docs\architecture\target-architecture.md
- docs\cicd\deployment-strategies.md
- docs\cicd\pipeline-standards.md
- docs\cicd\README.md
- docs\disaster-recovery\backup-restore.md
- docs\disaster-recovery\dr-plan.md
- docs\disaster-recovery\README.md
- docs\infrastructure\kubernetes-operations.md
- docs\infrastructure\README.md
- docs\infrastructure\security-compliance.md
- docs\infrastructure\terraform-standards.md
- docs\interview-proof\demo-script.md
- docs\interview-proof\metrics-dashboard.md
- docs\interview-proof\project-summary.md
- docs\interview-proof\README.md
- docs\monitoring\alert-runbooks.md
- docs\monitoring\observability-stack.md
- docs\monitoring\README.md
- docs\runbooks\database-issues.md
- docs\runbooks\failed-deployment.md
- docs\runbooks\high-cpu-memory.md
- docs\runbooks\incident-response.md
- docs\runbooks\pod-crash-loop.md
- docs\runbooks\README.md
- docs\workloads\credit-model-api.md
- docs\workloads\customer-rag.md
- docs\workloads\fraud-agent.md
- docs\workloads\genai-gateway.md
- docs\workloads\gpu-training-job.md
- docs\workloads\mlops-registry.md
- docs\workloads\README.md
- Generate-Codebook.ps1
- infrastructure\arm-templates\environments\dev\main.json
- infrastructure\arm-templates\environments\dev\README.md
- infrastructure\arm-templates\environments\production\main.json
- infrastructure\arm-templates\environments\production\README.md
- infrastructure\arm-templates\guardrails\azure-defender.json
- infrastructure\arm-templates\guardrails\azure-policy.json
- infrastructure\arm-templates\guardrails\monitoring-baseline.json
- infrastructure\arm-templates\guardrails\README.md
- infrastructure\aws-cdk\app.py
- infrastructure\aws-cdk\cdk.json
- infrastructure\aws-cdk\requirements.txt
- infrastructure\aws-cdk\ubuntu_ai\__init__.py
- infrastructure\aws-cdk\ubuntu_ai\ai_services_stack.py
- infrastructure\aws-cdk\ubuntu_ai\bedrock_stack.py
- infrastructure\aws-cdk\ubuntu_ai\databricks_stack.py
- infrastructure\terraform\backend-config\dev.tfvars
- infrastructure\terraform\backend-config\production.tfvars
- infrastructure\terraform\backend-config\README.md
- infrastructure\terraform\backend-config\staging.tfvars
- infrastructure\terraform\environments\dev\backend.tf
- infrastructure\terraform\environments\dev\main.tf
- infrastructure\terraform\environments\dev\providers.tf
- infrastructure\terraform\environments\dev\README.md
- infrastructure\terraform\environments\dev\terraform.tfvars
- infrastructure\terraform\environments\dev\variables.tf
- infrastructure\terraform\environments\production\backend.tf
- infrastructure\terraform\environments\production\main.tf
- infrastructure\terraform\environments\production\providers.tf
- infrastructure\terraform\environments\production\README.md
- infrastructure\terraform\environments\production\terraform.tfvars
- infrastructure\terraform\environments\production\variables.tf
- infrastructure\terraform\environments\staging\backend.tf
- infrastructure\terraform\environments\staging\main.tf
- infrastructure\terraform\environments\staging\providers.tf
- infrastructure\terraform\environments\staging\README.md
- infrastructure\terraform\environments\staging\terraform.tfvars
- infrastructure\terraform\environments\staging\variables.tf
- infrastructure\terraform\modules\aws-eks\main.tf
- infrastructure\terraform\modules\aws-eks\outputs.tf
- infrastructure\terraform\modules\aws-eks\README.md
- infrastructure\terraform\modules\aws-eks\variables.tf
- infrastructure\terraform\modules\aws-eks\versions.tf
- infrastructure\terraform\modules\aws-networking\main.tf
- infrastructure\terraform\modules\aws-networking\outputs.tf
- infrastructure\terraform\modules\aws-networking\README.md
- infrastructure\terraform\modules\aws-networking\variables.tf
- infrastructure\terraform\modules\aws-networking\versions.tf
- infrastructure\terraform\modules\aws-security\main.tf
- infrastructure\terraform\modules\aws-security\outputs.tf
- infrastructure\terraform\modules\aws-security\README.md
- infrastructure\terraform\modules\aws-security\variables.tf
- infrastructure\terraform\modules\azure-aks\main.tf
- infrastructure\terraform\modules\azure-aks\outputs.tf
- infrastructure\terraform\modules\azure-aks\README.md
- infrastructure\terraform\modules\azure-aks\variables.tf
- infrastructure\terraform\modules\azure-networking\main.tf
- infrastructure\terraform\modules\azure-networking\outputs.tf
- infrastructure\terraform\modules\azure-networking\README.md
- infrastructure\terraform\modules\azure-networking\variables.tf
- infrastructure\terraform\modules\azure-security\main.tf
- infrastructure\terraform\modules\azure-security\outputs.tf
- infrastructure\terraform\modules\azure-security\README.md
- infrastructure\terraform\modules\azure-security\variables.tf
- infrastructure\terraform\modules\databases\main.tf
- infrastructure\terraform\modules\databases\outputs.tf
- infrastructure\terraform\modules\databases\README.md
- infrastructure\terraform\modules\databases\variables.tf
- infrastructure\terraform\modules\monitoring\main.tf
- infrastructure\terraform\modules\monitoring\outputs.tf
- infrastructure\terraform\modules\monitoring\README.md
- infrastructure\terraform\modules\monitoring\variables.tf
- interview-proof\before-after-comparison.md
- interview-proof\demo-video-script.md
- interview-proof\jd-coverage-matrix.md
- interview-proof\metrics-summary.md
- interview-proof\portfolio-checklist.md
- interview-proof\project-presentation.md
- interview-proof\technical-deep-dive.md
- kubernetes\base\namespaces.yaml
- kubernetes\base\network-policies\default-deny.yaml
- kubernetes\base\network-policies\README.md
- kubernetes\base\rbac\README.md
- kubernetes\base\rbac\role-bindings.yaml
- kubernetes\base\rbac\roles.yaml
- kubernetes\base\rbac\service-accounts.yaml
- kubernetes\helm-charts\monitoring-stack\Chart.yaml
- kubernetes\helm-charts\monitoring-stack\templates\alertmanager.yaml
- kubernetes\helm-charts\monitoring-stack\templates\grafana.yaml
- kubernetes\helm-charts\monitoring-stack\templates\prometheus.yaml
- kubernetes\helm-charts\monitoring-stack\templates\README.md
- kubernetes\helm-charts\monitoring-stack\values.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\Chart.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\templates\_helpers.tpl
- kubernetes\helm-charts\ubuntu-ai-platform\templates\configmap.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\templates\deployment.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\templates\hpa.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\templates\ingress.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\templates\README.md
- kubernetes\helm-charts\ubuntu-ai-platform\templates\service.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\values.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\values-dev.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\values-production.yaml
- kubernetes\helm-charts\ubuntu-ai-platform\values-staging.yaml
- kubernetes\jobs\backup-job.yaml
- kubernetes\jobs\gpu-training-job.yaml
- kubernetes\jobs\README.md
- kubernetes\overlays\dev\kustomization.yaml
- kubernetes\overlays\dev\namespace-patch.yaml
- kubernetes\overlays\dev\README.md
- kubernetes\overlays\dev\resource-limits.yaml
- kubernetes\overlays\production\kustomization.yaml
- kubernetes\overlays\production\namespace-patch.yaml
- kubernetes\overlays\production\README.md
- kubernetes\overlays\staging\kustomization.yaml
- kubernetes\overlays\staging\namespace-patch.yaml
- kubernetes\overlays\staging\README.md
- kubernetes\workloads\credit-model-api\configmap.yaml
- kubernetes\workloads\credit-model-api\deployment.yaml
- kubernetes\workloads\credit-model-api\hpa.yaml
- kubernetes\workloads\credit-model-api\ingress.yaml
- kubernetes\workloads\credit-model-api\README.md
- kubernetes\workloads\credit-model-api\secrets.yaml
- kubernetes\workloads\credit-model-api\service.yaml
- kubernetes\workloads\customer-rag\deployment.yaml
- kubernetes\workloads\customer-rag\README.md
- kubernetes\workloads\customer-rag\service.yaml
- kubernetes\workloads\customer-rag\statefulset.yaml
- kubernetes\workloads\fraud-agent\deployment.yaml
- kubernetes\workloads\fraud-agent\hpa.yaml
- kubernetes\workloads\fraud-agent\README.md
- kubernetes\workloads\fraud-agent\service.yaml
- kubernetes\workloads\genai-gateway\deployment.yaml
- kubernetes\workloads\genai-gateway\ingress.yaml
- kubernetes\workloads\genai-gateway\README.md
- kubernetes\workloads\genai-gateway\service.yaml
- kubernetes\workloads\mlops-registry\deployment.yaml
- kubernetes\workloads\mlops-registry\pvc.yaml
- kubernetes\workloads\mlops-registry\README.md
- kubernetes\workloads\mlops-registry\service.yaml
- LICENSE
- monitoring\alertmanager\config.yml
- monitoring\alertmanager\templates\README.md
- monitoring\alertmanager\templates\slack-template.tmpl
- monitoring\elasticsearch\elasticsearch.yml
- monitoring\elasticsearch\index-templates\logs-template.json
- monitoring\elasticsearch\index-templates\README.md
- monitoring\elasticsearch\ingest-pipelines\logs-pipeline.json
- monitoring\elasticsearch\ingest-pipelines\README.md
- monitoring\fluentbit\fluent-bit.conf
- monitoring\fluentbit\parsers.conf
- monitoring\fluentbit\README.md
- monitoring\grafana\dashboards\ai-workloads-dashboard.json
- monitoring\grafana\dashboards\application-dashboard.json
- monitoring\grafana\dashboards\business-metrics-dashboard.json
- monitoring\grafana\dashboards\cost-dashboard.json
- monitoring\grafana\dashboards\infrastructure-dashboard.json
- monitoring\grafana\dashboards\kubernetes-dashboard.json
- monitoring\grafana\dashboards\README.md
- monitoring\grafana\datasources\prometheus.yml
- monitoring\grafana\datasources\README.md
- monitoring\grafana\provisioning\dashboards.yml
- monitoring\grafana\provisioning\README.md
- monitoring\opentelemetry\instrumentation\python-auto-instrumentation.yaml
- monitoring\opentelemetry\instrumentation\README.md
- monitoring\opentelemetry\otel-collector-config.yml
- monitoring\prometheus\alerting-rules.yml
- monitoring\prometheus\prometheus.yml
- monitoring\prometheus\recording-rules.yml
- monitoring\prometheus\scrape-configs\kubernetes-sd.yml
- monitoring\prometheus\scrape-configs\README.md
- monitoring\prometheus\scrape-configs\static-configs.yml
- README.md
- scripts\bash\backup_check.sh
- scripts\bash\cleanup_old_images.sh
- scripts\bash\collect_logs.sh
- scripts\bash\disk_usage_check.sh
- scripts\bash\gpu_monitoring.sh
- scripts\bash\k8s_diagnostics.sh
- scripts\bash\linux_health_check.sh
- scripts\bash\README.md
- scripts\powershell\AccessReviewReport.ps1
- scripts\powershell\AzureCostReport.ps1
- scripts\powershell\AzureResourceInventory.ps1
- scripts\powershell\EntraIDUserAudit.ps1
- scripts\powershell\README.md
- scripts\powershell\ServiceStatusCheck.ps1
- scripts\powershell\WindowsHealthCheck.ps1
- scripts\python\backup_validator.py
- scripts\python\certificate_checker.py
- scripts\python\cost_report.py
- scripts\python\deployment_health.py
- scripts\python\incident_report.py
- scripts\python\k8s_resource_report.py
- scripts\python\model_health_check.py
- scripts\python\README.md
- scripts\python\stale_resources.py
- security\compliance\audit-checklist.md
- security\compliance\banking-compliance.md
- security\compliance\README.md
- security\compliance\security-policies.md
- security\iam\aws-iam-policies\ai-platform-role.json
- security\iam\aws-iam-policies\data-scientist-role.json
- security\iam\aws-iam-policies\platform-engineer-role.json
- security\iam\aws-iam-policies\README.md
- security\iam\azure-rbac\ai-platform-role.json
- security\iam\azure-rbac\monitoring-role.json
- security\iam\azure-rbac\README.md
- security\iam\k8s-rbac\bindings.yaml
- security\iam\k8s-rbac\README.md
- security\iam\k8s-rbac\roles.yaml
- security\scanning\checkov-config.yaml
- security\scanning\README.md
- security\scanning\sonarqube.properties
- security\scanning\trivy-config.yaml
- security\secrets\external-secrets\aws-secrets-manager.yaml
- security\secrets\external-secrets\azure-key-vault.yaml
- security\secrets\external-secrets\README.md
- security\secrets\secrets-management.md
- testing\chaos-tests\network-latency-experiment.yaml
- testing\chaos-tests\node-drain-experiment.yaml
- testing\chaos-tests\pod-kill-experiment.yaml
- testing\chaos-tests\README.md
- testing\integration-tests\README.md
- testing\integration-tests\test_api_integration.py
- testing\integration-tests\test_workflows.py
- testing\load-tests\k6\credit-api-load.js
- testing\load-tests\k6\fraud-agent-load.js
- testing\load-tests\k6\gateway-load.js
- testing\load-tests\k6\README.md
- testing\load-tests\locust\locustfile.py
- testing\load-tests\locust\README.md
- workloads\credit-model-api\.env
- workloads\credit-model-api\.env.example
- workloads\credit-model-api\Codebase.md
- workloads\credit-model-api\docker-compose.yml
- workloads\credit-model-api\Dockerfile
- workloads\credit-model-api\Makefile
- workloads\credit-model-api\pytest.ini
- workloads\credit-model-api\requirements.txt
- workloads\credit-model-api\src\__init__.py
- workloads\credit-model-api\src\api\__init__.py
- workloads\credit-model-api\src\api\README.md
- workloads\credit-model-api\src\api\routes.py
- workloads\credit-model-api\src\config\__init__.py
- workloads\credit-model-api\src\config\README.md
- workloads\credit-model-api\src\config\settings.py
- workloads\credit-model-api\src\main.py
- workloads\credit-model-api\src\models\__init__.py
- workloads\credit-model-api\src\models\credit_model.py
- workloads\credit-model-api\src\models\README.md
- workloads\credit-model-api\tests\__init__.py
- workloads\credit-model-api\tests\README.md
- workloads\credit-model-api\tests\test_api.py
- workloads\customer-rag\docker-compose.yml
- workloads\customer-rag\Dockerfile
- workloads\customer-rag\requirements.txt
- workloads\customer-rag\src\config\README.md
- workloads\customer-rag\src\config\settings.py
- workloads\customer-rag\src\main.py
- workloads\customer-rag\src\rag\generator.py
- workloads\customer-rag\src\rag\README.md
- workloads\customer-rag\src\rag\retriever.py
- workloads\customer-rag\src\vector_db\milvus_client.py
- workloads\customer-rag\src\vector_db\README.md
- workloads\customer-rag\tests\README.md
- workloads\customer-rag\tests\test_rag.py
- workloads\fraud-agent\docker-compose.yml
- workloads\fraud-agent\Dockerfile
- workloads\fraud-agent\requirements.txt
- workloads\fraud-agent\src\agents\fraud_investigator.py
- workloads\fraud-agent\src\agents\README.md
- workloads\fraud-agent\src\agents\workflow.py
- workloads\fraud-agent\src\config\README.md
- workloads\fraud-agent\src\config\settings.py
- workloads\fraud-agent\src\main.py
- workloads\fraud-agent\tests\README.md
- workloads\fraud-agent\tests\test_agent.py
- workloads\genai-gateway\docker-compose.yml
- workloads\genai-gateway\Dockerfile
- workloads\genai-gateway\requirements.txt
- workloads\genai-gateway\src\config\README.md
- workloads\genai-gateway\src\config\settings.py
- workloads\genai-gateway\src\gateway\providers\azure_ai.py
- workloads\genai-gateway\src\gateway\providers\bedrock.py
- workloads\genai-gateway\src\gateway\providers\README.md
- workloads\genai-gateway\src\gateway\rate_limiter.py
- workloads\genai-gateway\src\gateway\router.py
- workloads\genai-gateway\src\main.py
- workloads\genai-gateway\tests\README.md
- workloads\genai-gateway\tests\test_gateway.py
- workloads\gpu-training-job\Dockerfile
- workloads\gpu-training-job\k8s-job.yaml
- workloads\gpu-training-job\requirements.txt
- workloads\gpu-training-job\src\config.py
- workloads\gpu-training-job\src\model.py
- workloads\gpu-training-job\src\README.md
- workloads\gpu-training-job\src\train.py
- workloads\gpu-training-job\tests\README.md
- workloads\gpu-training-job\tests\test_training.py
- workloads\mlops-registry\docker-compose.yml
- workloads\mlops-registry\mlflow\Dockerfile
- workloads\mlops-registry\mlflow\mlflow_config.py
- workloads\mlops-registry\mlflow\README.md
- workloads\mlops-registry\models\sample_models\README.md

---


<div style='page-break-after: always;'></div>

# File: .gitignore

```gitignore
# Git ignore file
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
pip-log.txt
pip-delete-this-directory.txt
.env
.venv
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec
*.log
*.bak
*.swp
.vscode/
.idea/
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
terraform.tfstate
terraform.tfstate.backup
*.tfvars
*.tfvars.json
.kube/
*.key
*.pem
*.crt
*.p12
node_modules/
.DS_Store
Thumbs.db

```


<div style='page-break-after: always;'></div>

# File: cicd\azure-devops\pipelines\deployment-pipeline.yml

```yml
# deployment-pipeline.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\azure-devops\pipelines\infrastructure-pipeline.yml

```yml
# infrastructure-pipeline.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\azure-devops\pipelines\mlops-pipeline.yml

```yml
# mlops-pipeline.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\azure-devops\pipelines\README.md

```md
# pipelines

```


<div style='page-break-after: always;'></div>

# File: cicd\azure-devops\templates\build-template.yml

```yml
# build-template.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\azure-devops\templates\deploy-template.yml

```yml
# deploy-template.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\azure-devops\templates\README.md

```md
# templates

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\actions\deploy-to-k8s\action.yml

```yml
# action.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\actions\deploy-to-k8s\README.md

```md
# deploy-to-k8s

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\ci-credit-model-api.yml

```yml
# ci-credit-model-api.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\ci-customer-rag.yml

```yml
# ci-customer-rag.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\ci-fraud-agent.yml

```yml
# ci-fraud-agent.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\ci-genai-gateway.yml

```yml
# ci-genai-gateway.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\kubernetes-deploy.yml

```yml
# kubernetes-deploy.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\README.md

```md
# workflows

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\release.yml

```yml
# release.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\security-scan.yml

```yml
# security-scan.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\github-actions\workflows\terraform-plan-apply.yml

```yml
# terraform-plan-apply.yml

```


<div style='page-break-after: always;'></div>

# File: cicd\jenkins\Jenkinsfile

```text
# Jenkinsfile

```


<div style='page-break-after: always;'></div>

# File: cicd\jenkins\jobs\legacy-batch-processing\jenkins-config.xml

```xml
# jenkins-config.xml

```


<div style='page-break-after: always;'></div>

# File: cicd\jenkins\jobs\legacy-batch-processing\README.md

```md
# legacy-batch-processing

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\budgets\aws-budgets.json

```json
# aws-budgets.json

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\budgets\azure-budgets.json

```json
# azure-budgets.json

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\budgets\README.md

```md
# budgets

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\cost-allocation-tags.md

```md
# cost-allocation-tags.md

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\recommendations\README.md

```md
# recommendations

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\recommendations\reserved-capacity.md

```md
# reserved-capacity.md

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\recommendations\rightsizing.md

```md
# rightsizing.md

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\recommendations\spot-instances.md

```md
# spot-instances.md

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\reports\cost-trend-analysis.py

```py
# cost-trend-analysis.py

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\reports\monthly-cost-report.py

```py
# monthly-cost-report.py

```


<div style='page-break-after: always;'></div>

# File: cost-optimization\reports\README.md

```md
# reports

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\backup-scripts\backup-databases.sh

```sh
# backup-databases.sh

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\backup-scripts\backup-etcd.sh

```sh
# backup-etcd.sh

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\backup-scripts\backup-k8s-resources.sh

```sh
# backup-k8s-resources.sh

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\backup-scripts\README.md

```md
# backup-scripts

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\backup-strategy.md

```md
# backup-strategy.md

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\dr-runbook.md

```md
# dr-runbook.md

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\dr-tests\failover-test.md

```md
# failover-test.md

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\dr-tests\README.md

```md
# dr-tests

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\dr-tests\restore-validation.md

```md
# restore-validation.md

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\restore-scripts\README.md

```md
# restore-scripts

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\restore-scripts\restore-databases.sh

```sh
# restore-databases.sh

```


<div style='page-break-after: always;'></div>

# File: disaster-recovery\restore-scripts\restore-k8s-resources.sh

```sh
# restore-k8s-resources.sh

```


<div style='page-break-after: always;'></div>

# File: docs\architecture\diagrams\README.md

```md
# diagrams

```


<div style='page-break-after: always;'></div>

# File: docs\architecture\network-design.md

```md
# network-design.md

```


<div style='page-break-after: always;'></div>

# File: docs\architecture\security-design.md

```md
# security-design.md

```


<div style='page-break-after: always;'></div>

# File: docs\architecture\target-architecture.md

```md
# target-architecture.md

```


<div style='page-break-after: always;'></div>

# File: docs\cicd\deployment-strategies.md

```md
# deployment-strategies.md

```


<div style='page-break-after: always;'></div>

# File: docs\cicd\pipeline-standards.md

```md
# pipeline-standards.md

```


<div style='page-break-after: always;'></div>

# File: docs\cicd\README.md

```md
# cicd

```


<div style='page-break-after: always;'></div>

# File: docs\disaster-recovery\backup-restore.md

```md
# backup-restore.md

```


<div style='page-break-after: always;'></div>

# File: docs\disaster-recovery\dr-plan.md

```md
# dr-plan.md

```


<div style='page-break-after: always;'></div>

# File: docs\disaster-recovery\README.md

```md
# disaster-recovery

```


<div style='page-break-after: always;'></div>

# File: docs\infrastructure\kubernetes-operations.md

```md
# kubernetes-operations.md

```


<div style='page-break-after: always;'></div>

# File: docs\infrastructure\README.md

```md
# infrastructure

```


<div style='page-break-after: always;'></div>

# File: docs\infrastructure\security-compliance.md

```md
# security-compliance.md

```


<div style='page-break-after: always;'></div>

# File: docs\infrastructure\terraform-standards.md

```md
# terraform-standards.md

```


<div style='page-break-after: always;'></div>

# File: docs\interview-proof\demo-script.md

```md
# demo-script.md

```


<div style='page-break-after: always;'></div>

# File: docs\interview-proof\metrics-dashboard.md

```md
# metrics-dashboard.md

```


<div style='page-break-after: always;'></div>

# File: docs\interview-proof\project-summary.md

```md
# project-summary.md

```


<div style='page-break-after: always;'></div>

# File: docs\interview-proof\README.md

```md
# interview-proof

```


<div style='page-break-after: always;'></div>

# File: docs\monitoring\alert-runbooks.md

```md
# alert-runbooks.md

```


<div style='page-break-after: always;'></div>

# File: docs\monitoring\observability-stack.md

```md
# observability-stack.md

```


<div style='page-break-after: always;'></div>

# File: docs\monitoring\README.md

```md
# monitoring

```


<div style='page-break-after: always;'></div>

# File: docs\runbooks\database-issues.md

```md
# database-issues.md

```


<div style='page-break-after: always;'></div>

# File: docs\runbooks\failed-deployment.md

```md
# failed-deployment.md

```


<div style='page-break-after: always;'></div>

# File: docs\runbooks\high-cpu-memory.md

```md
# high-cpu-memory.md

```


<div style='page-break-after: always;'></div>

# File: docs\runbooks\incident-response.md

```md
# incident-response.md

```


<div style='page-break-after: always;'></div>

# File: docs\runbooks\pod-crash-loop.md

```md
# pod-crash-loop.md

```


<div style='page-break-after: always;'></div>

# File: docs\runbooks\README.md

```md
# runbooks

```


<div style='page-break-after: always;'></div>

# File: docs\workloads\credit-model-api.md

```md
# credit-model-api.md

```


<div style='page-break-after: always;'></div>

# File: docs\workloads\customer-rag.md

```md
# customer-rag.md

```


<div style='page-break-after: always;'></div>

# File: docs\workloads\fraud-agent.md

```md
# fraud-agent.md

```


<div style='page-break-after: always;'></div>

# File: docs\workloads\genai-gateway.md

```md
# genai-gateway.md

```


<div style='page-break-after: always;'></div>

# File: docs\workloads\gpu-training-job.md

```md
# gpu-training-job.md

```


<div style='page-break-after: always;'></div>

# File: docs\workloads\mlops-registry.md

```md
# mlops-registry.md

```


<div style='page-break-after: always;'></div>

# File: docs\workloads\README.md

```md
# workloads

```


<div style='page-break-after: always;'></div>

# File: Generate-Codebook.ps1

```ps1
<#
.\Generate-Codebook.ps1 -ProjectPath "C:\project-ubuntu-ai"
#>


param(
    [string]$ProjectPath = (Get-Location).Path,
    [switch]$GeneratePdf
)

# ============================================================
# Configuration
# ============================================================

$Root = (Resolve-Path $ProjectPath).Path

$MarkdownFile = Join-Path $Root "Codebase.md"
$PdfFile      = Join-Path $Root "Codebase.pdf"

$ExcludedDirectories = @(
    ".git",
    ".github",
    "node_modules",
    "coverage",
    "dist",
    "build",
    "bin",
    "obj",
    "venv",
    ".venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".idea",
    ".vscode",
    "migrations"
)

$ExcludedExtensions = @(
    ".png",".jpg",".jpeg",".gif",".bmp",".ico",".svg",".webp",".avif",
    ".pdf",".zip",".7z",".rar",
    ".exe",".dll",".so",
    ".woff",".woff2",".ttf",".eot",
    ".pyc",".class",".db",".sqlite3",".log"
)

# Delete old markdown if it exists
if (Test-Path $MarkdownFile) {
    Remove-Item $MarkdownFile -Force
}

# ============================================================
# Helper Function
# ============================================================

function Add-Line {
    param([string]$Text)

    Add-Content -Path $MarkdownFile -Value $Text -Encoding UTF8
}

# ============================================================
# Scan Files
# ============================================================

Write-Host ""
Write-Host "Scanning repository..."
Write-Host ""

$Files = Get-ChildItem -Path $Root -Recurse -File | Where-Object {

    $relative = $_.FullName.Substring($Root.Length).TrimStart('\')

    foreach ($dir in $ExcludedDirectories) {
        if ($relative -split "\\" -contains $dir) {
            return $false
        }
    }

    if ($ExcludedExtensions -contains $_.Extension.ToLower()) {
        return $false
    }

    return $true

} | Sort-Object FullName

Write-Host "Found $($Files.Count) files."
Write-Host ""

# ============================================================
# Markdown Header
# ============================================================

Add-Line "# Staff Canteen Management System"
Add-Line ""
Add-Line "Generated: $(Get-Date)"
Add-Line ""
Add-Line "---"
Add-Line ""

# ============================================================
# Table of Contents
# ============================================================

Add-Line "## Table of Contents"
Add-Line ""

foreach ($file in $Files) {

    $relative = $file.FullName.Substring($Root.Length).TrimStart('\')

    Add-Line "- $relative"

}

Add-Line ""
Add-Line "---"
Add-Line ""

# ============================================================
# Add Every File
# ============================================================

$index = 1

foreach ($file in $Files) {

    $relative = $file.FullName.Substring($Root.Length).TrimStart('\')

    Write-Host "[$index/$($Files.Count)] $relative"

    $language = $file.Extension.TrimStart('.')

    if ([string]::IsNullOrWhiteSpace($language)) {
        $language = "text"
    }

    Add-Line ""
    Add-Line "<div style='page-break-after: always;'></div>"
    Add-Line ""
    Add-Line "# File: $relative"
    Add-Line ""

    # Opening code fence
    Add-Line ('```' + $language)

    try {

        $content = Get-Content $file.FullName -Raw -Encoding UTF8

        Add-Content -Path $MarkdownFile -Value $content -Encoding UTF8

    }
    catch {

        Add-Line "[Unable to read file.]"

    }

    # Closing code fence
    Add-Line '```'
    Add-Line ""

    $index++

}

Write-Host ""
Write-Host "Markdown created successfully!"
Write-Host ""
Write-Host $MarkdownFile

# ============================================================
# Optional PDF Generation
# ============================================================

if ($GeneratePdf) {

    $Pandoc = Get-Command pandoc -ErrorAction SilentlyContinue

    if ($Pandoc) {

        Write-Host ""
        Write-Host "Generating PDF..."

        & pandoc `
            $MarkdownFile `
            -o $PdfFile `
            --toc `
            --highlight-style=tango

        Write-Host ""
        Write-Host "PDF created:"
        Write-Host $PdfFile

    }
    else {

        Write-Host ""
        Write-Host "Pandoc was not found."
        Write-Host ""
        Write-Host "Install it from:"
        Write-Host "https://pandoc.org/installing.html"

    }

}
```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\environments\dev\main.json

```json
# main.json

```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\environments\dev\README.md

```md
# dev

```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\environments\production\main.json

```json
# main.json

```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\environments\production\README.md

```md
# production

```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\guardrails\azure-defender.json

```json
# azure-defender.json

```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\guardrails\azure-policy.json

```json
# azure-policy.json

```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\guardrails\monitoring-baseline.json

```json
# monitoring-baseline.json

```


<div style='page-break-after: always;'></div>

# File: infrastructure\arm-templates\guardrails\README.md

```md
# guardrails

```


<div style='page-break-after: always;'></div>

# File: infrastructure\aws-cdk\app.py

```py
# app.py

```


<div style='page-break-after: always;'></div>

# File: infrastructure\aws-cdk\cdk.json

```json
# cdk.json

```


<div style='page-break-after: always;'></div>

# File: infrastructure\aws-cdk\requirements.txt

```txt
# requirements.txt

```


<div style='page-break-after: always;'></div>

# File: infrastructure\aws-cdk\ubuntu_ai\__init__.py

```py
# ubuntu_ai

```


<div style='page-break-after: always;'></div>

# File: infrastructure\aws-cdk\ubuntu_ai\ai_services_stack.py

```py
# ai_services_stack.py

```


<div style='page-break-after: always;'></div>

# File: infrastructure\aws-cdk\ubuntu_ai\bedrock_stack.py

```py
# bedrock_stack.py

```


<div style='page-break-after: always;'></div>

# File: infrastructure\aws-cdk\ubuntu_ai\databricks_stack.py

```py
# databricks_stack.py

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\backend-config\dev.tfvars

```tfvars
# dev.tfvars

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\backend-config\production.tfvars

```tfvars
# production.tfvars

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\backend-config\README.md

```md
# backend-config

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\backend-config\staging.tfvars

```tfvars
# staging.tfvars

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\dev\backend.tf

```tf
# backend.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\dev\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\dev\providers.tf

```tf
# providers.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\dev\README.md

```md
# dev

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\dev\terraform.tfvars

```tfvars
# terraform.tfvars

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\dev\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\production\backend.tf

```tf
# backend.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\production\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\production\providers.tf

```tf
# providers.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\production\README.md

```md
# production

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\production\terraform.tfvars

```tfvars
# terraform.tfvars

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\production\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\staging\backend.tf

```tf
# backend.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\staging\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\staging\providers.tf

```tf
# providers.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\staging\README.md

```md
# staging

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\staging\terraform.tfvars

```tfvars
# terraform.tfvars

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\environments\staging\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-eks\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-eks\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-eks\README.md

```md
# aws-eks

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-eks\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-eks\versions.tf

```tf
# versions.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-networking\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-networking\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-networking\README.md

```md
# aws-networking

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-networking\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-networking\versions.tf

```tf
# versions.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-security\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-security\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-security\README.md

```md
# aws-security

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\aws-security\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-aks\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-aks\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-aks\README.md

```md
# azure-aks

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-aks\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-networking\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-networking\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-networking\README.md

```md
# azure-networking

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-networking\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-security\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-security\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-security\README.md

```md
# azure-security

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\azure-security\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\databases\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\databases\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\databases\README.md

```md
# databases

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\databases\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\monitoring\main.tf

```tf
# main.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\monitoring\outputs.tf

```tf
# outputs.tf

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\monitoring\README.md

```md
# monitoring

```


<div style='page-break-after: always;'></div>

# File: infrastructure\terraform\modules\monitoring\variables.tf

```tf
# variables.tf

```


<div style='page-break-after: always;'></div>

# File: interview-proof\before-after-comparison.md

```md
# before-after-comparison.md

```


<div style='page-break-after: always;'></div>

# File: interview-proof\demo-video-script.md

```md
# demo-video-script.md

```


<div style='page-break-after: always;'></div>

# File: interview-proof\jd-coverage-matrix.md

```md
# jd-coverage-matrix.md

```


<div style='page-break-after: always;'></div>

# File: interview-proof\metrics-summary.md

```md
# metrics-summary.md

```


<div style='page-break-after: always;'></div>

# File: interview-proof\portfolio-checklist.md

```md
# portfolio-checklist.md

```


<div style='page-break-after: always;'></div>

# File: interview-proof\project-presentation.md

```md
# project-presentation.md

```


<div style='page-break-after: always;'></div>

# File: interview-proof\technical-deep-dive.md

```md
# technical-deep-dive.md

```


<div style='page-break-after: always;'></div>

# File: kubernetes\base\namespaces.yaml

```yaml
# namespaces.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\base\network-policies\default-deny.yaml

```yaml
# default-deny.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\base\network-policies\README.md

```md
# network-policies

```


<div style='page-break-after: always;'></div>

# File: kubernetes\base\rbac\README.md

```md
# rbac

```


<div style='page-break-after: always;'></div>

# File: kubernetes\base\rbac\role-bindings.yaml

```yaml
# role-bindings.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\base\rbac\roles.yaml

```yaml
# roles.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\base\rbac\service-accounts.yaml

```yaml
# service-accounts.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\monitoring-stack\Chart.yaml

```yaml
# Chart.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\monitoring-stack\templates\alertmanager.yaml

```yaml
# alertmanager.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\monitoring-stack\templates\grafana.yaml

```yaml
# grafana.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\monitoring-stack\templates\prometheus.yaml

```yaml
# prometheus.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\monitoring-stack\templates\README.md

```md
# templates

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\monitoring-stack\values.yaml

```yaml
# values.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\Chart.yaml

```yaml
# Chart.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\templates\_helpers.tpl

```tpl
# _helpers.tpl

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\templates\configmap.yaml

```yaml
# configmap.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\templates\deployment.yaml

```yaml
# deployment.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\templates\hpa.yaml

```yaml
# hpa.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\templates\ingress.yaml

```yaml
# ingress.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\templates\README.md

```md
# templates

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\templates\service.yaml

```yaml
# service.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\values.yaml

```yaml
# values.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\values-dev.yaml

```yaml
# values-dev.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\values-production.yaml

```yaml
# values-production.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\helm-charts\ubuntu-ai-platform\values-staging.yaml

```yaml
# values-staging.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\jobs\backup-job.yaml

```yaml
# backup-job.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\jobs\gpu-training-job.yaml

```yaml
# gpu-training-job.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\jobs\README.md

```md
# jobs

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\dev\kustomization.yaml

```yaml
# kustomization.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\dev\namespace-patch.yaml

```yaml
# namespace-patch.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\dev\README.md

```md
# dev

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\dev\resource-limits.yaml

```yaml
# resource-limits.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\production\kustomization.yaml

```yaml
# kustomization.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\production\namespace-patch.yaml

```yaml
# namespace-patch.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\production\README.md

```md
# production

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\staging\kustomization.yaml

```yaml
# kustomization.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\staging\namespace-patch.yaml

```yaml
# namespace-patch.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\overlays\staging\README.md

```md
# staging

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\credit-model-api\configmap.yaml

```yaml
# configmap.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\credit-model-api\deployment.yaml

```yaml
# deployment.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\credit-model-api\hpa.yaml

```yaml
# hpa.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\credit-model-api\ingress.yaml

```yaml
# ingress.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\credit-model-api\README.md

```md
# credit-model-api

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\credit-model-api\secrets.yaml

```yaml
# secrets.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\credit-model-api\service.yaml

```yaml
# service.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\customer-rag\deployment.yaml

```yaml
# deployment.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\customer-rag\README.md

```md
# customer-rag

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\customer-rag\service.yaml

```yaml
# service.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\customer-rag\statefulset.yaml

```yaml
# statefulset.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\fraud-agent\deployment.yaml

```yaml
# deployment.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\fraud-agent\hpa.yaml

```yaml
# hpa.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\fraud-agent\README.md

```md
# fraud-agent

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\fraud-agent\service.yaml

```yaml
# service.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\genai-gateway\deployment.yaml

```yaml
# deployment.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\genai-gateway\ingress.yaml

```yaml
# ingress.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\genai-gateway\README.md

```md
# genai-gateway

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\genai-gateway\service.yaml

```yaml
# service.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\mlops-registry\deployment.yaml

```yaml
# deployment.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\mlops-registry\pvc.yaml

```yaml
# pvc.yaml

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\mlops-registry\README.md

```md
# mlops-registry

```


<div style='page-break-after: always;'></div>

# File: kubernetes\workloads\mlops-registry\service.yaml

```yaml
# service.yaml

```


<div style='page-break-after: always;'></div>

# File: LICENSE

```text
MIT License

```


<div style='page-break-after: always;'></div>

# File: monitoring\alertmanager\config.yml

```yml
# config.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\alertmanager\templates\README.md

```md
# templates

```


<div style='page-break-after: always;'></div>

# File: monitoring\alertmanager\templates\slack-template.tmpl

```tmpl
# slack-template.tmpl

```


<div style='page-break-after: always;'></div>

# File: monitoring\elasticsearch\elasticsearch.yml

```yml
# elasticsearch.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\elasticsearch\index-templates\logs-template.json

```json
# logs-template.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\elasticsearch\index-templates\README.md

```md
# index-templates

```


<div style='page-break-after: always;'></div>

# File: monitoring\elasticsearch\ingest-pipelines\logs-pipeline.json

```json
# logs-pipeline.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\elasticsearch\ingest-pipelines\README.md

```md
# ingest-pipelines

```


<div style='page-break-after: always;'></div>

# File: monitoring\fluentbit\fluent-bit.conf

```conf
# fluent-bit.conf

```


<div style='page-break-after: always;'></div>

# File: monitoring\fluentbit\parsers.conf

```conf
# parsers.conf

```


<div style='page-break-after: always;'></div>

# File: monitoring\fluentbit\README.md

```md
# fluentbit

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\dashboards\ai-workloads-dashboard.json

```json
# ai-workloads-dashboard.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\dashboards\application-dashboard.json

```json
# application-dashboard.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\dashboards\business-metrics-dashboard.json

```json
# business-metrics-dashboard.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\dashboards\cost-dashboard.json

```json
# cost-dashboard.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\dashboards\infrastructure-dashboard.json

```json
# infrastructure-dashboard.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\dashboards\kubernetes-dashboard.json

```json
# kubernetes-dashboard.json

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\dashboards\README.md

```md
# dashboards

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\datasources\prometheus.yml

```yml
# prometheus.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\datasources\README.md

```md
# datasources

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\provisioning\dashboards.yml

```yml
# dashboards.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\grafana\provisioning\README.md

```md
# provisioning

```


<div style='page-break-after: always;'></div>

# File: monitoring\opentelemetry\instrumentation\python-auto-instrumentation.yaml

```yaml
# python-auto-instrumentation.yaml

```


<div style='page-break-after: always;'></div>

# File: monitoring\opentelemetry\instrumentation\README.md

```md
# instrumentation

```


<div style='page-break-after: always;'></div>

# File: monitoring\opentelemetry\otel-collector-config.yml

```yml
# otel-collector-config.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\prometheus\alerting-rules.yml

```yml
# alerting-rules.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\prometheus\prometheus.yml

```yml
# prometheus.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\prometheus\recording-rules.yml

```yml
# recording-rules.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\prometheus\scrape-configs\kubernetes-sd.yml

```yml
# kubernetes-sd.yml

```


<div style='page-break-after: always;'></div>

# File: monitoring\prometheus\scrape-configs\README.md

```md
# scrape-configs

```


<div style='page-break-after: always;'></div>

# File: monitoring\prometheus\scrape-configs\static-configs.yml

```yml
# static-configs.yml

```


<div style='page-break-after: always;'></div>

# File: README.md

```md
# Project Ubuntu AI

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\backup_check.sh

```sh
# backup_check.sh

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\cleanup_old_images.sh

```sh
# cleanup_old_images.sh

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\collect_logs.sh

```sh
# collect_logs.sh

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\disk_usage_check.sh

```sh
# disk_usage_check.sh

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\gpu_monitoring.sh

```sh
# gpu_monitoring.sh

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\k8s_diagnostics.sh

```sh
# k8s_diagnostics.sh

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\linux_health_check.sh

```sh
# linux_health_check.sh

```


<div style='page-break-after: always;'></div>

# File: scripts\bash\README.md

```md
# bash

```


<div style='page-break-after: always;'></div>

# File: scripts\powershell\AccessReviewReport.ps1

```ps1
# AccessReviewReport.ps1

```


<div style='page-break-after: always;'></div>

# File: scripts\powershell\AzureCostReport.ps1

```ps1
# AzureCostReport.ps1

```


<div style='page-break-after: always;'></div>

# File: scripts\powershell\AzureResourceInventory.ps1

```ps1
# AzureResourceInventory.ps1

```


<div style='page-break-after: always;'></div>

# File: scripts\powershell\EntraIDUserAudit.ps1

```ps1
# EntraIDUserAudit.ps1

```


<div style='page-break-after: always;'></div>

# File: scripts\powershell\README.md

```md
# powershell

```


<div style='page-break-after: always;'></div>

# File: scripts\powershell\ServiceStatusCheck.ps1

```ps1
# ServiceStatusCheck.ps1

```


<div style='page-break-after: always;'></div>

# File: scripts\powershell\WindowsHealthCheck.ps1

```ps1
# WindowsHealthCheck.ps1

```


<div style='page-break-after: always;'></div>

# File: scripts\python\backup_validator.py

```py
# backup_validator.py

```


<div style='page-break-after: always;'></div>

# File: scripts\python\certificate_checker.py

```py
# certificate_checker.py

```


<div style='page-break-after: always;'></div>

# File: scripts\python\cost_report.py

```py
# cost_report.py

```


<div style='page-break-after: always;'></div>

# File: scripts\python\deployment_health.py

```py
# deployment_health.py

```


<div style='page-break-after: always;'></div>

# File: scripts\python\incident_report.py

```py
# incident_report.py

```


<div style='page-break-after: always;'></div>

# File: scripts\python\k8s_resource_report.py

```py
# k8s_resource_report.py

```


<div style='page-break-after: always;'></div>

# File: scripts\python\model_health_check.py

```py
# model_health_check.py

```


<div style='page-break-after: always;'></div>

# File: scripts\python\README.md

```md
# python

```


<div style='page-break-after: always;'></div>

# File: scripts\python\stale_resources.py

```py
# stale_resources.py

```


<div style='page-break-after: always;'></div>

# File: security\compliance\audit-checklist.md

```md
# audit-checklist.md

```


<div style='page-break-after: always;'></div>

# File: security\compliance\banking-compliance.md

```md
# banking-compliance.md

```


<div style='page-break-after: always;'></div>

# File: security\compliance\README.md

```md
# compliance

```


<div style='page-break-after: always;'></div>

# File: security\compliance\security-policies.md

```md
# security-policies.md

```


<div style='page-break-after: always;'></div>

# File: security\iam\aws-iam-policies\ai-platform-role.json

```json
# ai-platform-role.json

```


<div style='page-break-after: always;'></div>

# File: security\iam\aws-iam-policies\data-scientist-role.json

```json
# data-scientist-role.json

```


<div style='page-break-after: always;'></div>

# File: security\iam\aws-iam-policies\platform-engineer-role.json

```json
# platform-engineer-role.json

```


<div style='page-break-after: always;'></div>

# File: security\iam\aws-iam-policies\README.md

```md
# aws-iam-policies

```


<div style='page-break-after: always;'></div>

# File: security\iam\azure-rbac\ai-platform-role.json

```json
# ai-platform-role.json

```


<div style='page-break-after: always;'></div>

# File: security\iam\azure-rbac\monitoring-role.json

```json
# monitoring-role.json

```


<div style='page-break-after: always;'></div>

# File: security\iam\azure-rbac\README.md

```md
# azure-rbac

```


<div style='page-break-after: always;'></div>

# File: security\iam\k8s-rbac\bindings.yaml

```yaml
# bindings.yaml

```


<div style='page-break-after: always;'></div>

# File: security\iam\k8s-rbac\README.md

```md
# k8s-rbac

```


<div style='page-break-after: always;'></div>

# File: security\iam\k8s-rbac\roles.yaml

```yaml
# roles.yaml

```


<div style='page-break-after: always;'></div>

# File: security\scanning\checkov-config.yaml

```yaml
# checkov-config.yaml

```


<div style='page-break-after: always;'></div>

# File: security\scanning\README.md

```md
# scanning

```


<div style='page-break-after: always;'></div>

# File: security\scanning\sonarqube.properties

```properties
# sonarqube.properties

```


<div style='page-break-after: always;'></div>

# File: security\scanning\trivy-config.yaml

```yaml
# trivy-config.yaml

```


<div style='page-break-after: always;'></div>

# File: security\secrets\external-secrets\aws-secrets-manager.yaml

```yaml
# aws-secrets-manager.yaml

```


<div style='page-break-after: always;'></div>

# File: security\secrets\external-secrets\azure-key-vault.yaml

```yaml
# azure-key-vault.yaml

```


<div style='page-break-after: always;'></div>

# File: security\secrets\external-secrets\README.md

```md
# external-secrets

```


<div style='page-break-after: always;'></div>

# File: security\secrets\secrets-management.md

```md
# secrets-management.md

```


<div style='page-break-after: always;'></div>

# File: testing\chaos-tests\network-latency-experiment.yaml

```yaml
# network-latency-experiment.yaml

```


<div style='page-break-after: always;'></div>

# File: testing\chaos-tests\node-drain-experiment.yaml

```yaml
# node-drain-experiment.yaml

```


<div style='page-break-after: always;'></div>

# File: testing\chaos-tests\pod-kill-experiment.yaml

```yaml
# pod-kill-experiment.yaml

```


<div style='page-break-after: always;'></div>

# File: testing\chaos-tests\README.md

```md
# chaos-tests

```


<div style='page-break-after: always;'></div>

# File: testing\integration-tests\README.md

```md
# integration-tests

```


<div style='page-break-after: always;'></div>

# File: testing\integration-tests\test_api_integration.py

```py
# test_api_integration.py

```


<div style='page-break-after: always;'></div>

# File: testing\integration-tests\test_workflows.py

```py
# test_workflows.py

```


<div style='page-break-after: always;'></div>

# File: testing\load-tests\k6\credit-api-load.js

```js
# credit-api-load.js

```


<div style='page-break-after: always;'></div>

# File: testing\load-tests\k6\fraud-agent-load.js

```js
# fraud-agent-load.js

```


<div style='page-break-after: always;'></div>

# File: testing\load-tests\k6\gateway-load.js

```js
# gateway-load.js

```


<div style='page-break-after: always;'></div>

# File: testing\load-tests\k6\README.md

```md
# k6

```


<div style='page-break-after: always;'></div>

# File: testing\load-tests\locust\locustfile.py

```py
# locustfile.py

```


<div style='page-break-after: always;'></div>

# File: testing\load-tests\locust\README.md

```md
# locust

```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\.env

```env
APP_NAME=credit-model-api
APP_ENV=development
LOG_LEVEL=INFO
MODEL_VERSION=1.0.0-mock
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\.env.example

```example
APP_NAME=credit-model-api
APP_ENV=development
LOG_LEVEL=INFO
MODEL_VERSION=1.0.0-mock
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\Codebase.md

```md
# Staff Canteen Management System

Generated: 09/02/2026 01:15:38

---

## Table of Contents

- .env
- .env.example
- docker-compose.yml
- Dockerfile
- Makefile
- requirements.txt
- src\__init__.py
- src\api\__init__.py
- src\api\README.md
- src\api\routes.py
- src\config\__init__.py
- src\config\README.md
- src\config\settings.py
- src\main.py
- src\models\__init__.py
- src\models\credit_model.py
- src\models\README.md
- tests\__init__.py
- tests\README.md
- tests\test_api.py

---


<div style='page-break-after: always;'></div>

# File: .env

```env
APP_NAME=credit-model-api
APP_ENV=development
LOG_LEVEL=INFO
MODEL_VERSION=1.0.0-mock
```


<div style='page-break-after: always;'></div>

# File: .env.example

```example
APP_NAME=credit-model-api
APP_ENV=development
LOG_LEVEL=INFO
MODEL_VERSION=1.0.0-mock
```


<div style='page-break-after: always;'></div>

# File: docker-compose.yml

```yml
# docker-compose.yml
version: '3.8'

services:
  credit-model-api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: credit-model-api
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped
    networks:
      - ubuntu-ai-network

networks:
  ubuntu-ai-network:
    driver: bridge
```


<div style='page-break-after: always;'></div>

# File: Dockerfile

```text
# Dockerfile
# --- Build Stage ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Runtime Stage ---
FROM python:3.11-slim

WORKDIR /app

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY src/ ./src/

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Start command
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
```


<div style='page-break-after: always;'></div>

# File: Makefile

```text
# Makefile
.PHONY: venv install run test build docker-run docker-stop docker-logs lint clean

# ==========================================
# Virtual Environment Configuration (Windows)
# ==========================================
VENV_DIR = .venv
PYTHON = $(VENV_DIR)\Scripts\python.exe
PIP = $(VENV_DIR)\Scripts\pip.exe
PYTEST = $(VENV_DIR)\Scripts\pytest.exe
UVICORN = $(VENV_DIR)\Scripts\uvicorn.exe

# ==========================================
# Virtual Environment Management
# ==========================================
venv:
	python -m venv $(VENV_DIR)
	@echo Virtual environment created at $(VENV_DIR)

# ==========================================
# Local Development
# ==========================================
install: venv
	$(PIP) install -r requirements.txt

run:
	$(UVICORN) src.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(PYTEST) tests/ -v --tb=short

lint:
	@echo Linting passed (placeholder)

# ==========================================
# Docker Operations
# ==========================================
build:
	docker build -t credit-model-api:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f

# ==========================================
# Cleanup (Windows Native Commands)
# ==========================================
clean:
	@if exist $(VENV_DIR) rmdir /s /q $(VENV_DIR)
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@del /s /q *.pyc 2>nul
	@echo Cleanup complete.
```


<div style='page-break-after: always;'></div>

# File: requirements.txt

```txt
fastapi==0.115.4
uvicorn[standard]==0.32.0
pydantic==2.9.2
pydantic-settings==2.6.1
httpx==0.27.2
pytest==8.3.3
pytest-asyncio==0.24.0
python-json-logger==3.2.1
prometheus-fastapi-instrumentator==7.0.2
opentelemetry-api==1.27.0
opentelemetry-sdk==1.27.0
opentelemetry-instrumentation-fastapi==0.48b0
setuptools==75.8.0
```


<div style='page-break-after: always;'></div>

# File: src\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\api\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\api\README.md

```md
# api

```


<div style='page-break-after: always;'></div>

# File: src\api\routes.py

```py
# routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from prometheus_client import Counter, Histogram
from opentelemetry import trace

from src.models.credit_model import get_model
from src.config.settings import get_settings

router = APIRouter()
settings = get_settings()
model = get_model(settings.MODEL_VERSION)
tracer = trace.get_tracer(__name__)

# --- Custom AI Platform Metrics ---
CREDIT_PREDICTIONS_TOTAL = Counter(
    'afribank_credit_predictions_total', 
    'Total number of credit score predictions',
    ['decision'] # Labels: 'Approved' or 'Declined'
)

PREDICTION_LATENCY = Histogram(
    'afribank_prediction_latency_seconds', 
    'Time taken to process a credit prediction'
)

# --- Request/Response Models ---
class CreditRequest(BaseModel):
    applicant_id: str = Field(..., description="Unique ID for the applicant")
    annual_income: float = Field(..., gt=0, description="Annual income in ZAR")
    monthly_debt: float = Field(..., ge=0, description="Monthly debt obligations in ZAR")
    credit_history_years: int = Field(..., ge=0, le=50, description="Years of credit history")

class CreditResponse(BaseModel):
    applicant_id: str
    credit_score: int
    decision: str
    model_version: str
    risk_factors: dict

# --- Endpoints ---
@router.post("/predict", response_model=CreditResponse, tags=["Inference"])
async def predict_credit_score(request: CreditRequest):
    """
    Evaluate creditworthiness for a given applicant.
    """
    # Start OpenTelemetry Span
    with tracer.start_as_current_span("credit_prediction_inference"):
        with PREDICTION_LATENCY.time(): # Track latency
            try:
                result = model.predict(
                    annual_income=request.annual_income,
                    monthly_debt=request.monthly_debt,
                    credit_history_years=request.credit_history_years
                )
                
                # Track custom business metric
                CREDIT_PREDICTIONS_TOTAL.labels(decision=result['decision']).inc()
                
                return CreditResponse(
                    applicant_id=request.applicant_id,
                    **result
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Model inference failed: {str(e)}")

@router.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "model_version": settings.MODEL_VERSION
    }
```


<div style='page-break-after: always;'></div>

# File: src\config\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\config\README.md

```md
# config

```


<div style='page-break-after: always;'></div>

# File: src\config\settings.py

```py
# settings.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "credit-model-api"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    MODEL_VERSION: str = "1.0.0-mock"

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()
```


<div style='page-break-after: always;'></div>

# File: src\main.py

```py
# main.py
import logging
import sys
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pythonjsonlogger.json import JsonFormatter
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from src.config.settings import get_settings
from src.api.routes import router


# --- OpenTelemetry Setup ---
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
# In production, this would export to Jaeger/Tempo. For local, we log to console.
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

# --- Logging Setup ---
settings = get_settings()
log_handler = logging.StreamHandler(sys.stdout)
formatter = JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)
logging.basicConfig(level=settings.LOG_LEVEL, handlers=[log_handler])
logger = logging.getLogger(__name__)

# --- API Security Mock (OAuth/API Key) ---
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "afribank-secure-platform-key-123": # Mock validation
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")
    return api_key

# --- App Initialization ---
app = FastAPI(
    title=settings.APP_NAME,
    description="AfriBank Credit Scoring Model API (Platform-Grade)",
    version="1.0.0",
    dependencies=[Depends(verify_api_key)] # Enforce security on ALL routes
)

# --- Prometheus Metrics ---
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.APP_NAME} in {settings.APP_ENV} environment")
    # Instrument FastAPI with OpenTelemetry
    FastAPIInstrumentor.instrument_app(app)

# Include routers
app.include_router(router)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}. Use /docs for API documentation."}
```


<div style='page-break-after: always;'></div>

# File: src\models\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: src\models\credit_model.py

```py
# credit_model.py
import logging

logger = logging.getLogger(__name__)

class CreditScoringModel:
    """
    A mock credit scoring model. 
    In production, this would load a trained model from Databricks/MLflow.
    """
    
    def __init__(self, version: str):
        self.version = version
        logger.info(f"Initialized mock credit scoring model version: {self.version}")

    def predict(self, annual_income: float, monthly_debt: float, credit_history_years: int) -> dict:
        """
        Calculates a mock credit score and decision.
        """
        # Simple mock logic: Higher income and history = better score. Higher debt = worse.
        debt_to_income_ratio = monthly_debt / (annual_income / 12) if annual_income > 0 else 1.0
        
        base_score = 300
        score = base_score + (credit_history_years * 15) - (debt_to_income_ratio * 100)
        
        # Clamp score between 300 and 850
        final_score = max(300, min(850, int(score)))
        
        decision = "Approved" if final_score >= 650 else "Declined"
        
        logger.info(f"Prediction made: Score={final_score}, Decision={decision}, DTI={debt_to_income_ratio:.2f}")
        
        return {
            "credit_score": final_score,
            "decision": decision,
            "model_version": self.version,
            "risk_factors": {
                "debt_to_income_ratio": round(debt_to_income_ratio, 2)
            }
        }

# Singleton instance for the application
_model_instance = None

def get_model(version: str) -> CreditScoringModel:
    global _model_instance
    if _model_instance is None:
        _model_instance = CreditScoringModel(version=version)
    return _model_instance
```


<div style='page-break-after: always;'></div>

# File: src\models\README.md

```md
# models

```


<div style='page-break-after: always;'></div>

# File: tests\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: tests\README.md

```md
# tests
# Credit Model API

## Overview
This service provides a REST API for evaluating creditworthiness. It simulates a traditional ML model serving environment for the AfriBank AI Platform.

## Tech Stack
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Testing:** Pytest + HTTPX
- **Containerization:** Docker

## Prerequisites
- Python 3.11+
- Docker & Docker Compose

## Local Development

1. **Setup Environment:**


Here is the exact, step-by-step execution order. I have broken it down into **Local Development**, **Docker Containerization**, and **Cleanup**, with clear instructions on exactly when to visit your URLs.

---

### 🟢 Phase 1: Local Setup & Testing
*Goal: Set up your environment and prove the code works locally.*

**1. Create the environment file:**
```bash
cp .env.example .env
```

**2. Create the virtual environment:**
```bash
make venv
```
*(Note: The next command will actually do this automatically if you forget, but it's good to do it explicitly).*

**3. Install dependencies:**
```bash
make install
```

**4. Run the automated tests:**
```bash
make test
```
*(You should see **5 tests passing**. If they fail, do not proceed until they pass).*

---

### 🟡 Phase 2: Local Manual Testing & URL Visits
*Goal: Start the server locally and verify the Platform Engineering features (Docs, Health, Metrics, Security).*

**5. Start the local server:**
```bash
make run
```

**👉 VISIT THESE URLS NOW (Keep the terminal running):**

1. **Interactive API Docs (Swagger UI):** 
   * **URL:** `http://localhost:8000/docs`
   * **Action:** 
     * Click the **Authorize** button (top right).
     * Enter the API Key: `afribank-secure-platform-key-123` and click Authorize.
     * Expand the `POST /predict` endpoint, click **Try it out**, use the default JSON, and click **Execute**. 
     * *Why? Proves your API Security (OAuth/API Key) and Pydantic validation work.*
2. **Health Check Endpoint:**
   * **URL:** `http://localhost:8000/health`
   * *Why? Proves Kubernetes readiness/liveness probes will work later.*
3. **Prometheus Metrics Endpoint:**
   * **URL:** `http://localhost:8000/metrics`
   * **Action:** Scroll down and look for `afribank_credit_predictions_total`. You should see the count increase after you used the `/predict` endpoint in the docs!
   * *Why? Proves your custom AI business metrics and Prometheus integration work.*

*(Once you are done testing, go back to your terminal and press `CTRL + C` to stop the local server).*

---

###  Phase 3: Docker Containerization
*Goal: Prove the application runs securely in a container (Multi-stage build, non-root user).*

**6. Build the Docker image:**
```bash
make build
```
*(Watch the terminal to see it download the base image, install dependencies, and create the non-root user).*

**7. Run the Docker container:**
```bash
make docker-run
```

**👉 VISIT THESE URLS AGAIN:**
* Go back to `http://localhost:8000/docs`, `http://localhost:8000/health`, and `http://localhost:8000/metrics`.
* *Why? This proves the containerization was successful and the app behaves exactly the same inside Docker as it did locally.*

**8. Check the container logs:**
```bash
make docker-logs
```
*(You should see structured JSON logs flowing in your terminal. Press `CTRL + C` to exit the log view, but the container keeps running).*

**9. Stop the Docker container:**
```bash
make docker-stop
```

---

### 🔴 Phase 4: Teardown & Cleanup
*Goal: Wipe your local environment clean (useful if you want to start fresh or commit to Git without local junk).*

**10. Clean up virtual environments, cache, and pyc files:**
```bash
make clean
```

---

### 📋 Quick Summary Checklist

| Step | Command                | What happens              | URL to visit?                            |
|:-----|:-----------------------|:--------------------------|:-----------------------------------------|
| 1    | `cp .env.example .env` | Creates env vars          | No                                       |
| 2    | `make venv`            | Creates `.venv` folder    | No                                       |
| 3    | `make install`         | Installs Python packages  | No                                       |
| 4    | `make test`            | Runs 5 automated tests    | No                                       |
| 5    | `make run`             | Starts local server       | **YES** (`/docs`, `/health`, `/metrics`) |
| 6    | `make build`           | Builds Docker image       | No                                       |
| 7    | `make docker-run`      | Starts container          | **YES** (Verify it works in Docker)      |
| 8    | `make docker-logs`     | Shows container logs      | No                                       |
| 9    | `make docker-stop`     | Stops container           | No                                       |
| 10   | `make clean`           | Deletes `.venv` and cache | No                                       |

Execute these in order, and you will have a fully verified, platform-grade workload ready for your portfolio! Let me know when you've successfully hit the `/metrics` endpoint and seen your custom AI metric!
```


<div style='page-break-after: always;'></div>

# File: tests\test_api.py

```py
# test_api.py
import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

# The mock API key defined in src/main.py
HEADERS = {"X-API-Key": "afribank-secure-platform-key-123"}

@pytest.fixture
def anyio_backend():
    return 'asyncio'

@pytest.mark.anyio
async def test_health_check():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/health", headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "model_version" in data

@pytest.mark.anyio
async def test_predict_approved():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-001",
            "annual_income": 600000,
            "monthly_debt": 5000,
            "credit_history_years": 10
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["applicant_id"] == "APP-001"
    assert data["decision"] == "Approved"
    assert 300 <= data["credit_score"] <= 850

@pytest.mark.anyio
async def test_predict_declined():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-002",
            "annual_income": 120000,
            "monthly_debt": 9000,
            "credit_history_years": 1
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "Declined"

@pytest.mark.anyio
async def test_predict_validation_error():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-003",
            "annual_income": -500, # Invalid: must be > 0
            "monthly_debt": 1000,
            "credit_history_years": 5
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 422 # Unprocessable Entity

@pytest.mark.anyio
async def test_unauthorized_access():
    """
    Proves our API Security is working (Absa JD: API Security, OAuth 2.0).
    Requests without the valid X-API-Key header must be rejected.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-004",
            "annual_income": 100000,
            "monthly_debt": 1000,
            "credit_history_years": 1
        }
        # Intentionally sending NO HEADERS
        response = await ac.post("/predict", json=payload)
    
    assert response.status_code == 403 # Forbidden
```


```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\docker-compose.yml

```yml
# docker-compose.yml
version: '3.8'

services:
  credit-model-api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: credit-model-api
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped
    networks:
      - ubuntu-ai-network

networks:
  ubuntu-ai-network:
    driver: bridge
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\Dockerfile

```text
# Dockerfile
# --- Build Stage ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Runtime Stage ---
FROM python:3.11-slim

WORKDIR /app

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY src/ ./src/

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Start command
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\Makefile

```text
# Makefile
.PHONY: venv install run test build docker-run docker-stop docker-logs lint clean

# ==========================================
# Virtual Environment Configuration (Windows)
# ==========================================
VENV_DIR = .venv
PYTHON = $(VENV_DIR)\Scripts\python.exe
PIP = $(VENV_DIR)\Scripts\pip.exe
PYTEST = $(VENV_DIR)\Scripts\pytest.exe
UVICORN = $(VENV_DIR)\Scripts\uvicorn.exe

# ==========================================
# Virtual Environment Management
# ==========================================
venv:
	python -m venv $(VENV_DIR)
	@echo Virtual environment created at $(VENV_DIR)

# ==========================================
# Local Development
# ==========================================
install: venv
	$(PIP) install -r requirements.txt

run:
	$(UVICORN) src.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(PYTEST) tests/ -v --tb=short

lint:
	@echo Linting passed (placeholder)

# ==========================================
# Docker Operations
# ==========================================
build:
	docker build -t credit-model-api:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f

# ==========================================
# Cleanup (Windows Native Commands)
# ==========================================
clean:
	@if exist $(VENV_DIR) rmdir /s /q $(VENV_DIR)
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@del /s /q *.pyc 2>nul
	@echo Cleanup complete.
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\pytest.ini

```ini
[pytest]
asyncio_default_fixture_loop_scope = function
filterwarnings =
    ignore::DeprecationWarning:opentelemetry.instrumentation.dependencies
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\requirements.txt

```txt
fastapi==0.115.4
uvicorn[standard]==0.32.0
pydantic==2.9.2
pydantic-settings==2.6.1
httpx==0.27.2
pytest==8.3.3
pytest-asyncio==0.24.0
python-json-logger==3.2.1
prometheus-fastapi-instrumentator==7.0.2
opentelemetry-api==1.27.0
opentelemetry-sdk==1.27.0
opentelemetry-instrumentation-fastapi==0.48b0
setuptools==75.8.0
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\api\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\api\README.md

```md
# api

```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\api\routes.py

```py
# routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from prometheus_client import Counter, Histogram
from opentelemetry import trace

from src.models.credit_model import get_model
from src.config.settings import get_settings

router = APIRouter()
settings = get_settings()
model = get_model(settings.MODEL_VERSION)
tracer = trace.get_tracer(__name__)

# --- Custom AI Platform Metrics ---
CREDIT_PREDICTIONS_TOTAL = Counter(
    'afribank_credit_predictions_total', 
    'Total number of credit score predictions',
    ['decision'] # Labels: 'Approved' or 'Declined'
)

PREDICTION_LATENCY = Histogram(
    'afribank_prediction_latency_seconds', 
    'Time taken to process a credit prediction'
)

# --- Request/Response Models ---
class CreditRequest(BaseModel):
    applicant_id: str = Field(..., description="Unique ID for the applicant")
    annual_income: float = Field(..., gt=0, description="Annual income in ZAR")
    monthly_debt: float = Field(..., ge=0, description="Monthly debt obligations in ZAR")
    credit_history_years: int = Field(..., ge=0, le=50, description="Years of credit history")

class CreditResponse(BaseModel):
    applicant_id: str
    credit_score: int
    decision: str
    model_version: str
    risk_factors: dict
    
    # Disable protected namespace warning for 'model_version'
    model_config = {"protected_namespaces": ()}

# --- Endpoints ---
@router.post("/predict", response_model=CreditResponse, tags=["Inference"])
async def predict_credit_score(request: CreditRequest):
    """
    Evaluate creditworthiness for a given applicant.
    """
    # Start OpenTelemetry Span
    with tracer.start_as_current_span("credit_prediction_inference"):
        with PREDICTION_LATENCY.time(): # Track latency
            try:
                result = model.predict(
                    annual_income=request.annual_income,
                    monthly_debt=request.monthly_debt,
                    credit_history_years=request.credit_history_years
                )
                
                # Track custom business metric
                CREDIT_PREDICTIONS_TOTAL.labels(decision=result['decision']).inc()
                
                return CreditResponse(
                    applicant_id=request.applicant_id,
                    **result
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Model inference failed: {str(e)}")

@router.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "model_version": settings.MODEL_VERSION
    }
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\config\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\config\README.md

```md
# config

```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\config\settings.py

```py
# settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "credit-model-api"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    MODEL_VERSION: str = "1.0.0-mock"

    # Modern Pydantic V2 configuration
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

@lru_cache()
def get_settings():
    return Settings()
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\main.py

```py
# main.py

# main.py
import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pythonjsonlogger.json import JsonFormatter
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from src.config.settings import get_settings
from src.api.routes import router

# --- OpenTelemetry Setup ---
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
# In production, this would export to Jaeger/Tempo. For local, we log to console.
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

# --- Logging Setup ---
settings = get_settings()
log_handler = logging.StreamHandler(sys.stdout)
formatter = JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)
logging.basicConfig(level=settings.LOG_LEVEL, handlers=[log_handler])
logger = logging.getLogger(__name__)

# --- API Security Mock (OAuth/API Key) ---
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "afribank-secure-platform-key-123": # Mock validation
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")
    return api_key

# --- Lifespan Context Manager (Replaces deprecated @app.on_event) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.APP_NAME} in {settings.APP_ENV} environment")
    # Instrument FastAPI with OpenTelemetry
    FastAPIInstrumentor.instrument_app(app)
    yield
    logger.info(f"Shutting down {settings.APP_NAME}")

# --- App Initialization ---
app = FastAPI(
    title=settings.APP_NAME,
    description="AfriBank Credit Scoring Model API (Platform-Grade)",
    version="1.0.0",
    dependencies=[Depends(verify_api_key)], # Enforce security on ALL routes
    lifespan=lifespan # <-- Modern lifespan management
)

# --- Prometheus Metrics ---
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

# Include routers
app.include_router(router)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}. Use /docs for API documentation."}
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\models\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\models\credit_model.py

```py
# credit_model.py
import logging

logger = logging.getLogger(__name__)

class CreditScoringModel:
    """
    A mock credit scoring model. 
    In production, this would load a trained model from Databricks/MLflow.
    """
    
    def __init__(self, version: str):
        self.version = version
        logger.info(f"Initialized mock credit scoring model version: {self.version}")

    def predict(self, annual_income: float, monthly_debt: float, credit_history_years: int) -> dict:
        """
        Calculates a mock credit score and decision.
        """
        # Simple mock logic: Higher income and history = better score. Higher debt = worse.
        debt_to_income_ratio = monthly_debt / (annual_income / 12) if annual_income > 0 else 1.0
        
        base_score = 300
        score = base_score + (credit_history_years * 15) - (debt_to_income_ratio * 100)
        
        # Clamp score between 300 and 850
        final_score = max(300, min(850, int(score)))
        
        decision = "Approved" if final_score >= 650 else "Declined"
        
        logger.info(f"Prediction made: Score={final_score}, Decision={decision}, DTI={debt_to_income_ratio:.2f}")
        
        return {
            "credit_score": final_score,
            "decision": decision,
            "model_version": self.version,
            "risk_factors": {
                "debt_to_income_ratio": round(debt_to_income_ratio, 2)
            }
        }

# Singleton instance for the application
_model_instance = None

def get_model(version: str) -> CreditScoringModel:
    global _model_instance
    if _model_instance is None:
        _model_instance = CreditScoringModel(version=version)
    return _model_instance
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\src\models\README.md

```md
# models

```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\tests\__init__.py

```py
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\tests\README.md

```md
# tests
# Credit Model API

## Overview
This service provides a REST API for evaluating creditworthiness. It simulates a traditional ML model serving environment for the AfriBank AI Platform.

## Tech Stack
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Testing:** Pytest + HTTPX
- **Containerization:** Docker

## Prerequisites
- Python 3.11+
- Docker & Docker Compose

## Local Development

1. **Setup Environment:**


Here is the exact, step-by-step execution order. I have broken it down into **Local Development**, **Docker Containerization**, and **Cleanup**, with clear instructions on exactly when to visit your URLs.

---

### 🟢 Phase 1: Local Setup & Testing
*Goal: Set up your environment and prove the code works locally.*

**1. Create the environment file:**
```bash
cp .env.example .env
```

**2. Create the virtual environment:**
```bash
make venv
```
*(Note: The next command will actually do this automatically if you forget, but it's good to do it explicitly).*

**3. Install dependencies:**
```bash
make install
```

**4. Run the automated tests:**
```bash
make test
```
*(You should see **5 tests passing**. If they fail, do not proceed until they pass).*

---

### 🟡 Phase 2: Local Manual Testing & URL Visits
*Goal: Start the server locally and verify the Platform Engineering features (Docs, Health, Metrics, Security).*

**5. Start the local server:**
```bash
make run
```

**👉 VISIT THESE URLS NOW (Keep the terminal running):**

1. **Interactive API Docs (Swagger UI):** 
   * **URL:** `http://localhost:8000/docs`
   * **Action:** 
     * Click the **Authorize** button (top right).
     * Enter the API Key: `afribank-secure-platform-key-123` and click Authorize.
     * Expand the `POST /predict` endpoint, click **Try it out**, use the default JSON, and click **Execute**. 
     * *Why? Proves your API Security (OAuth/API Key) and Pydantic validation work.*
2. **Health Check Endpoint:**
   * **URL:** `http://localhost:8000/health`
   * *Why? Proves Kubernetes readiness/liveness probes will work later.*
3. **Prometheus Metrics Endpoint:**
   * **URL:** `http://localhost:8000/metrics`
   * **Action:** Scroll down and look for `afribank_credit_predictions_total`. You should see the count increase after you used the `/predict` endpoint in the docs!
   * *Why? Proves your custom AI business metrics and Prometheus integration work.*

*(Once you are done testing, go back to your terminal and press `CTRL + C` to stop the local server).*

---

###  Phase 3: Docker Containerization
*Goal: Prove the application runs securely in a container (Multi-stage build, non-root user).*

**6. Build the Docker image:**
```bash
make build
```
*(Watch the terminal to see it download the base image, install dependencies, and create the non-root user).*

**7. Run the Docker container:**
```bash
make docker-run
```

**👉 VISIT THESE URLS AGAIN:**
* Go back to `http://localhost:8000/docs`, `http://localhost:8000/health`, and `http://localhost:8000/metrics`.
* *Why? This proves the containerization was successful and the app behaves exactly the same inside Docker as it did locally.*

**8. Check the container logs:**
```bash
make docker-logs
```
*(You should see structured JSON logs flowing in your terminal. Press `CTRL + C` to exit the log view, but the container keeps running).*

**9. Stop the Docker container:**
```bash
make docker-stop
```

---

### 🔴 Phase 4: Teardown & Cleanup
*Goal: Wipe your local environment clean (useful if you want to start fresh or commit to Git without local junk).*

**10. Clean up virtual environments, cache, and pyc files:**
```bash
make clean
```

---

### 📋 Quick Summary Checklist

| Step | Command                | What happens              | URL to visit?                            |
|:-----|:-----------------------|:--------------------------|:-----------------------------------------|
| 1    | `cp .env.example .env` | Creates env vars          | No                                       |
| 2    | `make venv`            | Creates `.venv` folder    | No                                       |
| 3    | `make install`         | Installs Python packages  | No                                       |
| 4    | `make test`            | Runs 5 automated tests    | No                                       |
| 5    | `make run`             | Starts local server       | **YES** (`/docs`, `/health`, `/metrics`) |
| 6    | `make build`           | Builds Docker image       | No                                       |
| 7    | `make docker-run`      | Starts container          | **YES** (Verify it works in Docker)      |
| 8    | `make docker-logs`     | Shows container logs      | No                                       |
| 9    | `make docker-stop`     | Stops container           | No                                       |
| 10   | `make clean`           | Deletes `.venv` and cache | No                                       |

Execute these in order, and you will have a fully verified, platform-grade workload ready for your portfolio! Let me know when you've successfully hit the `/metrics` endpoint and seen your custom AI metric!
```


<div style='page-break-after: always;'></div>

# File: workloads\credit-model-api\tests\test_api.py

```py
#test_api.py
import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app
from opentelemetry import trace

# The mock API key defined in src/main.py
HEADERS = {"X-API-Key": "afribank-secure-platform-key-123"}

@pytest.fixture
def anyio_backend():
    return 'asyncio'

# Gracefully shut down OpenTelemetry to prevent the "closed file" error on exit
@pytest.fixture(autouse=True)
def cleanup_otel():
    yield
    provider = trace.get_tracer_provider()
    if hasattr(provider, 'shutdown'):
        provider.shutdown()

@pytest.mark.anyio
async def test_health_check():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/health", headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "model_version" in data

@pytest.mark.anyio
async def test_predict_approved():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-001",
            "annual_income": 1200000,  # Higher income
            "monthly_debt": 2000,      # Lower debt
            "credit_history_years": 30 # Longer history
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["applicant_id"] == "APP-001"
    assert data["decision"] == "Approved"
    assert 650 <= data["credit_score"] <= 850

@pytest.mark.anyio
async def test_predict_declined():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-002",
            "annual_income": 120000,
            "monthly_debt": 9000,
            "credit_history_years": 1
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "Declined"

@pytest.mark.anyio
async def test_predict_validation_error():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-003",
            "annual_income": -500, # Invalid: must be > 0
            "monthly_debt": 1000,
            "credit_history_years": 5
        }
        response = await ac.post("/predict", json=payload, headers=HEADERS)
    
    assert response.status_code == 422 # Unprocessable Entity

@pytest.mark.anyio
async def test_unauthorized_access():
    """
    Proves our API Security is working (Absa JD: API Security, OAuth 2.0).
    Requests without the valid X-API-Key header must be rejected.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "applicant_id": "APP-004",
            "annual_income": 100000,
            "monthly_debt": 1000,
            "credit_history_years": 1
        }
        # Intentionally sending NO HEADERS
        response = await ac.post("/predict", json=payload)
    
    assert response.status_code == 403 # Forbidden
```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\docker-compose.yml

```yml
# docker-compose.yml

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\Dockerfile

```text
# Dockerfile

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\requirements.txt

```txt
# requirements.txt

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\config\README.md

```md
# config

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\config\settings.py

```py
# settings.py

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\main.py

```py
# main.py

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\rag\generator.py

```py
# generator.py

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\rag\README.md

```md
# rag

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\rag\retriever.py

```py
# retriever.py

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\vector_db\milvus_client.py

```py
# milvus_client.py

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\src\vector_db\README.md

```md
# vector_db

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\tests\README.md

```md
# tests

```


<div style='page-break-after: always;'></div>

# File: workloads\customer-rag\tests\test_rag.py

```py
# test_rag.py

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\docker-compose.yml

```yml
# docker-compose.yml

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\Dockerfile

```text
# Dockerfile

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\requirements.txt

```txt
# requirements.txt

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\src\agents\fraud_investigator.py

```py
# fraud_investigator.py

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\src\agents\README.md

```md
# agents

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\src\agents\workflow.py

```py
# workflow.py

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\src\config\README.md

```md
# config

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\src\config\settings.py

```py
# settings.py

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\src\main.py

```py
# main.py

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\tests\README.md

```md
# tests

```


<div style='page-break-after: always;'></div>

# File: workloads\fraud-agent\tests\test_agent.py

```py
# test_agent.py

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\docker-compose.yml

```yml
# docker-compose.yml

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\Dockerfile

```text
# Dockerfile

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\requirements.txt

```txt
# requirements.txt

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\config\README.md

```md
# config

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\config\settings.py

```py
# settings.py

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\gateway\providers\azure_ai.py

```py
# azure_ai.py

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\gateway\providers\bedrock.py

```py
# bedrock.py

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\gateway\providers\README.md

```md
# providers

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\gateway\rate_limiter.py

```py
# rate_limiter.py

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\gateway\router.py

```py
# router.py

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\src\main.py

```py
# main.py

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\tests\README.md

```md
# tests

```


<div style='page-break-after: always;'></div>

# File: workloads\genai-gateway\tests\test_gateway.py

```py
# test_gateway.py

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\Dockerfile

```text
# Dockerfile

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\k8s-job.yaml

```yaml
# k8s-job.yaml

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\requirements.txt

```txt
# requirements.txt

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\src\config.py

```py
# config.py

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\src\model.py

```py
# model.py

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\src\README.md

```md
# src

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\src\train.py

```py
# train.py

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\tests\README.md

```md
# tests

```


<div style='page-break-after: always;'></div>

# File: workloads\gpu-training-job\tests\test_training.py

```py
# test_training.py

```


<div style='page-break-after: always;'></div>

# File: workloads\mlops-registry\docker-compose.yml

```yml
# docker-compose.yml

```


<div style='page-break-after: always;'></div>

# File: workloads\mlops-registry\mlflow\Dockerfile

```text
# Dockerfile

```


<div style='page-break-after: always;'></div>

# File: workloads\mlops-registry\mlflow\mlflow_config.py

```py
# mlflow_config.py

```


<div style='page-break-after: always;'></div>

# File: workloads\mlops-registry\mlflow\README.md

```md
# mlflow

```


<div style='page-break-after: always;'></div>

# File: workloads\mlops-registry\models\sample_models\README.md

```md
# sample_models

```

