import time


import graphic_dolar as graphic
import infos_dolar as infos

#this value we will use for the interval, you can change it however you want
wait = 3

prices = [3.30, 4.00]
hours = [12, 13.00]

for c in range(0, 3):
	info = infos.info('USD')

	prices.append(info[0])
	hours.append(info[1])

	time.sleep(wait)


print(prices, hours)
graphic.graphic(prices, hours)

