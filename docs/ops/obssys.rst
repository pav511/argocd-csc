######
obssys
######

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/obssys <https://github.com/lsst-ts/argocd-csc/tree/master/apps/obssys>`_
   * - Type
     - Helm_
   * - Namespace
     - ``argocd``

.. rubric:: Overview

This collector application handles the CSCs associated with the Observatory Systems.
The list of applications can vary by ``environment``.
This application uses an internal chart that lives in ``apps/obssys/templates`` and creates the `Argo CD`_ specifications for the child applications.
