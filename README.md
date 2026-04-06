# Práctica 2 - Ejercicios de Python

Este repositorio contiene la resolución de los ejercicios correspondientes a la Práctica 2. 

El proyecto está estructurado separando la lógica para resolver las consignas y los datos de prueba:
* `src/`: Contiene los módulos de Python (`.py`) con las funciones de procesamiento (simulación de competencia, estadísticas de texto, duración de playlist y filtro de spoilers).
* `notebooks/`: Contiene el archivo Jupyter Notebook (`.ipynb`) desde donde se importan las funciones y se ejecutan las pruebas visuales.
* `requirements.txt`: Archivo con la lista completa de dependencias y librerías necesarias para el entorno.
## Requisitos previos
Para ejecutar este proyecto correctamente, es necesario tener instalado:
* Python 3.13.2
* pip

## Guía de Instalación y Configuración

Siga estos pasos para configurar el entorno de ejecución de **Python 3.13.2** y asegurar que todas las dependencias funcionen correctamente.
Es fundamental utilizar un entorno virtual para aislar las dependencias y evitar conflictos de versiones.

1.  clona el repositorio

2.  Crear el entorno:

    python -m venv .venv

3.  Activar el entorno:
    * En Windows: `.\.venv\Scripts\activate`
    * En macOS/Linux: `source .venv/bin/activate`

4. Instalación de Dependencias
    * pip install -r requirements.txt
## Ejecución

1. Con el entorno activado, lanzá Jupyter:

jupyter lab

2. Abrí la carpeta notebooks/ y ejecutá los
ejercicios.