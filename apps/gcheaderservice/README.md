# gcheaderservice

A Helm chart for deploying the GCHeaderService CSC.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | This specifies the scheduling constraints of the pod |
| annotations | object | `{}` | This allows the specification of pod annotations |
| entrypoint | string | `nil` | This key allows specification of a script to override the entrypoint |
| env | object | `{}` | This section holds a set of key, value pairs for environmental variables (ENV_VAR: value) |
| envSecrets | list | `[]` | This section holds specifications for secret injection. If this section is used, each object listed must have the following attributes defined: _name_ (The label for the secret), _secretName_ (The name of the vault store reference. Uses the _namespace_ attribute to construct the full name), _secretKey_ (The key in the vault store containing the necessary secret) |
| image.nexus3 | string | `nil` | The tag name for the Nexus3 Docker repository secrets if private images need to be pulled |
| image.pullPolicy | string | `"IfNotPresent"` | The policy to apply when pulling an image for deployment |
| image.repository | string | `"lsstts/test"` | The Docker registry name of the container image to use for the CSC |
| image.tag | string | `"develop"` | The tag of the container image to use for the CSC |
| initContainer | object | `{}` | This section sets the optional use of an init container for multus networking. If this section is used, the following attributes must to be specified: _repository_ (The Docker registry name of the init container image), _tag_ (The tag of the init container image), _pullPolicy_ (The policy to apply when pulling an image for init container deployment) |
| namespace | string | `"csc"` | This is the namespace in which the CSC will be placed |
| nfsMountpoint | list | `[]` | This section holds the information necessary to create a NFS mount for the container. If this section is used, each object listed can have the following attributes defined: _name_ (A label identifier for the mountpoint), _path_ (The path inside the container to mount), _readOnly_ (This sets if the NFS mount is read only or read/write), _server_ (The hostname of the NFS server), _serverPath_ (The path exported by the NFS server) |
| nodeSelector | object | `{}` | This allows the specification of using specific nodes to run the pod |
| osplVersion | string | `"V6.9.0"` | This is the version of the OpenSplice library to run. It is used to set the location of the OSPL configuration file |
| pvcMountpoint | list | `[]` | This section holds the information necessary to create a volume mount for the container. If this section is used, each object listed can have the following attributes defined: _name_ (A label identifier for the mountpoint), _path_ (The path inside the container to mount), _accessMode_ (This sets the required access mode for the volume mount), _claimSize_ (The requested physical disk space size for the volume mount), _storageClass_ (The Kubernetes provided storage class), _ids.uid_ (OPTIONAL: An alternative UID for mounting), _ids.gid_ (OPTIONAL: An alternative GID for mounting) |
| resources | object | `{}` | This allows the specification of resources (CPU, memory) requires to run the container |
| service.port | int | `nil` | The port number to use for the Service. |
| service.type | string | `nil` | The Service type for the application. This is either ClusterIP (internal access) or LoadBalancer (external access) |
| service.use | bool | `false` | This sets the use of a Service API for the application |
| shmemDir | string | `nil` | This is the path to the Kubernetes local store where the shared memory database will be written |
| tolerations | list | `[]` | This specifies the tolerations of the pod for any system taints |
| useExternalConfig | bool | `true` | This sets whether to rely on the ConfigMap for OSPL configuration or the internal OSPL configuration |
| useHostIpc | bool | `nil` | This sets the use of the host inter-process communication system. Defaults to true if not specified |
| useHostPid | bool | `nil` | This sets the use of the host process ID system. Defaults to true if not specified |