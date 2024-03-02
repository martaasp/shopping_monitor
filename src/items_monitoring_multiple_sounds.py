import sys
import time
import pygame
from common.utils import Utilities as ut
from common.logger import Logger

start = time.time() ## Vamos a medir cuánto dura la ejecución

logger = Logger()
utilities = ut()
CURRENT_PATH = sys.argv[1]
SHOPPING_LIST_FILE = CURRENT_PATH+'/shopping_list.yml'

pygame.mixer.init()
shopping_list = ut.load_shopping_list(SHOPPING_LIST_FILE)
driver = ut.setup_driver()
for item, info in shopping_list.items():
    utilities.check_availability(driver, info['URL'], info['SIZE'], CURRENT_PATH+'/audio_clips/'+info['MUSIC'])
driver.quit()

end = time.time()
logger.warning(f'Duración: {round(end-start,2)}s')