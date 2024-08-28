# Corelight App For Splunk Documentation

The Corelight App for Splunk enables incident responders and threat hunters who use Splunk® and Splunk Enterprise Security to work faster and more effectively.

|                            |                                          |
|----------------------------|------------------------------------------|
| App Version                | 2.5.1                                    |
| App Build                  | 146                                      |
| Splunk Enterprise Versions | 9.3.x, 9.2.x, 9.1.x                      |
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
| port_descriptions                | port_desc_2.5.0.csv                        | Gives port descriptions to ports.                 |
| corelight_systems                | corelight_systems_2.5.0.csv                | Auto-generated from sensor data                   |
| corelight_services               | corelight_services_2.5.0.csv               | Auto-generated from services data                 |
| corelight_dns_ports              | corelight_dns_ports_2.5.0.csv              | Auto-generated from DNS data                      |
| orelight_dns_record_types        | corelight_dns_record_type_2.5.0.csv        | Auto-generated from NDS data                      |
| corelight_files_mime_types       | corelight_files_mime_types_2.5.0.csv       | Auto-generated from files data                    |
| corelight_software_types         | corelight_software_types_2.5.0.csv         | Auto-generated from software data                 |
| corelight_dns_reply_code         | corelight_dns_reply_code_2.5.0.csv         | Provided to lookup reply code types               |
| corelight_conn_state_description | corelight_conn_state_description_2.5.0.csv | Describes connection states                       |
| corelight_status_action          | corelight_status_action_2.5.0.csv          | Describes Corelight action and status             |
| ssh_inference                    | ssh_inference_lookup_2.5.0.csv             | Describes inferences                              |
| corelight_inferences_description | corelight_inferences_description_2.5.0.csv | Describes inferences                              |
| corelight_severity               | corelight_severities_2.5.0.csv             | Maps severity ids and severity text               |
| corelight_error_messages         | corelight_error_messages_2.5.0.csv         | Contains information on Corelight Error messages. |

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

Version 2.5.0 of Corelight App For Splunk has the following known issues:

- None

Versions prior to 2.4.7 have the following known issues:

- Any dashboard that uses the `inferences{}` field may have issues with search settings.

Versions prior to 2.4.6 have the following known issues:

- During calculation of the community id with the `cid` command, the transport was not correct for IPv6 `src_ip` fields.

> **NOTE** : The dashboard will show the duplicate count if the data has been ingested multiple times.
