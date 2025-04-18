import import_declare_test  # noqa: F401
from corelight_helpers.logger_manager import setup_logging
from corelight_helpers.conf_helper import get_conf_file, update_conf_file
from import_declare_test import ta_name
import sys
import traceback
from solnlib import conf_manager
import splunk.admin as admin
from solnlib.utils import is_true

logger = setup_logging("corelight_sync_logging_configuration")


class GetSessionKey(admin.MConfigHandler):
    """To get Splunk session key."""

    def __init__(self):
        """Initialize."""
        self.session_key = self.getSessionKey()


def sync_apl_logging():
    try:
        session_key = sys.stdin.readline().strip()
        logger.info(
            "message=sync_apl_logging | Started sync_logging_configuration."
        )
        apl_logging_data = get_conf_file(
            file="apl_logging",
            session_key=session_key,
            stanza="CorelightForSplunk"
        )

        old_corelightforsplunk_settings = get_conf_file(
            file="corelightforsplunk_settings",
            session_key=session_key,
            stanza="apl_logging"
        )

        if not is_true(old_corelightforsplunk_settings.get("sync_logging")):
            updated_apl_logging_data = {
                "cid": apl_logging_data.get("cid", "INFO"),
                "modularinput": apl_logging_data.get("modularinput", "INFO"),
                "restclient": apl_logging_data.get("restclient", "INFO"),
                "utilities": apl_logging_data.get("utilities", "INFO"),
                "kenny_loggins": apl_logging_data.get("kenny_loggins", "WARN"),
                "sync_logging": 1
            }

            update_conf_file(
                file="corelightforsplunk_settings",
                stanza_name="apl_logging",
                stanza=updated_apl_logging_data,
                session_key=session_key,
            )
            logger.info(
                "message=sync_successfull | updated corelightforsplunk_settings successfully."
            )
            
        else:
            logger.info(
                "message=already_synced | Logging Configuration is already synced."
            )

        update_inputs_conf = {
            "disabled": 1
        }
        update_conf_file(
            file="inputs",
            stanza_name=r"script://$SPLUNK_HOME/etc/apps/CorelightForSplunk/bin/sync_logging_configuration.py",
            stanza=update_inputs_conf,
            session_key=session_key,
        )
        update_conf_file(
            file="inputs",
            stanza_name=r"script://$SPLUNK_HOME\etc\apps\CorelightForSplunk\bin\sync_logging_configuration.py",
            stanza=update_inputs_conf,
            session_key=session_key,
        )
        logger.info(
            "message=disable_input | disabled scripted inputs sync_logging_configuration successfully."
        )
        logger.info(
            "message=sync_apl_logging | apl_logging configuration has been synced successfully."
        )

    except Exception:
        logger.error(f"Error occured while syncing apl_logging: {traceback.format_exc()}")

if __name__ == "__main__":
    sync_apl_logging()
