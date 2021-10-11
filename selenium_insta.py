from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstaBot:
    def __init__(self, user, senha):
        self.user = user
        self.senha = senha
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\gabriel.pinto\\Desktop\\geckodriver-v0.26.0-win64\\geckodriver.exe")

    # Vai até o site do instagram e faz o login.
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)

        botao_login = driver.find_element_by_xpath("//input[@name='username']")
        botao_login.click()
        botao_login.send_keys(self.user)

        botao_senha = driver.find_element_by_xpath("//input[@name='password']")
        botao_senha.click()
        botao_senha.send_keys(self.senha)
        botao_senha.send_keys(Keys.RETURN)
        time.sleep(5)

        self.comentar_nas_fotos('futebol')

    # Função para fazer o comentário ser digitado devagar.
    @staticmethod
    def digitar_como_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)

    # Vai até a página da hashtag desejada.
    def comentar_nas_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")

        # Laço de repetição usado para rolar a página 3 vezes.
        for c in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)

        # Busca todos os elementos com a tag 'a'.
        hrefs = driver.find_elements_by_tag_name("a")
        foto_hrefs = [elem.get_attribute('href') for elem in hrefs]

        # Mostra quantas fotos foram encontradas até o momento, para mais fotos, adicione um range maior no for.
        print(hashtag + ' fotos: ' + str(len(foto_hrefs)))

        for foto_hrefs in foto_hrefs:
            driver.get(foto_hrefs)

            # Rola a página para garantir que a imagem esteja dentro da área visível.
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                comentarios_frases = ["cometários para as postagens"]

                # Vai até o botão de comentários.
                driver.find_element_by_class_name('Ypffh').click()
                comentar = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(5, 10))

                # Digita devagar para parecer mais humano (ou menos robô).
                self.digitar_como_pessoa(random.choice(comentarios_frases), comentar)
                time.sleep(random.randint(10, 15))

                # Clica no botão 'Publicar' para postar o comentário na foto.
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(random.randint(30, 250))

            except Exception as erro:
                print(erro)
                time.sleep(5)


samsepiol = InstaBot("USER", "SENHA")
samsepiol.login()
