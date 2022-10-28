##############
CSC Helm Chart
##############

0.10.0
------

  This version provides for injecting Butler secrets into the application pod.
  In order to use this version, the following needs to be added to the application `values.yaml`:

  .. code::

    # -- This key allows for specification of Butler secret information
    # If this section is used, it must contain the following attribute:
    # __containerPath__ (The directory location for the Butler secret)
    # __dbUser__ (The username for the Butler backend database)
    butlerSecret:

  To activate the feature, the site-specific values files need to have explicit information added.
  This is an example from the ``atqueue`` `values-tucson-teststand.yaml`:

  .. code::

    butlerSecret:
      containerPath: /home/saluser/.lsst
      dbUser: oods

0.9.2
-----

  This is the canonical version of the CSC Helm chart.
  It contains the following functionality:

  * Specify the container image for the application
  * Specify environmental variables for the application
  * Specify secret type environmental variables for the application
  * Provide the capability of overriding the container entrypoint
  * Specify Persistent Volume Claims for application ephemeral storage
  * Specify NFS mounts for application data sharing
  * Ability to use either external or internal OSPL configuration
  * Provide flexible location of the OSPL shmem directory
  * Provide annotation capability for the application pod
  * Provide mechanism for init containers for handling multus access
  * Allow application pods to use host PID and IPC spaces
  * Provide the capability for a Service attachment for the application
