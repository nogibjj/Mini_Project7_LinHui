from setuptools import setup

setup(
    name="Mini_Project7_LinHui",
    version="0.1",
    py_modules=["main"],
    install_requires=[

    ],
    package_data={
        "": ["Deaths&Insurance.db"],
    },
    entry_points={
        "console_scripts": [
            "SQL-tool = main:main",
        ],
    },
)
