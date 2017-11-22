import yaml

from .errors import MambaError

def parse(path):
    try:
        with open(path) as mamba_file:
            config = yaml.load(mamba_file)
    except OSError:
        raise MambaError("No mamba.yml config file found in repository")
    return config