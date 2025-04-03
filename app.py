from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import subprocess

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    # Find the location of the Chrome binary
    try:
        result = subprocess.run(['which', 'google-chrome'], stdout=subprocess.PIPE, text=True)
        chrome_path = result.stdout.strip()
        
        if chrome_path:
            print(f"Google Chrome binary found at: {chrome_path}")
        else:
            print("Google Chrome binary not found.")

    except Exception as e:
        print(f"Error finding Chrome binary: {e}")

    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.binary_location = "/opt/google/chrome/opt/google/chrome/google-chrome"
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-zygote')
    options.add_argument('--disable-background-timer-throttling')
    options.add_argument('--disable-renderer-backgrounding')
    options.add_argument('--disable-backgrounding-occluded-windows')
    options.add_argument('--disable-features=VizDisplayCompositor')

    # If we find a chrome binary, use it
    if chrome_path:
        options.binary_location = chrome_path

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://google.com')  # Replace with your target URL
    title = driver.title
    driver.quit()
    
    return jsonify({'title': title})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
