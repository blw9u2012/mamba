import os
import click

class DefaultConfig(object):
    # Default configuration settings
    MONGODB_SETTINGS = {
        'db': 'mamba-ci',
        'connect':  False
    }
    APPLICATION_DATAPATH = click.get_app_dir('mamba')
    JOB_DATAPATH = os.path.join(APPLICATION_DATAPATH, 'jobs')
    DEFAULT_CONFIGURATION_FILE = os.path.join(APPLICATION_DATAPATH, 'server-config.yml')
    LOG_FILE_PATH = os.path.join(APPLICATION_DATAPATH, 'server-log')
