from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import json
from TryYandexLocators import TryYandexLocators as loc
from profiles import Profile
from resultprofiles import ProfileResult
from bs4 import BeautifulSoup 
import sys


class YandexScraper:

	URL = 'https://yandex.ru/people'
	
	def wait(self,how,what,lst=False):
		if not lst:
			return WebDriverWait(self.driver,5).until(lambda driver:driver.find_element(how,what))
		if lst:
			return WebDriverWait(self.driver,5).until(lambda driver:driver.find_elements(how,what))

	def set_up(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get(self.URL)
		try:
			assert 'Яндекс' in self.driver.title
		except AssertionError:
			self.driver.quit()
	
	def filling_checkboxes(self,prof):
		age = self.wait(loc.age_field['by'],loc.age_field['value'])
		age.send_keys(prof.get_age())
		geo = self.wait(loc.geo_field['by'],loc.geo_field['value'])
		geo.send_keys(prof.get_location())
		education = self.wait(loc.education_field['by'],loc.education_field['value'])
		education.send_keys(prof.get_education())
		job = self.wait(loc.job_field['by'],loc.job_field['value'])
		job.send_keys(prof.get_job())
		

	def clicking_socials(self,prof):
		OK = self.wait(loc.odno['by'],loc.odno['value'])
		VK = self.wait(loc.vkontakte['by'],loc.vkontakte['value'])
		fb = self.wait(loc.facebook['by'],loc.facebook['value'])
		social_dict =  {'OK':OK,'VK':VK,'FB':fb}
		for item in social_dict:
			if item in prof.get_social_networks():
				social_dict.get(item).click()
	
	def click_more(self,prof):
		click_for_more =self.wait(loc.more_button['by'],loc.more_button['value']).click()
		choose_items = self.wait(loc.more_items['by'],loc.more_items['value'],True)		
		for item in choose_items:
			if item.text in prof.get_detailed_networks():
				self.driver.execute_script("window.scrollTo(611, 142)")
				item.click()
	

	def search(self,prof):
		search_box = self.wait(loc.search_field['by'],loc.search_field['value'])
		search_box.send_keys(prof.get_name())
		search_box.send_keys(Keys.ENTER)
	
	def making_info(self,data_bem):
		make_dict = json.loads(data_bem)
		get_content  = make_dict.get(loc.content['key'])[loc.content['val1']][loc.content['val2']][loc.content['val3']]
		soup = BeautifulSoup(get_content, "html.parser")
		job_and_univer = soup.find_all(loc.get_full['tag'],attrs={loc.get_full['by']:loc.get_full['value']})
		full_job = job_and_univer[0].get_text()
		full_univer = job_and_univer[1].get_text()
		return full_job,full_univer
			
	def get_info(self):
		self.driver.refresh() 
		info = self.wait(loc.get_people['by'],loc.get_people['value'],True)
		results = []
		for item in info:
			resultprofiles = ProfileResult()
			try:				
				name = item.find_element(loc.get_name['by'],loc.get_name['value']).text
				resultprofiles.set_name(name)
				link = item.find_element(loc.get_link['by'],loc.get_link['value']).get_attribute('href')
				resultprofiles.set_link(link)
				location = item.find_element(loc.get_location['by'],loc.get_location['value']).text
				resultprofiles.set_location(location)
				if 'Подробно' not in item.text:
					job = item.find_elements(loc.get_row['by'],loc.get_row['value'])[0].text
					resultprofiles.set_job(job)
					univer = item.find_elements(loc.get_row['by'],loc.get_row['value'])[1].text
					resultprofiles.set_univer(univer)
				else:
					html = item.get_attribute('data-bem')
					full_job, full_univer = self.making_info(html)
					resultprofiles.set_job(full_job)
					resultprofiles.set_univer(full_univer)	
			except (TimeoutException,NoSuchElementException,IndexError):
				pass

			results.append(resultprofiles)
		return results	
	
	def is_new_page_displayed(self):
		return self.wait(loc.new_page['by'],loc.new_page['value']).is_displayed()

	def new_page(self):
		page = self.wait(loc.new_page['by'],loc.new_page['value']).click()
		
		
	def tear_down(self):
		self.driver.quit()
		

	def clear_all_fields(self):
		search_box = self.wait(loc.search_field['by'],loc.search_field['value']).clear()		
		self.driver.execute_script("window.scrollTo(651, 16)")
		all_boxes = self.wait(loc.clear_button['by'],loc.clear_button['value']).click()


def read_input(file):
	try:
		with open(file) as f:
			data = json.load(f)
			profiles = [Profile(**profile) for profile in data["profiles"]]
		return profiles
	except ValueError:
		sys.exit('Json decode error! Please check file format')
	except FileNotFoundError:
		sys.exit('File not found! Please enter correct file path')	

def write_to_file(file,content):
	with open(file,'w+') as f:
		f.write(content)

try:
	file_path = sys.argv[1]
except IndexError:
	sys.exit('please enter file path')

members = read_input(file_path)		
y = YandexScraper()
y.set_up()

all_results = []

for member in members:
	y.click_more(member)
	y.clicking_socials(member)
	y.filling_checkboxes(member)
	y.search(member)
	try:
		while y.is_new_page_displayed():
			all_results.extend(y.get_info())
			y.new_page()
	except TimeoutException:
		pass
	y.clear_all_fields()
results_json = json.dumps([person.dumping() for person in all_results],ensure_ascii=False)
print(results_json)

#write_to_file(file_path+"results.txt", results_json)
y.tear_down()
