import requests

def dns_query(name):
    headers = {
        "Accept": "application/dns-json",
    }
    params = {
        "name": name,
        "type": "A"
    }

    response = requests.get(f"https://1.1.1.1/dns-query", headers=headers, params=params)

    result = response.json()

    answer = result['Answer']
    first_query_answer = answer[0]
    ip_addr = first_query_answer['data']

    return ip_addr


print(dns_query("fmi.unibuc.ro"))
