from setuptools import setup, find_packages

setup(
    name="excelify",
    version="0.1.0",
    install_requires=[
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0"
    ],
    author="Roberto Lima",
    author_email="robertolima.izphera@gmail.com",
    description="📊 Facilite a leitura, manipulação e exportação de arquivos Excel e CSV com Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/robertolima-dev/excelify",
    packages=find_packages(),
    install_requires=[                      # 🔗 Dependências do projeto
        "pandas>=1.0.0",
        "openpyxl>=3.0.0",
        "pytest>=6.0.0"                    # Para execução dos testes
    ],
    classifiers=[                           # 🎯 Classificações para PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    license="MIT", 
)
