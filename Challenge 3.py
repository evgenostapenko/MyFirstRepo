import requests
import re

url = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
response_data = re.search('<!--\n.*-->', url.text, re.MULTILINE | re.DOTALL).group()


a = []
s = ''

count = 0

for i in response_data:
    a.append(i)

for i in a:
    count += 1
    if i.islower():
        if (a[count - 2].isupper() and a[count - 3].isupper() and a[count - 4].isupper() and not a[count - 5].isupper()):

            if (a[count ].isupper() and a[count +1].isupper() and a[count +2].isupper() and not a[count + 3].isupper() ):
                s += i

print (s)

