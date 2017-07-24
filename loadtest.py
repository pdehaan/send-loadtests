import json
import os
import requests

url = os.environ['URL_SERVER'] + '/upload'


def upload_file(url, filename, aad='ff00', id='123456789012345678901234'):
    with open(filename, 'rb') as file:
        # Build JSON payload for X-File-Metadata header.
        metadata = {}
        metadata['aad'] = aad
        metadata['id'] = id
        metadata['filename'] = filename

        files = {'file': (filename, file)}
        headers = {'X-File-Metadata': json.dumps(metadata)}

        # POST the payload to the API server.
        res = requests.post(url, files=files, headers=headers)
        # Parse response into JSON object.
        data = json.loads(res.text)

        # Confirm the response contains the expected keys.
        if not {'delete', 'id', 'url'} <= set(data):
            raise ValueError("Missing `delete`, `id`, or `url` token in response")
        else:
            print(res.text)
            pass


upload_file(url, 'loadtest.py')
