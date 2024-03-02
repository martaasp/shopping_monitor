import sys
import pygame
import time
from common.utils import Utilities as ut
from common.logger import Logger
import os

start = time.time() ## Vamos a medir cuánto dura la ejecución
logger = Logger()
CURRENT_PATH=sys.argv[1]
SHOPPING_LIST_FILE = CURRENT_PATH+'/shopping_list.yml'
AUDIO_FOLDER=CURRENT_PATH+'/audio_clips/'
ALARM_SOUND=AUDIO_FOLDER+sorted(os.listdir(AUDIO_FOLDER))[0]
utilities = ut()
pygame.mixer.init()
shopping_list = ut.load_shopping_list(SHOPPING_LIST_FILE)
driver = ut.setup_driver()

AVAILABILITY=[]
for item, info in shopping_list.items():
    AVAILABILITY.append(utilities.check_availability(driver, info['URL'], info['SIZE'],None, False))
driver.quit()
if any(AVAILABILITY): 
    utilities.play_sound(ALARM_SOUND)

end = time.time()
logger.warning(f'Duración: {round(end-start,2)}s')