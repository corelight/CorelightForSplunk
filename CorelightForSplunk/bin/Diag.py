"""
Written by Kyle Smith for Aplura, LLC
Copyright (C) 2016-2022 Aplura, ,LLC

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
from __future__ import absolute_import
import logging
import os
from splunk.appserver.mrsparkle.lib.util import make_splunkhome_path


# Use the **args pattern to ignore options we don't care about.
def setup(parser=None, callback=None, **kwargs):
    logging.debug("setup() was called!")

    # Declare that we're going to use REST later
    callback.will_need_rest()


# The options are out of order, as is possible for keyword invocation
def collect_diag_info(diag, options=None, global_options=None, app_dir=None, **kwargs):
    # Set limit to 5 GB.
    diag.data_limit = 5368709120
    app = app_dir.split(os.path.sep)[-1]
    logging.info("collect_diag_info() was called for app {}".format(app))

    # Collect a directory from the app
    a_dir = os.path.join(app_dir)
    logging.info("collecting app: {}".format(a_dir))
    diag.add_dir(a_dir, '')

    # diag methods
    # /opt/splunk/lib/python3.7/site-packages/splunk/clilib/info_gather.py:AppScopedDiagDataAdder
    # .add_dir, add_file, add_string, add_rest_endpoint

    modinputs_dir = make_splunkhome_path(["var", "lib", "splunk", "modinputs"])
    if not os.path.exists(modinputs_dir):
        logging.info(f"action=collect_modinputs path={modinputs_dir} status=failed")
        modinputs_dir = os.path.join(os.environ["SPLUNK_DB"], "modinputs")
    if not os.path.exists(modinputs_dir):
        logging.error(f"action=collect_modinputs_checkpoints path={modinputs_dir} status=not_found")
    else:
        logging.info(f"action=collect_modinputs_checkpoints path={modinputs_dir} status=found")
        diag.add_dir(modinputs_dir, "01_modinput_checkpoints")

    # Collect some REST endpoint data
    diag.add_rest_endpoint("/services/server/info", os.path.join("02_rest", "server_info.xml"))

    system_logs = make_splunkhome_path(["var", "log", "splunk"])
    if not os.path.exists(system_logs):
        logging.info(f"action=collect_system_logs path={system_logs} status=does_not_exist")
        system_logs = os.path.join(os.environ["SPLUNK_HOME"], "var", "log", "splunk")
    if not os.path.exists(system_logs):
        logging.error(f"action=collect_system_logs path={system_logs} status=does_not_exist")
    else:
        logging.info(f"action=collect_system_logs path={system_logs} status=found")
        for x in ["splunkd.log", "python.log", "relaymodaction.log", "python_modular_input.log", "splunkd_stderr.log"]:
            diag.add_file(os.path.join(system_logs, x), os.path.join("03_system_logs", x))

    app_logs = make_splunkhome_path(["var", "log", "splunk", app])
    if not os.path.exists(app_logs):
        logging.info(f"action=collect_app_logs path={app_logs} status=does_not_exist")
        app_logs = os.path.join(os.environ["SPLUNK_HOME"], "var", "log", "splunk", app)
    if not os.path.exists(app_logs):
        logging.error(f"action=collect_app_logs path={app_logs} status=does_not_exist")
    else:
        logging.info(f"action=collect_app_logs path={app_logs} status=found")
        diag.add_dir(app_logs, "04_application_logs")


