#######
Secrets
#######

Vault
-----

The CSC deployment leverages the `Vault <https://www.hashicorp.com/products/vault>`_ system provided by SQuaRE for `Kubernetes secret management <https://phalanx.lsst.io/arch/secrets.html#vault>`_.
This deployment uses the ``ts/software`` extension to the nominal vault path for a given site.
Each secret is maintained by its own collection key and then sub-divisions for individual secrets.
The current keys and values will be enumerated here.
Only the nexus3-docker key is available at all sites.
The others depend on site capabilities needing those secrets.

nexus3-docker
  This is the image pull secret for all CSC and private containers.

  .dockerconfigjson
    The JSON encoded credentials responsible for pulling from the nexus repository.

love
  This contains the secrets needed for the LOVE system

  database-password
    The password for the Postgres database.

  manager-secret-key
    The internal key for the LOVE manager backend.

  manager-process-connection-password
    The frontend to manager connection credential.

  manager-admin-user-password
    Password for ``admin``.

  manager-user-user-password
    Password for ``user``.

  manager-cmd-user-password
    Password for ``cmd-user``.

  manager-authlist-user-password
    Password for the ``authlist-user``.

  redis-password
    The password for the redis system.

lfa
  This contains the credentials for writing objects to the S3 LFA.

  aws-access-key-id
    The access key ID (**AWS_ACCESS_KEY_ID**) for the S3 system.
  aws-secret-access-key
    The secret access key (**AWS_SECRET_ACCESS_KEY**) for the S3 system.

1Password
---------

CSC operations uses the LSST IT 1password system to store credentials used in the build, deployment and operations process.
There is not a way to extract secrets from this system and inject them into the Vault.
A potential upgrade for ease-of-use would be to construct a way to handle this process based on work SQuaRE has already done.
