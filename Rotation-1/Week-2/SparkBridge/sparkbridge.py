from flask import Flask
import requests
import json
import time
import ConfigParser

app = Flask(__name__)
url = ""
data = {}
header = {}

@app.route("/")
def spark_VM_approval():
   r = requests.post(url=url, json=data, headers=header)
   print r.text
   
   wait_for_reponse = True
   print "Polling Spark"
   while(wait_for_reponse):
      resp = requests.get(url=url, params=data, headers=header)
   
      ds = json.loads(resp.text)
   
      first = ds['items'][0]['text'].lower()
      second = ds['items'][1]['text'].lower()

      # Look at the last two entries to determine yes/no response
      if first != u'allow vm creation?':
         if first == u'yes' and second == u'allow vm creation?':
            return 'ok'
         else:
            return 'error'

      time.sleep(2)
	  
if __name__ == "__main__":
   config = ConfigParser.RawConfigParser()
   config.read('sparkroom.cfg')
   url = config.get('SparkRoom', 'URL')
   room_id = config.get('SparkRoom', 'roomId')
   auth_token = config.get('SparkRoom', 'authToken')
   data = {"roomId": room_id, "text":"Allow VM Creation?"}
   header = {"Authorization": auth_token, "Content-Type": "application/json"}
   app.run(host='0.0.0.0',debug=True)


