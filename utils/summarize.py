import requests


class Summarizer:

    def __init__(self, api_key):

        self.api_key = api_key

        self.api_url = (
            "https://api-inference.huggingface.co/models/"
            "facebook/bart-large-cnn"
        )

    def summarize(self, text):

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "inputs": text,
            "parameters": {
                "max_length": 130,
                "min_length": 30,
                "do_sample": False
            }
        }

        try:

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            result = response.json()

            if isinstance(result, list):

                if len(result) > 0:

                    if "summary_text" in result[0]:

                        return result[0]["summary_text"]

            return "Unable to generate summary."

        except Exception as e:

            return f"Error: {str(e)}"