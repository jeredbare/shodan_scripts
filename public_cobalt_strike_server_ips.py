import requests

def results():
    api_key = "[your_api_key]"
    url = "https://api.shodan.io/shodan/host/search?key={}&query=product&facets=cobalt strike team server".format(api_key)


    response = requests.request("GET", url)

    json = response.json()
    json = json['matches']

    for i in json:
        # putting ips in a list
        ips = i['ip_str']
        print(str(ips))

results()

            

