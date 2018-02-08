from selenium import webdriver
chrome_path = r"D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://apps.hcso.org/PropertySale.aspx")