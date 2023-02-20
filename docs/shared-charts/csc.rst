##############
CSC Helm Chart
##############

0.11.0
------

  This version provides the ability to have a configuration file (YAML) for a CSC and provides the specification of a security context for the pods. Use this version if you need to add either of the following to the ``values.yaml``:

  .. code::

    # -- This key allows specification of a YAML configuration file
    # If this section is used, it must contain the following attributes defined:
    # _path_ (The container path for the configuration file),
    # _filename_ (The configuration file name),
    # _content_ (The YAML content for the configuration file)
    configfile: {}

    # -- This key allows for the specification of a pod security context for volumes.
    # If this section is used, it must contain the following attributes:
    # _user_ (The user id for the volumes)
    # _group_ (The group id for the volumes)
    # _fsGroup_ (OPTIONAL: A special supplemental group that applies to all containers in a pod)
    securityContext: {}

  To activate the configuration file feature, the site-specific values files need to have explicit information added.
  This a snippet of an example from the ``atoods`` ``values-tucson-teststand.yaml``:

  .. code::

      configfile:
        path: /etc
        filename: atoods.yaml
        content: |
          defaultInterval: &interval
              days: 0
              hours: 0
              minutes: 0
              seconds: 0

  To activate the security context, the site-specific values files need to have explicit information added.
  This is an example:

  .. code::

    securityContext:
      user: 1042
      group: 3323
      fsGroup: 3323


0.10.0
------

  This version provides for injecting Butler secrets into the application pod.
  In order to use this version, the following needs to be added to the application ``values.yaml``:

  .. code::

    # -- This key allows for specification of Butler secret information
    # If this section is used, it must contain the following attribute:
    # __containerPath__ (The directory location for the Butler secret)
    # __dbUser__ (The username for the Butler backend database)
    butlerSecret:

  To activate the feature, the site-specific values files need to have explicit information added.
  This is an example from the ``atqueue`` ``values-tucson-teststand.yaml``:

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
