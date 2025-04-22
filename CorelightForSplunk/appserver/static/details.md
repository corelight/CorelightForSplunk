# Corelight App For Splunk Documentation

The Corelight App for Splunk enables incident responders and threat hunters who use Splunk® and Splunk Enterprise Security to work faster and more effectively.

|                            |                                          |
|----------------------------|------------------------------------------|
| App Version                | 2.6.1                                    |
| App Build                  | 181                                      |
| Splunk Enterprise Versions | 10.X, 9.X                                |
| Platforms                  | Splunk Enterprise, Splunk Cloud          |
| Splunkbase Url             | <https://splunkbase.splunk.com/app/3884> |
| Author                     | Corelight, Inc.         |
| Creates an index           | False                                    |
| Implements summarization   | No                                       |
| Summary Indexing           | False                                    |
| Report Acceleration        | False                                    |
| Release Date               | 03/05/2025                               |

**IMPORTANT**

When upgrading from Corelight App For Splunk version 2.4.4 or earlier, remove the previous app before installing the latest Corelight App For Splunk app release. Additionally, check in the `local/data/ui/views` folder for conflicting dashboards.

**Corrupt CSV**

In versions of Corelight App For Splunk 2.5.3 and earlier, there is a semi-corrupt lookup. The lookup still works as intended, but will generate an increased volume in internal logging warnings. These additional logs do not increase license usage, as they are in the `_internal` index. The following search command can be executed within the Corelight App For Splunk to correct the CSV.

    | inputlookup corelight_base64conversion |outputlookup corelight_base64conversion

## Corelight App For Splunk - Dashboard Overview

The Corelight App For Splunk transforms complex network data into actionable security intelligence, enabling faster threat detection and incident response. By seamlessly integrating with Corelight Sensors and Zeek data, the app provides security teams with comprehensive visibility through specialized dashboards covering alert aggregation, protocol analysis, threat intelligence matching, and network behavior analytics. Built for security analysts, incident responders, and threat hunters, the app streamlines investigation workflows and enhances threat hunting capabilities with features like MITRE ATT&CK framework integration, automated alert correlation, and detailed traffic analysis.

### Security Workflows Dashboards

- **Alert Aggregations**: Consolidates and prioritizes security alerts with MITRE ATT&CK mapping for streamlined threat response

- **Intel**: Monitors IOC matches from external threat intelligence sources in network traffic

- **IP Interrogation**: Analyzes specific IP addresses for connection patterns, protocol usage, and network interactions

- **Log Hunting**: Enables detailed investigation of network events with customizable filters and search criteria

- **Notices**: Tracks system-generated security notices and intelligence alerts with severity classification

- **Security Posture**: Provides comprehensive overview of network security status including alerts, encryption, and DNS health

- **RDP Inferences**: Monitors Remote Desktop Protocol connections, authentication patterns, and security protocols

- **SSH Inferences**: Analyzes SSH connection patterns, authentication methods, and potential security issues

- **Suricata IDS Alert Overview**: Displays intrusion detection alerts with temporal patterns and severity levels

- **VPN Insights**: Tracks VPN usage patterns, connections, and user activity across the network

### Data Explorer Dashboards

- **Connections**: Visualizes top services, ports, dataflows, and network connection patterns

- **DNS**: Monitors DNS query patterns and potential exfiltration attempts through domain analysis

- **Files**: Identifies suspicious files, executables, and compressed file transfers

- **HTTP**: Analyzes HTTP transactions for suspicious patterns in headers, user agents, and requests

- **Software**: Tracks software versions and usage patterns across monitored network traffic

- **SSL and x509**: Monitors SSL/TLS certificates and validation status for encrypted traffic

### Data Insights Dashboards

- **Secure Channel Insights**: Analyzes encrypted and non-encrypted SSL, SSH, TLS, and x509 traffic

- **Name Resolution Insights**: Provides deep analysis of DNS traffic patterns and potential threats

- **Remote Activity Insights**: Monitors remote access patterns and authentication attempts

### Corelight Menu Dashboards

- **Configuration**: Manages app settings, indexes, and logging configuration

- **Lookup Generation**: Creates and manages lookup files for dashboard filtering

- **Sensor Overview**: Provides operational status of Corelight sensors

- **About**: Displays app version information and documentation

# User Guide

## Custom Search Commands

`cid` is a custom command provided to turn a tuple of `src_ip`, `src_port`, `dest_ip`, and `dest_port` into a community string.

## Lookups

Corelight App For Splunk contains several lookup files.

<div class="note">

It is a best practice and recommendation to **not** use the direct CSV name, as these will change between versions. Use the `transforms` name as listed in the table.

</div>

|                                  |                                             |                                                   |
|----------------------------------|---------------------------------------------|---------------------------------------------------|
| Transforms                       | Filename                                    | Description                                       |
| port_descriptions                | port_desc_2.5.4.csv                         | Gives port descriptions to ports.                 |
| corelight_systems                | corelight_systems_2.5.4.csv                 | Auto-generated from sensor data                   |
| corelight_services               | corelight_services_2.5.4.csv                | Auto-generated from services data                 |
| corelight_dns_ports              | corelight_dns_ports_2.5.4.csv               | Auto-generated from DNS data                      |
| corelight_dns_record_types       | corelight_dns_record_type_2.5.4.csv         | Auto-generated from NDS data                      |
| corelight_files_mime_types       | corelight_files_mime_types_2.5.4.csv        | Auto-generated from files data                    |
| corelight_software_types         | corelight_software_types_2.5.4.csv          | Auto-generated from software data                 |
| corelight_dns_reply_code         | corelight_dns_reply_code_2.5.4.csv          | Provided to lookup reply code types               |
| corelight_conn_state_description | corelight_conn_state_description_2.5.4.csv  | Describes connection states                       |
| corelight_status_action          | corelight_status_action_2.5.4.csv           | Describes Corelight action and status             |
| ssh_inference                    | ssh_inference_lookup_2.5.4.csv              | Describes inferences                              |
| corelight_inferences_description | corelight_inferences_description_2.5.4.csv  | Describes inferences                              |
| corelight_severity               | corelight_severities_2.5.4.csv              | Maps severity ids and severity text               |
| corelight_error_messages         | corelight_error_messages_2.5.4.csv          | Contains information on Corelight Error messages. |
| corelight_alert_aggregations     | corelight_alert_aggregations_enrichment.csv | Provides enrichments for Suricata alerts.         |

## Scripts and binaries

This App provides the following scripts:

- cid.py

  - Script for use with the `cid` command.

- Diag.py

  - Custom diag generation

- Utilities.py

  - Splunk utilities for python scripts

- version.py

  - The splunk app version for logging purposes

- app_properties.py

  - The Splunk extension properties.

## Event Generator

Corelight App For Splunk does not make use of an event generator.

## Acceleration

1.  Summary Indexing: No

2.  Data Model Acceleration: No

3.  Report Acceleration: No
