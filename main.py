#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Hàm chính: crawl trang TopCV
def crawl_topcv_headless(url, max_jobs=20):
    # (Phần cấu hình driver như trên)
    options = Options()
    options.binary_location = "/snap/bin/chromium"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    # options.add_argument("--window-size=640,480")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    # options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-images")
    options.add_argument("--disable-javascript")  # Temporarily disable JS to avoid Cloudflare
    options.add_argument("--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'")
    
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        
        # Truy cập URL và chờ JS chạy
        driver.get(url)

        # Print all the html
        print(driver.page_source)

    except Exception as e:
        print(f"Error occurred: {e}")
        raise
    finally:
        if 'driver' in locals():
            driver.quit()
    # return jobs


if __name__ == "__main__":
    url = "https://www.topcv.vn/viec-lam/nhan-vien-ke-toan-cong-truong-tu-02-nam-kinh-nghiem-thu-nhap-den-15-trieu-tai-my-loc-nam-dinh/1811427.html?ta_source=BoxFeatureJob_LinkDetail"
    # data = crawl_topcv_headless(url)
    # print(json.dumps(data, ensure_ascii=False, indent=2))

    time_start = time.perf_counter()

    crawl_topcv_headless(url)

    time_end = time.perf_counter()
    print(f"Time taken: {time_end - time_start:.4f} seconds")
