"""Translation utils."""
import os
import pathlib

from .error import ExitApp


def get_lokalise_token():
    """Get lokalise token."""
    token = os.environ.get("LOKALISE_TOKEN")

    if token is not None:
        return token

    token_file = pathlib.Path(".lokalise_token")

    if not token_file.is_file():
        raise ExitApp(
            "Lokalise token not found in env LOKALISE_TOKEN or file .lokalise_token"
        )

    return token_file.read_text().strip()
