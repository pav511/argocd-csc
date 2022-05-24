# love

Parent application to bootstrap LOVE deployment

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| apps | list | `["love-commander","love-manager","love-nginx","love-producer"]` | The list of applications for the LOVE service |
| env | string | `nil` | The environment (location) to set for the configuration. This picks the Helm values file to use in the deployment. |
| spec.destination.server | string | `"https://kubernetes.default.svc"` | The URL for the Kubernetes server |
| spec.source.repoURL | string | `"https://github.com/lsst-ts/argocd-csc"` | The repository URL that contains the configuration |
| spec.source.targetRevision | string | `"HEAD"` | The target revision (repository branch) to use for the configuration |
