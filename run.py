import requests
import time
import os
import re

token = os.getenv('TOKEN')  # authorization
url = "https://discord.com/api/v9/channels/1279755843830677518/messages"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"{token}"
}

nonce_file = 'nonce.txt'
if os.path.exists(nonce_file):
    with open(nonce_file, 'r') as file:
        nonce = file.read().strip()
else:
    nonce = "1289965169659426784"  # change middle number +1 every time
    with open(nonce_file, 'w') as file:
        file.write(nonce)

for _ in range(324):  # Loop exactly 324 times
    match = re.search(r"(.*?)(\d{6})(\d{4})", nonce)
    if match:
        prefix = match.group(1)
        middle = match.group(2)
        suffix = match.group(3)
        new_middle = str(int(middle) + 1).zfill(6)  # Increase by 1 and keep 6 digits
        nonce = f"{prefix}{new_middle}{suffix}"

        data = {
            "mobile_network_type": "wifi",
            "content": "AIf le",
            "nonce": nonce,
            "tts": False,
            "flags": 0
        }

        response = requests.post(url, headers=headers, json=data)
        print(response.status_code)
        print(response.json())
        print(nonce)

        with open(nonce_file, 'w') as file:
            file.write(nonce)
    else:
        print("error")
        break

    time.sleep(61)
