################
ospl-main-daemon
################

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/ospl-main-daemon <https://github.com/lsst-ts/argocd-csc/tree/main/apps/ospl-main-daemon>`_
   * - Type
     - Helm_
   * - Namespace
     - ``ospl-daemon``

.. rubric:: Overview

This application handles instantiating the main (primary) OpenSplice daemon for shared memory mode across the entire control system.
When starting the Kubernetes_ deployed control system, it is vital that this application is started (synced) first, if it is present,  as it sets the communication pathway for all other components.
The application is managed by an internal Helm chart located in ``apps/ospl-main-daemon/templates``.
