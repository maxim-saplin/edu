from playwright.sync_api import sync_playwright
import time

def measure_load_time(url, timeout=30000):
    with sync_playwright() as p:
        # Launch the browser in headless mode
        browser = p.chromium.launch(headless=True)
        # page = browser.new_page(record_video_dir="videos/")
        page = browser.new_page()

        start_time = time.time()

        # Navigate to the Streamlit app URL and wait until network is idle
        page.goto(url, wait_until='networkidle')

        # You can also wait for a specific element that indicates the app has fully loaded
        #page.wait_for_selector('button', timeout=timeout)

        # End timing
        end_time = time.time()
        #page.screenshot(path='screenshot.png')

        load_time = end_time - start_time

        browser.close()

        return load_time


import numpy as np

# Run the load time measurement 10 times and calculate the average and standard deviation
load_times = []
for i in range(1):
    load_time = measure_load_time('http://localhost:8501')
    load_times.append(load_time)
    print(f"Iteration {i+1}: Load time is {load_time} seconds")
average_time = np.mean(load_times)
std_deviation = np.std(load_times)
std_deviation_percent = (std_deviation / average_time) * 100

# Print the average load time and the standard deviation in percent
print(f"Average Streamlit app load time: {average_time:.2f} seconds")
print(f"Standard deviation: {std_deviation:.2f} seconds ({std_deviation_percent:.2f}%)")