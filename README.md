# 📚 **excel-toolkit-for-py - Manipulação e Conversão Avançada de Arquivos Excel**

📊 **excel-toolkit-for-py** é um pacote Python completo que facilita a **leitura, manipulação, validação e conversão de arquivos Excel e CSV**, utilizando `pandas` e `openpyxl`. Ideal para automações robustas envolvendo planilhas!

---

## ✨ **Principais Funcionalidades**

- 📥 **Leitura de arquivos Excel (`.xlsx`) e CSV (`.csv`).**
- 📤 **Exportação de DataFrames para Excel e CSV.**
- 🔄 **Conversão entre Excel e JSON.**
- 🔗 **Junção e divisão de arquivos Excel.**
- 🛡️ **Validações automatizadas de dados e esquemas.**
- 📊 **Suporte a múltiplas planilhas.**
- ✅ **Integração com `pytest` para testes automatizados.**
- 🔒 **Suporte a arquivos Excel protegidos por senha.**
- 📝 **Validação de células vazias.**
- 🎨 **Formatação condicional.**
- 📈 **Manipulação de fórmulas e gráficos.**
- 📦 **Exportação para múltiplos formatos (JSON, XML, HTML, PDF).**

---

## ⚡ **Instalação**

Instale o pacote via **PyPI**:

```bash
pip install excel_toolkit_for_py
```

> 💡 As dependências `pandas`, `openpyxl`, `msoffcrypto-tool`, `xlrd`, `xlwt`, `weasyprint`, `jinja2`, `numpy` e `scipy` são instaladas automaticamente.

---

## 🚀 **Como Usar**

### 📥 **Leitura de Arquivos Excel e CSV**

```python
from excel_toolkit_for_py.reader import read_excel, read_csv, get_sheet_names, get_dict_sheets

sheet_names = get_sheet_names("dados.xlsx")
print(sheet_names) # ['Sheet1', 'Sheet2']

# Retorna um dicionário com todas as abas
sheet_names = get_dict_sheets("dados.xlsx", sheet_name=None)
print(sheet_names)

# Lendo um arquivo Excel
df_excel = read_excel("dados.xlsx", sheet_name="Sheet1")
print(df_excel.head(10)) # Retorna os 10 primeiros registros
print(df_excel.tail(8)) # Retorna os 8 últimos registros
print(df_excel.to_string()) # Converte a planilha toda para string
print(df_excel) # Todos os dados, porém se a planilha for grande, trunca

# Lendo um arquivo CSV
df_csv = read_csv("dados.csv")
print(df_csv.head())
```

---

### 📤 **Exportação de DataFrames para Excel e CSV**

```python
from excel_toolkit_for_py.writer import write_excel, write_csv
import pandas as pd

df = pd.DataFrame({
    "Nome": ["Alice", "Bob", "Carlos"],
    "Idade": [25, 30, 22]
})

write_excel(df, "saida.xlsx", sheet_name="Usuarios")
write_csv(df, "saida.csv")
```

---

### 📤 **Converter uma lista em Excel**

```python
from excel_toolkit_for_py.writer import write_list_to_excel

data = [["Nome", "Idade", "Cidade"],
         ["Alice", 25, "São Paulo"],
         ["Carlos", 30, "Rio de Janeiro"],
         ["Mariana", 22, "Belo Horizonte"]]

write_list_to_excel("dados.xlsx", data)
print("Arquivo Excel criado com sucesso!")
```

---

### 🔄 **Conversão: Excel para JSON e vice-versa**

```python
from excel_toolkit_for_py.conversions import excel_to_json, json_to_excel

# Excel -> JSON
json_data = excel_to_json("dados.xlsx")
print(json_data)

# JSON -> Excel
json_to_excel(json_data, "novo_dados.xlsx")
```

---

### 🛡️ **Validação de Estrutura e Dados**

```python
from excel_toolkit_for_py.validations import validate_excel_schema

schema = {"Nome": str, "Idade": int}
validacao = validate_excel_schema("dados.xlsx", schema)
print("✅ Validação bem-sucedida!" if validacao else "❌ Validação falhou.")
```

---

### 🔒 **Trabalhando com Arquivos Protegidos**

```python
from excel_toolkit_for_py.advanced_features import read_protected_excel, protect_excel

# Ler um arquivo protegido
df = read_protected_excel("arquivo_protegido.xlsx", password="minha_senha")

# Proteger um arquivo
protect_excel("arquivo.xlsx", password="nova_senha")
```

---

### 📝 **Validação de Células Vazias**

```python
from excel_toolkit_for_py.advanced_features import validate_empty_cells

# Validar células vazias
resultado = validate_empty_cells(df, threshold=0.1)
print(f"Células vazias: {resultado['empty_cells']}")
print(f"Colunas com muitas células vazias: {resultado['columns_above_threshold']}")
```

---

### 🎨 **Formatação Condicional**

```python
from excel_toolkit_for_py.advanced_features import apply_conditional_formatting

# Aplicar formatação condicional
regras = [{
    'range': 'A1:C10',
    'type': 'cellIs',
    'operator': '>',
    'formula': '30',
    'format': {
        'fill': 'FF0000',
        'font': {'bold': True}
    }
}]

apply_conditional_formatting("arquivo.xlsx", regras)
```

---

### 📈 **Manipulação de Fórmulas e Gráficos**

```python
from excel_toolkit_for_py.advanced_features import extract_formulas, add_chart

# Extrair fórmulas
formulas = extract_formulas("arquivo.xlsx")
print(f"Fórmulas encontradas: {formulas}")

# Adicionar gráfico
add_chart(
    file_path="arquivo.xlsx",
    chart_type="bar",
    data_range="A1:B10",
    title="Meu Gráfico"
)
```

---

### 📦 **Exportação para Múltiplos Formatos**

```python
from excel_toolkit_for_py.exporters import to_json, to_xml, to_html, to_pdf
import pandas as pd

# Criar dados de exemplo
df = pd.DataFrame({
    "Nome": ["Alice", "Bob", "Carlos"],
    "Idade": [25, 30, 22],
    "Cidade": ["São Paulo", "Rio", "BH"]
})

# Exportar para JSON
to_json(df, "dados.json")

# Exportar para XML
to_xml(df, "dados.xml")

# Exportar para HTML (com template opcional)
to_html(df, "dados.html", template_path="template.html")

# Exportar para PDF (com template opcional)
to_pdf(df, "dados.pdf", template_path="template.html")
```

Template HTML de exemplo (`template.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Relatório de Dados</title>
    <style>
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
    </style>
</head>
<body>
    <h1>Relatório de Dados</h1>
    {{ data.to_html(index=False, classes='table') }}
</body>
</html>
```

---

### 📊 **Análise de Dados: Estatísticas, Outliers, Correlações e Pivot Table**

```python
from excel_toolkit_for_py.data_analysis import (
    calculate_basic_stats, detect_outliers, calculate_correlations, create_pivot_table
)
import pandas as pd

# Exemplo de DataFrame
sample_df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 100],  # Inclui outlier
    'B': [10, 20, 30, 40, 50, 60],
    'C': ['a', 'b', 'c', 'd', 'e', 'f'],
    'D': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
})

# Estatísticas básicas
stats = calculate_basic_stats(sample_df)
print(stats)

# Detecção de outliers
outliers = detect_outliers(sample_df, method='zscore', threshold=2.0)
print(outliers)

# Correlações
corr = calculate_correlations(sample_df)
print(corr)

# Tabela dinâmica (pivot table)
pivot = create_pivot_table(
    sample_df,
    index='C',
    values=['A', 'B'],
    aggfunc='mean'
)
print(pivot)
```

---

## 🧪 **Testes**

Execute os testes unitários com **pytest**:

```bash
pytest tests/ --maxfail=1 --disable-warnings -v
```

---

## 🏗 **Estrutura do Projeto**

```
excel_toolkit/
│
├── excel_toolkit_for_py/                # 📦 Código do pacote
│   ├── __init__.py
│   ├── reader.py            # 📥 Funções de leitura
│   ├── writer.py            # 📤 Funções de exportação
│   ├── conversions.py       # 🔄 Funções de conversão Excel <-> JSON
│   ├── validations.py       # 🛡️ Funções de validação de dados
│   ├── advanced_features.py # 🔧 Funções avançadas
│   ├── data_analysis.py     # 📊 Funções de análise de dados
│   ├── exporters.py         # 📤 Funções de exportação
│   ├── utils.py             # 🛠️ Funções utilitárias
│
├── tests/                   # 🧪 Testes unitários
│   ├── test_reader.py
│   ├── test_writer.py
│   ├── test_conversions.py
│   ├── test_validations.py
│   ├── test_advanced_features.py
│   ├── test_data_analysis.py
│   ├── test_exporters.py
│
├── pyproject.toml           # ⚙️ Configuração do pacote
├── README.md                # 📚 Documentação do projeto
├── LICENSE                  # 📜 Licença MIT
└── MANIFEST.in              # 📋 Inclusão de arquivos extras
```

---

## 📝 **Licença**

Distribuído sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 **Autor**

Desenvolvido por **[Roberto Lima](https://robertolima-developer.vercel.app/)** 🚀✨

---

## 💬 **Contato**

- 📧 **Email**: robertolima.izphera@gmail.com
- 💼 **LinkedIn**: [Roberto Lima](https://www.linkedin.com/in/roberto-lima-01/)
- 💼 **Website**: [Roberto Lima](https://robertolima-developer.vercel.app/)
- 💼 **Gravatar**: [Roberto Lima](https://gravatar.com/deliciouslyautomaticf57dc92af0)

---

## ⭐ **Gostou do projeto?**

Deixe uma ⭐ no repositório e compartilhe com a comunidade! 🚀✨
