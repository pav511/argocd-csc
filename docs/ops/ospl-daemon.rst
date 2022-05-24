###########
ospl-daemon
###########

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/ospl-daemon <https://github.com/lsst-ts/argocd-csc/tree/main/apps/ospl-daemon>`_
   * - Type
     - Helm_
   * - Namespace
     - ``ospl-daemon``

.. rubric:: Overview

This application handles instantiating an OpenSplice daemon for shared memory mode on each node within the Kubernetes_ cluster.
When starting the Kubernetes_ deployed control system, it is vital that this application is started (synced) first as it sets the communication pathway for all other components.
The application is managed by an internal Helm chart located in ``apps/ospl-daemon/templates``.
