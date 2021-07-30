##############################
Bootstrapping a new deployment
##############################

Since creating new CSC deployments is an infrequent process, knowledge of that procedure might atrophy over time.
What is written here is how to bring up a new CSC deployment from scratch.
As mentioned before, the CSC deployment relies heavily on services provided by SQuaRE, so close coordination with them will be necessary.

#. Check with SQuaRE to see if a `vault <https://vault.lsst.codes>`_ is available.
    a. Once it is available, begin to populate it with the necessary secrets.
#. Once the Kubernetes_ system has been prepared by SQuaRE, get the following:
    a. The `Argo CD`_ login credentials.
    #. The `Kubernetes`_ config (``kubectl`` config) file for the cluster.
#. Ask IT for any special ingress routes for the system.
    a. Example: The HeaderService instances can run with a web service for header file serving, so they require an ingress, but were not designed to leverage the standard cluster ingress route.
    Therefore they were given a route that started with the lower-cased CSC name (``atheaderservice.<site>.lsst.org``) to differentiate the instances.
#. Choose an environment name for the new deployment
#. Ensure that all configuration has been committed to site specific ``values-<environment>.yaml`` files and available in the ``argocd-csc`` repository.
#. Log into the `Argo CD`_ instance from the command-line.
#. Run the ``create_apps.py`` script from the `argocd-admin <https://github.com/lsst-ts/argocd-admin>`_ repository.
