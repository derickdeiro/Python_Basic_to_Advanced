from selenium import webdriver
from time import sleep  # apenas para verificar a velocidade das ações


# para istanciar a automacao do navegador - PODE COPIAR
class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'  # caminho do chromedriver
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')  # a pasta que utilizará para acessar
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)

    def acessa(self, site):
        self.chrome.get(site)  # acessa o site desejado (exemplo: github)

    def sair(self):
        self.chrome.quit()  # sai do site.

    # EXEMPLO para o GITHUB
    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')  # o texto precisa ser identico ao do site
            btn_sign_in.click()  # clica no botão encontrado com o texto acima
        except Exception as e:
            print(f'Erro ao clicar em Sign in', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')  # campo html de login
            input_password = self.chrome.find_element_by_id('password')  # campo html de senha
            btn_login = self.chrome.find_element_by_name('commit')
            input_login.send_keys('derick.deiro@gmail.com')
            input_password.send_keys('Ljzn8ujnkk15#')
            btn_login.click()
        except Exception as e:
            print(f'Erro ao fazer login', e)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print(f'Erro ao clicar no perfil', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print(f'Erro ao fazer logout', e)

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name(
            'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_perfil()
    chrome.faz_logout()

    chrome.clica_sign_in()
    chrome.faz_login()

    sleep(20)
    chrome.sair()
