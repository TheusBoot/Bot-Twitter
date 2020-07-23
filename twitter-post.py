from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Bot_twitter:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def twittar(self,mensagem, tempo=10,finalizar=True):
        self.browser = webdriver.Firefox()
        sleep(5)
        self.browser.get('https://twitter.com/login')
        sleep(5)

        log = self.browser.find_element_by_name('session[username_or_email]')
        sen = self.browser.find_element_by_name('session[password]')

        log.send_keys(self.login)
        sen.send_keys(self.senha)
        sleep(3)
        sen.send_keys(Keys.ENTER)
        sleep(tempo)
        tw = self.browser.find_element_by_css_selector('.notranslate.public-DraftEditor-content')
        sleep(5)
        tw.send_keys(mensagem)
        sleep(6)
        bt = self.browser.find_element_by_css_selector('.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1n0xq6e.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr').click()
        sleep(5)
        
        if finalizar == True:
            self.browser.quit()

bot = Bot_twitter('Matheuscombatcf@hotmail.com','Matheus@zz00')

bot.twittar(mensagem='zero sono',tempo=11,finalizar=True)


