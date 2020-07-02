from selenium import webdriver
import time

# bot original do canal youtube
class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "teste bot elias :)!!!"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["GRUPO DE VENDAS", "Marcos Ramos"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        try:
            self.driver.get('https://web.whatsapp.com')
            time.sleep(4)#5   original 30
            for grupo_ou_pessoa in self.grupos_ou_pessoas:
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
                time.sleep(3)
                campo_grupo.click()# ate aki entra no grupo ok
                chat_box = self.driver.find_element_by_class_name('_3uMse')# entrou no grupo porem deu erro  apos entrar no grupo 01/07/2020   ('_3FRCZ')
                time.sleep(3)# passou apos alterar para _3uMse   01/07/2020
                chat_box.click()
                chat_box.send_keys(self.mensagem)# até aki ok 01/07/2020 escreve mensagem porem gera exceção para enviar
                botao_enviar = botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")     #self.driver.elements_by_class_name('_2FVVk _2UL8j')                       #### originalself.driver.find_element_by_xpath("//span[@data-icon='send']") # carrega menu de pesquisa de outro grupos e amigo //span[@data-icon='send']
                time.sleep(3)
                botao_enviar.click()
                time.sleep(5)



                #driver.find_elements_by_class_name('_3M-N-')
        except Exception as e:
            print(e)


bot = WhatsappBot()
bot.EnviarMensagens()
