class Student:
	def __init__(self,first_name,second_name,age):
		self.first_name=first_name
		self.second_name=second_name
		self.age=age
		

	def full_name(self):
		name=self.first_name + self.second_name
		return name

	def year_of_birth(self):
		return 2019-self.age

	def greeting(self):
		return "Hello {} you were born {}".format(self.first_name,2019-self.age)
	
	def initials(self):
		initial=self.first_name+self.second_name
		return initial
			