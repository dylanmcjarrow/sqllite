from pathlib import Path
from typing import List

import alembic.config


def run_alembic(db_url: str, args: List[str]):
    cmdline = alembic.config.CommandLine(prog=".".join(__name__.split(".")[:-1]))

    options = cmdline.parser.parse_args(args)
    if not hasattr(options, "cmd"):
        cmdline.parser.error("too few arguments")

    conf_file = options.config
    if not "-c" in args:
        conf_file = Path(__file__).parent.joinpath("alembic.ini").as_posix()

    cfg = alembic.config.Config(
        file_=conf_file,
        ini_section=options.name,
        cmd_opts=options,
    )
    cfg.set_main_option("script_location", Path(__file__).parent.as_posix())
    cfg.set_main_option("sqlalchemy.url", db_url)

    cmdline.run_cmd(cfg, options)
