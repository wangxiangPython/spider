import random
import time
import multiprocessing
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def handle_douyin(driver):
    while True:
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("com.ss.android.ugc.aweme:id/ahx")):
            driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahx").click()
            driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahx").send_keys("191433445")
            while driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahx").text != "191433445":
                driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahx").send_keys("191433445")
                time.sleep(0.1)

        driver.find_element_by_id("com.ss.android.ugc.aweme:id/fh9").click()

        # 点击用户
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='用户']")):
            driver.find_element_by_xpath("//android.widget.TextView[@text='用户']").click()

        # 点击用户图片
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='关注']")):
            driver.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView[1]").click()

        # 点击粉丝
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='粉丝']")):
            driver.find_element_by_xpath("//android.widget.TextView[@text='粉丝']").click()

        time.sleep(3)

        l = get_size(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.15)

        while True:
            if "没有更多了" in driver.page_source:
                break
            elif "TA还没有粉丝" in driver.page_source:
                break
            else:
                driver.swipe(x1, y1, x1, y2)
                time.sleep(0.2)

        driver.find_element_by_id("com.ss.android.ugc.aweme:id/kq").click()
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/kq").click()
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahx").clear()

def handle_appium(device,port):
    cap = {
        "platformName": "Android",
        "platformVersion": "6.0",
        # "deviceName": "0b3c34710c37721e",
        # "udid":"0b3c34710c37721e",
        "deviceName": device,
        "udid": device,
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
        "noReset": True,
        "unicodekeyboard": True,
        "resetkeyboard": True
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
    # driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", cap)

    try:
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("com.ss.android.ugc.aweme:id/ay8")):
            driver.find_element_by_id("com.ss.android.ugc.aweme:id/ay8").click()
    except:
        pass
    handle_douyin(device)


def main():
    m_list = []
    device_list = ['0b3c34710c37721e']
    for device in range(len(device_list)):
        port = 4723 + 2*device
        m_list.append(multiprocessing.Process(target=handle_appium,args=(device_list[device],port)))
    for m1 in m_list:
        m1.start()
    for m2 in m_list:
        m2.join()

if __name__ == '__main__':
    main()