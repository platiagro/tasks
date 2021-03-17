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
    proc = subprocess.Popen(["seldon-core-microservice", interface_name, api_type])

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
    dict or str or bytes

    Raises
    ------
    AssertionError
        When the returned response status code isn't 200 OK.
    """
    response = requests.post(
        "http://localhost:5000/api/v1.0/predictions",
        json=data,
    )
    print("response.status_code")
    print(response.status_code)
    print("response.content")
    print(response.content)
    assert response.status_code == 200

    body = response.json()
    if "data" in body:
        return body["data"]
    elif "strData" in body:
        return body["strData"]
    elif "binData" in body:
        return body["binData"]

    return body
