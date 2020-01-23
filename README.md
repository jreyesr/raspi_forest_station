# raspi-forest-station

Repositorio del código para usar una Raspberry Pi como estación de recolección de datos para el Bosque Protector Prosperina. Funcionalmente equivalente a [SensoresServicio](https://github.com/rfcx-espol/SensoresServicio), pero usa una Raspberry Pi en lugar de un smartphone Android y un Arduino Mega.

## Estructura

TODO: Imagen, explicación de cada script

## Instrucciones de instalación

1. Copiar los scripts de Python del repositorio a la carpeta `/home/pi`
1. Configurar los scripts para que se ejecuten en el arranque con `crontab -e`, agregar

    ```
    TODO
    ```
    
1. Reiniciar la Raspberry Pi
1. Verificar que los scripts estén ejecutándose con ps -axf

## Funcionalidades

### Funcionalidades completas

* Comunicación con sensor ambiental y captura de datos por intervalo (actualmente 1 captura por minuto)
* Comunicación con sensor de movimiento
* Comunicación con la cámara y captura de datos cuando se detecta movimiento
* Persistencia de datos en base de datos SQLite (hasta que sean enviados)
* Envío de datos al servidor

### Funcionalidades por desarrollar

* Captura de audio (no hay interfaz de audio USB)
* Envío de audio a servidor

### Bugs, limitaciones y posibles mejoras

* Verificar qué ocurre si la cámara se desconecta (es posible que el proceso de la cámara se detenga)
* Cambiar los procesos a un monitor de procesos que los reinicie si se detienen (por ejemplo, [daemontools](http://cr.yp.to/daemontools.html))
* Confirmar que los datos no se eliminen de la base de datos hasta que hayan sido transmitidos al servidor
