= Application Certification README

Hi. If you are AppCert Team, thanks for reading. If you aren't, yay!

This documentation is meant to clarify some points that are common in our libraries. We try to be transparent in our handling of data, and will describe how certain features are achieved. 

== Proxy Configuration
We include a dashboard to configure proxies for use within the app. The setup modal contains a place for username and password. The username and password are encrypted, and the resulting encrypted storage stanza is put in the parameter `proxy_credential`. Meaning, there is no storage in plaintext of the proxy credential. The setting stored in the parameter is a pointer to the encrypted storage stanza.

== Modular Input Configuration
Generically, we include a modular input configuration javascript file which allows the user to configure a modular input in a more friendly manner. Most modular inputs contain a "hostname" or "tenanturl" or similar parameter, which refers to the host of the API being consumed. While the input will allow "http" protocols to be configured, the setting for "https" should be hardcoded within the modular input python code itself IF the appliance/technology allows ONLY HTTP. Some technologies provide both methods, so we must provide both options for configuration. Please refer to the python code (generally in the "build_url" overridden function of the modular input / rest client code) to determine actual protocol used.

Where a password is shown inside of the App_Config dashboard, the JS will create an encrypted credential that correlates to host and username. 

== appserver/addons
Included in appserver/addons are the pre-built version-correct Add-Ons designed to be complimentary to this app. They are not dependencies, but are intended for complex architectures. If present, they would refer to the following nomenclatures:

Input Add-On: IA-CorelightAppForSplunk
Domain Add-On: DA-CorelightAppForSplunk
Technology Add-On: TA-CorelightAppForSplunk
Support Add-On: SA-CorelightAppForSplunk