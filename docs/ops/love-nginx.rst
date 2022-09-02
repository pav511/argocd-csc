##########
love-nginx
##########

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/love-nginx <https://github.com/lsst-ts/argocd-csc/tree/main/apps/love-nginx>`_
   * - Type
     - Helm_
   * - Namespace
     - ``love``

.. rubric:: Overview

This application handles the instantiation of the LSST Observers Visualization Environment (LOVE) NGINX server.
When starting the Kubernetes_ deployed control system, this application is started by the ``love`` collector application and that must be started after the ``ospl-daemon`` application and possibly the ``kafka-producers`` application but before any of the other control system components including those on bare metal.
The application is managed an internal Helm_ chart located in ``apps/love-nginx/templates``.
