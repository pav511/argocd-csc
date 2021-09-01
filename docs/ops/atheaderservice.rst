###############
atheaderservice
###############

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/atheaderservice <https://github.com/lsst-ts/argocd-csc/tree/master/apps/atheaderservice>`_
   * - Type
     - Helm_
   * - Namespace
     - ``auxtel``

.. rubric:: Overview

This application handles creating header files for LATISS (also known as ATCamera).
The application is managed by the `csc Helm chart <https://github.com/lsst-ts/charts/tree/master/charts/csc>`_.
It uses extra API specifications to handle the web service used to server the header files.
Those specifications are in ``apps/atheaderservice/templates``.
