Proyecto de AutoGluon: Entrenamiento, Preprocesamiento e Inferencia (Tarea 5)
===================================================================

Este repositorio contiene scripts para preprocesar datos, entrenar un modelo de AutoGluon y ejecutar inferencia. Además, se provee documentación generada con Sphinx y contenedores Docker para facilitar la ejecución en diferentes entornos.

Estructura del Proyecto
-----------------------

```
project/
├── src/
│   ├── train.py              # Script para entrenar el modelo. Acepta argumentos para rutas y parámetros.
│   ├── inference.py          # Script para ejecutar inferencia con el modelo entrenado.
│   └── prep.py               # Script para preprocesar los datos.
├── requirements.txt          # Lista de dependencias (autogluon, pandas, etc.)
├── Dockerfile.train          # Dockerfile para el contenedor de entrenamiento.
└── Dockerfile.inference      # Dockerfile para el contenedor de inferencia.

├── data/
│   ├── raw/                  # Archivos CSV originales (e.g., train.csv, test.csv, sample_submission.csv)
│   ├── prep/                 # Archivo preprocesado para entrenamiento (train_preprocessed.csv)
│   ├── inference/            # Archivo preprocesado para inferencia (test_preprocessed.csv)
│   └── predictions/          # Archivo de predicciones (predictions.csv) generado tras la inferencia.
├── models/                   # Directorio donde se guarda el modelo entrenado.
├── docs/
│   ├── build/                # Documentación generada en HTML.
│   └── source/               # Fuentes de la documentación Sphinx.
│       ├── index.rst         # Página principal de la documentación.
│       ├── train.rst         # Documentación del script de entrenamiento.
│       ├── inference.rst     # Documentación del script de inferencia.
│       └── docker_usage.rst  # Instrucciones de uso de Docker.

```

Requisitos
----------

- Docker (para construir y ejecutar contenedores)
- Sphinx (para generar la documentación)


Uso de Docker
-------------

Para facilitar el despliegue, se crearon dos contenedores Docker: uno para el entrenamiento y otro para la inferencia.

Imagen de Entrenamiento
~~~~~~~~~~~~~~~~~~~~~~~

Construye la imagen de entrenamiento con:

    docker build -t mi_entrenamiento:latest -f Dockerfile.train .

Imagen de Inferencia
~~~~~~~~~~~~~~~~~~~~

Construye la imagen de inferencia con:

    docker build -t mi_inferencia:latest -f Dockerfile.inference .

Ejecutar Contenedores
~~~~~~~~~~~~~~~~~~~~~

Ejecución del Contenedor de Entrenamiento
------------------------------------------

Asegúrate de que el archivo preprocesado "data/prep/train_preprocessed.csv" exista (generado con prep.py) y monta los volúmenes necesarios para acceder a los datos y guardar el modelo:

    docker run -v "$(pwd)/data:/app/data" -v "$(pwd)/models:/app/models" mi_entrenamiento:latest \
        --train_data "/app/data/prep/train_preprocessed.csv" \
        --save_path "/app/models" \
        --time_limit 60

Este comando:
- Monta el directorio "data/" del host en "/app/data" dentro del contenedor.
- Monta el directorio "models/" del host en "/app/models" para persistir el modelo entrenado.

Ejecución del Contenedor de Inferencia
---------------------------------------

Asegúrate de que el archivo preprocesado "data/inference/test_preprocessed.csv" y el modelo en "models/" estén disponibles. Luego, ejecuta:

    docker run -v "$(pwd)/data:/app/data" -v "$(pwd)/models:/app/models" mi_inferencia:latest \
        --test_data "/app/data/inference/test_preprocessed.csv" \
        --model_path "/app/models" \
        --output "/app/data/predictions/predictions.csv"

Este comando monta los directorios necesarios para que el contenedor pueda acceder a los datos y al modelo, y guarde las predicciones en "data/predictions/".

Preprocesamiento, Entrenamiento e Inferencia sin Docker
--------------------------------------------------------

Si deseas ejecutar los scripts directamente en tu entorno local:

1. Preprocesar los Datos:

       python src/prep.py

2. Entrenar el Modelo:

       python src/train.py --train_data "data/prep/train_preprocessed.csv" --save_path "models" --time_limit 60

3. Ejecutar Inferencia:

       python src/inference.py --test_data "data/inference/test_preprocessed.csv" --model_path "models" --output "data/predictions/predictions.csv"

Documentación con Sphinx
------------------------

La documentación del proyecto se encuentra en el directorio "docs/source". Para generar la documentación HTML:

1. Navega al directorio "docs":

       cd docs

2. Ejecuta:

       make html

3. Abre el archivo generado en "docs/build/html/index.html" en tu navegador para ver la documentación completa.

La documentación incluye detalles sobre:
- train.py: Script de entrenamiento.
- inference.py: Script de inferencia.
- docker_usage.rst: Instrucciones y ejemplos de uso de Docker.

Screenshots de Entradas y Salidas
---------------------------------

En la entrega vía CANVAS se debe incluir un HTML con:
- El contenido del Dockerfile y los comandos utilizados.
- Screenshots (capturas de pantalla) que muestren:
  - La terminal con la ejecución de los comandos de Docker (las entradas).
  - Los mensajes de salida, como confirmación de que el modelo se ha guardado o las predicciones han sido generadas (las salidas).

Estas capturas sirven para evidenciar el correcto funcionamiento de los contenedores y la generación de archivos (modelo, predicciones, etc.).

Contribuciones
--------------

Si deseas contribuir, por favor abre un issue o envía un pull request.

Licencia
--------

Este proyecto se distribuye bajo la Licencia MIT.
