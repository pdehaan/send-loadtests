import molotov
import json
import os


url = os.environ['URL_SERVER'] + '/upload'
_AAD = 'ff00'
_ID = '123456789012345678901234'
_FILENAME = 'loadtest.py'
_METADATA_CACHE = {}


def get_file_metadata(aad=_AAD, _id=_ID, filename=_FILENAME):
    if filename in _METADATA_CACHE:
        return _METADATA_CACHE[filename]
    metadata = {}
    metadata['aad'] = aad
    metadata['id'] = _id
    metadata['filename'] = filename
    res = _METADATA_CACHE[filename] = json.dumps(metadata)
    return res


@molotov.scenario()
async def upload_file(session):
    headers = {'X-File-Metadata': get_file_metadata()}

    with open(_FILENAME, 'rb') as file:
        files = {'file': file}

        async with session.post(url, data=files, headers=headers) as response:
            res = await response.json()
            # Confirm the response contains the expected keys.
            if not {'delete', 'id', 'url'} <= set(res):
                raise ValueError("Missing `delete`, `id`, or `url` token in response")
