# Corelight App For Splunk Documentation

The Corelight App for Splunk enables incident responders and threat hunters who use Splunk® and Splunk Enterprise Security to work faster and more effectively.

|                            |                                          |
|----------------------------|------------------------------------------|
| App Version                | 2.5.1                                    |
| App Build                  | 151                                      |
| Splunk Enterprise Versions | 9.1, 9.0, 8.2, 8.1                       |
| Platforms                  | Splunk Enterprise, Splunk Cloud          |
| Splunkbase Url             | <https://splunkbase.splunk.com/app/3884> |
| Author                     | Aplura, LLC. and Corelight, Inc.         |
| Creates an index           | False                                    |
| Implements summarization   | No                                       |
| Summary Indexing           | False                                    |
| Report Acceleration        | False                                    |

<div class="important">

If upgrading from a Splunk app version 2.4.4 or earlier, the previous app must be deleted for the updated dashboards to appear. Additionally, check in the `local/data/ui/views` folder for conflicting dashboards.

</div>

The App and Add-on extract information and knowledge from Zeek (formerly known as Bro) via Corelight Sensors or open-source Zeek, resulting in powerful security insights through key traffic dashboards such as:

- Intel: Find IOCs from external sources matched in network traffic.

- Notices: See situations flagged by the Notice policy for further investigation.

- IP Interrogation: Identify anomalies by reviewing top protocol usage, internal vs. external connections, top connections by bytes transferred and more.

- Log Hunting: Accelerate your hunt by narrowing down many logs to only the logs that matter.

- Detections: Find and respond to off-port protocol usage, IOC matches, and other potentially interesting events.

- Connections: Gain situational awareness using lists of top services, ports, dataflows, originators, and responders.

- HTTP: Find suspicious HTTP transactions by reviewing a list of top host headers, originators, rare user agents and rare host headers.

- DNS: Detect DNS exfiltration by spotting queries to non-existent domains and high connection counts.

- Files: Find executables hidden in benign extensions and compressed files.

- Corelight Egress Monitor: Find risky North/South user connections to weak SSL versions.

# User Guide

## Key concepts for Corelight App For Splunk

### Configure the Technical Add-On for use with Corelight.

1.  The Technical Add-On should be placed upon the servers that will get the forwarded data from the Corelight Sensor.

2.  This step is OPTIONAL based on your environment. The full App contains the required configurations for full index-time parsing.

3.  Questions should be asked at <https://www.corelight.com/support>

## Indexes

### Getting Data In

By default, all events will be written to the \`\`main\`\` index. Please see Corelight documentation on how to change the destination index from the appliance.

### Searching for Data

By default, all Corelight information is searched for using the `corelight_idx` event type. To change the location for the app to search for Corelight data, edit the `corelight_idx` event type to point to your Corelight index.

## Custom Search Commands

`cid` is a custom command provided to turn a tuple of `src_ip`, `src_port`, `dest_ip`, and `dest_port` into a community string.

## Lookups

Corelight App For Splunk contains several lookup files.

<div class="note">

It is a best practice and recommendation to **not** use the direct CSV name, as these will change between versions. Use the `transforms` name as listed in the table.

</div>

|                                  |                                            |                                                   |
|----------------------------------|--------------------------------------------|---------------------------------------------------|
| Transforms                       | Filename                                   | Description                                       |
| port_descriptions                | port_desc_2.5.1.csv                        | Gives port descriptions to ports.                 |
| corelight_systems                | corelight_systems_2.5.1.csv                | Auto-generated from sensor data                   |
| corelight_services               | corelight_services_2.5.1.csv               | Auto-generated from services data                 |
| corelight_dns_ports              | corelight_dns_ports_2.5.1.csv              | Auto-generated from DNS data                      |
| orelight_dns_record_types        | corelight_dns_record_type_2.5.1.csv        | Auto-generated from NDS data                      |
| corelight_files_mime_types       | corelight_files_mime_types_2.5.1.csv       | Auto-generated from files data                    |
| corelight_software_types         | corelight_software_types_2.5.1.csv         | Auto-generated from software data                 |
| corelight_dns_reply_code         | corelight_dns_reply_code_2.5.1.csv         | Provided to lookup reply code types               |
| corelight_conn_state_description | corelight_conn_state_description_2.5.1.csv | Describes connection states                       |
| corelight_status_action          | corelight_status_action_2.5.1.csv          | Describes Corelight action and status             |
| ssh_inference                    | ssh_inference_lookup_2.5.1.csv             | Describes inferences                              |
| corelight_inferences_description | corelight_inferences_description_2.5.1.csv | Describes inferences                              |
| corelight_severity               | corelight_severities_2.5.1.csv             | Maps severity ids and severity text               |
| corelight_error_messages         | corelight_error_messages_2.5.1.csv         | Contains information on Corelight Error messages. |

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

## Known Issues

Version 2.5.1 of Corelight App For Splunk has the following known issues:

- None

Versions prior to 2.4.7 have the following known issues:

- Any dashboard that uses the `inferences{}` field may have issues with search settings.

Versions prior to 2.4.6 have the following known issues:

- During calculation of the community id with the `cid` command, the transport was not correct for IPv6 `src_ip` fields.

# Installation

## Software requirements

### Splunk Enterprise system requirements

Because this App runs on Splunk Enterprise, all the Splunk Enterprise system requirements at [Splunk System Requirements](https://docs.splunk.com/Documentation/Splunk/latest/Installation/Systemrequirements) apply.

### Download

Download Corelight App For Splunk at <https://splunkbase.splunk.com/app/3884>.

# Installation steps

## Deploy to single server instance

Follow these steps to install the app in a single server instance of Splunk Enterprise:

1.  Deploy as you would any App, and restart Splunk. Do NOT install any other Corelight Apps or Add-Ons.

## Deploy to Splunk Cloud

1.  Install via the Splunk Cloud App Browser located in the manager pages.

2.  If there are issues, or it is not shown, please contact Splunk Cloud Support.

## Deploy to a Distributed Environment

1.  For each Search Head in the environment, deploy the App.

    1.  If a deployer is used, use the deployer methodology.

    2.  DO NOT SEND any other Corelight Apps or Add-Ons to the Search Head Cluster (SHC) or Search heads.

2.  For each indexer in the environment, deploy a copy of the \|ta_name\| Add-On that is located as mentioned above.

# Troubleshooting

## Actions

- Check the Monitoring Console for errors

## Questions and answers

Access questions and answers specific to Corelight App For Splunk at <https://answers.splunk.com>. Be sure to tag your question with the App.

## Support

- Support Email: <appsupport@corelight.com>

- Support Website: <https://www.corelight.com/support>

- Support Offered: Email, Web

Support is available via email at <appsupport@corelight.com>. Responses vary on working days between working hours. Find the latest information about the App and integration on the support website.

# Release Notes

## Version 2.5.1

- Lookup Updates

  - Removed versioning from generated lookups to prevent upgrade issues between generations.

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

# Third-party software

## Aplura, LLC Components

Components Written by Aplura, LLC Copyright © 2016-2023 Aplura, ,LLC

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, eMA 02110-1301, USA.
