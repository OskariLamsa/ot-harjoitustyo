"""Tämä tekee testejä"""
from invoke import task


@task
def start(ctx):
    """Aukaise peli"""
    ctx.run("python3 game.py", pty=True)


@task
def test(ctx):
    """"suorita testit"""
    ctx.run("pytest", pty=True)


@task
def coverage_report(ctx):
    """Tee coverage raportti """
    ctx.run("coverage run --branch -m pytest", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)
