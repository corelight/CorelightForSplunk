# Release Notes

## Version 2.5.1

- Enhanced queries for the Security Posture, and Data Insights dashboards.

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
