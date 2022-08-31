####################
Repository Structure
####################

Layout
======

The repository consists of the `apps <https://github.com/lsst-ts/argocd-csc/tree/main/apps>`_, `bin <https://github.com/lsst-ts/argocd-csc/tree/main/bin>`_, `charts <https://github.com/lsst-ts/argocd-csc/tree/main/charts>`_, `docs <https://github.com/lsst-ts/argocd-csc/tree/main/docs>`_ and `services <https://github.com/lsst-ts/argocd-csc/tree/main/services>`_ directories.
The ``apps`` directory contains the specifications of what is deployed to the `Kubernetes`_ system for each control system application.
Each application is contained within its own directory.
Some of the directories handle `Kubernetes`_  cluster setup that is leveraged by the deployed applications.
The ``services`` directory contains the application specifications for items assisting in the operations of observatory functions.
Within each application, there may be configuration that applies to all sites.
This is provided in the ``values.yaml`` file within each application directory.
The site specific configuration is controlled by ``values-<environment>.yaml`` files where ``environment`` is the given short-hand for a deployment target.
The ``charts`` directory contains Helm_ charts shared among applications.
The ``bin`` directory contains scripts useful for administering the configuration repository and the `Argo CD`_ deployment.

Charts
======

Each application is now its own self-contained Helm_ chart.
This means the ``Chart.yaml`` file contains no specified dependencies and the version reflects that of the contained Helm_ chart.
The ``templates`` directory contains all the Helm_ chart manifests and supporting files needed to deploy the given application.
The CSC applications use a common chart found in ``charts/csc`` and that directory is linked into the CSC application directory as ``templates``.
The collector applications, except ``love``, use a common chart found in the ``charts/csc_collector`` directory and that directory is linked into the collector application directory as ``templates``.
Due to the way the configuration works, all sites use the same internal charts and there currently is no way to adjust that behavior.

Chart Versioning
================

Now that all the applications use charts internal to the repository, the version specified in the application ``Chart.yaml`` file is now the chart version.
Any updates to the ``templates`` directory must result in the ``version`` attribute of the application ``Chart.yaml`` file being incremented.
If a shared chart is update, the ``version`` in all associated application ``Chart.yaml`` files must be updated.
The ``update_shared_chart_version.py`` script (see :ref:`Configuration-Helper-Scripts`) is provided to make this operation easier to handle.
We do not use the ``version`` attribute to track the application version since those are covered by the `ts_cycle_build <https://ts-cycle-build.lsst.io>`_ mechanism and can move independently of the `Argo CD`_ configuration.
