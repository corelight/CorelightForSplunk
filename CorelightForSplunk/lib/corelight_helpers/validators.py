"""This file is used for validation."""
from splunktaucclib.rest_handler.endpoint.validator import Validator
from .logger_manager import setup_logging
from .conf_helper import get_conf_file, create_service, update_conf_file
import splunk.admin as admin
from copy import deepcopy
from solnlib.utils import is_true

SSL_ERROR = "_ssl.c"


class GetSessionKey(admin.MConfigHandler):
    """Session key."""

    def __init__(self):
        """Initialize Session Key."""
        self.session_key = self.getSessionKey()


class LoggingValidator(Validator):
    """This class validates corelight logging configuration."""

    def validate(self, value, data):
        """Validate corelight logging configuration."""
        try:
            self.logger = setup_logging('corelight_logging_configurations')
            self.logger.info("message=logging_validation | Corelight logging sync started.")
            session_key = GetSessionKey().session_key

            updated_apl_logging_data = {
                "cid": data.get("cid", "INFO"),
                "modularinput": data.get("modularinput", "INFO"),
                "restclient": data.get("restclient", "INFO"),
                "utilities": data.get("utilities", "INFO"),
                "kenny_loggins": data.get("kenny_loggins", "WARN")
            }

            update_conf_file(
                file="apl_logging",
                stanza_name="CorelightForSplunk",
                stanza=updated_apl_logging_data,
                session_key=session_key,
            )
            self.logger.info(
                "message=update_apl_logging | apl_logging configuration has been synced successfully."
            )
            return True

        except Exception as e:
            if SSL_ERROR in str(e):
                msg = (
                    "SSL certificate verification failed. Please add a valid SSL certificate."
                )
                self.logger.exception(f'message=logging_validation_error | {msg}')
            else:
                self.logger.exception(
                    f"message=logging_validation_error | Error occued while validating logging Settings. Error : {e}"
                )
                msg = "Some unexpected error occured. Please check the logs."
            self.put_msg(msg)
            return False


class ConfigurationValidator(Validator):
    """This class validates corelight configuration."""

    CORELIGHT_MACRO_INDEX = "corelight_idx"
    CORELIGHT_EVENTTYPE_INDEX = "corelight_idx"
    CORELIGHT_ST_MACROS_DICT = {
        "": {
            "corelight_st_intel": [""],
            "corelight_st_notice": [""],
            "corelight_st_ip_interr_http": [""],
            "corelight_st_log_hunting": [""],
            "corelight_st_ssh": [""],
            "corelight_st_dpd": [""],
            "corelight_st_suricata": [""]
        },
        "Corelight": {
            "corelight_st_intel": ["corelight_intel"],
            "corelight_st_notice": ["corelight_notice"],
            "corelight_st_ip_interr_http": ["corelight_http*"],
            "corelight_st_log_hunting": ["corelight_corelight*"],
            "corelight_st_ssh": ["corelight_ssh"],
            "corelight_st_dpd": ["corelight_dpd"],
            "corelight_st_suricata": ["corelight_suricata_corelight"]
        },
        "Zeek": {
            "corelight_st_intel": ["bro_intel"],
            "corelight_st_notice": ["bro_notice", "bro:notice:json"],
            "corelight_st_ip_interr_http": ["bro_http*"],
            "corelight_st_log_hunting": ["bro_bro*"],
            "corelight_st_ssh": ["bro_ssh"],
            "corelight_st_dpd": ["bro_dpd"],
            "corelight_st_suricata": ["bro_suricata_bro"]
        }
    }
    CORELIGHT_EVT_MACROS_DICT = {
        "": {
            "corelight_evt_smtp": [""],
            "corelight_evt_all": [""],
            "corelight_evt_conn": [""],
            "corelight_evt_suri": [""],
            "connection_corelight_evt_conn_base": [""],
            "corelight_evt_http": [""],
            "corelight_evt_files": [""],
            "corelight_evt_dns": [""],
            "corelight_evt_software": [""],
            "corelight_evt_x509": [""],
            "corelight_evt_ssl": [""],
            "corelight_evt_metric_bro": [""],
            "corelight_evt_metric_iface": [""],
            "corelight_evt_metric_system": [""]
        },
        "Corelight": {
            "corelight_evt_smtp": ["corelight_smtp"],
            "corelight_evt_all": ["corelight*"],
            "corelight_evt_conn": ["corelight_conn"],
            "corelight_evt_suri": ["corelight_suri"],
            "connection_corelight_evt_conn_base": ["corelight_conn_base"],
            "corelight_evt_http": ["corelight_http"],
            "corelight_evt_files": ["corelight_files"],
            "corelight_evt_dns": ["corelight_dns"],
            "corelight_evt_software": ["corelight_software"],
            "corelight_evt_x509": ["corelight_x509"],
            "corelight_evt_ssl": ["corelight_ssl"],
            "corelight_evt_metric_bro": ["corelight_metrics_bro"],
            "corelight_evt_metric_iface": ["corelight_metrics_iface"],
            "corelight_evt_metric_system": ["corelight_metrics_system"]
        },
        "Zeek": {
            "corelight_evt_smtp": ["bro_smtp"],
            "corelight_evt_all": ["bro*"],
            "corelight_evt_conn": ["bro_conn"],
            "corelight_evt_suri": ["bro_suri"],
            "connection_corelight_evt_conn_base": ["bro_conn_base"],
            "corelight_evt_http": ["bro_http"],
            "corelight_evt_files": ["bro_files"],
            "corelight_evt_dns": ["bro_dns"],
            "corelight_evt_software": ["bro_files"],
            "corelight_evt_x509": ["bro_x509"],
            "corelight_evt_ssl": ["bro_ssl"],
            "corelight_evt_metric_bro": ["bro_metrics_bro"],
            "corelight_evt_metric_iface": ["bro_metrics_iface"],
            "corelight_evt_metric_system": ["bro_metrics_system"]
        }
    }
    CORELIGHT_SAVED_SEARCHES_CONF = {
        "suricata_detections_search": "Corelight_Suricata_Detections",
        "sensor_lookup_gen": "corelight_sensor_lookup_gen",
        "dns_port_lookup_gen": "corelight_dns_port_lookup_gen",
        "files_mime_lookup_gen": "corelight_files_mime_type_lookup_gen",
        "software_lookup_gen": "corelight_software_types_lookup_gen",
        "dns_record_lookup_gen": "corelight_dns_record_type_lookup_gen",
        "service_lookup_gen": "corelight_service_lookup_gen"
    }

    def update_macros(self, service, macro_name, macro_string):
        """Update macro_name with the macro_string provided."""
        try:
            service.post(
                "properties/macros/{}".format(macro_name), definition=macro_string
            )
            self.logger.info(
                "message=update_macros | Updated macro {} with: {} Successfully.".format(macro_name, macro_string)
            )
        except Exception as e:
            self.logger.exception(
                f"message=update_macros_error | Error occued while updating macro. Error : {e}"
            )
            return False

    def update_eventtypes(self, service, eventtype_name, eventtype_string):
        """Update eventtype_name with the eventtype_string provided."""
        try:
            service.post(
                "properties/eventtypes/{}".format(eventtype_name), search=eventtype_string
            )
            self.logger.info(
                "message=update_eventtypes | Updated eventtype {} with: {} Successfully.".format(
                    eventtype_name, eventtype_string
                )
            )
        except Exception as e:
            self.logger.exception(
                f"message=update_eventtypes_error | Error occued while updating eventtype. Error : {e}"
            )
            return False

    def update_app_istall(self, service, is_app_configured):
        """Update install stanza in app.conf with the is_app_configured provided."""
        try:
            service.post(
                "properties/app/{}".format("install"), is_configured=is_app_configured
            )
            self.logger.info(
                "message=update_app_istall | Updated [install] with: {} Successfully.".format(is_app_configured)
            )
        except Exception as e:
            self.logger.exception(
                f"message=update_app_istall_error | Error occued while updating [install]. Error : {e}"
            )
            return False

    def enable_savedsearches(self, service, saved_searches_names):
        """Enable the saved searches provided in the parameters."""
        try:
            for saved_searches_name in saved_searches_names:
                saved_search = service.saved_searches[saved_searches_name]
                saved_search.enable()
                self.logger.info(
                    "message=update_savedsearches | Saved Search: {} is enabled Successfully.".format(
                        saved_searches_name
                    )
                )
        except Exception as e:
            self.logger.error(
                f"message=update_savedsearches_error | Error occued while updating savedsearches. Error: {e}"
            )
            return False

    def disable_savedsearches(self, service, saved_searches_names):
        """Disable the saved searches provided in the parameters."""
        try:
            for saved_searches_name in saved_searches_names:
                saved_search = service.saved_searches[saved_searches_name]
                saved_search.disable()
                self.logger.info(
                    "message=update_savedsearches | Saved Search: {} is disabled Successfully.".format(
                        saved_searches_name
                    )
                )
        except Exception as e:
            self.logger.exception(
                f"message=update_savedsearches_error | Error occued while updating savedsearches. Error : {e}"
            )
            return False

    def get_updated_macros(self, products, ref_dict):
        """Get updated macros."""
        result = dict()
        for p in products:
            for k, v in ref_dict.get(p, {}).items():
                if k in result:
                    result[k].extend(v)
                else:
                    result[k] = v
        return result

    def update_st_evt_macros(self, service, new_updated_st_macros, new_updated_evt_macros):
        """Update sourcetype and eventtype macros."""
        for evt_stanza_name, evt_values in new_updated_st_macros.items():
            macro_string = f'sourcetype IN ({",".join(evt_values)})'
            self.update_macros(
                service, evt_stanza_name, macro_string
            )
        for evt_stanza_name, evt_values in new_updated_evt_macros.items():
            macro_string = f'eventtype IN ({",".join(evt_values)})'
            self.update_macros(
                service, evt_stanza_name, macro_string
            )

    def validate(self, value, data):
        """Validate corelight configuration."""
        try:
            self.logger = setup_logging('corelight_configurations')
            self.logger.info("message=configuration_validation | Corelight configuration started.")
            session_key = GetSessionKey().session_key

            parameters = get_conf_file(
                file="corelightforsplunk_settings",
                session_key=session_key,
                stanza="app_settings"
            )

            service = create_service()

            diff_data = {}
            for key in data.keys():
                if parameters.get(key) != data.get(key) and (
                    parameters.get(key) or data.get(key)
                ):
                    diff_data.update({key: data.get(key)})

            for diff_data_key, diff_data_value in diff_data.items():
                if diff_data_key == "indexes":
                    macro_string = "index IN ({})".format(
                        diff_data.get("indexes")
                    )
                    self.update_macros(
                        service, self.CORELIGHT_MACRO_INDEX, macro_string
                    )
                    eventtype_string = "index IN ({})".format(
                        diff_data.get("indexes")
                    )
                    self.update_eventtypes(
                        service, self.CORELIGHT_EVENTTYPE_INDEX, eventtype_string
                    )
                if diff_data_key == "sourcetype_core":
                    products = diff_data.get("sourcetype_core").split(',')
                    products = [p.strip() for p in products]
                    new_updated_st_macros = self.get_updated_macros(products, deepcopy(self.CORELIGHT_ST_MACROS_DICT))
                    new_updated_evt_macros = self.get_updated_macros(products, deepcopy(self.CORELIGHT_EVT_MACROS_DICT))
                    self.update_st_evt_macros(service, new_updated_st_macros, new_updated_evt_macros)
                if diff_data_key == "app_configured":
                    self.update_app_istall(service, diff_data.get("app_configured"))
                for field, saved_search in self.CORELIGHT_SAVED_SEARCHES_CONF.items():
                    if diff_data_key == field:
                        saved_search_value = is_true(diff_data.get(field))
                        saved_searches = [saved_search]
                        if saved_search_value:
                            self.enable_savedsearches(service, saved_searches)
                        else:
                            self.disable_savedsearches(service, saved_searches)

            return True

        except Exception as e:
            if SSL_ERROR in str(e):
                msg = (
                    "SSL certificate verification failed. Please add a valid SSL certificate."
                )
                self.logger.exception(f'message=configuration_validation_error | {msg}')
            else:
                self.logger.exception(
                    f"message=configuration_validation_error | Error occued while "
                    f"validating configuration Settings. Error : {e}"
                )
                msg = "Some unexpected error occured. Please check the logs."
            self.put_msg(msg)
            return False
