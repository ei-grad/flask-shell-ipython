from setuptools import setup
setup(
    name="flask-shell-ipython",
    author="Andrew Grigorev",
    author_email="andrew@ei-grad.ru",
    description="Replace default `flask shell` command by similar command running IPython.",
    url="http://github.com/ei-grad/flask-shell-ipython",
    version="0.4.0",
    py_modules=['flask_shell_ipython'],
    install_requires=[
        'flask>=1.0',
        'click',
        'IPython>=5.0.0',
    ],
    entry_points={
        'flask.commands': [
            'shell=flask_shell_ipython:shell',
        ],
    },
)
