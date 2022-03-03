from urllib.parse import ParseResult

import click

from ..cli import db_cli
from .alembic_runner import run_alembic


@db_cli.command(
    "alembic",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def alembic_cli(ctx: click.Context, args):
    """Run commands directly with alembic (type -h for alembic options)."""
    db_url: ParseResult = ctx.obj["db_url"]

    run_alembic(db_url.geturl(), args)
    return 0
