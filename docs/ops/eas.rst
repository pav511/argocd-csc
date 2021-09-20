###
eas
###

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/eas <https://github.com/lsst-ts/argocd-csc/tree/master/apps/eas>`_
   * - Type
     - Helm_
   * - Namespace
     - ``argocd``

.. rubric:: Overview

This collector application handles the CSCs associated with the Environmental Awareness System.
The list of applications can vary by ``environment``.
This application uses an internal chart that lives in ``apps/eas/templates`` and creates the `Argo CD`_ specifications for the child applications.
This collector application deals with many indexed CSCs and those indicies are part of the child application deployment names (e.g. ``dimm1``).
The configuration needs to know how long the CSC name is to be able to fetch the index in order to match it to the appropriate ``values-<csc name><index>.yaml`` file.
This is necessary since there are currently no helper functions that provide string lengths.
Below is an example of how to specify the offset for a CSC.

.. code:: yaml

  indexed:
    dimm: 4
    weatherstation: 14
    dsm: 3

Rather than use release names built like ``<lowecase csc name><index>`` (e.g., ``dsm1``), one can provide a mapping to use different release names:

.. code:: yaml

  renameMap:
    ess1: comcam-ess01
    ess101: mtdome-ess01
