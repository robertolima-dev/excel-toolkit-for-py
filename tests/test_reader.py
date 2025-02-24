import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# tests/test_reader.py
import pytest
import pandas as pd
from excel_toolkit.reader import read_excel, read_csv


def test_read_excel(tmp_path):
    """Testa a leitura de um arquivo Excel."""
    file_path = tmp_path / "test.xlsx"
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_excel(file_path, index=False, engine='openpyxl', sheet_name='Sheet1')

    # ✅ Correção: especificar sheet_name para garantir retorno de DataFrame
    df_read = read_excel(file_path, sheet_name='Sheet1')
    pd.testing.assert_frame_equal(df, df_read)


def test_read_csv(tmp_path):
    """Testa a leitura de um arquivo CSV."""
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_csv(file_path, index=False)

    df_read = read_csv(file_path)
    pd.testing.assert_frame_equal(df, df_read)
