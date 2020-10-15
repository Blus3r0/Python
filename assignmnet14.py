import urllib.request, urllib.parse, urllib.error
import json
import ssl
#Este programa conecta a una api proporcionada por el curso de Python de la plataforma Coursera, en caso que
#no se posea una api key de google maps, luego retorna las coordernadas de la localidad que ud ingrese
#Escrito por Carlos Correa, para el curso de Python de la plataforma Coursera

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving... ', url)
    uh = urllib.request.urlopen(url, context= ctx)
    data = uh.read().decode()
    print('Retrieved: ', len(data),' caracters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js ['status'] != 'OK':
        print('Failure to retrieve')
        print(data)
        continue
    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lat"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    place_id = js['results'][0]['place_id']
    print(location)
    print(place_id)