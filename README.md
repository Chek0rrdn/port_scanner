# Port Scanner

Este es un simple escáner de puertos en Python que te permite escanear un rango de puertos en un host específico. Utiliza el módulo `socket` y `concurrent.futures.ThreadPoolExecutor` para realizar el escaneo de manera eficiente en paralelo

## Uso

Para ejecutar el escáner, sigue estos pasos:


1. Para ejecutar el escáner, sigue estos pasos:
2. Clona este repositorio o copia el código en un archivo Python (por ejemplo,  `port_scanner.py`).
3. Clona este repositorio o copia el código en un archivo Python (por ejemplo, 

```bash
python3 port_scanner.py -t [HOST] -p [PORT_RANGE]
```

Reemplaza [HOST] con la dirección IP o el nombre del host que deseas escanear y [PORT_RANGE] con el rango de puertos que deseas escanear. Puedes especificar un solo puerto, un rango (por ejemplo, 1-100), o una lista de puertos separados por comas (por ejemplo, 80,443,8080).

## Ejemplo

```bash
python3 port_scanner.py -t 192.168.1.1 -p 1-1000
```

Esto escaneará los puertos del 1 al 1000 en el host con la dirección IP 192.168.1.1.

## Opciones

- `-t` o `--target`: Especifica el host a escanear.
- `-p` o `--port`: Especifica el rango de puertos a escanear.

## Notas

- El escáner utiliza un máximo de 200 hilos en paralelo para realizar el escaneo de puertos de manera eficiente.
- Puedes interrumpir el escáner en cualquier momento presionando `Ctrl+C`.

¡Nota! Ten en cuenta que escanear puertos sin permiso puede estar sujeto a restricciones legales y éticas. Asegúrate de tener autorización antes de escanear puertos en cualquier red o sistema que no sea de tu propiedad. El mal uso de esta herramienta puede tener consecuencias legales.
