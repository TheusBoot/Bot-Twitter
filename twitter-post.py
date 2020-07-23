from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Bot_twitter:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def twittar(self,mensagem, tempo=10):
        self.browser = webdriver.Firefox()
        sleep(5)
        self.browser.get('https://twitter.com/login')
        sleep(5)

        log = self.browser.find_element_by_name('session[username]')
        sen = self.browser.find_element_by_name('session[password]')

        log.send_keys(self.login)
        sen.send_keys(self.senha)
        sleep(3)
        sen.send_keys(Keys.ENTER)