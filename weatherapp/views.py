from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e499bd403012004e26f5132e6cb59c66'
        res = urllib.request.urlopen(url).read()
        json_data=json.loads(res)
        data={
            "countrycode":str(json_data['sys']['country']),
            "coordinates":str("{:.2f}".format(json_data['coord']['lon']))+', '+ str("{:.2f}".format(json_data['coord']['lat'])),
            "temp":str("{:.2f}".format(json_data['main']['temp']-273.15))+'°C',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            "city":city
        }

    else:
        city=''
        data={}
    return render(request, 'index.html',data)
