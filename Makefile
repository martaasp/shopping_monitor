# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                       7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  command_to_execute

SCHEDULE="* * * * *" # La expresión cron (cada minuto)

CURRENT_PATH := $(PWD)
PYTHON := /usr/bin/python3
MONITORIZACION_PRENDAS_SCRIPT := src/items_monitoring.py
UNIQUE_SOUND_PARAMETER := True
MULTIPLE_SOUND_PARAMETER := False
ADD_CRON_SCRIPT := cron/add_job.sh
REMOVE_CRON_SCRIPT := cron/remove_job.sh

clean: # Quitar script del crontab
	@echo "Quitando el script del crontab..."
	chmod +x $(REMOVE_CRON_SCRIPT)
	./$(REMOVE_CRON_SCRIPT) $(MONITORIZACION_PRENDAS_SCRIPT)

init:  # Instalar dependencias y actualizar pip
	@echo "Instalando dependencias desde requirements.txt..."
	$(PYTHON) -m pip install --upgrade pip
	pip install -r requirements.txt
	chmod +x $(ADD_CRON_SCRIPT)

install_multiple_sound: init # Añadir monitorizacion_prendas.py al crontab
	@echo "Añadiendo el script al crontab..."
	./$(ADD_CRON_SCRIPT) $(MONITORIZACION_PRENDAS_SCRIPT) ${MULTIPLE_SOUND_PARAMETER} $(CURRENT_PATH) $(SCHEDULE)

install_unique_sound: init # Añade monitorizacion_prendas_v2.py al crontab
	@echo "Añadiendo el script al crontab..."	
	./$(ADD_CRON_SCRIPT) $(MONITORIZACION_PRENDAS_SCRIPT) ${UNIQUE_SOUND_PARAMETER} $(CURRENT_PATH) $(SCHEDULE)

run_multiple_sounds: # Ejecuta monitorizacion_prendas.py directamente
	$(PYTHON) $(MONITORIZACION_PRENDAS_SCRIPT) ${MULTIPLE_SOUND_PARAMETER} $(CURRENT_PATH)

run_unique_sound: # Ejecuta monitorizacion_prendas_v2.py directamente
	$(PYTHON) $(MONITORIZACION_PRENDAS_SCRIPT) ${UNIQUE_SOUND_PARAMETER} $(CURRENT_PATH)

help: # mostrar ayuda
	@echo "Opciones disponibles en este Makefile:"
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "Ejemplo de ejecucion: \033[36mmake run_unique_sound\033[0m"