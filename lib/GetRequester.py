import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self, url='https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'):
        response = requests.get(url)
        return response.content

    def load_json(self):
        resp_list = []
        json_resps = json.loads(self.get_response_body())
        for json_resp in json_resps:
            resp_list.append(json_resp)

        return resp_list