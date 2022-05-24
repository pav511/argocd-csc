###############
kafka-producers
###############

.. list-table::
   :widths: 10,40

   * - Edit on GitHub
     - `/apps/kafka-producers <https://github.com/lsst-ts/argocd-csc/tree/main/apps/kafka-producers>`_
   * - Type
     - Helm_
   * - Namespace
     - ``kafka-producers``

.. rubric:: Overview

This application handles the instantiation of the Kafka_ producers responsible for converting DDS topics to Kafka_ messages.
When starting the Kubernetes_ deployed control system, this application must be started after the ``ospl-daemon`` application but before any of the other control system components including those on bare metal.
The application is managed by the `kafka-producers Helm chart <https://github.com/lsst-ts/charts/tree/main/charts/kafka-producers>`_.

.. _Kafka: https://kafka.apache.org/
