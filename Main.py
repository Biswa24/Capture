from PIL import Image
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from datetime import datetime
import os


ob=Screenshot_Clipping.Screenshot()
img_dir = './static/img/'
pdf_dir = './static/pdf/'

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")

# driver = webdriver.Chrome(excutable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options )

def img_gen(url):
	if url == None :
		return
	#driver.get('https://itsbiswa.me')

	DRIVER = ('./chromedriver')
	driver = webdriver.Chrome(DRIVER)
	driver.get(url)
	img_name =  str(datetime.now()) +".png"
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


