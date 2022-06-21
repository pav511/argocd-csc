# maintel

Parent application to bootstrap Main Telescope CSC deployment

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cscs | list | `[]` | The list of applications (CSCs) to deploy via the collector app |
| env | string | `nil` | The environment (location) to set for the configuration. This picks the Helm values file to use in the deployment. |
| indexed | object | `{"mtaircompressor":15}` | A dictionary of _name_: _length_ used for getting the correct indexed Helm values file |
| isSim | list | `[]` | The list of applications that are run as simulators |
| namespace | string | `"maintel"` | The namespace for the child applications |
| renameMap | object | `{}` | A dictionary of _app name_: _new name_ used to set the application name to _new name_ |
| spec.destination.server | string | `"https://kubernetes.default.svc"` | The URL for the Kubernetes server |
| spec.source.repoURL | string | `"https://github.com/lsst-ts/argocd-csc"` | The repository URL that contains the configuration |
| spec.source.targetRevision | string | `"HEAD"` | The target revision (repository branch) to use for the configuration |
