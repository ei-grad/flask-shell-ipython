import pytest
from click.testing import CliRunner
from flask import Flask

from flask_shell_ipython import shell


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app


@pytest.fixture
def runner(app):
    return CliRunner()


def test_shell_command(runner, app):
    with app.app_context():
        result = runner.invoke(shell)
    assert result.exit_code == 0
    assert "IPython" in result.output


def test_shell_command_no_banner(runner, app):
    with app.app_context():
        result = runner.invoke(shell, ["--no-banner", "--no-confirm-exit"])
    assert result.exit_code == 0
    assert result.output == "\nIn [1]: "


def test_shell_command_with_custom_config(runner, app):
    app.config["IPYTHON_CONFIG"] = {
        "InteractiveShell": {"confirm_exit": False},
        "TerminalIPythonApp": {"display_banner": False}
    }
    with app.app_context():
        result = runner.invoke(shell)
    assert result.exit_code == 0
    assert result.output == "\nIn [1]: "
