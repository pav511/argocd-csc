####################
Repository Structure
####################

Layout
======

The repository consists of the `apps <https://github.com/lsst-ts/argocd-csc/tree/master/apps>`_ and `docs <https://github.com/lsst-ts/argocd-csc/tree/master/docs>`_ directories.
The ``apps`` directory contains the specifications of what is deployed to the `Kubernetes`_ system for each control system application.
Each application is contained within its own directory.
Some of the directores handle `Kubernetes`_  cluster setup that is leveraged by the deployed applications.
Within each application, there may be configuration that applies to all sites.
This is provided in the ``values.yaml`` file within each application directory.
The site specific configuration is controlled by ``values-<environment>.yaml`` files where ``environment`` is the given short-hand for a deployment target.

For many operations, the standalone `argocd-admin <https://github.com/lsst-ts/argocd-admin>`_ repository contains scripts that help with those operational interactions.
This repository will eventually be incorporated into this one at some point in the near future.

Charts
======

Each application its own `Helm`_ chart, but all charts at this level are given the same version number as specified in the ``Chart.yaml`` file.
This version number is never changed even when the dependency charts change versions.
Most applications use charts provided by third-party application charts or charts in the `Telescope and Site charts repository <https://github.com/lsst-ts/charts>`_.
For the latter, new chart versions are handled through interactions described in that repository's README.
In either case, the dependency versions are updated within the ``Chart.yaml`` for the given application that requires a new version.
Due to the way the configuration works, all sites use the same dependency versions and there currently is no way to adjust that behavior.
Some applications use extra deployment manifests beyond what is given in the associated dependency chart.
Those extra manifests are placed in the ``templates`` directory within the given application.
