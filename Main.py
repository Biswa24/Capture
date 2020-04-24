from PIL import Image
import os
from os import environ
#print(os.path.dirname(os.path.abspath(__file__))+'/chromedriver')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Screenshot import Screenshot_Clipping
from datetime import datetime



ob=Screenshot_Clipping.Screenshot()

img_dir = './static/img/'
pdf_dir = './static/pdf/'


def img_gen(url):
	if url == None :
		return
	#driver.get('https://itsbiswa.me')
	#print(os.path.dirname(os.path.abspath(__file__)))

	# DRIVER = ('./chromedriver/chromedriver_mac')
	# DRIVER = ('./chromedriver/chromedriver_linux')
	# driver = webdriver.Chrome(DRIVER)

	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")

	# if executable_path is not None:
	# 	executable_path = os.path.abspath(executable_path)
	# 	driver = webdriver.Chrome(excutable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
	# else:
	# 	driver = webdriver.Chrome(chrome_options=chrome_options)
	# driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
	
	driver.get(url)
	img_name =  str(datetime.now().replace(microsecond=0)) +".png"
	img_name=img_name.replace(" ", "-")
	mg_url=ob.full_Screenshot(driver, save_path=img_dir, image_name=img_name)
	driver.quit()
	return img_name
	
def pdf_gen(img_name):
	img_name = str(img_name).strip()
	img_path = os.path.join(img_dir, img_name)
	im1 = Image.open(img_path)
	#im1.show()
	im1 = im1.convert('RGB')
	img_name = img_name[:-3]+'pdf'
	pdf_path = os.path.join(pdf_dir, img_name)
	im1.save(r'{}'.format(pdf_path))
	return img_name


