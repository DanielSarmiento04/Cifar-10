from fastapi import FastAPI

app = FastAPI(
    title="Cifar 10 Api",
    description='''
    This is a simple api for cifar 10 dataset.

    The classes trainer are the next:

    - airplane
    - automobile
    - bird
    - cat
    - deer
    - dog
    - frog
    - horse
    - ship
    - truck
    ''',
    version="1.0",

)

from .views import *