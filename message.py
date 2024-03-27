import requests
import json

url = "https://graph.facebook.com/v18.0/269133159612855/messages"

header = {
    "Authorization": "Bearer EAANGdidOBeEBO7aCQijINI4pPPLcuiOHI6FocP4ZBxSpSBSazelVMW0M3pUZCOem7BUHOqdEEhk6d6FRYzedBOHztKZBzye4uBPGekquxiAbVX1lqBSyZAlVAr2P8Ff77bJFCTClZCUVb0lZAUIqexlMUvOFyIYy3rirqxYZCJHV9m00LEpWbBduIMPXgyZBFlHeCELwZBZBZCfuJLX3BrXVbrPcQzZAN8nZA72FMyPY4aU5skI8ZD",
    "Content-Type": "application/json"
}

body = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "919100153671",
    "type": "image",
    "image":{
        "link":"https://i.imgur.com/GpEHUxM.jpeg"
    }
}

res = requests.post(url, headers=header,data=json.dumps(body))

print(res)
print(res.json())