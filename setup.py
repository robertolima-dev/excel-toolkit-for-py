from setuptools import find_packages, setup

setup(
    name="excel_toolkit_for_py",
    version="1.1.6",
    author="Roberto Lima",
    author_email="robertolima.izphera@gmail.com",
    description="📊 Facilite a leitura, manipulação, conversão, validação e exportação de arquivos Excel e CSV com Python.", # noqa501
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/robertolima-dev/excel-toolkit-for-py",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "openpyxl>=3.0.0",
    ],
    classifiers=[
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
    project_urls={
        "Homepage": "https://github.com/robertolima-dev/excel-toolkit-for-py", # noqa501
        "Repository": "https://github.com/robertolima-dev/excel-toolkit-for-py", # noqa501
        "Issues": "https://github.com/robertolima-dev/excel-toolkit-for-py/issues", # noqa501
    },
)
