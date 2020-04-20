from PIL import Image
from selenium import webdriver
from Screenshot import Screenshot_Clipping
import os

ob=Screenshot_Clipping.Screenshot()

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(excutable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options )

# DRIVER = ('./chromedriver')
# driver = webdriver.Chrome(DRIVER)
driver.get('https://itsbiswa.me')
mg_url=ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
driver.quit()
im1 = Image.open(r'./Myimage.png')
im1.show()
# im1 = im1.convert('RGB')
# im1.save(r'./Resume.pdf')


