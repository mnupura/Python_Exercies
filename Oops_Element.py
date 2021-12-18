class Element():
	def __init__(self,name,symbol,number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number

	def dump(self):
		print('Values: '+ self.__name + ', ' + self.__symbol + ', '+ str(self.__number))

	def __str__(self):
		return ('String Values: '+ self.__name + ', ' + self.__symbol + ', '+ str(self.__number))

	def get_name(self):
		return self.__name

	def get_symbol(self):
		return self.__symbol

	def get_number(self):
		return (str(self.__number))
 
hydrogen = Element('Hydrogen','H',1)
#hydrogen.dump()

# Using dictionary
dict_hydro = {'name':'Hydrogen',
				'symbol': 'H',
				'number': 1}
hydrogen_dict = Element(**dict_hydro)	#named tupple
#hydrogen_dict.dump()

# Using __str__ method
hydrogen_str = Element('Nitrogen','N',2)
print(hydrogen_str)

# Using getter methods
print('Get Name: '+hydrogen_str.get_name())
print('Get Symbol: '+hydrogen_str.get_symbol())
print('Get Number: '+hydrogen_str.get_number())


