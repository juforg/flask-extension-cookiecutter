import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.extension_slug}}"""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.extension_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
