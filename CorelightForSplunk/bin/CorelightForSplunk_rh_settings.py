
import import_declare_test

from splunktaucclib.rest_handler.endpoint import (
    field,
    validator,
    RestModel,
    MultipleModel,
)
from splunktaucclib.rest_handler import admin_external, util
from splunktaucclib.rest_handler.admin_external import AdminExternalHandler
import logging
from corelight_helpers.validators import ConfigurationValidator, LoggingValidator

util.remove_http_proxy_env_vars()


fields_app_settings = [
    field.RestField(
        'indexes',
        required=True,
        encrypted=False,
        default='main',
        validator=ConfigurationValidator()
    ), 
    field.RestField(
        'sourcetype_core',
        required=False,
        encrypted=False,
        default='Corelight',
        validator=None
    ), 
    field.RestField(
        'local_network_blocks',
        required=False,
        encrypted=False,
        default='',
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'app_configured',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'suricata_detections_search',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'sensor_lookup_gen',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'dns_port_lookup_gen',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'files_mime_lookup_gen',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'software_lookup_gen',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'dns_record_lookup_gen',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'service_lookup_gen',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    )
]
model_app_settings = RestModel(fields_app_settings, name='app_settings')


fields_apl_logging = [
    field.RestField(
        'cid',
        required=True,
        encrypted=False,
        default='INFO',
        validator=LoggingValidator()
    ), 
    field.RestField(
        'sync_logging',
        required=True,
        encrypted=False,
        default=0,
        validator=None
    ), 
    field.RestField(
        'kenny_loggins',
        required=True,
        encrypted=False,
        default='WARN',
        validator=None
    ), 
    field.RestField(
        'modularinput',
        required=True,
        encrypted=False,
        default='INFO',
        validator=None
    ), 
    field.RestField(
        'restclient',
        required=True,
        encrypted=False,
        default='INFO',
        validator=None
    ), 
    field.RestField(
        'utilities',
        required=True,
        encrypted=False,
        default='INFO',
        validator=None
    )
]
model_apl_logging = RestModel(fields_apl_logging, name='apl_logging')


endpoint = MultipleModel(
    'corelightforsplunk_settings',
    models=[
        model_app_settings, 
        model_apl_logging
    ],
    need_reload=False,
)


if __name__ == '__main__':
    logging.getLogger().addHandler(logging.NullHandler())
    admin_external.handle(
        endpoint,
        handler=AdminExternalHandler,
    )
