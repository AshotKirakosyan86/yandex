


class ProfileResult:
	
	
	def __init__(self,name='',location='',link='',job='',univer=''):
		self.name = name
		self.location = location
		self.link = link
		self.job = job
		self.univer = univer
		
	def set_name(self,name):
		self.name = name

	def set_location(self,location):
		self.location = location

	def set_link(self,link):
		self.link = link		

	def set_job(self,job):
		self.job = job

	def set_univer(self,univer):
		self.univer = univer

	def dumping(self):
		return {'name': self.name,'location': self.location,'link': self.link,'job':self.job,'univer':self.univer}




	