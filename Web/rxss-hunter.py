# Author : Emre Aslan
# Twitter: twitter.com/aslanewre  
# Github : github.com/aslanemre

import requests

print("""
<<<<<<<<<<<<<>>>>>>>>>>>>
      RXSS TESTER
<<<<<<<<<<<<<>>>>>>>>>>>>
""")

# if you want set the header add header datas this variable.
target = input("[ ? ] Set a site for rxss testing : ")
print("")
header = ""
payloads=open("payloads.txt","r")
for payload in payloads.readlines():
    # enter the site like this : http(s)://xxx.site.xxx/path/page?parameter=
    target_with_payload = target+str(payload)
    testing = requests.get(url=target_with_payload, headers=header)
    if str(payload) in str(testing.text):
        print("[ + ] Possible XSS Found : ",str(payload))
    else:
        print("[ ! ] Nothing Found :( ")
