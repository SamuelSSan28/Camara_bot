from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import json
from datetime import datetime


class Scraping_camara:
    def __init__(self):
        self.chromedriver = './chromedriver'
        pass

    def acess(self, last_acess):
        page = 0
        find = False
        projetos = {}
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox");
        options.add_argument("--disable-dev-shm-usage");
        aux = ""
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.set_page_load_timeout(10000)
        driver.get("http://www.splonline.com.br/cmteresina/spl/consulta-producao.aspx")
        i = 1   

        try:

            while True:
                try:
                    for i in range(2, 12): 
                        autores = []
                        endereco_processo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[1]'
                        processo = driver.find_element_by_xpath(endereco_processo).text.split(": ")[1]
                        endereco_protocolo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[2]'
                        protocolo = int(driver.find_element_by_xpath(endereco_protocolo).text.split("º ")[1])
                        autores=[]

                        if protocolo == last_acess:
                            aux = last_acess
                            driver.close()
                            return projetos

                        endereco_tipo = '//*[@id="tabela"]/tbody/tr['+str(i)+']/td/div[1]/strong/a'
                        tipo = driver.find_element_by_xpath(endereco_tipo).text

                        if ("Indicação" in tipo):
                            continue

                        
                        #print(processo,protocolo,last_acess )

                        endereco_data = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[3]'
                        data = driver.find_element_by_xpath(endereco_data).text.split(": ")[1].split(" ")[0]
                        endereco_situacao = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[4]'
                        situacao = driver.find_element_by_xpath(endereco_situacao).text.split(": ")[1]
                        endereco_autor = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[6]'
                        autor = driver.find_element_by_xpath(endereco_autor).text.split(": ")[1]
                        aux = autor.split(", ")
                        for u in aux:
                            autores.append(u)
                        endereco_resumo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[7]'
                        resumo = driver.find_element_by_xpath(endereco_resumo).text
                        endereco_setor = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[8]'
                        setor = driver.find_element_by_xpath(endereco_setor).text.split(": ")[1]
                        endereco_fase = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[9]'
                        fase = driver.find_element_by_xpath(endereco_fase).text.split(": ")[1]
                        projetos.update({processo: {"protocolo": protocolo, "tipo":tipo, "data": data, "situacao": situacao, "autor": autor, "resumo": resumo, "setor": setor, "fase": fase, "autores": autores}})

                       
                    if page < 6:
                        page += 1
                    pagina = '//*[@id="ContentPlaceHolder1_rptPaging_lbPaging_' + str(page) + '"]'
                    button = driver.find_element_by_xpath(pagina)
                    button.click()
                    time.sleep(10)
                
                except Exception as err:
                    data_e_hora_atuais = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    e = "Error: {0} no dia ".format(err) + data_e_hora_atuais +". Não Conseguiu ler o site\n"
                    arq = open('logs.txt', 'a+')
                    arq.write(e)
                    arq.close()
                    return 0
                    
        except Exception as err :
            data_e_hora_atuais = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            e = "Error: {0} no dia ".format(err) + data_e_hora_atuais +"\n"
            arq = open('logs.txt', 'a+')
            arq.write(e)
            arq.close()
