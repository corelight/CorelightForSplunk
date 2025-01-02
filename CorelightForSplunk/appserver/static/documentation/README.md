# Corelight App For Splunk Documentation

The Corelight App for Splunk enables incident responders and threat hunters who use Splunk® and Splunk Enterprise Security to work faster and more effectively.

|                            |                                            |
|----------------------------|--------------------------------------------|
| App Version                | 2.5.2                                      |
| App Build                  | 162                                        |
| Splunk Enterprise Versions | 9.4.x, 9.3.x, 9.2.x, 9.1.x                 |
| Platforms                  | Splunk Enterprise, Splunk Cloud            |
| Splunkbase Url             | <https://splunkbase.splunk.com/app/3884>   |
| Author                     | Corelight, Inc.                            |
| Creates an index           | False                                      |
| Implements summarization   | No                                         |
| Summary Indexing           | False                                      |
| Report Acceleration        | False                                      |
| Release Date               | 11/25/2024                                 |

<div class="important">

When upgrading from Corelight App For Splunk version 2.4.4 or earlier, remove the previous app before installing the latest Corelight App For Splunk app release. Additionally, check in the `local/data/ui/views` folder for conflicting dashboards.

</div>

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
| port_descriptions                | port_desc_2.5.2.csv                         | Gives port descriptions to ports.                 |
| corelight_systems                | corelight_systems_2.5.2.csv                 | Auto-generated from sensor data                   |
| corelight_services               | corelight_services_2.5.2.csv                | Auto-generated from services data                 |
| corelight_dns_ports              | corelight_dns_ports_2.5.2.csv               | Auto-generated from DNS data                      |
| orelight_dns_record_types        | corelight_dns_record_type_2.5.2.csv         | Auto-generated from NDS data                      |
| corelight_files_mime_types       | corelight_files_mime_types_2.5.2.csv        | Auto-generated from files data                    |
| corelight_software_types         | corelight_software_types_2.5.2.csv          | Auto-generated from software data                 |
| corelight_dns_reply_code         | corelight_dns_reply_code_2.5.2.csv          | Provided to lookup reply code types               |
| corelight_conn_state_description | corelight_conn_state_description_2.5.2.csv  | Describes connection states                       |
| corelight_status_action          | corelight_status_action_2.5.2.csv           | Describes Corelight action and status             |
| ssh_inference                    | ssh_inference_lookup_2.5.2.csv              | Describes inferences                              |
| corelight_inferences_description | corelight_inferences_description_2.5.2.csv  | Describes inferences                              |
| corelight_severity               | corelight_severities_2.5.2.csv              | Maps severity ids and severity text               |
| corelight_error_messages         | corelight_error_messages_2.5.2.csv          | Contains information on Corelight Error messages. |
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

# Installation

## Software requirements

### Splunk Enterprise system requirements

Review the Splunk Enterprise system requirements at [Splunk Enterprise system Requirements](https://docs.splunk.com/Documentation/Splunk/latest/Installation/Systemrequirements) at <https://docs.splunk.com>.

### Download

The Corelight App For Splunk and the TA for Corelight add-on are available on Splunkbase.

- [Corelight App for Splunk](https://splunkbase.splunk.com/app/3884)

- [TA for Corelight add-on](https://splunkbase.splunk.com/app/3885)

**Important**: The **TA for Corelight** add-on is required on indexers, or index clusters. If your Corelight sensors send data directly to a heavy forwarder or a Splunk Cloud Platform receiver that is a heavy forwarder, the **TA for Corelight** is also required on those instances. The add-on is not required on search heads, or single-instance Splunk Enterprise environments.

# App Installation steps

Your Splunk Enteprise infrastructure will determine where the Corelight App for Splunk is installed.

## Splunk Cloud Platform customers

Contact your Splunk Administrator before installing Splunk apps in your Splunk Cloud Platform environment. The Corelight App for Splunk supports self-service installation. Cloud app installation guidance is available in [Install apps on your Splunk Cloud Platform deployment](https://docs.splunk.com/Documentation/SplunkCloud/latest/Admin/SelfServiceAppInstall#Install_a_public_app_from_Splunkbase) at <https://docs.splunk.com>

## Splunk Enterprise on-premises customers

When working with an on-premises Splunk Enterprise infrastructure, contact your Splunk Administrator to determine what locations and options are available for installing and distributing Splunk Apps. Installing Splunk apps typically requires administrative credentials.

### Splunk Enterprise single-instance

To deploy to single server instance of Splunk Enterprise:

1.  Log in to Splunk Web as an administrator.

2.  Browse to **Apps** \> **Find More Apps**.

3.  Use the search box to find **Corelight**.

4.  Click the **Install** button for the **Corelight App for Splunk**.

5.  (Optional) If a restart is required, click **Restart Splunk** to restart Splunk services.

### Other Splunk Enterprise architectures

Review the [Corelight App for Splunk documentation](https://docs.corelight.com) at <https://docs.corelight.com>

## Install the Add-on

The **TA for Corelight** add-on is required on indexers, or index clusters. If your Corelight sensors send data directly to a heavy forwarder or a Splunk Cloud Platform receiver that is a heavy forwarder, the **TA for Corelight** is also required on those instances. The add-on is not required on search heads, or single-instance Splunk Enterprise environments.

- Contact your Splunk Administrator. To determine which instances require the **TA for Corelight** add-on, you must understand the data flow from the sensor network to the Splunk Enterprise indexers, including any intermediate forwarding layers, and the tools used to deploy changes to those Splunk Enterprise instances.

## Configuration Steps

Configuring the Corelight App For Splunk requires the \`\`admin_all_objects\`\` capability, typical reserved for administrative users only. Once the configuration changes are saved, the admin user is no longer required.

1.  Log in to Splunk Web on the search head as an administrator.

2.  Browse to **Apps** \> **Corelight App for Splunk**.

3.  Select the **Corelight** drop-down, and click **Configuration**.

4.  Review the **Indexes** field, and add all indexes that contain Corelight sensor log data.

5.  Review the **Products** field, and verify that **Corelight** is selected.

    - If the **Corelight** option is selected, the dashboard searches will use log data source types beginning with the name \`\`corelight\_\`\`.

    - If the **Zeek** option is selected, the dashboard searches will use log data source types beginning with the name \`\`bro\_\`\`. If those source types do not exist in the indexes configured, the dashboard panels will display a warning about missing eventtypes. For example, \`\`Eventtype *bro_x509* does not exist or is disabled.\`\` If your sensor log sources don’t use source type names starting with \`\`bro\_\`\`, you can disable the **Zeek** option.

6.  Review the **Local Network Block(s)** field, and define your local networks in CIDR format. The networks defined in the app should match the **Local Network Blocks** defined on the Corelight sensor, or in the Fleet Manager sensor policy. For more information on sensor local networks, see [Configure network infrastructure](https://docs.corelight.com/docs/sensor/sensor/bro/setup.html#localizing) at <https://docs.corelight.com>.

7.  Click **Save Application Configuration**.

8.  Once the configuration is saved, ensure that the saved search provided for Suricata Detection aggregation (`Corelight_Suricata_Detections`) is enabled.

    - This is done in the "Searches, Reports, and Alerts" section of Splunk.

    - For more information, please refer to [the Splunk Documentation](https://docs.splunk.com/Documentation/Splunk/latest/Report/Createandeditreports#Disable_a_report).

## Generate the lookup files

The data in the lookup files is used as a data source for filtering the results on dashboard panels, such as the Corelight sensor hostnames, and common service names and ports. The lookup files do not run on a schedule, and must be generated again to reflect recent changes.

1.  Log in to Splunk Web on the search head.

2.  Browse to **Apps** \> **Corelight App for Splunk**.

3.  Select the **Corelight** drop-down, and click **Lookup Generation**. **Important**: The lookup files are created using the \`\`outputlookup\`\` command. If the dashboard panels do not populate automatically, and a warning is displayed **Found potentially risky command: outputlookup**, you can click the warning and choose **Run Query Anyway**. For more information about the use of \`\`outputlookup\`\`, see [Commands that trigger SPL safeguards](https://docs.splunk.com/Documentation/Splunk/latest/Security/SPLsafeguards?ref=hk#Commands_that_trigger_SPL_safeguards) on <https://docs.splunk.com>.

4.  Verify the data appears on the panels. Some panels might not populate if the data source isn’t available, or wasn’t found in an index.

## Next Steps

Use app dashboards such as the Data Explorer dashboards to verify the sensor data is available in Splunk Enterprise, and the Corelight App For Splunk is configured.

# Troubleshooting

## Actions

- Check the Monitoring Console for errors

- Validate if the Index(s), Product(s) and Local Network Block(s) are configured (Corelight \> Configuration).

- Ensure the lookup tables were fully updated by running the searches in the Lookup Generation dashboard (Corelight \> Lookup Generation)

## Support

- Support Email: None

- Support Website: <https://www.corelight.com/support>

- Support Offered: Web

App support is available through the [Corelight Support site](https://corelight.com/support/) at <https://corelight.com>.

You can find the latest documentation on the [Corelight documentation site](https://docs.corelight.com) at <https://docs.corelight.com>.

# Release Notes

## Version 2.5.2

### What’s New

- Enhanced queries for the Alert Aggregations, Alert Aggregations Details, Security Posture, Sensor Overview, VPN Insights Dashboard.

## Version 2.5.1

### What’s New

- **Alert Aggregations**

  - Introducing a new suite of dashboards designed to aggregate Suricata alerts. These dashboards feature AI-driven enrichments and mappings to the MITRE ATT&CK framework, offering a comprehensive analytical perspective.

  - New Dashboards:

    - Alert Aggregations

    - Alert Aggregations Details

- **Corelight_ssh Integration**

  - Added `corelight_ssh` to the CIM framework with accurate tagging and mapping to their respective Splunk Data Models.

### Improvements to Functionality

- **Lookup Updates**

  - Removed versioning from generated lookups to prevent upgrade issues between generations.

- **Optimized Performance:**

  - Enhanced search performance on Security Posture panels, including SMBv1, FTP, and DNS.

### Issue Resolutions

- **Field Alias Adjustments:**

  - Updated `corelight_http`, `corelight_http_red`, and `corelight_http2` stanzas in `props.conf` to correctly handle field aliases for `bytes_in` and `bytes_out`.

- Lookup Updates

  - Removed versioning from generated lookups to prevent upgrade issues between generations.

- Dashboard Updates

  - Updated various dashboards for formatting and search optimizations.

- Upgraded `splunk-sdk` to 2.0.2.

## Version 2.5.0

- Dashboard Updates

  - Updated the `Welcome` dashboard

  - Added `Security Posture`

  - Added `Secure Channel Insights`

  - Added `Name Resolution Insights`

  - Added `Remote Activity Insights`

## Version 2.4.10

- Bug

  - \[DESK-1536\] - Various sourcetypes did not have the proper time extraction for the Corelight Appliance.

## Version 2.4.9

- Dashboard Enhancements

  - HTTP

    - Added dropdown filter for User Agents. Shows Top 100 only.

  - VPN Insights

    - Added dropdown filter for Inferences.

    - Fixed incorrect query for `Largest Transfers Between Host Pairs Over VPN`

  - Intel

    - Added dropdown filter for Incident Types.

  - Notices

    - Added a textual filter field for `msg` or `note` fields.

- Updated `Corelight Suricata IDS Alerts` dashboard.

- Extractions

  - Updated various sourcetypes to remove confusion around src/dest fields relating to `id.*` fields.

## Version 2.4.8

- Updated TA for proper permissions to pass Splunk Cloud

- Updated `corelight_ntp` sourcetype: correct an if statement

## Version 2.4.7

- Removed `KV_MODE` on `corelight_tsv` as invalid against `INDEXED_EXTRACTIONS`

- Updated lookups to a version based file-naming convention to facilitate Splunk Cloud updates.

- Additional CIM additions for additional sourcetypes

## Version 2.4.6

- Updated to CIM v5.1

- Fixed bug in `cid` search command relating to icmp6 with IPv6 src_ips.

- Updated `inferences` props for better extractions.

## Version 2.4.5

- Converted `cid` custom command to a v2 Search Command.

- Updated `splunklib` to current version.

- Updated Configuration Management page

- Added additional support easier diagnostic gathering

# Review and Optimization (removed on Release)

# Name Resolution Insights

## Reviewed: No Change

- **\*Responding DNS Servers**\*

  - Single Value

  - Table

- ****\*Unusual Qtypes****\*

  - Single Value

  - Table

- ****\*NXDOMAIN Responses****\*

  - Single Value

  - Table

- ****\*Failed DNS Queries****\*

  - Single Value

## Reviewed: Change

- ****\*Failed DNS Queries****\*

  - Table: "ds_dns_tbl_name_res_failed_table"

- **\*DNS Query Volume Over Time**\*

  - Single Value: "ds_dns_sv_volume_count"

- **\*Monitoring DNS Query Response Times \> 15ms**\*

  - Single Value: "ds_dns_sv_name_res_query_response_base"

  - Table: "ds_dns_tbl_name_res_query_response_base"

## Reviewed: Questions

- **\*DNS Query Volume Over Time**\*

  - Chart

  - What is this supposed to show? Right now it is "count of dns events over time", but the blurb indicates "avg rtt by qtype_name" should be displayed.

  - What is 35s as the average? of what?
