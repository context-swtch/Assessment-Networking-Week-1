"""Functions that interact with the Postcode API."""

import requests as req


def validate_postcode(postcode: str) -> bool:
    """Returns True if a postcode is valid, False otherwise."""
    pass


def get_postcode_for_location(lat: float, long: float) -> str:
    """Returns the closest postcode to a valid location."""
    pass


def get_postcode_completions(postcode_start: str) -> list[str]:
    """Returns a list of possible postcodes based on a starting string."""
    pass


def get_postcodes_details(postcodes: list[str]) -> dict:
    """Returns a dictionary of regions and associated postcodes."""
    pass
