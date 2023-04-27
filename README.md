# Flask-Shell-IPython

`flask-shell-ipython` is a Python package that replaces the default `flask
shell` command with a similar command that runs IPython. This provides an
enhanced interactive Python shell with additional features like syntax
highlighting, tab-completion, and more.

## Installation

To install `flask-shell-ipython`, simply run:

```bash
pip install flask-shell-ipython
```

## Usage

After installing `flask-shell-ipython`, the `flask shell` command will
automatically use IPython instead of the default Python shell. There are no
additional steps required.

```bash
flask shell
```

You can also pass any valid IPython arguments after the `flask shell` command:

```bash
flask shell --no-banner -i foo.py
```

## Configuration

You can configure IPython settings by adding an `IPYTHON_CONFIG` key to your
Flask app's configuration. The value should be a dictionary containing the
configuration options you'd like to set.

For example:

```python
app.config['IPYTHON_CONFIG'] = {
    'InteractiveShell': {
        'colors': 'Linux',
        'confirm_exit': False,
    },
}
```

## Testing

To run tests for `flask-shell-ipython`, install the `pytest-forked` plugin,
which enables running tests in isolated forked subprocesses to ensure running a
clean IPython instance for each test case.

### Installing Dependencies

Install testing dependencies from `requirements-test.txt`:

```bash
pip install -r requirements-test.txt
```

### Running Tests

After installing the dependencies, run the test suite with the `--forked` option:

```bash
pytest --forked
```

Please, note that does pytest-forked does not work on Windows. To test
flask-shell-ipython on Windows run each test manually.

## License

`flask-shell-ipython` is licensed under the MIT License. See the
[LICENSE](LICENSE) file for more information.

## Contributing

If you'd like to contribute to the project, feel free to submit a pull request
on the GitHub repository at http://github.com/ei-grad/flask-shell-ipython.
