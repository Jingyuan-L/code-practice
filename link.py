from selenium import webdriver
import time
def refresh():
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434")
    for i in range(100):
        time.sleep(0.01)
        driver.refresh()
    driver.close()

if __name__ == "__main__":
    refresh()