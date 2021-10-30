from selenium import webdriver
from selenium.common.exceptions import TimeoutException , NoSuchElementException , ElementNotInteractableException
import pandas as pd 
import os
import time
from time import sleep

browser = webdriver.Chrome(executable_path = "C:/Users/admin/AppData/Local/Programs/Python/Python38-32/Scripts/programs/chromedriver.exe")

#start_time = time.perf_counter()

browser.implicitly_wait(5)
browser.maximize_window()


url = [
	'https://in.tradingview.com/markets/stocks-india/market-movers-large-cap/' , 
	# 'https://in.tradingview.com/markets/stocks-india/market-movers-gainers/' ,
	# 'https://in.tradingview.com/markets/stocks-india/market-movers-losers/'
	]

for URL in url:
	browser.get(URL)

	#STEP 1 - GETTING THE FILE BASE NAME

	file_name = URL.split('/')[-2]
	#print(file_name)
	print(f'Scraping {URL} ...')

	#STEP 2- CREATING AN EXCEL WRITER'S OBJECT

	excl_writer = pd.ExcelWriter(file_name + '.xlsx')

	#STEP 3 - ITERATE EACH CATEGORY

	categories = ['Overview' , 'Performance' , 'Valuation' , 'Dividends' , 'Margins' , 'Income Statement' ,
	              'Balance Sheet' , 'Oscillators' , 'Trend-Following']


	for category in categories:

		print(f'Processing the report: {category}')

		try:
			tab = browser.find_element_by_xpath(f'//div[text()="{category}"]')

			try:
				tab.click()
			except ElementNotInteractableException:
				pass

			#DELAYING TO GET THE TABLE LOADED
			sleep(5)

			df = pd.read_html(browser.page_source)[0]
			df.replace('-','', inplace=True)
			df.to_excel(excl_writer,sheet_name=category, index=False)


		except(NoSuchElementException,TimeoutException):
			print(f'Report {category} not found')
			continue

		excl_writer.save()

browser.quit()


