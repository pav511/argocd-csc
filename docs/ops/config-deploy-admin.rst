###########################################
Configuration and Deployment Administration
###########################################

The ``bin`` directory contains scripts helpful to the administration of the configuration and deployment.
Some scripts require the ``pyyaml`` package which can be installed using the ``requirements.txt`` file in this directory.
The scripts will be discussed in two sections: those that relate to the administration of the configuration repository and those that relate to the administrations of the deployment.
The ``helpers.py`` file contains a number of constants and functions used by the scripts in this directory.

Configuration Helper Scripts
----------------------------

These scripts handle operations on the configuration repository.

update_parameter.py
  This script can update any parameter for a given environment file within the entire configuration repository.
  The parameters may be accessed by using dot notation: :guilabel:`key1.key2.param`.
  Mainly, this is used to update the cycle build tag for all of the deployed applications.
  This can be accomplished by running the following from the top-level repository directory:

  .. code-block:: bash

    python bin/update_parameter.py --env tucson-teststand image.tag c0025

update_shared_chart_version.py
  This script makes it easy to change the chart versions on all applications that have shared charts.
  The shared chart type and the version are passed as arguments.
  The list of shared chart types can be found by using the help flag on the script.
  Running from the top-level repository directory:

  .. code-block:: bash

    python bin/update_shared_chart_version.py csc 0.10.0

Deployment Helper Scripts
-------------------------

These scripts handle operations on the `Argo CD`_ deployment.

create_apps.py
  This script is used to create all of the deployment applications when a new cluster is stood up.

argocd_login.py
  This script sets up port forwarding authentication for interactions with the deployment.
  It requires a file with the username and password on separate lines for the site specific `Argo CD`_ login.

sync_apps.py
  This script is used to sync all applications when doing a cycle build deployment or restarting a system after maintenance.

change_target_revision.py
  This allows one to change the target revision (branch) for a given application or set of applications.
  This is useful to test changes to chart information or configurations before merging to ``main``.
  Collector applications will need to have the target revision also applied in the ``values-<environment>.yaml`` file to stop out-of-sync issues on the child apps.
  The target revision should always be reset to ``HEAD`` once testing is completed and updates merged to ``main``.
