import datetime
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

TargetTime = "2023-04-16 16:39:00.00000000"     #设置抢购时间
WebDriver = webdriver.Chrome()
WebDriver.get("https://show.bilibili.com/platform/detail.html?id=71212&from=pc_ticketlist")   #输入目标购买页面
time.sleep(1)
print("进入购票页面成功")
WebDriver.find_element(By.CLASS_NAME, "nav-header-register").click()
print("请在10s内登录")
time.sleep(10)

# if(WebDriver.find_element(By.CLASS_NAME, "product-buy")):
#     print("确认此页面为预购页面")
#     time.sleep(3)
# elif(WebDriver.find_element(By.CLASS_NAME, "product-buy.enable")):
#     print("确认此页面为直接购买页面")
#     time.sleep(3)
# else:
#     print("此页面未发现预购按钮")
#     time.sleep(3)

# while True:
#     try:
#         WebDriver.find_element(By.CLASS_NAME, "product-buy.enable")
#         print("找到购买按钮")
#         break
#     except:
#         print("无购买按钮")

while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now + "     " + TargetTime)
    if now >= TargetTime:
        WebDriver.refresh()
        break

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






