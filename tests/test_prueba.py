'''
Created on 27 oct. 2023

@author: alj70
'''
import unittest

import selenium

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from pages.sambsung_registro import NavHome as Sambsung_registro

import logging

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome() 
        self.action = ActionChains(self.driver)
        
        self.driver.maximize_window() 
        self.driver.implicitly_wait(5)
        self.driver.get("https://shop.samsung.com/ar/")
    
        
    def test_001_moviles(self): 
        #Móviles:
        try: 
            movil = self.driver.find_element(By.XPATH,Sambsung_registro.xpath_movil)
            self.action.move_to_element(movil).perform()
            
            time.sleep(3)
            self.driver.find_element(By.XPATH,Sambsung_registro.xpath_movil).click()
       
            #Validar Click en link "Moviles":
            assert self.driver.current_url==Sambsung_registro.url_moviles
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
            
    def test_01_hover_movil(self):
        #Validar Hover:
        movil = self.driver.find_element(By.XPATH,Sambsung_registro.xpath_movil)
        assert movil.value_of_css_property('outline')=='rgb(0, 0, 0) none 0px'
            
    def test_001_titulo(self):
        
        #Validar Titulo:
        self.assertEqual(self.driver.title,'Samsung Shop: descubrí la gama completa | Samsung Argentina')

        
    def test_002_sambsung(self):
        
        #Logo Sambsung (Home):
        sambsung = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung)
        sambsung.click()
        if sambsung:
            print("the link goes back to home")
        time.sleep(3)
        
        self.assertEqual(self.driver.title,'Samsung Shop: descubrí la gama completa | Samsung Argentina')
    
        
    def test_003(self):
        #Validar title.isupper()
        self.assertFalse(self.driver.title.isupper())

    def test_004_tv(self):
        #TV & Audio:
        try:          
            tv_audio = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_tvyaudio)
            self.action.move_to_element(tv_audio).perform()
            
            time.sleep(3)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_tvyaudio).click()#Click enlace
            
            #Validar Click en link "TV & Audio":
            assert self.driver.current_url==Sambsung_registro.url_tv_audio
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung).click()#Click Home (Sambsung)
            
        except WebDriverException as e:
            print("Event not Found")
            print(e)
    
    def test_04_hover_tv_audio(self):
        #Validar Hover:
        tv_audio = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_tvyaudio)
        assert tv_audio.value_of_css_property('outline')=='rgb(0, 0, 0) none 0px'
    
    
    def test_005_electrodomesticos(self):
        #Electrodomesticos:
        try:
            
            electrodomesticos = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_electrodomesticos)
            self.action.move_to_element(electrodomesticos).perform()#Hover
           
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_electrodomesticos).click()#Click enlace
            
            #Validar Click en link "Electrodomesticos":
            assert self.driver.current_url==Sambsung_registro.url_electrodomesticos
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung).click()#Click Home (Sambsung)
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        
    def test_05_hover_computacion(self):
        electrodomesticos = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_electrodomesticos)
        assert electrodomesticos.value_of_css_property('outline')=='rgb(0, 0, 0) none 0px'
    
    def test_006_computacion(self):
        #Computación:
        try:
            
            computacion = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_computacion)
            self.action.move_to_element(computacion).perform()#Hover
           
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_computacion).click()#Click enlace
            
            #Validar Click en link "Computacion":
            assert self.driver.current_url==Sambsung_registro.url_computacion
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung).click()#Click Home (Sambsung)
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        
        
    def test_007_oferta(self):
        #Oferta:
        try:
            
            oferta = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_ofertas)
            self.action.move_to_element(oferta).perform() #Hover
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_ofertas).click() #Click enlace
            
            #Validar Click en link "Oferta":
            assert self.driver.current_url==Sambsung_registro.url_ofertas
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung).click() #Click Home (Sambsung)
       
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        
        
    def test_008_plan_canje(self):
        #Plan Canje:
        try:
            
            plan_canje = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_plan_canje)
            
            self.action.move_to_element(plan_canje).perform()#Hover
            time.sleep(2)
            
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_plan_canje).click()#Click enlace
            
            #Validar Click en link "Plan Canje":
            assert self.driver.current_url==Sambsung_registro.url_plan_canje
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung).click()#Click Home (Sambsung)    
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        
    
    def test_009_soporte(self):
        #Soporte:
        try:
            soporte = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_soporte)
            
            self.action.move_to_element(soporte).perform()#Hover
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_soporte).click()#Click enlace
            
            #Validar Click en link "Soporte":
            assert self.driver.current_url==Sambsung_registro.url_soporte
            
            self.driver.get("https://shop.samsung.com/ar/")# Redirección al Home por que el click en el link anterior me dirige a otra ventana
            time.sleep(2)
            
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung).click()#Click Home (Sambsung)
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        
        
    def test_010_negocios(self):
        #Para negocios:
        try:
            
            negocios = self.driver.find_element(By.XPATH, Sambsung_registro.xpath_negocios)
            self.action.move_to_element(negocios).perform()#Hover
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_negocios).click()#Click enlace
            
            #Validar Click en link "Negocios":
            assert self.driver.current_url==Sambsung_registro.url_neogcios
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, Sambsung_registro.xpath_sambsung).click()#Click Home (Sambsung)
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        
    
        
        
    def tearDown(self):
        
        time.sleep(3)
        self.driver.quit()
        pass



if __name__ == '__main__':
    unittest.main()