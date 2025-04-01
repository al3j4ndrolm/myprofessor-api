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
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # If we find a chrome binary, use it
    if chrome_path:
        options.binary_location = chrome_path

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://example.com')  # Replace with your target URL
    title = driver.title
    driver.quit()
    
    return jsonify({'title': title})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
