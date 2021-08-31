####
love
####

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/love <https://github.com/lsst-ts/argocd-csc/tree/master/apps/love>`_
   * - Type
     - Helm_
   * - Namespace
     - ``argocd``

.. rubric:: Overview

This collector application handles the components associated with the LSST Observers Visualization Environment (LOVE).
The list of applications does not usually vary by ``environment``.
It is possible a new service is introduced at a test stand, but eventually that service will be placed at all sites.
This application uses an internal chart that lives in ``apps/love/templates`` and creates the `Argo CD`_ specifications for the child applications.
