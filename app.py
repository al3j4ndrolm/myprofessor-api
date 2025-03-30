from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://example.com')  # Replace with your target URL
    title = driver.title
    driver.quit()
    
    return jsonify({'title': title})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
