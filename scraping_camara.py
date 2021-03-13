from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

class Scraping_camara:
    def __init__(self):
        self.chromedriver = 'LINK_CHROMEDRIVER'
        pass

    def acess(self, last_acess):
        page = 0
        find = False
        projetos = {}
        driver = webdriver.Chrome(self.chromedriver)
        driver.set_page_load_timeout(10000)
        driver.get("http://www.splonline.com.br/cmteresina/consulta-cronologico.aspx")

        try:
            button = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_anos"]/a[1]')
            button.click()

            while find == False:
                
                for i in range(2, 12): 
                    autores = []
                    endereco_processo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[1]'
                    processo = driver.find_element_by_xpath(endereco_processo).text.split(": ")[1]
                    autores=[]

                    if processo == last_acess:
                        find = True
                        break
                    tipo = driver.find_element_by_xpath(endereco_processo).text.split(" N")[0]
                    endereco_protocolo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[2]'
                    protocolo = driver.find_element_by_xpath(endereco_protocolo).text.split("º ")[1]
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
                    
                page += 1
                pagina = '//*[@id="ContentPlaceHolder1_rptPaging_lbPaging_' + str(page) + '"]'
                button = driver.find_element_by_xpath(pagina)
                button.click()
                time.sleep(3)

            print(projetos)
            return(projetos)
            driver.close()
        except Exception as e :
            print("ERRO em Camara",e)

#sc = Scraping_camara()
#sc.acess("480 /2021")
