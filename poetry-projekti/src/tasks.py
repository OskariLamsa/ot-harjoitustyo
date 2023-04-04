from invoke import task

@task
def start(ctx):
	ctx.run("python3 game.py", pty=True)
@task
def test(ctx):
	ctx.run("pytest", pty=True)
@task
def coverage_report(ctx):
	ctx.run("coverage run --branch -m pytest", pty=True)
	ctx.run("coverage report -m", pty=True)
	ctx.run("coverage html", pty=True)
