
from invoke import task


@task
def upload(ctx):
    ctx.run('rm -rf dist build *.egg-info')
    ctx.run('python setup.py bdist')
    ctx.run('python setup.py bdist_wheel')
    ctx.run('twine upload dist/*')
    ctx.run('rm -rf dist build *.egg-info')


@task
def clean(ctx):
    ctx.run('rm -rf dist build *.egg-info')


@task
def uninstall_all(ctx):
    ctx.run('pip freeze | xargs pip uninstall --yes')
