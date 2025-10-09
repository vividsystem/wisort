from pathlib import Path
from config import loaded
from files import move
from files.sort import by_extension
from files.move import lib_map
from time import sleep
import typer

app = typer.Typer(
    help="""
🪄 wisort — The Magical File Sorting Companion

Sort, cleanse, and enchant your files with a touch of magic.
"""
)


def target_arg():
    return typer.Argument(
        Path.cwd(),
        help="Directory to sort (default: current directory)",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    )


def dry_run_opt():
    return typer.Option(False, "--dry-run", "-d", help="Simulate actions")


def verbose_opt():
    return typer.Option(False, "--verbose", "-v", help="Verbose output")


def quiet_opt():
    return typer.Option(False, "--quiet", "-q", help="Suppress non-critical output")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


@app.command(
    help="🪶 The magical apprentice that sorts your library of spellbooks and as you tell him"
)
def apprentice(
    target: Path = target_arg(),
    verbose: bool = verbose_opt(),
    quiet: bool = quiet_opt(),
):
    if not quiet:
        print("""
            The apprentice stubles into your condominium sleepily.
        """)
    if len(loaded.libraries) == 0:
        if not quiet:
            print("""
            After a considerable amount of time searching for a library in your humble abode the apprentice realises there isn't one. 
            The apprentice sighs...    
            'Where does master keep sending me?', he said to himself as he left your dwelling visibly frustrated.
            """)
        return

    if not quiet:
        print(f"""
            Your {len(loaded.libraries.keys())} libraries excite the apprentice as he gazes at the rows of neatly stored books in all the bookshelves
        """)
        print("""
            After a brief moment of reviewing your books he snorts. 
            'Oh man the people nowadays really don't have structure in their libraries. I can see why my master sent me'
            """)
    sorted = by_extension(target, loaded)
    l_map = lib_map(loaded.libraries)

    # future refactor maybe: replace l_map[k] by format_dest(l_map[k], path) or something to make formatting of the filename and options like flatten easier to implement
    dest_map = {
        path.absolute(): l_map[k]
        for k, paths in sorted.items()
        if k in l_map
        for path in paths
    }

    if not quiet:
        print(f"""
            Ensuing a quick inspection of your spellbooks he realised there where only {len(dest_map)} books that needed organizing.
        """)

        for path, dest in dest_map.items():
            print(f"""          {path.relative_to(target)} → {dest}""")

        print("""
            He remembered a nice spell his master thaught him the previous day to levitate and move objects.
            After an astoundingly high number of attempts he finally managed to move all books to their destinations using the spell. 
            Unsatisfied he sighed: 'If only I had done this normally without spells I would long be home by now.'.
            """)

    move(dest_map, loaded)

    if loaded.orders.dedupe:
        pass

    return


@app.command(
    help="🔮 Keeps your spellbooks and library organized for you as he was thaught."
)
def magician(
    target: Path = target_arg(),
    dry_run: bool = dry_run_opt(),
    verbose: bool = verbose_opt(),
    quiet: bool = quiet_opt(),
):
    print("A fully certified magician does your work")


@app.command(help="🧹 Full spellbook: sort, dedupe, and format code")
def witch(
    target: Path = target_arg(),
    verbose: bool = verbose_opt(),
    quiet: bool = quiet_opt(),
):
    pass
