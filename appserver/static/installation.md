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
