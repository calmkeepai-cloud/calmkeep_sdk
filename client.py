import requests
import time


class CalmkeepError(Exception):
    pass


class CalmkeepClient:

    def __init__(
        self,
        calmkeep_key: str,
        claude_key: str,
        base_url: str = "https://diargallop--calmkeep-service-calmkeep-service.modal.run/",
        timeout: int = 120,
        max_retries: int = 3
    ):

        if not calmkeep_key:
            raise CalmkeepError("Missing Calmkeep API key")

        if not claude_key:
            raise CalmkeepError("Missing Claude API key")

        self.calmkeep_key = calmkeep_key
        self.claude_key = claude_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

    def complete(self, prompt: str, **params):

        if not prompt:
            raise CalmkeepError("Prompt cannot be empty")

        payload = {
            "prompt": prompt,
            "params": params
        }

        headers = {
            "calmkeep_key": self.calmkeep_key,
            "anthropic_api_key": self.claude_key
        }

        url = f"{self.base_url}/runtime"

        attempt = 0

        while attempt < self.max_retries:

            try:

                response = requests.post(
                    url,
                    headers=headers,
                    json=payload,
                    timeout=self.timeout
                )

                if response.status_code != 200:
                    raise CalmkeepError(
                        f"Calmkeep API error {response.status_code}: {response.text}"
                    )

                data = response.json()

                if not data.get("ok"):
                    raise CalmkeepError(data)

                return data["result"]["text"]

            except requests.exceptions.RequestException as e:

                attempt += 1

                if attempt >= self.max_retries:
                    raise CalmkeepError(
                        f"Failed after {self.max_retries} attempts: {str(e)}"
                    )

                time.sleep(1.5 * attempt)

    def stream(self, prompt: str, **params):

        payload = {
            "prompt": prompt,
            "params": params
        }

        headers = {
            "calmkeep_key": self.calmkeep_key,
            "anthropic_api_key": self.claude_key
        }

        url = f"{self.base_url}/runtime"

        try:

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                stream=True,
                timeout=self.timeout
            )

            if response.status_code != 200:
                raise CalmkeepError(
                    f"Calmkeep API error {response.status_code}: {response.text}"
                )

            for line in response.iter_lines():

                if not line:
                    continue

                yield line.decode("utf-8")

        except requests.exceptions.RequestException as e:

            raise CalmkeepError(str(e))

    def __call__(self, prompt: str, **params):
        return self.complete(prompt, **params)