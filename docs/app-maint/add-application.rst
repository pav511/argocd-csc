###############
Add Application
###############

Add a directory to ``/apps`` named for the application. Then add a ``Chart.yaml`` file and point the dependancy chart to the appropriate one for the new application.
Add ``values-<environment>.yaml`` files for each environment in which that application will be deployed.
If the application needs to be integrated with a collector application, add the application name to the list in the appropriate environment files in the collector.

The application needs to be created at the sites the environment files point too.
If the application is part of a collector application, then once the change with the application is committed and pushed to GitHub, syncing the collector application will create the application.
After the application is created, it can then be synced via methods described in the previous section.
An application that is not part of a collector application must be created manually.
The `Argo CD`_ command-line is the preferred mechanism for this.
The application can be created by the following logging into the appropriate environment `Argo CD`_ instance:

.. prompt:: bash

  argocd app create <app deploy name> --dest-namespace argocd --dest-server https://kubernetes.default.svc --repo https://github.com/lsst-ts/argocd-csc.git --revision HEAD --path apps/<app name> --values values-<environment>.yaml

The ``<app deploy name>`` and ``<app name>`` directory don't have to match but should be the same for most instances.
The main variation is CSCs that are run in simulation mode are identified with ``-sim`` at the end of the application deployment name, but the application directory is the name of the CSC.
