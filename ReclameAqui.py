from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep

# Informe o nome da empresa para ser extraído as informações
nome_empresa = input("Informe o nome da empresa (Se houver mais de um nome, favor colocar o separador '-') : ")

# Inicia o Webdriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Abre o link e coloca em fullscreen
navegador.get('https://www.reclameaqui.com.br/empresa/' + nome_empresa + '/')
sleep(3)
navegador.maximize_window()

# Verifica se a mensagem de empresa não existe está presente
mensagem_nao_existe = navegador.find_elements(By.CLASS_NAME, 'info-404')
if mensagem_nao_existe:
    print("A empresa não existe.")
else:
    # Faz o scraping da aba 6 meses
    def seisMeses():
        score6meses = navegador.find_elements(By.CLASS_NAME, 'stats')
        with open('nota6meses.txt', 'w') as file:
            for i in score6meses:
                nota6meses = i.text
                file.write(nota6meses + '\n')

    # Faz o scraping da aba Geral
    def geral():
        score_geral = navegador.find_elements(By.CLASS_NAME, 'stats')
        with open('notaGeral.txt', 'w') as file:
            for i in score_geral:
                notaGeral = i.text
                file.write(notaGeral + '\n')

    sleep(5)
    # Chama a função
    seisMeses()
    sleep(3)
    # Faz o rolamento da página
    pyautogui.press('pagedown')
    sleep(5)
    # Clica na aba Geral
    pyautogui.click(327, 261)
    # Chama a função
    geral = geral()

# Fecha o navegador
navegador.quit()
