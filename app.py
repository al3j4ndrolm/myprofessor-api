from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = "/usr/bin/google-chrome"  # Correct Chrome binary location for most Linux systems

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://google.com')  # Replace with your target URL
    title = driver.title
    driver.quit()
    
    return jsonify({'title': title})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
