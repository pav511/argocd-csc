#######
Secrets
#######

Vault
-----

The CSC deployment leverages the `Vault <https://www.hashicorp.com/products/vault>`_ system provided by SQuaRE for `Kubernetes secret management <https://phalanx.lsst.io/about/secrets.html#vault>`_.
This deployment uses the ``ts/software`` extension to the nominal vault path for a given site.
Each secret is maintained by its own collection key and then sub-divisions for individual secrets.
The source of truth for the secrets is handled by 1Password system.

.. note::

  The pull secret for the nexus repository is now managed by SQuaRE since they have images stored in that system. Any update to the login (username or password) for that system **MUST** be coordinated with the SQuaRE team.

.. warning::

  The information given below is kept here for historical purposes until the
  new secret management system is merged. Once it is, this information will
  be removed.

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

.. _1Password: https://1password.com/

CSC operations uses the `1Password`_ system to store credentials used in the build, deployment and operations process.

The ``Build and Deploy`` vault in the `LSST IT 1Password`_ system is where the source of truth is kept for all of the secrets stored in the `Vault`_ system.
Each secret is stored in either a Login or a Secure Note object.
Inside that object, there must be a key named ``generate_secrets_key`` whose value is two words separated by a space.
The first word is the secret key name and the second is the name of that secret among the secrets for that key.
There may also be one or more keys named ``environment``.
Its values are the domain names of the environments to which that specific secret applies.
If ``environment`` is missing, that 1Password object provides a default for the given ``generate_secrets_key`` key, which will be used if there is no other object with the same key and a matching environment.

These 1Password objects are used by the `generate_secrets.py script <https://github.com/lsst-ts/argocd-csc/blob/main/installer/generate_secrets.py>`__ as part of the installation process to retrieve the persistent secrets.
Ephemeral secrets that can be reset when the environment is reinstalled are generated during the installation process.
`update_secrets.sh <https://github.com/lsst-ts/argocd-csc/blob/main/installer/update_secrets.sh>`__ uses the ``onepassword_uuid`` setting in `/installer/site-config.yaml <https://github.com/lsst-ts/argocd-csc/blob/main/installer/site-config.yaml>`__ to locate the appropriate 1Password vault.
