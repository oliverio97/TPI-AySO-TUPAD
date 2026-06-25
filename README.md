Trabajo Integrador: Virtualización y Entornos Aislados
Descripción del Proyecto
Este repositorio contiene el código fuente y la documentación correspondientes al Trabajo Integrador de la materia Arquitectura y Sistemas Operativos. El objetivo principal de este proyecto es lograr una comprensión profunda y práctica de los conceptos de virtualización, así como el manejo de entornos de desarrollo aislados.
El caso práctico desarrollado consta de la configuración de un hipervisor, el despliegue de un sistema operativo invitado, y la posterior ejecución de un script de cálculo de promedios (promedio.py) desarrollado en Python.
Requisitos Previos
Hipervisor: Oracle VirtualBox.
Sistema Operativo Invitado: Imagen ISO oficial de Ubuntu Linux.
Control de versiones: Git / GitHub Desktop.
Guía de Instalación y Ejecución
1. Montaje de la Máquina Virtual
Descargar e instalar Oracle VirtualBox en el sistema operativo anfitrión.
Crear una nueva máquina virtual desde la interfaz del hipervisor.
Configurar la arquitectura de la VM, asignando los recursos adecuados de hardware, como memoria RAM y almacenamiento de expansión dinámica.
2. Instalación de Ubuntu
Montar la imagen ISO de Ubuntu en la unidad óptica virtual de la máquina recién creada e iniciarla.
Seguir los pasos del asistente de instalación para configurar el idioma, teclado y la instalación del sistema operativo.
3. Despliegue y Ejecución del Script en Python
Iniciar sesión en el entorno gráfico de Ubuntu y abrir la terminal de comandos.
Clonar este repositorio dentro de la máquina virtual (o utilizar un git pull si ya fue clonado previamente) para obtener el archivo promedio.py.
Verificar la disponibilidad del intérprete ejecutando python3 --version.
Ejecutar el programa ingresando el comando python3 promedio.py.
El script solicitará el ingreso de tres notas al usuario mediante un bucle, calculará la suma de los valores y mostrará el promedio final en pantalla.
Equipo de Desarrollo y Reparto de Tareas
El presente trabajo se desarrolló implementando una división de tareas equitativa, asegurando que cada miembro del equipo asumiera aproximadamente el 50% del esfuerzo total del proyecto.
Miembro del Equipo


Tareas Principales Asignadas:

**Mauro Liciaga**: 
Investigación bibliográfica inicial, instalación y configuración base de la máquina virtual en VirtualBox, y redacción preliminar del Marco Teórico.

**Oliverio Arce**: 
Diseño y codificación del script de Python en el IDE, pruebas de depuración en el sistema anfitrión y estructuración inicial del repositorio de Git.
Ambos
Pruebas de transferencia del archivo hacia la VM, ejecución en la terminal de Ubuntu, captura de evidencias visuales, redacción de conclusiones y edición del informe PDF.

