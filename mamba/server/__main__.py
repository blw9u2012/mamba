import os
import click
import logging


@click.command()
@click.option('-c', '--config', help="Path to configuration file.")
@click.option('-d', '--debug', flag_value=True, help="Run server is debug mode")
@click.version_option()

def main(config, debug):
    """
    Manage server
    """
    pass
