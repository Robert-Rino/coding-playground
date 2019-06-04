from celery import Celery, group

app = Celery('test_tasks', broker='pyamqp://guest:guest@localhost//', backend='rpc://')

@app.task
def add(x,y):
    return x+y

@app.task
def total_sum(numbers):
    return sum(numbers)

job = group([
    add.s(2,2),
    add.s(4,4),
    add.s(8,8),
    add.s(16,16),
    add.s(32,32),
    add.s(64,64),])

