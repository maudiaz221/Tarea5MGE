Welcome to Mauricio Diaz Tarea 5!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   train
   
   inference


DockerFiles
===============================

Dockerfile para entrenamiento:
--------------------------------

.. code-block:: dockerfile

    # Imagen base con Python 3.8 en versión ligera
    FROM python:3.8-slim

    # Establecer el directorio de trabajo
    WORKDIR /app

    # Copiar los archivos del proyecto al contenedor
    COPY . /app

    # Instalar dependencias
    RUN pip install --no-cache-dir -r requirements.txt

    # Comando para ejecutar el entrenamiento
    CMD ["python", "train.py"]


Dockerfile para inferencia:
----------------------------

.. code-block:: dockerfile

    # Imagen base con Python 3.8 en versión ligera
    FROM python:3.8-slim

    # Establecer el directorio de trabajo
    WORKDIR /app

    # Copiar los archivos del proyecto al contenedor
    COPY . /app

    # Instalar dependencias
    RUN pip install --no-cache-dir -r requirements.txt

    # Comando para ejecutar la inferencia
    CMD ["python", "inference.py"]



Construcción de Imágenes Docker
===============================

Para construir la imagen de entrenamiento, usa:

.. code-block:: bash

    docker build -t mi_entrenamiento:latest -f Dockerfile.train .

Para construir la imagen de inferencia, usa:

.. code-block:: bash

    docker build -t mi_inferencia:latest -f Dockerfile.inference .


Ejecución de los Contenedores
=============================

Ejemplo de ejecución del contenedor de entrenamiento:

.. code-block:: bash

    docker run -v "$(pwd)/data:/app/data" -v "$(pwd)/models:/app/models" mi_entrenamiento:latest \
        --train_data "/app/data/prep/train_preprocessed.csv" \
        --save_path "/app/models" \
        --time_limit 60

Ejemplo de ejecución del contenedor de inferencia:

.. code-block:: bash

    docker run -v "$(pwd)/data:/app/data" -v "$(pwd)/models:/app/models" mi_inferencia:latest \
        --test_data "/app/data/inference/test_preprocessed.csv" \
        --model_path "/app/models" \
        --output "/app/data/predictions/predictions.csv"