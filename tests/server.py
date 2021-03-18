import subprocess
import random
import time

import requests


class Server:
    """
    Starts seldon core deployment server.

    Attributes
    ----------
    interface_name : str
    api_type : str
    """

    def __init__(self, interface_name="Model", api_type="REST"):
        self.proc = None
        self.interface_name = interface_name
        self.api_type = api_type
        self.port = random.randint(5000, 9000)

    def __enter__(self):
        """
        Starts seldon core deployment server.

        Parameters
        ----------
        interface_name : str
        api_type : str

        Raises
        ------
        RuntimeError
            When the process that runs the server exits (because of an error).
        """
        self.proc = subprocess.Popen(
            ["seldon-core-microservice", self.interface_name, self.api_type, "--port", str(self.port)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        wait_time = 0
        while True:
            time.sleep(5)
            wait_time += 5
            poll = self.proc.poll()
            if poll is not None:
                # p.subprocess is not alive
                raise RuntimeError(f"deployment exited with status: {self.proc.returncode}")

            # Checks whether the server is healthy and running
            response = requests.get(f"http://localhost:{self.port}/health/ping")
            if response.status_code == 200:
                break

            if wait_time > 300:
                # p.subprocess took too long to be healthy (> 5 minutes)
                print(self.proc.stderr.read().decode(), flush=True)
                self.proc.kill()
                raise RuntimeError(f"deployment took too long to be ready")

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.proc.kill()

    def test(self, data):
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
            f"http://localhost:{self.port}/api/v1.0/predictions",
            json=data,
        )

        if response.status_code != 200:
            print(self.proc.stderr.read().decode(), flush=True)

        body = response.json()
        if "data" in body:
            return body["data"]
        elif "strData" in body:
            return body["strData"]
        elif "binData" in body:
            return body["binData"]

        return body
