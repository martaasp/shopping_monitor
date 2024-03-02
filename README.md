# SHOPPING MONITOR
1. [Introducción](#introducción)
2. [Preparación](#preparación)
3. [Uso](#uso)
4. [Ayuda](#ayuda)

## Introducción

Este proyecto comprueba la disponibilidad del conjunto de prendas indicadas y crea una alarma cuando identifica disponibilidad. 

> NOTA: El proyecto ha sido probado con la tienda online de _ZARA España_, _Massimo Dutti España_ y _Mango España_

## Preparación

### Prerrequisitos

Este proyecto ha sido probado con Python 3.11.7. Se puede verificar la versión de `python` instalado con:

```bash
python --version
```

### Instalación

Seguir estos pasos para instalar y configurar el proyecto en el dispositivo local:

1. **Clonar el repositorio**

    Se puede clonar con un cliente `git`:
    ```bash
    git clone https://github.com/martaasp/shopping_monitor.git
    cd shopping_monitor
    ```
    
    O descargar el repositorio comprimido en un `ZIP`

2. **Inicializar el proyecto**

    Ejecutar el siguiente comando para instalar las dependencias necesarias y preparar el entorno:

    ```bash
    make init
    ```

    Este comando actualizará pip, instalará las dependencias desde `requirements.txt` y dará permisos de ejecución a los scripts necesarios.

## Uso

Este proyecto incluye 2 modos para monitorizar la disponibilidad de productos y alertar sobre cambios. Se pueden configurar estos scripts para que se ejecuten automáticamente (explicado en [Monitorizar periódicamente](#monitorizar-periódicamente)).

Cada modo es una versión distinta del mismo proyecto: 
- __MODO 1 -__  Revisa la disponibilidad de todas las prendas y, cuando termina la revisión, si encuentra disponibilidad en alguna prenda, dispara una alarma. En este caso, la alarma consiste en el primer sonido (en orden alfabético) almacenado en el directorio `audio_clips`

- __MODO 2-__ Revisa la disponibilidad de todas las prendas y, según va encontrando disponibilidad, dispara una alarma. En este caso, al configurar cada prenda se debe indicar el sonido de cada una.

### Crear la lista de prendas a monitorizar

Abrir el archivo [`shopping_list.yml`](shopping_list.yml) y añadir la _URL_, _talla_ y _sonido_ siguiendo el formato del siguiente ejemplo:

- __MODO 1-__ Para el primer modo, como todas las prendas tendrán el mismo sonido de alarma, será suficiente con indicar la _URL_ y la _talla_. No obstante, se podrá utilizar el formato de __MODO 2__

    ```yml
    falda:
        URL: https://www.zara.com/es/es/falda-midi-tubo-pespuntes-p02813641.html
        SIZE: XL
    ```

- __MODO 2-__ Para el segundo modo, se deberá indicar la _URL_, la _talla_ y el _sonido_ de alarma de cada prenda.
    ```yml
    falda:
        URL: https://www.zara.com/es/es/falda-midi-tubo-pespuntes-p02813641.html
        SIZE: XL
        MUSIC: mixkit-fast-rocket-whoosh-1714.mp3
    ```
Los archivos `mp3` deben guardarse en el directorio `audio_clips`

### Monitorizar periódicamente

Para añadir una tarea al crontab y que el script se ejecute periódicamente:

> Nota: Actualmente está configurado para que la tarea se ejecute cada minuto. Si se quiere modificar, se deberá actualizar la variable `SCHEDULE` en el archivo [`Makefile`](Makefile)

- __MODO 1 -__ Para monitorizar con sonido único para todas las prendas:

    ```bash
    make install_unique_sound
    ```

- __MODO 2 -__ Para monitorizar con un sonido distinto para cada prenda:

    ```bash
    make install_multiple_sound
    ```

> Nota: Cuando se ejecuta la tarea periódicamente, los logs se almacenan en `logs/execution_log.log`. Se pueden ver en tiempo real ejecutando el siguiente comando en un terminal: 
> ```bash
> tail -f logs/execution_log.log
> ```

### Ejecución Directa

También se pueden ejecutar los scripts directamente sin añadirlos al crontab:

- __MODO 1 -__ Para sonido único:
    
    ```bash
    make run_unique_sound
    ```

- __MODO 2 -__ Para sonido distinto para cada prenda:
    
    ``` bash
    make run_multiple_sounds
    ```

### Quitar la monitorización periódica

Para quitar las tareas añadidas al crontab:

```bash
make clean
```

## Ayuda

Para ver todas las opciones disponibles, ejecutar:

```bash
make help
```

