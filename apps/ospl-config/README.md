# ospl-config

Handle OSPL configuration.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| ddsi2TracingEnabled | bool | `false` | Enable/disable tracing for the ddsi2 service |
| ddsi2TracingLogfile | string | `"stdout"` | The location to write the ddsi2 service tracing |
| ddsi2TracingVerbosity | string | `"finer"` | The verbosity level for the ddsi2 service tracing |
| deliveryQueueMaxSamples | int | `10000` | The maximum delivery samples to queue |
| domainReportEnabled | bool | `false` | Enable/disable tracing for the domain service |
| dsGracePeriod | string | `"60s"` | The maximum grace period (seconds) for the discovery time |
| durabilityServiceAlignmentComboPeriodInitial | float | `2.5` | The alignment combination period (seconds) for the durability service |
| durabilityServiceAlignmentComboPeriodOperational | float | `0.1` | The alignment combination operational period (seconds) for the durability service |
| durabilityServiceInitialDiscoveryPeriod | string | `"10.0"` | The initial discovery period (seconds) for the durability service |
| durabilityServiceTracingEnabled | bool | `false` | Enable/disable tracing for the durability service |
| durabilityServiceTracingLogfile | string | `"stdout"` | The location to write the durability service tracing |
| durabilityServiceTracingVerbosity | string | `"FINER"` | The verbosity level for the durability service tracing |
| maxSamplesWarnAt | int | `50000` | The maximum number of samples that generate a system warning |
| monitorStackSize | int | `6000000` | The stack size for the monitoring system |
| namespacePolicyAlignee | string | `"Lazy"` | Set the namespace alignee policy |
| namespaces | list | `["auxtel","calsys","eas","love","maintel","obssys","kafka-producers","ospl-daemon","uws","dds-test"]` | List of namespaces where the OSPL configuration will be placed |
| networkInterface | string | `"net1"` | The network interface that DDS will bind too |
| schedulingClass | string | `"Default"` | The scheduling class for the system |
| schedulingPriority | int | `0` | The scheduling priority for the system |
| shmemSize | int | `504857600` | The size (bytes) of the shared memory allocation |
| squashParticipants | bool | `true` | Enable/disable the squashing of participants |
| waterMarksWhcAdaptive | bool | `true` | Enable/disable the adaptive high watermarks |
| waterMarksWhcHigh | string | `"8MB"` | Size of the final high watermarks |
| waterMarksWhcHighInit | string | `"8MB"` | Size of the initial high watermarks |
