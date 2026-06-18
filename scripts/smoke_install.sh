#!/usr/bin/env bash
# Builda o wheel e instala numa venv limpa (sem deps de dev) para pegar
# dependências/entry points que só faltam fora do ambiente de desenvolvimento.
# Faz um teste FUNCIONAL (escreve/lê um CSV de verdade), não só import --
# um import limpo não pega bugs de dependências com bindings nativos
# (ver o caso do bcrypt/passlib no SmartSecurityPy).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

rm -rf dist build
rm -rf ./*.egg-info 2>/dev/null || true
python -m build

VENV_DIR="$(mktemp -d)/venv"
python -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install -q "$(ls dist/*.whl)"

"$VENV_DIR/bin/python" -c "
import tempfile, os
import pandas as pd
from excel_toolkit_for_py.writer import write_csv
from excel_toolkit_for_py.reader import read_csv

df = pd.DataFrame({'a': [1, 2], 'b': ['x', 'y']})
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, 'out.csv')
    write_csv(df, path)
    loaded = read_csv(path)
    assert list(loaded['a']) == [1, 2]
print('IMPORT + FUNCTIONAL OK')
"

rm -rf "$(dirname "$VENV_DIR")"
echo "Smoke test passou."
