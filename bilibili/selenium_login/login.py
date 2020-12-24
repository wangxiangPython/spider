import sys
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains #鼠标动作链模块

from setting import KSB_UNAME,KSB_PWD,BILI_UNAME,BILI_PWD
from parse_code import base64_api

url = 'https://passport.bilibili.com/login'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
driver.maximize_window()
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"login-username")))
WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//*[@id="login-username"]'))
#输入账号
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(BILI_UNAME)
time.sleep(1)
#输入密码
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(BILI_PWD)
time.sleep(1)
#点击登录
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()

# WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_css_selector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div'))

#第一种方法根据元素定位直接截取验证码图片
#截取验证码图片
#此处没有时间等待 截图会报找不到元素   显性等待解出来的图片不全

time.sleep(2)
images = driver.find_element_by_css_selector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div')
images.screenshot('yzm.png')


code_result = base64_api(KSB_UNAME,KSB_PWD,'yzm.png')
print(code_result)

#坐标实现点击

# 103,192|218,127|107,113
result_list = code_result.split('|')
for result in result_list:
    x = result.split(',')[0]
    y = result.split(',')[1]
    #move_to_element_with_offset    根据元素实现点击操作
    #perform    实现整个鼠标动作链
    ActionChains(driver).move_to_element_with_offset(images,int(x),int(y)).click().perform()

time.sleep(1)
#点击确认按钮
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a/div').click()

# 登录后获取cookie
cookies = driver.get_cookies()
print(cookies)

# 第二种方法截全屏幕
# #location可以获取这个元素左上角坐标
# print(images.location)
# #size可以获取这个元素的宽和高
# print(images.size)
# driver.save_screenshot('screenshot.png')
# sys.stdin.flush()
# #计算验证码的左上右下的横切面
# left = images.location['x']
# top = images.location['y']
# right = images.location['x']+images.size['width']
# down = images.location['y']+images.size['height']
# im = Image.open('screenshot.png')
# im = im.crop((left,top,right,down))
# im.save('yzm.png')


# driver.quit()
