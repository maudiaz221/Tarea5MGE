"""
This script preprocesses raw training and test datasets using AutoGluon's feature generator.
It transforms the data and saves the preprocessed versions for model training and inference.
"""

import os
import pandas as pd
from autogluon.tabular import TabularDataset
from autogluon.features.generators import AutoMLPipelineFeatureGenerator



# Get the absolute path of the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prep_data():
    """
    Loads raw data, applies feature transformation, and saves the preprocessed datasets.

    Steps:
    1. Load raw training and test datasets.
    2. Apply AutoGluon's feature engineering.
    3. Transform the datasets.
    4. Save the preprocessed datasets for training and inference.
    """

    # Define file paths dynamically
    train_path = os.path.join(BASE_DIR, "data", "raw", "train.csv")
    test_path = os.path.join(BASE_DIR, "data", "raw", "test.csv")
    res_path = os.path.join(BASE_DIR, "data", "raw", "sample_submission.csv")
    output_train_path = os.path.join(BASE_DIR, "data", "prep", "train_preprocessed.csv")
    output_test_path = os.path.join(
        BASE_DIR, "data", "inference", "test_preprocessed.csv"
    )

    # Load raw datasets
    res_data = pd.read_csv(res_path)
    train_data = TabularDataset(train_path)
    test_data = TabularDataset(test_path)

    # Initialize AutoGluon's feature generator
    feature_generator = AutoMLPipelineFeatureGenerator(
        enable_numeric_features=True,
    )

    # Join of x and y test
    test_data = pd.merge(test_data, res_data, on="Id", how="inner")

    # Fit feature generator to training data (using 'SalePrice' as the target variable)
    feature_generator.fit(train_data, label="SalePrice")

    # Transform the datasets
    train_data = feature_generator.transform(train_data)
    test_data = feature_generator.transform(test_data)

    # Ensure the output directories exist before saving
    os.makedirs(os.path.dirname(output_train_path), exist_ok=True)

    # Save the transformed datasets
    train_data.to_csv(output_train_path)
    test_data.to_csv(output_test_path)

    print("Preprocessed data saved!")
