import pygame
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
from .logger import Logger, Styles

SIZES_MAP = {'XS': 0, 'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
STOCK=[]
logger = Logger()

class Utilities:    
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

    def play_sound(self, music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    
    def check_availability(self, driver, url, size, music, play_music=True):
        driver.get(url) # abrir URL con selenium
        html_content = driver.page_source # extraer html
        soup = BeautifulSoup(html_content, 'lxml') # guarda en objeto BeautifulSoup para buscar la info

        item_title = soup.find('title').get_text()
        logger.info(f"Buscando disponibilidad", item_title)
        mapped_size = SIZES_MAP.get(size.upper(), 'Invalid size')
        if mapped_size == 'Invalid size':
            logger.warning(f"La talla '{size}' no es válida. El valor introducido debe ser uno de los siguientes {list(SIZES_MAP.keys())}",item_title)
            return
        # Coger el bloque de las tallas
        sizes_block=soup.find('div', attrs={'class': 'size-selector-list__wrapper'})
        
        try:
            size_status=sizes_block.find('li', attrs={'class': 'size-selector-list__item', 
                                   'id': re.compile(fr'product-size-selector-\d+-item-{mapped_size}')})['data-qa-action']
            logger.debug(f"Mensaje de stock: {size_status}",item_title)
        except:
            logger.error("No se encontró la talla",item_title)
            return
     
        if size_status != 'size-out-of-stock':
            logger.success('¡En stock!',item_title)
            if play_music: 
                self.play_sound(music)
            return True

