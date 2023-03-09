########################
CSC-Collector Helm Chart
########################

0.3.0
-----

  This version centralizes the ``values.yaml`` into the ``values/csc_collector`` directory and is linked into the collector applications.
  This means the ``namespace`` attribute must be added to the site specific values file.
  It also contains an improvement that removes the need to specify the ``indexed`` attribute any longer.

0.2.0
-----

  This is the canonical version of the chart.
  It contains the following functionality:

  * Specifying the CSCs that belong to a given collector app
  * Handling indexed components
  * Allow components to be specified as simulators
  * Allow name remapping of applications
