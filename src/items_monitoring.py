import os
import sys
import time
import pygame
from common.utils import Utilities as ut
from common.logger import Logger

start = time.time() ## Vamos a medir cuánto dura la ejecución

logger = Logger()
utilities = ut()
pygame.mixer.init()

SOUND_MODE = ut.srt_to_bool(sys.argv[1])
CURRENT_PATH = sys.argv[2]
SHOPPING_LIST_FILE = CURRENT_PATH+'/shopping_list.yml'

if SOUND_MODE: 
    AUDIO_FOLDER = CURRENT_PATH+'/audio_clips/'
    ALARM_SOUND = AUDIO_FOLDER+sorted(os.listdir(AUDIO_FOLDER))[0]
    AVAILABILITY = []

shopping_list = ut.load_shopping_list(SHOPPING_LIST_FILE)
driver = ut.setup_driver()

for item, info in shopping_list.items():
    if SOUND_MODE: 
        AVAILABILITY.append(utilities.check_availability(driver, info['URL'], info['SIZE'], None, False))
    else: 
        utilities.check_availability(driver, info['URL'], info['SIZE'], CURRENT_PATH+'/audio_clips/'+info['MUSIC'])

driver.quit()
if SOUND_MODE and any(AVAILABILITY): 
    utilities.play_sound(ALARM_SOUND)

end = time.time()
logger.warning(f'Duración: {round(end-start,2)}s')