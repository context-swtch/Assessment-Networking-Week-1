"""A CLI application for interacting with the Postcode API."""

from argparse import ArgumentParser
from postcode_functions import validate_postcode, get_postcode_completions


def main(arguments: ArgumentParser) -> None:
    """The main entry point of the program."""
    if arguments.mode == 'validate':
        # Attempt to validate tje postcode
        if validate_postcode(arguments.postcode):
            print(f"{arguments.postcode} is a valid postcode.")
        else:
            print(f"{arguments.postcode} is not a valid postcode.")
        return
    if arguments.mode == 'complete':
        # attempt to complete the postcode
        postcodes = get_postcode_completions(arguments.postcode)
        if postcodes is not None:
            for i in range(5):
                print(postcodes[i])
        else:
            print(f'No matches for {arguments.postcode}.')
        return


def parse_args() -> ArgumentParser:
    """Parse command line arguments."""
    parser = ArgumentParser(
        description="Postcode API CLI Tool.")
    parser.add_argument(
        "--mode", "-m", type=str, choices=['validate', 'complete'], required=True,
        help="Attempt to validate/complete postcode.")

    parser.add_argument(
        "postcode", type=str,
        help="Postcode argument that accepts a string.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    args.postcode = args.postcode.upper().strip()
    main(args)
