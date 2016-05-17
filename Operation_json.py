import json
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
# encodedjson = json.dumps(obj)
# print repr(obj)
# print encodedjson

d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2,sort_keys=True,indent=4)
d3 = json.dumps(data2,sort_keys=True)
print d1