import subprocess
import time

import requests


def run(interface_name="Model", api_type="REST"):
    """
    Starts seldon core deployment server.

    Parameters
    ----------
    interface_name : str
    api_type : str

    Returns
    -------
    subprocess.Popen

    Raises
    ------
    RuntimeError
        When the process that runs the server exits (because of an error).
    """
    proc = subprocess.Popen(
        f"seldon-core-microservice {interface_name} {api_type}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    while True:
        time.sleep(5)
        poll = proc.poll()
        if poll is not None:
            # p.subprocess is not alive
            raise RuntimeError(f"deployment exited with status: {proc.returncode}")

        # Checks whether the server is healthy and running
        response = requests.get("http://localhost:5000/health/ping")
        if response.status_code == 200:
            break

    return proc


def test(data):
    """
    Sends a test request to seldon core deployment server.

    Parameters
    ----------
    data : dict

    Returns
    -------
    dict or str or bytes or None
    """
    response = requests.post(
        "http://localhost:5000/api/v1.0/predictions",
        json=data,
    )

    if response.status_code != 200:
        return None

    body = response.json()
    if "data" in body:
        return body["data"]
    elif "strData" in body:
        return body["strData"]
    elif "binData" in body:
        return body["binData"]

    return body
