import json
from django.shortcuts import render
from .Scrap import *
from requests import get

my_api_key = '6437aa77c1074ce531dc13fafff8fad2c77fdf834177d1e6657dfecc50eccbd8'

def index(request):
    return render(request,'index.html')

def paris(request):
    #res = get('https://allsportsapi.com/api/football/?met=H2H&APIkey&firstTeamId=2616&secondTeamId=2617='+my_api_key)
    ScrapUrl = 'resultat-foot-03-08-2019'
    res = scrapFootDemain(ScrapUrl)
    #tab = scrapDirect()
    return render(request, 'paris.html', {'res': res})

def match(request):
    #jeu = scrapFoot()
    #res = get('https://allsportsapi.com/api/football/?met=H2H&APIkey=6437aa77c1074ce531dc13fafff8fad2c77fdf834177d1e6657dfecc50eccbd8&firstTeamId=2616&secondTeamId=2617')
    #data = json.loads(res.text)
    tab = scrapDirect()
    return render(request, 'match.html', {'res': tab})
