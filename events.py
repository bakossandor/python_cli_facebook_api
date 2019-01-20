from search import search
import click

@click.command()
@click.argument("city")
def cli(city):
    for place in search(city):
        click.echo(place["name"])