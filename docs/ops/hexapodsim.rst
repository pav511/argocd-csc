##########
hexapodsim
##########

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/hexapodsim <https://github.com/lsst-ts/argocd-csc/tree/main/apps/hexapodsim>`_
   * - Type
     - Helm_
   * - Namespace
     - ``auxtel``

.. rubric:: Overview

This application is a special component that is required to run the ATHexapod in simulation mode and only used at the various test stands.
The summit environment does not require this application since the real hardware is present there.
Application creation is handled by the ``auxtel`` collector application.
Once the application is started, it is never shutdown even when there is a cycle upgrade.
This is due to the fact that the application is not a CSC and does not rely on DDS.
It uses an internal Helm_ chart that is kept in ``apps/hexapodsim/templates``.
