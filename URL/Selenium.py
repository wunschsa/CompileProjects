from selenium import webdriver

#brew install chromedriver

br = webdriver.Chrome(executable_path='/home/wunschsa/URL/chromedriver.exe')
br.get('https://www.reddit.com/')
