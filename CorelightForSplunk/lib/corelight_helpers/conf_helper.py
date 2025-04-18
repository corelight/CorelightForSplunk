"""Conf handler which returns conf information."""
from solnlib import conf_manager
import splunk.admin as admin
import splunk.clilib.cli_common
import splunklib.client as client
import socket

# Splunk imports
from import_declare_test import ta_name


class GetSessionKey(admin.MConfigHandler):
    """To get Splunk session key."""

    def __init__(self):
        """Initialize."""
        self.session_key = self.getSessionKey()


def get_conf_file(
    file,
    app=ta_name,
    session_key=None,
    stanza=None,
    realm="__REST_CREDENTIAL__#{}#configs/conf-{}",  # noqa E502
):
    """
    Conf info returns the file information.

    :param session_key:
    :param file:
    :param app:
    :param realm:
    :return: Conf File Object
    """
    if session_key is None:
        session_key = GetSessionKey().session_key
    cfm = conf_manager.ConfManager(
        session_key, app, realm=realm.format(ta_name, file)
    ).get_conf(file)
    if stanza:
        return cfm.get(stanza)
    return cfm


def update_conf_file(
    file,
    stanza_name,
    stanza,
    app=ta_name,
    session_key=None,
    encrypt_keys=None
):
    """Update stanza.

    It will try to encrypt the credential automatically fist if
    encrypt_keys are not None else keep stanza untouched.

    Arguments:
        file: Conf file name.
        stanza_name: Stanza name.
        stanza: Stanza to update.
        app: App name.
        session_key: Session Key.
        encrypt_keys: Field names to encrypt.
    """
    if session_key is None:
        session_key = GetSessionKey().session_key
    cfm = conf_manager.ConfManager(
        session_key, app).get_conf(file)
    cfm.update(stanza_name, stanza)
    cfm.reload()


def resolve_host(hostname):
    """Resolve hostname to IPv4/IPv6 address."""
    try:
        # This returns a list of (family, type, proto, canonname, sockaddr) tuples
        infos = socket.getaddrinfo(hostname, None)

        # Filter for IPv4 and IPv6 addresses
        ipv4_addresses = [info for info in infos if info[0] == socket.AF_INET]
        ipv6_addresses = [info for info in infos if info[0] == socket.AF_INET6]

        # Prefer IPv4, but fallback to IPv6 if necessary
        if ipv4_addresses:
            address = ipv4_addresses[0][4][0]
        elif ipv6_addresses:
            address = ipv6_addresses[0][4][0]
        else:
            return None  # No suitable address found
        return address
    except socket.gaierror:
        return None


def create_service(sessionkey=None):
    """Create Service to communicate with splunk."""
    mgmt_uri = splunk.clilib.cli_common.getMgmtUri()
    hostname = mgmt_uri.split("//")[-1].split(":")[0]  # Extract hostname from URI
    mgmt_port = mgmt_uri.split(":")[-1]

    # Resolve hostname to IPv4 address
    ip_address = resolve_host(hostname)
    if not ip_address:
        raise Exception("Failed to resolve Splunk management URI to an IP address.")

    if not sessionkey:
        sessionkey = GetSessionKey().session_key

    service = client.connect(host=ip_address, port=mgmt_port, token=sessionkey, app=ta_name)
    return service
