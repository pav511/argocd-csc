# ospl-main-daemon

A Helm chart for handling the OSPL main shared memory daemon

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | This specifies the scheduling constraints of the pod |
| annotations | object | `{"k8s.v1.cni.cncf.io/networks":"kube-system/macvlan-conf"}` | This allows the specification of pod annotations. |
| domainId | int | `0` | Specify the domainId for the daemon |
| env | object | `{}` | This section holds a set of key, value pairs for environmental variables |
| fullnameOverride | string | `""` | Specify the deployed application name specifically. Overrides all other names. |
| image | object | `{"pullPolicy":"IfNotPresent","repository":"ts-dockerhub.lsst.org/ospl-daemon","tag":"c0010"}` | This section holds the configuration of the container image |
| image.pullPolicy | string | `"IfNotPresent"` | The policy to apply when pulling an image for deployment |
| image.repository | string | `"ts-dockerhub.lsst.org/ospl-daemon"` | The Docker registry name of the container image |
| image.tag | string | `"c0010"` | The tag of the container image |
| imagePullSecrets | list | `[]` | The list of pull secrets needed for the images. If this section is used, each object listed can have the following attributes defined: _name_ (The label identifying the pull-secret to use) |
| initContainer | object | `{}` | This section sets the optional use of an init container for multus networking. If this section is used, the following attributes must to be specified: _repository_ (The Docker registry name of the init container image), _tag_ (The tag of the init container image), _pullPolicy_ (The policy to apply when pulling an image for init container deployment) |
| nameOverride | string | `""` | Adds an extra string to the release name. |
| namespace | string | `"ospl-daemon"` | This is the namespace in which the OSPL daemon will be placed |
| nodeSelector | object | `{}` | This allows the specification of using specific nodes to run the pod |
| resources | object | `{}` | This allows the specification of resources (CPU, memory) requires to run the container |
| tolerations | list | `[]` | This specifies the tolerations of the pod for any system taints |
