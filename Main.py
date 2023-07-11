import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import cv2

def Init():
    ch_options = Options()
    ch_options.add_argument("--headless")
    global TargetTime
    TargetTime = "2023-07-12 23:00:00.00000000"  # 设置抢购时间

    global WebDriver
    # WebDriver = webdriver.Chrome(chrome_options=ch_options)         #使用headless游览器，速度更快
    WebDriver = webdriver.Chrome()  # 使用可视化游览器
    WebDriver.get("https://show.bilibili.com/platform/detail.html?id=73710&from=pc_ticketlist")  # 输入目标购买页面

    global Price, Session
    Session = '1'  # 场次设置：修改引号内部的数字，数字对应第选项的序号，选项序号从左到右从1开始依次排列
    Price = '1'  # 加个设置：设置方法与场次设置一样

    time.sleep(1)
    print("进入购票页面成功")

    WebDriver.find_element(By.CLASS_NAME, "nav-header-register").click()
    time.sleep(1)

    print("登录完成后关闭qrimg页面")
    WebDriver.save_screenshot('./QRcode.png')
    qrimg = cv2.imread('./QRcode.png')
    cv2.imshow("qrimg", qrimg)
    key = cv2.waitKey(0)
    WebDriver.find_element(By.CLASS_NAME, "bili-mini-close").click()

    # print("请在10s内登录")
    # time.sleep(10)

def Select():
    while True:
        try:
            WebDriver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/div[4]/ul[1]/li[2]/div[' + Session + ']').click()
            WebDriver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/div[4]/ul[2]/li[2]/div[' + Price + ']').click()
            break
        except:
            print("等待刷新")


def Wait():
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now + "     " + TargetTime)
        if now >= TargetTime:
            WebDriver.refresh()
            Select()
            break

def Buy():
    print("test1")
    while True:
        try:
            WebDriver.find_element(By.CLASS_NAME, "product-buy.enable").click()
            # time.sleep(5)
            print("进入购买页面成功")
        except:
            print("无法点击购买")

        try:
            WebDriver.find_element(By.CLASS_NAME, "confirm-paybtn.active").click()
            print("订单创建完成，请在一分钟内付款")
            # time.sleep(60)
        except:
            print("无法点击创建订单")


if __name__ == '__main__':
    Init()
    Select()
    Wait()
    Buy()


