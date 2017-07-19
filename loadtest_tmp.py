import json
import os
from urllib.parse import urljoin

from molotov import (
    scenario,
    global_setup,
    global_teardown,
    setup,
)


@scenario(100)
async def upload_file(session):
    with open('Dockerfile', 'rb') as file:
        r = requests.post('https://send.stage.mozaws.net/upload', files={'Dockerfile': file})


    res = await utils.create_shot(session)
    assert res.status < 400
