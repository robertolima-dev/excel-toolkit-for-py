# 📜 Changelog


## [1.4.1] - 2026-06-18
### Fixed
- `pyproject.toml` was missing `license = { text = "MIT" }` and the
  `License :: OSI Approved :: MIT License` classifier, so the published
  PyPI page didn't display the license correctly.

### Changed
- Removed duplicated `setup.py`; `pyproject.toml` is now the single
  source of package metadata. Build via `python -m build` + `twine
  check`, with CI (`ci.yml`) and tag-triggered release (`release.yml`)
  publishing to PyPI.

## [1.4.0] - 2025-01-29
### Changed
- Updated all code comments and documentation to English
- Updated minimum Python version to 3.8+
- Updated dependencies to latest compatible versions
- Added scipy dependency to pyproject.toml
- Fixed version inconsistencies across all files

### Added
- Enhanced error handling and validation
- Improved code formatting and structure
- Better type hints and documentation

## [1.3.0] - 2025-05-29
### Adicionado
- Novo módulo de Análise de Dados (`data_analysis.py`) com as funções:
  - `calculate_basic_stats`: Estatísticas básicas (média, mediana, moda, desvio padrão, mínimo, máximo, quartis)
  - `detect_outliers`: Detecção de outliers por z-score ou IQR
  - `calculate_correlations`: Matriz de correlação entre colunas numéricas
  - `create_pivot_table`: Criação de tabela dinâmica (pivot table)
- Testes automatizados para todas as funções de análise de dados
- Exemplo de uso das funções de análise de dados adicionado ao README
- Dependências `numpy` e `scipy` adicionadas ao setup

## [1.1.8] - 2025-04-16
### Adicionado
- Novas funcionalidades de exportação:
  - Exportação para JSON com suporte a DataFrames e dicionários
  - Exportação para XML com suporte a DataFrames e dicionários
  - Exportação para HTML com suporte a templates personalizados
  - Exportação para PDF com suporte a templates personalizados

## [1.1.7] - 2025-03-21
### Adicionado
- Ajuste na documentação

## [1.1.6] - 2025-03-21
### Adicionado
- Ajuste na documentação

## [1.1.5] - 2025-03-21
### Adicionado
- Adionado a função write_list_to_excel

## [1.1.4] - 2025-03-21
### Adicionado
- Adionado novas funções

## [1.1.3] - 2025-03-19
### Adicionado
- Instalações de dependências

## [1.1.2] - 2025-02-25
### Adicionado
- Novas validações e conversões

## [0.1.1] - 2025-02-24
### Adicionado
- 🚀 Ajuste README

## [0.1.0] - 2025-02-24
### Adicionado
- 🚀 Primeira versão com limpeza de dados com excel toolkit for py.
