# Release Notes

## Version 2.5.2

### What’s New

Enhanced queries for the Alert Aggregations, Alert Aggregations Details, Security Posture, Sensor Overview, VPN Insights Dashboard.

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
