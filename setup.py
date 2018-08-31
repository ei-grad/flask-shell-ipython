from setuptools import setup
setup(
    name="flask-shell-ipython",
    author="Andrew Grigorev",
    author_email="andrew@ei-grad.ru",
    description="Replace default `flask shell` command by similar command running IPython.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="http://github.com/ei-grad/flask-shell-ipython",
    version="0.3.1",
    py_modules=['flask_shell_ipython'],
    install_requires=[
        'flask>=0.11',
        'click',
        'IPython>=5.0.0',
    ],
    entry_points={
        'flask.commands': [
            'shell=flask_shell_ipython:shell',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: Flask',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
