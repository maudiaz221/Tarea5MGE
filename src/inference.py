"""
Este script realiza inferencia usando un modelo entrenado de AutoGluon.
Se parametrizan la ruta de entrada de datos, el modelo y la salida de las predicciones.
"""

import os
import argparse
from autogluon.tabular import TabularDataset, TabularPredictor

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_inference(test_path, model_path, output_path):
    """
    Ejecuta el modelo para generar predicciones.

    Parámetros:
      - test_path: Ruta al CSV de datos de prueba preprocesados.
      - model_path: Directorio del modelo entrenado.
      - output_path: Ruta donde se guardarán las predicciones.
    """
    test_data = TabularDataset(test_path)
    predictor = TabularPredictor.load(model_path)
    predictions = predictor.predict(test_data)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    predictions.to_csv(output_path)
    print("¡Predicciones guardadas en:", output_path, "!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Realizar inferencia con un modelo entrenado de AutoGluon")
    parser.add_argument("--test_data", type=str, default=os.path.join(BASE_DIR, "data", "inference", "test_preprocessed.csv"),
                        help="Ruta al CSV de datos de prueba preprocesados")
    parser.add_argument("--model_path", type=str, default=os.path.join(BASE_DIR, "models"),
                        help="Directorio del modelo entrenado")
    parser.add_argument("--output", type=str, default=os.path.join(BASE_DIR, "data", "predictions", "predictions.csv"),
                        help="Ruta donde se guardarán las predicciones")
    args = parser.parse_args()
    
    run_inference(args.test_data, args.model_path, args.output)