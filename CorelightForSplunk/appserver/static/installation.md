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
