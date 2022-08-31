###################
rubintv-broadcaster
###################

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/services/rubintv-broadcaster <https://github.com/lsst-ts/argocd-csc/tree/main/services/rubintv-broadcaster>`_
   * - Type
     - Helm_
   * - Namespace
     - ``rubintv-broadcaster``

.. rubric:: Overview

This application handles the RubinTV broadcaster services.
It runs the scripts specified in the `rubintv_production <https://github.com/lsst-sitcom/rubintv_production>`_ repository.
The application uses an internal Helm_ chart located in ``services/rubintv-broadcasters/templates``.
