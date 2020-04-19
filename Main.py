from PIL import Image
from selenium import webdriver
from Screenshot import Screenshot_Clipping
import os

ob=Screenshot_Clipping.Screenshot()
DRIVER = ('./chromedriver')
driver = webdriver.Chrome(DRIVER)
driver.get('https://itsbiswa.me')
mg_url=ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
driver.quit()
im1 = Image.open(r'./Myimage.png')
#im1.show()
im1 = im1.convert('RGB')
im1.save(r'./Resume.pdf')


