# Infrastructure

Infrastructure-as-code assets for the Azure deployment baseline belong here, including Terraform modules, Bicep definitions, and Kubernetes manifests when AKS is required.

## Azure baseline

Infrastructure definitions in this directory should preserve the preferred Azure footprint:

- Azure Front Door,
- Azure API Management,
- Azure App Service or AKS,
- Azure Database for PostgreSQL,
- Azure Cache for Redis,
- Azure Blob Storage,
- Azure Service Bus,
- Azure Key Vault,
- Azure Monitor,
- Microsoft Sentinel,
- Azure AI Search,
- Azure Machine Learning,
- GitHub Actions or Azure DevOps,
- Defender for Cloud.

## Layout rule

- `terraform/` should hold reusable Terraform modules and environment compositions.
- `bicep/` should hold Azure-native deployment definitions when Bicep is preferred.
- `kubernetes/` should hold AKS manifests or Helm-oriented deployment assets only when container orchestration is justified.

