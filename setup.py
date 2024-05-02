from setuptools import setup

setup(
    name="check-todo",
    version="1.0.0",
    py_modules=["check_todo"],
    entry_points={
        "console_scripts": [
            "check-todo=check_todo:main",
        ],
    },
    author="Ayo Lin",
    author_email="ayo1103@gmail.com",
    description="Checks for 'TODO' in staged files before committing.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)