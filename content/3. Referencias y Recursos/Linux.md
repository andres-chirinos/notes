---
title: Linux
description: 
permalink: 
aliases: 
tags: 
draft: "false"
date: 2024-09-03 20:42
---
Linux es un sistema operativo de código abierto desarrollado por Linus Torvalds en 1991. A diferencia de otros sistemas operativos, las funciones de Linux permiten a cualquier persona acceder, modificar y distribuir su código fuente. Esto ha generado una gran diversidad de versiones de Linux, más conocidas como distribuciones.
## Kernel
El kernel es el elemento principal de los sistemas operativos Linux. Funciona como la interfaz fundamental entre el hardware de una computadora y sus procesos. Este se comunica con los procesos y gestiona los recursos de manera eficiente. Algunas de sus funciones clave que son propias de un sistema operativo son.
- **Gestión de la memoria:** Supervisa cuánta memoria se utiliza para almacenar qué tipo de elementos y dónde se guardan.
- **Gestión de los procesos:** Determina qué procesos pueden usar la unidad central de procesamiento (CPU) y cuándo.
- **Controladores de dispositivos:** Actúa como mediador entre el hardware y los procesos.
- **Seguridad y llamadas al sistema:** Recibe solicitudes de servicio por parte de los procesos.
El kernel trabaja en su propio mundo pequeño llamado espacio del kernel, mientras que lo que está a la vista del usuario (como exploradores y archivos) se encuentra en el espacio del usuario, 

## Distribuciones
Las distribuciones son versiones específicas de Linux que incluyen el kernel junto con aplicaciones y programas adicionales. Algunas de las distribuciones más conocidas son:
    - **Ubuntu:** Popular por su facilidad de uso y amplia comunidad de usuarios.
    - **Debian:** Conocida por su estabilidad y enfoque en el software libre.
    - **Fedora:** Desarrollada por Red Hat y orientada a la innovación.
    - **CentOS:** Basada en el código fuente de Red Hat Enterprise Linux.
    - **Arch Linux:** Dirigida a usuarios avanzados y personalización extrema.
    - **openSUSE:** Con énfasis en herramientas gráficas y administración sencilla

## Directorio root
En Linux, el sistema de archivos sigue una estructura jerárquica con un directorio raíz representado por `/`. Donde cada directorio tiene su propósito especifico en los cuales  algunos directorios importantes dentro del directorio raíz son:
    - `/bin`: Contiene archivos binarios esenciales (comandos básicos).
    - `/etc`: Configuraciones del sistema.
    - `/home`: Directorios personales de los usuarios.
    - `/lib`: Bibliotecas compartidas.
    - `/usr`: Programas y archivos no esenciales.
    - `/var`: Datos variables (logs, spool, etc.).
    - `/tmp`: Archivos temporales.
    - `/dev`: Dispositivos.
    - `/proc`: Información sobre procesos en tiempo real.
    - `/root`: Directorio personal del superusuario (root).
## Proxy
Un proxy es un intermediario entre tu conexión y el servidor al que intentas acceder. Imagina que vas a abrir una página web: en lugar de conectarte directamente al servidor donde está alojada esa página, la conexión primero pasa por el proxy y luego llega al destino.

### Funciones
- **Seguridad y protección:** El proxy actúa como un puente levadizo a la entrada del castillo. Protege contra amenazas como ataques DDoS y ofusca la comunicación entre los dispositivos finales y los servidores web.
- **Ocultar la dirección IP:** Cuando te conectas a través de un proxy, utilizas la dirección IP del proxy en lugar de la tuya real. Esto ayuda a preservar tu privacidad.
- **Filtrar contenido:** Los proxies pueden bloquear o permitir ciertos tipos de contenido según reglas predefinidas.
- **Almacenar caché:** Los proxies de caché almacenan copias temporales de páginas web para acelerar su carga en futuras solicitudes.
- **Evitar bloqueo geográfico:** Al usar un proxy ubicado en otro país, puedes acceder a contenido restringido geográficamente

### Características Técnicas
- Pérdida de velocidad: Debido a que la conexión pasa por el proxy, puede haber una disminución en la velocidad.
- Configuración: Existen proxies gratuitos y de pago. La elección correcta es importante para evitar cortes y asegurar un buen rendimiento.
- Tipos de proxies: Además de los mencionados, hay otros como los proxies inversos (que protegen servidores internos) y los proxies transparentes (que no requieren configuración en el cliente).
- Protocolos: Los proxies pueden funcionar con diferentes protocolos, como HTTP, HTTPS, SOCKS, etc.

## Bibliografía
- ¿Para Qué Sirve Un Servidor Proxy? (¿Y Cómo Funciona?). (2023, February 23). Kinsta. Retrieved August 30, 2024, from https://kinsta.com/es/base-de-conocimiento/que-es-un-proxy/
- ¿Qué es el kernel Linux? y ¿Cuáles son sus funciones? (2019, February 27). Red Hat. Retrieved August 30, 2024, from https://www.redhat.com/es/topics/linux/what-is-the-linux-kernel