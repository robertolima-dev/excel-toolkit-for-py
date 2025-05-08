"""
Excel Toolkit for Python - Uma biblioteca para manipulação de arquivos Excel e CSV
"""

from .advanced_features import (add_chart, apply_conditional_formatting,
                                extract_formulas, protect_excel,
                                read_protected_excel, validate_empty_cells)
from .conversions import csv_to_excel, excel_to_csv
from .exporters import to_html, to_json, to_pdf, to_xml
from .reader import read_csv, read_excel
from .validations import validate_csv, validate_excel
from .writer import write_csv, write_excel

__version__ = "1.2.0"
__author__ = "Roberto Lima"
__email__ = "robertolima.izphera@gmail.com"

__all__ = [
    'read_excel',
    'read_csv',
    'write_excel',
    'write_csv',
    'excel_to_csv',
    'csv_to_excel',
    'validate_excel',
    'validate_csv',
    'validate_empty_cells',
    'apply_conditional_formatting',
    'extract_formulas',
    'add_chart',
    'protect_excel',
    'read_protected_excel',
    'to_json',
    'to_xml',
    'to_html',
    'to_pdf'
]
