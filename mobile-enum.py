import requests 
import sys

lable = sys.argv[1]
value = sys.argv[2

if lable = 'ph':
  print('phone')
  
  req = requests.get("http://example.com/getnum="+value+" ")
  print(red.content)
  
else:
  print('error occured')
