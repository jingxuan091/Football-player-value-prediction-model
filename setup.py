from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='shopping_for_players',
      version="0.0.10",
      description="predicts football players transfer value",
      author="Andrea, Andrew, Jin",
      install_requires=requirements,
      packages=find_packages()
      )
