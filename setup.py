from setuptools import setup

setup(
    name="check-todo",
    version="1.0.5",
    py_modules=["check_todo"],
    install_requires=["pre-commit"],
    entry_points={
        "console_scripts": [
            "check-todo=check_todo:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A pre-commit hook to check for TODO comments in staged files.",
)
