########
test-csc
########

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/test-csc <https://github.com/lsst-ts/argocd-csc/tree/main/apps/test-csc>`_
   * - Type
     - Helm_
   * - Namespace
     - ``dds-test``

.. rubric:: Overview

This application allows you to stand up a Test CSC.
The default ``namespace`` for the Test CSC is ``dds-test``, but can be changed by adding that parameter to the appropriate values file.
The configuration also needs to be passed an index via the ``RUN_ARG`` environment variable.
There are a couple of index specific values files available in the application.
The ``values-test42.yaml`` is reserved for SQuaRE use.
The application is managed by an internal Helm_ chart located in ``charts/csc``.
