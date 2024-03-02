# SHOPPING MONITOR
1. [Introducción](#introducción)
2. [Preparación](#preparación)
3. [Uso](#uso)
4. [Ayuda](#ayuda)

## Introducción

Este proyecto comprueba periódicamente la disponibilidad del conjunto de prendas indicadas y crea una alarma cuando identifica disponibilidad. 

> NOTA: El proyecto ha sido probado con la tienda online de ZARA España, Massimo Dutti España y Mango España. Actualmente no está disponible para otras tiendas.

## Preparación

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu ordenador.

### Prerrequisitos

Antes de comenzar, asegúrate de tener Python instalado. Este proyecto ha sido probado con Python 3.11.7. Puedes verificar tu versión de Python con:

```bash
python --version
```

### Instalación

Para instalar y configurar el proyecto en tu local, sigue estos pasos:

1. **Clona el repositorio**

    Puedes clonarlo con un cliente `git`:
    ```bash
    git clone https://github.com/martaasp/shopping_monitor.git
    cd shopping_monitor
    ```
    O descargar el repositorio comprimido en un `ZIP`

2. **Inicializa el proyecto**

    Ejecuta el siguiente comando para instalar las dependencias necesarias y preparar el entorno:

    ```bash
    make init
    ```

    Este comando actualizará pip, instalará las dependencias desde `requirements.txt` y dará permisos de ejecución a los scripts necesarios.

## Uso

Este proyecto incluye scripts para monitorizar la disponibilidad de productos y alertar sobre cambios. Puedes configurar estos scripts para que se ejecuten automáticamente.

Existen 2 versiones: 
- __VERSIÓN 1 -__  Revisa la disponibilidad de todas las prendas y, cuando termina la revisión, si encuentra disponibilidad en alguna prenda, dispara una alarma. En este caso, la alarma consiste en el primer sonido (en orden alfabético) almacenado en el directorio `audio_clips`

- __VERSIÓN 2-__ Revisa la disponibilidad de todas las prendas y, según va encontrando disponibilidad, dispara una alarma. En este caso, al configurar cada prenda se debe indicar el sonido de cada una.

### Crear la lista de prendas a monitorizar

Abre el archivo [`shopping_list.yml`](shopping_list.yml) y añade la URL, talla y sonido siguiendo el formato del siguiente ejemplo:

- __VERSIÓN 1-__ Para la primera versión, como todas las prendas tendrán el mismo sonido de alarma, será suficiente con indicar la URL y la talla. No obstante, se podrá utilizar el formato de la __VERSIÓN 2__

    ```yml
    falda:
        URL: https://www.zara.com/es/es/falda-midi-tubo-pespuntes-p02813641.html
        SIZE: XL
    ```

- __VERSIÓN 2-__ Para la segunda versión, se deberá indicar la URL, la talla y el sonido de alarma de cada prenda.
    ```yml
    falda:
        URL: https://www.zara.com/es/es/falda-midi-tubo-pespuntes-p02813641.html
        SIZE: XL
        MUSIC: mixkit-fast-rocket-whoosh-1714.mp3
    ```
Los archivos `mp3` deben guardarse en el directorio `audio_clips`

### Monitorizar periódicamente

Para añadir una tarea al crontab y que nuestro script se ejecute periódicamente, se :

> Nota: Actualmente está configurado para que la tarea se ejecute cada minuto. Si quieres modificarla, actualiza la variable `SCHEDULE` en el archivo [`Makefile`](Makefile)

- __VERSIÓN 1 -__ Para monitorizar con sonido único para todas las prendas:

    ```bash
    make install_unique_sound
    ```
- __VERSIÓN 2 -__ Para monitorizar con un sonido distinto para cada prenda:

    ```bash
    make install_multiple_sound
    ```
> Nota: Cuando ejecutas la tarea periódicamente, los logs se almacenan en `logs/execution_log.log`. Puedes ir viéndolos ejecutando el siguiente comando en un terminal: 
> ```bash
> tail -f logs/execution_log.log
> ```

### Ejecución Directa

También puedes ejecutar los scripts directamente sin añadirlos al crontab:

- __VERSIÓN 1 -__ Para sonido único:
    ```bash
    make run_unique_sound
    ```

- __VERSIÓN 2 -__ Para sonido distinto para cada prenda:
    ``` bash
    make run_multiple_sounds
    ```

### Quitar la monitorización periódica

Para quitar las tareas añadidas al crontab:

- __VERSIÓN 1 -__ Quitar la tarea de sonido único:

    ```bash
    make clean_unique_sound
    ```

- __VERSIÓN 2 -__ Quitar la tarea de múltiples sonidos:

    ```bash
    make clean_multiple_sound
    ```

Quitar ambas tareas (puedes ejecutar este comando aunque solo hayas añadido una verisón):

```bash
make clean
```

## Ayuda

Para ver todas las opciones disponibles en este Makefile, ejecuta:

```bash
make help
```

