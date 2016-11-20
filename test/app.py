import hug


@hug.get('/0')
def divide_by_zero():
    return 1 / 0


api = hug.API(__name__)
