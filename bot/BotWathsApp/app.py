# Importar Bicliotecas

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# Navegador até o whatsapp

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Definir contatos e grupos e mensagem a ser enviada
contatos = ['Lilian Rosendo', 'Pedro Henrique']
mensagem =  'Boa tarde e só um teste!'
# Buscar Contatos/ Grupos
def buscar_contato(contato):
    pass
campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyble-text selectable-text")]')
time.sleep(3)
campo_pesquisa.click()
campo_pesquisa.send_keys(contatos)
campo_pesquisa.send_keys(Keys.ENTER)
time.sleep(5)

def enviar_mensagem(mensagem):
    pass
campo_mensagem = driver.find_element_by_xpath('//div[contains(@class,"copyble-text selectable-text")]')
campo_mensagem[1].click()
time.sleep(3)
campo_mensagem[1].send_keys(mensagem)
campo_mensagem[1].send_keys(Keys.ENTER)
for contato in contatos:
 buscar_contato (contato)
enviar_mensagem(mensagem)
# Campo de pesquisa 'copyble-text selectable-text'
# Campo mensagem privada 'copyble-text slectable-text'
# Enviar mensagens para o contato/gruppo