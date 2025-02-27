"""
Este script entrena un modelo usando AutoGluon y lo guarda en un directorio especificado.
Se parametrizan la ruta de entrada de datos y la ruta de salida del modelo.
"""

import os
import argparse
from autogluon.tabular import TabularDataset, TabularPredictor

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def train_model(train_path, save_path, time_limit):
    """
    Entrena un modelo y lo guarda.

    Parámetros:
      - train_path: Ruta al CSV de datos preprocesados.
      - save_path: Directorio donde se guardará el modelo.
      - time_limit: Límite de tiempo para el entrenamiento.
    """
    target = "SalePrice"
    train_data = TabularDataset(train_path)
    TabularPredictor(label=target, path=save_path).fit(train_data, time_limit=time_limit)
    print("¡Entrenamiento completado! Modelo guardado en:", save_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Entrenar modelo con AutoGluon")
    parser.add_argument("--train_data", type=str, default=os.path.join(BASE_DIR, "data", "prep", "train_preprocessed.csv"),
                        help="Ruta al CSV de datos de entrenamiento preprocesados")
    parser.add_argument("--save_path", type=str, default=os.path.join(BASE_DIR, "models"),
                        help="Directorio donde se guardará el modelo entrenado")
    parser.add_argument("--time_limit", type=int, default=10,
                        help="Tiempo límite (en segundos) para el entrenamiento")
    args = parser.parse_args()
    
    train_model(args.train_data, args.save_path, args.time_limit)