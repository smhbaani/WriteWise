import requests


class Paraphraser:

    def __init__(self, api_key):

        self.api_key = api_key

        self.api_url = (
            "https://api-inference.huggingface.co/models/"
            "humarin/chatgpt_paraphraser_on_T5_base"
        )

    def paraphrase(self, text):

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "inputs": text
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

                    if "generated_text" in result[0]:

                        return result[0]["generated_text"]

            return "Unable to generate paraphrased text."

        except Exception as e:

            return f"Error: {str(e)}"