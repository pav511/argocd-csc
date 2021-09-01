########
test-csc
########

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/test-csc <https://github.com/lsst-ts/argocd-csc/tree/master/apps/test-csc>`_
   * - Type
     - Helm_
   * - Namespace
     - ``any``

.. rubric:: Overview

This application allows you to stand up a Test CSC.
It must be given a NFS mount that has a clone of the `ts_config_ocs <https://github.com/lsst-ts/ts_config_ocs>`_ repository.
The configuration needs to implement the ``namespace`` key since the Test CSC does not have a logical home in the system provided namespaces.
Since the application uses the deployment container, it must over-ride the entry point for the container by specifying the ``entrypoint`` key and passing these script contents:

.. code:: yaml

    entrypoint: |
      #!/usr/bin/bash

      source ${HOME}/.setup_sal_env.sh

      export TS_CONFIG_OCS_DIR=/opt/lsst/software/ts_config_ocs

      run_test_csc.py ${RUN_ARG} &

      pid="$!"

      wait ${pid}

The application is managed by the `csc Helm chart <https://github.com/lsst-ts/charts/tree/master/charts/csc>`_.
