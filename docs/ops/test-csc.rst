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
     - ``any``

.. rubric:: Overview

This application allows you to stand up a Test CSC.
The configuration needs to implement the ``namespace`` key since the Test CSC does not have a logical home in the system provided namespaces.
The configuration also needs to be passed an index via the ``RUN_ARG`` environment variable.
There are a couple of index specific values files available in the application.
The ``values-test42.yaml`` is reserved for SQuaRE use.
The application is managed by the `csc Helm chart <https://github.com/lsst-ts/charts/tree/main/charts/csc>`_.
