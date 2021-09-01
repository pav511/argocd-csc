###########################
CSC Operations with Argo CD
###########################

`Argo CD`_ is the mechanism used to control the deployment configuration of some control system components to Kubernetes_.
The description of the control system architecture is given in `LSE-150 <https://ls.st/lse-150>`_.
The `SQuaRE RSP deployment introduction <https://phalanx.lsst.io/introduction.html>`_ has a good brief on the concepts of the deployment mechanism.
The deployment system uses Helm_ charts to control the delivered content to Kubernetes_.
More information on the charts used for control system deployment can be found in `TSTN-019 <https://tstn-019.lsst.io/>`_.
The `Argo CD`_ configuration and this documentation are stored in the `argocd-csc <https://github.com/lsst-ts/argocd-csc>`_ repository in GitHub_.

This deployment mechanism leverages many technologies provided by Data Management's `SQuaRE <https://github.com/lsst-sqre>`_ group.
This documentation bears heavy resemblance to theirs as many of the concepts and applications of methodologies are similar is not the same.

The following environments are managed by `Argo CD`_ using configuration in this repository.
The links are links to the `Argo CD`_ dashboards, which require authentication.
The names are the environment names used internally in this repository to name values files and for other purposes.

.. _CSC-Ops-with-ArgoCD-UI-URLs:

* `tucson-teststand <https://tucson-teststand.lsst.codes/argo-cd>`_
* `ncsa-teststand <https://lsst-argocd-nts-efd.ncsa.illinois.edu/argo-cd>`_
* `base-teststand <https://base-lsp.lsst.codes/argo-cd>`_
* `summit <https://summit-lsp.lsst.codes/argo-cd>`_

Overview
========

This section provides a description of the repository and ancillary systems used for control system application deployment.

.. toctree::
   :maxdepth: 2

   arch/repository
   arch/secrets

Application Maintenance
=======================

This section handles adding, upgrading and maintaining control system applications.
The actions described in this section require access to the `Argo CD`_ UIs or Kubernetes_ instances.
The UIs require credentials for access and those are stored in the Rubin Observatory IT's 1password system.
For the Kubernetes_ systems, the appropriate ``kubeconfig`` file can be obtained by the site specific Rancher instance.

.. toctree::
   :maxdepth: 2

   app-maint/upgrade-application
   app-maint/add-application
   app-maint/making-changes

Operations Guide
================

These sections describe some of the more important applications used in the deployment as well as how to bootstrap a new deployment.

Applications
------------

.. toctree::
   :maxdepth: 2

   ops/cluster-config
   ops/ospl-config
   ops/ospl-daemon
   ops/kafka-producers
   ops/hexapodsim
   ops/test-csc
   ops/atheaderservice
   ops/ccheaderservice

The rest of the CSC applications do not require any extra APIs.
All of those applications are managed by the `csc Helm chart <https://github.com/lsst-ts/charts/tree/master/charts/csc>`_.
The LOVE applications (``love-<component>``) are mostly handled by their own charts, but this system isn't yet deployed via `Argo CD`_ yet.
Once it is, the rest of the components will be documented.

.. _CSC-Ops-with-ArgoCD-Collector-Apps:

Collector Applications
----------------------

These applications are what `Argo CD`_ calls an app of apps.
They are collections of child applications (CSCs, components or both) that are grouped into a particular namespace.
All collector applications, except ``love``, support running simulators for a CSC.
The ``summit`` environment is expected to run in real mode, but can be made to use a simulator by specifying CSCs in the ``runAsSim`` key.
All other sites assume that the CSCs will run in simulation mode except those specified in the ``noSim`` key.

.. toctree::
   :maxdepth: 2

   ops/auxtel
   ops/eas
   ops/love
   ops/maintel
   ops/obssys

Bootstrapping
-------------

.. toctree::
   :maxdepth: 2

   ops/bootstrapping
