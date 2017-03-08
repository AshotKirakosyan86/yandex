from selenium.webdriver.common.by import By 


class TryYandexLocators:
	# locators for search func
	search_field = {'by':By.CLASS_NAME,'value':'input__control'}
	# locators for filling_checkboxes func
	age_field = {'by':By.NAME,'value':'ps_age'}
	geo_field = {'by':By.NAME,'value':'ps_geo'}
	education_field = {'by':By.NAME,'value':'ps_edu'}
	job_field = {'by':By.NAME,'value':'ps_job'}
	# locators for clicking_socials func
	odno = {'by':By.XPATH,'value':"//input[@name='ps_network' and @value='5']"}
	vkontakte = {'by':By.XPATH,'value':"//input[@name='ps_network' and @value='4']"}
	facebook = {'by':By.XPATH,'value':"//input[@name='ps_network' and @value='2']"}
	# locators for more func
	more_button = {'by':By.CLASS_NAME,'value':'select_side_right'}
	more_items = {'by':By.CLASS_NAME,'value':'select__item'}
	# locators for new page funcs
	new_page = {'by':By.XPATH,'value':'//a[contains(text(), "дальше")]'}
	no_result = {'by':By.CLASS_NAME,'value':'misspell__message'}
	# locators for clear_all_fields func
	clear_button  = {'by':By.XPATH,'value':'//span[contains(text(), "Очистить")]'}
	# locators for new_info func
	get_people = {'by':By.CLASS_NAME,'value':'people'}
	get_name = {'by':By.CLASS_NAME,'value':'serp-item__title'}
	get_link = {'by':By.CLASS_NAME,'value':'link'}
	get_location = {'by':By.CLASS_NAME,'value':'people__birth'}
	get_row = {'by':By.CLASS_NAME,'value':'data-row'}
	# locators for making_list func
	content = {'key':'serp-item','val1':'preview','val2':'ppl','val3':'content'}
	get_full = {'tag':'td','by':'class','value':'full-info__cell full-info__cell_type_description'}




