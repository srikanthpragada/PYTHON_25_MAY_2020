import requests


resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code == 200:
    details = resp.json()  # convert json to dict
    print(details['name'])
    print(details['location'])
    print(details['followers'])
else:
    print("Sorry! Could not get details of user!")
