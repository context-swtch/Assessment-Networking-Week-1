"""Functions that interact with the Postcode API."""
import requests as req

POSTCODE_API_URL = 'https://api.postcodes.io/'


def handle_response(res: req.Response) -> dict:
    """Handles the response, checks the status code, and raises appropriate errors."""
    # Check for successful response
    if res.status_code >= 200 and res.status_code < 300:
        try:
            return res.json()
        except ValueError as exc:
            raise req.RequestException("Invalid JSON response.") from exc

    # Handle various error scenarios
    if res.status_code == 404:
        raise req.RequestException(f"Resource not found: {res.url}")
    if 400 <= res.status_code < 500:
        raise req.RequestException(f"Client error occurred: {res.text}")
    if res.status_code == 500:
        raise req.RequestException(
            "Server error occurred. Unable to access API.")

    return {}


def validate_postcode(postcode: str) -> bool:
    """Returns True if a postcode is valid, False otherwise."""
    if not isinstance(postcode, str):
        raise TypeError("Function expects a string.")

    url = f"{POSTCODE_API_URL}postcodes/{postcode}/validate"

    res = req.get(url, timeout=10)

    response = handle_response(res)
    return response['result']


def get_postcode_for_location(lat: float, long: float) -> str:
    """Returns the closest postcode to a valid location."""
    if not isinstance(lat, float):
        raise TypeError("Function expects two floats.")
    if not isinstance(long, float):
        raise TypeError("Function expects two floats.")

    url = f"{POSTCODE_API_URL}postcodes?lon={long}&lat={lat}"

    res = req.get(url, timeout=10)

    response = handle_response(res)

    if response['result'] is None:
        raise ValueError("No relevant postcode found.")

    return response['result']


def get_postcode_completions(postcode_start: str) -> list[str]:
    """Returns a list of possible postcodes based on a starting string."""
    if not isinstance(postcode_start, str):
        raise TypeError("Function expects a string.")

    url = f"{POSTCODE_API_URL}postcodes/{postcode_start}/autocomplete"

    res = req.get(url, timeout=10)

    response = handle_response(res)

    if response['result'] is None:
        return None
        # raise ValueError("No relevant postcode found.")

    return response['result']


def get_postcodes_details(postcodes: list[str]) -> dict:
    """Returns a dictionary of regions and associated postcodes."""
    if not isinstance(postcodes, list):
        raise TypeError("Function expects a list of strings.")

    if not all(isinstance(postcode, str) for postcode in postcodes):
        raise TypeError("Function expects a list of strings.")

    postcode_struct = {"postcodes": postcodes}
    url = f"{POSTCODE_API_URL}postcodes"
    res = req.post(url, json=postcode_struct, timeout=10)
    response = handle_response(res)

    return response
