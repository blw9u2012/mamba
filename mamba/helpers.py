import os
from urllib.parse import urlparse

def get_repository_name(repository_url):
    parts = urlparse(repository_url)
    return os.path.splitext(os.path.basename(parts.path))[0]