import requests
import webbrowser
endpoint = "https://api.nasa.gov/planetary/apod"
api_key = "5sjIPiQHxVEc5vyGCvXI3hdQFOHndbwi2h956s5A"
query_params = {"api_key": api_key}
response = requests.get(endpoint, params= query_params)
response.text
print(response.text)
picture = response.json()
#url = picture["hdurl"]
text = open("NASA_text.txt", "w")
text.write(picture["explanation"])
text.close()
#webbrowser.open(url, new=2, autoraise=True)
# https://realpython.com/python-api/