from setuptools import setup
setup(
    name="Flask Shell IPython",
    version="0.1",
    py_modules=['flask_shell_ipython'],
    entry_points={
        'flask.commands': [
            'shell=flask_shell_ipython:shell',
        ],
    },
)
