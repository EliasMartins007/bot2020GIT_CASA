from selenium import webdriver

#meu exemplo 01/07/2020
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # observar minusculo e maiusculo
from selenium.webdriver.chrome.options import Options # observar minusculo e maiusculo
#fim do meu exemplo

import time


#teste elias 01/07/2020
import os

# teste elias 01/07/2020
# Setamos o caminho de nossa aplicação.
# ARMAZENAR DIRETORIO PRINCIPAL EM VARIAVEL
dir_path = os.getcwd()


# fim teste elias 01/07/2020


#


class WhatsappBot:
    # teste elias 01/07/2020
    # Setamos o caminho de nossa aplicação.
    # ARMAZENAR DIRETORIO PRINCIPAL EM VARIAVEL
    #dir_path = os.getcwd()
    #fim teste elias 01/07/2020


    def _init_(self):
        self.mensagem = "bom dia , https://www.youtube.com"
        self.grupos = ["GRUPO DE VENDAS"] # ["GRUPO DE FAMILIA", "GRUPO 2", "GRUPO 3"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')




    def EnviarMensagens(self):
        try:
            #icone de grupo na tela de todo os contatos e grupos
            #<span dir="auto" title="GRUPO DE VENDAS" class="_3ko75 _5h6Y_ _3Whw5">GRUPO DE VENDAS</span>

            #campo texto da tela
            #<div tabindex="-1" class="_2FVVk _2UL8j">

            #teste elias 01/07/2020
            ##self.driver.c
            #driver = webdriver.Chrome(dir_path + 'chromedriver.exe')
            #fim elias

            #botão de envio
            #<span data-icon="send" class="">
            self.driver.get('https://web.whatsapp.com')# gera exceção nessa linha não reconhece  drive como pertencente da class Whatsapp 01/07/2020
            time.sleep(30)
            for grupo in self.grupos:
                grupo =self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")#("//span[@title='GRUPO DE VENDAS']")
                time.sleep(3)# gera tempo para não travar o bot
                grupo.click()
                chat_box = self.driver.find_element_by_class_name('_3FRCZ') # do ananda ('_3u328')  # caixa de texto para conversas
                time.sleep(3)# gera tempo para não travar o bot
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)# gera tempo para não travar o bot
                botao_enviar.click()
                time.sleep(5)# gera tempo para não travar o bot

        except Exception as e:
            print(e)

 #       pass...
bot = WhatsappBot()
bot.EnviarMensagens()


