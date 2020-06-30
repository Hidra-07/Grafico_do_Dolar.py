import requests

#if you want to change the currency just put the acronym of it example USD, BTC ...
def info(usd):
	#acronyms must always be capitalized
	dolar_format = usd.upper()

	url = f'https://economia.awesomeapi.com.br/all/{dolar_format}'
	r = requests.get(url)

	print(f'[+] Request status code: {r.status_code} [+]')

	infos = r.json()
	price = infos[dolar_format]['high']
	hours = infos[dolar_format]['create_date']

	return [price, hours]

#dolar_info = info('USD')
#print(dolar_info)

