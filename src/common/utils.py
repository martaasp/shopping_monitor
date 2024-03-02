import pygame
import yaml
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
from .logger import Logger

ZARA_SIZES_MAP = {'XS': 0, 'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
MANGO_SIZES_MAP = {'XXS':18, 'XS': 19, 'S': 20, 'M': 21, 'L': 22, 'XL': 23, 'XXL': 24}

STOCK=[]


class Utilities:
    def __init__(self):
        self.logger = Logger()
    
    @staticmethod  
    def srt_to_bool(str):
        if str in ['True', 'true', 1, 't', 'T']:
            return True
        else: return False
        
    @staticmethod    
    def load_shopping_list(file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
        
    @staticmethod
    def setup_driver():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') 
        options.add_argument('--disable-gpu') 
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    @staticmethod
    def play_sound(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    
    def check_availability(self, driver, url, size, music, play_music=True):
        soup = self.get_title(driver, url)
        self.logger.info("Buscando disponibilidad")
        if 'zara' in url:
            return self.zara_check_availability(soup, size, music, play_music)
        if 'massimodutti' in url:
            return self.massimodutti_check_availability(driver, size, music, play_music)
        if 'mango' in url:
            return self.mango_check_availability(driver, size, music, play_music)
        
        
    def get_title(self, driver, url):
        driver.get(url)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'lxml')
        item_title = soup.find('title').get_text()
        self.logger.set_item_name(item_title)
        return soup
    
    def zara_check_availability(self, soup, size, music, play_music):
        mapped_size = ZARA_SIZES_MAP.get(size.upper(), 'Invalid size')
        
        if mapped_size == 'Invalid size':
            self.logger.warning(f"La talla '{size}' no es válida. El valor introducido debe ser uno de los siguientes {list(ZARA_SIZES_MAP.keys())}")
            return
        
        sizes_block=soup.find('div', attrs={'class': 'size-selector-list__wrapper'})
        
        try:
            size_status=sizes_block.find('li', attrs={'class': 'size-selector-list__item', 
                                   'id': re.compile(fr'product-size-selector-\d+-item-{mapped_size}')})['data-qa-action']
            #self.logger.debug(f"Mensaje de stock: {size_status}")
        except:
            self.logger.error("No se encontró la talla")
            return
     
        if size_status != 'size-out-of-stock':
            self.logger.success('¡En stock!')
            if play_music: 
                self.play_sound(music)
            return True
        else: self.logger.error("No se encontró la talla")

    def massimodutti_check_availability(self, driver, size, music, play_music):
        ul_element = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.btn-group.product-size-selector"))
                    )
        buttons = ul_element.find_elements(By.CSS_SELECTOR, "button.product-size-selector__button")
       
        size_found=False 
        for button in buttons:
            if button.text == size.upper():
                self.logger.success('¡En stock!')
                size_found=True
                if play_music: 
                    self.play_sound(music)
                    break
                
        if not size_found: 
            self.logger.error("No se encontró la talla")
            
        return size_found
    
    def mango_check_availability(self, driver, size, music, play_music):
        mapped_size = MANGO_SIZES_MAP.get(size.upper(), 'Invalid size')
        
        if mapped_size == 'Invalid size':
            self.logger.warning(f"La talla '{size}' no es válida. El valor introducido debe ser uno de los siguientes {list(ZARA_SIZES_MAP.keys())}")
            return
        
        micro_frontend = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, "micro-frontend[name='productDesktop']"))
                        )
        time.sleep(1)
        sizes_block = micro_frontend.find_element(By.CSS_SELECTOR, "div.size-selector-container")
        html_content = sizes_block.get_attribute('innerHTML')
        my_soup = BeautifulSoup(html_content, 'lxml')
        size_status = None
        try:
            size_status = my_soup.find('span', attrs={'id':f'size-{mapped_size}'})['data-available']
        except:
            self.logger.error("No se encontró la talla")
            return
        
        if size_status and size_status=='true':
            self.logger.success('¡En stock!')
            if play_music: 
                self.play_sound(music)
            return True
        else: self.logger.error("No se encontró la talla")
