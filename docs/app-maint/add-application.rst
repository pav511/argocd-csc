###############
Add Application
###############

The following is the procedure to add a new application to the system.

#. Add a directory to ``/apps`` named for the application.
    a. For example, ``/apps/my_new_application`` for an application named ``my_new_application``.
#. Add a ``Chart.yaml`` file and point the dependency chart to the appropriate one for the new application.
#. Add ``values-<environment>.yaml`` files for each environment in which that application will be deployed.
    a. For example, add ``values-summit.yaml`` for the summit environment.
#. If the application needs to be integrated with a :ref:`collector application <CSC-Ops-with-ArgoCD-Collector-Apps>`, add the application name to the list in the appropriate environment file in the collector.

If the application is part of a :ref:`collector application <CSC-Ops-with-ArgoCD-Collector-Apps>`, then once the change with the application is committed and pushed to GitHub, syncing the collector application will create the application.
After the application is created, it can then be synced via methods described in :ref:`CSC-Ops-with-ArgoCD-Upgrade-Application`.

An application that is not part of a collector application must be created manually.
To create an application using the command-line, log into the appropriate `Argo CD`_ environment and run the following command:

.. prompt:: bash

  argocd app create <app deploy name> --dest-namespace argocd --dest-server https://kubernetes.default.svc --repo https://github.com/lsst-ts/argocd-csc.git --revision HEAD --path apps/<app name> --values values-<environment>.yaml

The ``<app deploy name>`` and ``<app name>`` directory don't have to match but should be the same for most instances.
The main variation is CSCs that are run in simulation mode are identified with ``-sim`` at the end of the application deployment name, but the application directory is the name of the CSC.
