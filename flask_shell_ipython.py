import sys

import click
from flask.cli import with_appcontext


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument("ipython_args", nargs=-1, type=click.UNPROCESSED)
@with_appcontext
def shell(ipython_args):
    """Runs a shell in the app context.

    Runs an interactive Python shell in the context of a given
    Flask application. The application will populate the default
    namespace of this shell according to its configuration.
    This is useful for executing small snippets of management code
    without having to manually configure the application.
    """
    import IPython
    from IPython.terminal.ipapp import load_default_config
    from traitlets.config.loader import Config
    from flask.globals import current_app as app

    if "IPYTHON_CONFIG" in app.config:
        config = Config(app.config["IPYTHON_CONFIG"])
    else:
        config = load_default_config()

    config.TerminalInteractiveShell.banner1 = f"""Python {sys.version} on {sys.platform}
IPython: {IPython.__version__}
App: {app.import_name}{' [debug]' if app.debug else ''}
Instance: {app.instance_path}
"""

    IPython.start_ipython(
        argv=ipython_args,
        user_ns=app.make_shell_context(),
        config=config,
    )
