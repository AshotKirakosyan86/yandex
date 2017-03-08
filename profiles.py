class Profile:
	
	
	def __init__(self,name='',age='',location='',job='',education='',social_networks=[],detailed_networks=['LinkedIn']):
		self.name = name
		self.age = age
		self.location = location
		self.job = job
		self.education = education
		self.social_networks = social_networks
		self.detailed_networks = detailed_networks

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_location(self):
		return self.location

	def get_job(self):
		return self.job

	def get_education(self):
		return self.education

	def get_social_networks(self):
		return self.social_networks

	def get_detailed_networks(self):
		return self.detailed_networks






