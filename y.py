import requests
import json
from  geopy.geocoders import Nominatim
sam=input('Enter a city or country: ')
cam=sam.lower()
geolocator = Nominatim()
city =cam
country =cam
loc = geolocator.geocode(city+','+ country)
sal=str(loc.latitude)
que=str(loc.longitude)
key="2994bd671f8d0d8201dca167570b8393"
response=requests.get(' https://api.darksky.net/forecast/'+key+'/'+sal+','+que)
data=response.json()
result1=(data['currently']['temperature'])
result2=(data['currently']['summary'])
resultmain=(result1-32)*5/9
print('latitude: '+ str(sal), 'longitude: '+str(que))
print('Summary: ' +result2)
print('It is currently '+str(result1)+'F '+'/'+str(resultmain)+'C')
wam=input('Do you want advanced information[Y/N]')
wam1=wam.upper()
if wam1=='Y':
    print('Showing additional information')
    for i in data['currently']:
        print(i +'=',data['currently'][i])
else:
    print('Understanable. Have a nice Day!')