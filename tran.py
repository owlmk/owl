import urllib.request
import urllib.parse
import hashlib
import time
import random
import sys

request = urllib.request
tra = sys.argv[1:]
tra = ' '.join(tra)
u = 'fanyideskweb'
d = tra
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'

sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
date = {'from' : 'AUTO' , 'to': 'AUTO', 'i': tra , 'client': 'fanyideskweb', 'doctype' : 'json'  , 'Version' : '2.1' , 'keyfrom' :'fanyi.web', 'action' :'FY_BY_CLICKBUTTON' , 'typoResult' :'true', 'sign': sign, 'salt': f }
date = urllib.parse.urlencode(date).encode('utf-8')
response = request.urlopen(url , date  )
result = response.read().decode('utf-8')
result = eval(result)
print ('\n' , result['translateResult'][0][0]['tgt'] , end = '\n')
try :
	print (result['smartResult']['entries'][1])
except KeyError :
	pass 
with open("./单词.txt", 'a') as f:
	f.write('\n' + tra + '\t' + result['translateResult'][0][0]['tgt'] + '\t')
	try :
		f.write(result['smartResult']['entries'][1])
	except:
		pass
	
	
