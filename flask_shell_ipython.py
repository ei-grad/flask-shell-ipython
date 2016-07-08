import os
import sys

import click

from flask.cli import with_appcontext


@click.command()
@with_appcontext
def shell():
    """Runs a shell in the app context.

    Runs an interactive Python shell in the context of a given
    Flask application. The application will populate the default
    namespace of this shell according to it's configuration.
    This is useful for executing small snippets of management code
    without having to manually configuring the application.
    """
    import IPython
    from flask.globals import _app_ctx_stack
    app = _app_ctx_stack.top.app
    banner = 'Python %s on %s\nIPython: %s\nApp: %s%s\nInstance: %s\n' % (
        sys.version,
        sys.platform,
        IPython.__version__,
        app.import_name,
        app.debug and ' [debug]' or '',
        app.instance_path,
    )

    ctx = {}

    # Support the regular Python interpreter startup script if someone
    # is using it.
    startup = os.environ.get('PYTHONSTARTUP')
    if startup and os.path.isfile(startup):
        with open(startup, 'r') as f:
            eval(compile(f.read(), startup, 'exec'), ctx)

    ctx.update(app.make_shell_context())

    IPython.embed(banner1=banner, user_ns=ctx)
