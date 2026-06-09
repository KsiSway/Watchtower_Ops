import os
import subprocess

env = os.environ.copy()
cmd = [
    'git', 'filter-branch', '-f', '--env-filter',
    'export GIT_AUTHOR_NAME="ksisway"\nexport GIT_AUTHOR_EMAIL="cleeman1989@gmail.com"\nexport GIT_COMMITTER_NAME="ksisway"\nexport GIT_COMMITTER_EMAIL="cleeman1989@gmail.com"',
    'HEAD'
]
subprocess.run(cmd, env=env)
