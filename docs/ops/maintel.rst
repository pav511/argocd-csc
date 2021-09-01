#######
maintel
#######

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/maintel <https://github.com/lsst-ts/argocd-csc/tree/master/apps/maintel>`_
   * - Type
     - Helm_
   * - Namespace
     - ``argocd``

.. rubric:: Overview

This collector application handles the CSCs associated with the Main Telescope.
The list of applications can vary by ``environment``.
This application uses an internal chart that lives in ``apps/maintel/templates`` and creates the `Argo CD`_ specifications for the child applications.
