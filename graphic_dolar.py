import matplotlib.pyplot as plt


#change the parameters according to your will
def graphic(prices, hours, title='Preco dolar', Xlabel='horas', Ylabel='Preco'):
	plt.title(title)
	plt.xlabel(Xlabel)
	plt.ylabel(Ylabel)


	plt.plot(hours, prices)
	plt.show()

#prices = [1, 3]
#hours = [10.0, 11.99]
#graphic(prices, hours)