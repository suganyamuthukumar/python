
import memcache
import json

def getCachedData():
    memcache_client= memcache.Client(['vmwahcres16-stg.corp.netapp.com:11211'])
    x = '{ "name":"John", "age":35, "city":"New York"}'
   # memcache_client.set("user3",x)
    print(json.loads(memcache_client.get('user1')))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # print(encryptData())
    getCachedData()
