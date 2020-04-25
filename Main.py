from PIL import Image
import os
from os import environ,listdir
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

	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")

	if os.environ['FLASK_ENV'] == 'development':
		DRIVER = ('./chromedriver/chromedriver_mac')
		# DRIVER = ('./chromedriver/chromedriver_linux')
		driver = webdriver.Chrome(DRIVER)
	else:
		driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
	
	driver.get(url)
	img_name =  str(datetime.now().replace(microsecond=0)) +".png"
	img_path = os.path.join(img_dir,img_name)
	# img_url=ob.full_Screenshot(driver, save_path=img_dir, image_name=img_name)
	S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
	driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
	driver.find_element_by_tag_name('body')
	driver.save_screenshot(img_path)  # has scrollbar
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


def delete(val,time_diff):

	if val =='img':
		dir = img_dir
	elif val == 'pdf':
		dir = pdf_dir
	else:
		print("Error")

	dir_name = listdir(dir)
	try :
		dir_name.remove('.DS_Store')
	except:
		pass
	files_name = [i[:-4] for i in dir_name]
	date_time_obj = [datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in files_name]

	curr_time = datetime.now().replace(microsecond=0)

	difference = [(curr_time - i).total_seconds() for i in date_time_obj]
	if len(difference) == 0:
		print("No files")
		return

	time = time_diff*60

	for i,j in enumerate(difference):
		if j > time:
			img_path = os.path.join(dir,dir_name[i])
			os.remove(img_path)
			print("Deleted {} file".format(dir_name[i]))

	return
