class Element():
	def __init__(self,name,symbol,number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number

	def str(self):
		print('Values: '+ self.__name + ', ' + self.__symbol + ', '+ str(self.__number))

	def get_name(self):
		print('Name: '+ self.__name)

	def get_symbol(self):
		print('Symbol: '+ self.__symbol)

	def get_number(self):
		print('Number: '+ str(self.__number))
 
hydrogen = Element('Hydrogen','H',1)
#hydrogen.dump()

dict_hydro = {'name':'Hydrogen',
				'symbol': 'H',
				'number': 1}

hydrogen_dict = Element(**dict_hydro)	#named tupple
#hydrogen_dict.dump()

hydrogen_str = Element('Nitrogen','N',2)
print(hydrogen_str)
hydrogen_str.str()
hydrogen_str.get_name()
hydrogen_str.get_symbol()
hydrogen_str.get_number()


