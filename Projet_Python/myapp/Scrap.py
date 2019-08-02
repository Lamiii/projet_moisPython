from requests import get
from bs4 import BeautifulSoup

def scrapDirect():
	url = 'https://www.matchendirect.fr/live-score/'
	img_url = 'https://www.matchendirect.fr'
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')

	table = html_soup.find('div', attrs = {'id':'livescore'}) 
	compt = 0

	mydata = []
	matchs = []
    

	for row in table.findAll('div', attrs = {'class':'panel panel-info'}): 
        
        
		a_desc = row.find('h3', attrs = {'class':'panel-title'}).get_text() 
		matchs_ctg = {}

		for pi_b in row.findAll('div', class_ = 'panel-body'):
			grp = []

			for el in row.findAll('tr'):
				resultat = {}
                
				heure = el.find('td', attrs = {'class':'lm1'}).get_text() 
				time = el.find('td', attrs = {'class':'lm2 lm2_1'}).get_text()
				eqA = el.find('span', attrs = {'class':'lm3_eq1'}).get_text()
				eqB = el.find('span', attrs = {'class':'lm3_eq2'}).get_text()

				imA = el.find('span', attrs={'class': 'lm3_eq1'}).img
				imgA = imA.get('data-src')

				imB = el.find('span', attrs={'class': 'lm3_eq2'}).img
				imgC = imB.get('data-src')

				try:
					img_ep1 = img_url+imgA
				except:
					img_ep1 = 'http://www.nan.ci/img/logo-nan.png'

				print("img1")
				print(img_ep1)

				try:
					img_ep2 = img_url+imgC
				except:
					img_ep2 = 'http://www.nan.ci/img/logo-nan.png'

				print("img2")
				print(img_ep2)

				scors =  el.find('span', attrs = {'class':'lm3_score'}).get_text()

				resultat['heure'] = heure
				resultat['time'] = time
				resultat['eqa'] = eqA
				resultat['eqb'] = eqB
				resultat['scors'] = scors
				resultat['img1'] = img_ep1
				resultat['img2'] = img_ep2

				grp.append(resultat)
                
		matchs_ctg['ctgo'] = a_desc
		matchs_ctg['match'] = grp
		mydata.append(matchs_ctg)

	data = mydata
	return data

def scrapUrl():
	
	href = {}
	url = 'https://www.matchendirect.fr/'
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')

	table = html_soup.find('ul', attrs = {'id':'sous_menu_sport'}) 

	lien = table.findAll('li')
	lien_hier = lien[0].a.get('href')
	lien_demain = lien[2].a.get('href')
	href['hier'] = lien_hier
	href['demain'] = lien_demain
	return href

def scrapFootHier(lien):

	today = 'https://www.matchendirect.fr/'
	url = today + lien
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')

	table = html_soup.find('div', attrs = {'id':'livescore'}) 
	compt = 0

	mydata = []
	matchs = []
    

	for row in table.findAll('div', attrs = {'class':'panel panel-info'}): 
        
        
		a_desc = row.find('h3', attrs = {'class':'panel-title'}).get_text() 
		matchs_ctg = {}

		for pi_b in row.findAll('div', class_ = 'panel-body'):
			grp = []

			for el in row.findAll('tr'):
				resultat = {}
                
				heure = el.find('td', attrs = {'class':'lm1'}).get_text() 
				time = el.find('td', attrs = {'class':'lm2'}).get_text()
				eqA = el.find('span', attrs = {'class':'lm3_eq1'}).get_text()
				eqB =  el.find('span', attrs = {'class':'lm3_eq2'}).get_text()

				scors =  el.find('span', attrs = {'class':'lm3_score'}).get_text()

				resultat['heure'] = heure
				resultat['time'] = time
				resultat['eqa'] = eqA
				resultat['eqb'] = eqB
				resultat['scors'] = scors

				grp.append(resultat)
                
		matchs_ctg['ctgo'] = a_desc
		matchs_ctg['match'] = grp
		mydata.append(matchs_ctg)

	data = mydata
	return data

def scrapFootDemain(lien):

	today = 'https://www.matchendirect.fr/'
	url = today + lien
	response = get(url)
	img_url = 'https://www.matchendirect.fr'
	html_soup = BeautifulSoup(response.text, 'html.parser')

	table = html_soup.find('div', attrs = {'id':'livescore'}) 
	compt = 0

	mydata = []
	matchs = []
    

	for row in table.findAll('div', attrs = {'class':'panel panel-info'}): 
        
        
		a_desc = row.find('h3', attrs = {'class':'panel-title'}).get_text() 
		matchs_ctg = {}

		for pi_b in row.findAll('div', class_ = 'panel-body'):
			grp = []

			for el in row.findAll('tr'):
				resultat = {}
                
				heure = el.find('td', attrs = {'class':'lm1'}).get_text() 
				time = el.find('td', attrs = {'class':'lm2'}).get_text()
				eqA = el.find('span', attrs = {'class':'lm3_eq1'}).get_text()
				eqB =  el.find('span', attrs = {'class':'lm3_eq2'}).get_text()

				scors =  el.find('span', attrs = {'class':'lm3_score'}).get_text()
				imA = el.find('span', attrs={'class': 'lm3_eq1'}).img
				imgA = imA.get('data-src')

				imB = el.find('span', attrs={'class': 'lm3_eq2'}).img
				imgC = imB.get('data-src')

				try:
					img_ep1 = img_url + imgA
				except:
					img_ep1 = 'http://www.nan.ci/img/logo-nan.png'

				print("img1")
				print(img_ep1)

				try:
					img_ep2 = img_url + imgC
				except:
					img_ep2 = 'http://www.nan.ci/img/logo-nan.png'

				print("img2")
				print(img_ep2)

				scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

				resultat['heure'] = heure
				resultat['time'] = time
				resultat['eqa'] = eqA
				resultat['eqb'] = eqB
				resultat['scors'] = scors
				resultat['img1'] = img_ep1
				resultat['img2'] = img_ep2

				grp.append(resultat)

		matchs_ctg['ctgo'] = a_desc
		matchs_ctg['match'] = grp
		mydata.append(matchs_ctg)

	data = mydata
	return data



def scrapFoot():
	url = 'https://www.matchendirect.fr/'
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')

	table = html_soup.find('div', attrs={'id': 'livescore'})
	compt = 0

	mydata = []
	matchs = []

	for row in table.findAll('div', attrs={'class': 'panel panel-info'}):

		a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()
		matchs_ctg = {}

		for pi_b in row.findAll('div', class_='panel-body'):
			grp = []

			for el in row.findAll('tr'):
				resultat = {}

				heure = el.find('td', attrs={'class': 'lm1'}).get_text()
				time = el.find('td', attrs={'class': 'lm2'}).get_text()
				eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
				eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()

				scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

				resultat['heure'] = heure
				resultat['time'] = time
				resultat['eqa'] = eqA
				resultat['eqb'] = eqB
				resultat['scors'] = scors

				grp.append(resultat)

		matchs_ctg['ctgo'] = a_desc
		matchs_ctg['match'] = grp
		mydata.append(matchs_ctg)

	data = mydata
	return data