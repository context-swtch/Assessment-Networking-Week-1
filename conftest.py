"""Fixtures used by multiple tests."""

# pylint: skip-file

import subprocess

import shlex

import pytest


@pytest.fixture()
def run_shell_command():
    """Runs a command in the shell, returning any standard output and error messages."""

    def func(command):
        
        result = subprocess.run(shlex.split(command), capture_output=True)
        return result.stdout.decode("UTF-8"), result.stderr.decode("UTF-8")

    return func