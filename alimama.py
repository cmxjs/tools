#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File Name: alimama.py
@Author: xiaojinshui@casachina.com.cn
@Description:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
)

with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)
    url = "http://ad.alimama.com/index.htm"
    driver.get(url)

    sleep(2)
    driver.switch_to.frame(0)
    wait.until(presence_of_element_located((By.ID, "fm-login-id")))
    driver.find_element(By.ID, "fm-login-id").send_keys("q970693290")
    driver.find_element(By.ID, "fm-login-password").send_keys("xxxxx")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.fm-btn > button").click()
    sleep(2)
