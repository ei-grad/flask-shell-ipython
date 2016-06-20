from setuptools import setup
setup(
    name="flask-shell-ipython",
    author="Andrew Grigorev",
    author_email="andrew@ei-grad.ru",
    description="Replace default `flask shell` command by similar command running IPython.",
    url="http://github.com/ei-grad/flask-shell-ipython",
    version="0.1",
    py_modules=['flask_shell_ipython'],
    install_requires=[
        'flask>=0.11',
        'click',
        'IPython',
    ],
    entry_points={
        'flask.commands': [
            'shell=flask_shell_ipython:shell',
        ],
    },
)
