import click
import os
import Lynx.utils.config as config

from Lynx import cli
from Lynx.utils.log import *
from Lynx.utils.language import cpp
from Lynx.utils.constants import CPP_STANDARDS, CHECKERS, VALIDATORS


@cli.command()
@click.argument("problem", type=click.Path())
@click.option(  # language
    "--language",
    default="c++14",
    help="The language used when generating data.",
    type=click.Choice(CPP_STANDARDS),
)
@click.option(  # checker
    "--checker",
    type=click.Choice(CHECKERS),
    default="custom",
    help="Use a checker (special judge). You can specify the checker provided by testlib or use your customized checker by just giving a flag.",
)
@click.option(  # validator
    "--validator",
    type=click.Choice(VALIDATORS),
    default="custom",
    help="Use a validator. You can also use the validator provided by testlib in a similar way as the checker.",
)
def init(problem, language, checker, validator):
    """This command initializes a lynx problem directory."""
    # Turn the problem path into an absolute path
    if not os.path.isabs(problem):
        problem = os.path.join(os.getcwd(), problem)
    debug(f"problem route is {problem}")
    if os.path.exists(problem):
        error_and_exit(f"Problem directory {problem} already exists.")
    if language in CPP_STANDARDS:
        cpp.init_problem(problem, language, checker, validator)
