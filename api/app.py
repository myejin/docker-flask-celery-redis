from flask import Flask, url_for
from celery import states
from worker import my_celery 

app = Flask(__name__)

@app.route('/')
def root():
    return 'OK'

@app.route('/add/<param1>/<param2>')
def add(param1, param2):
    task = my_celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    resp = f'{task.id} >> <a href="{url_for("check_task", task_id=task.id)}">진행상황 보러가기</a>'
    return resp 

@app.route('/check/<task_id>')
def check_task(task_id):
    resp = my_celery.AsyncResult(task_id) 
    if resp.state == states.PENDING:
        return f'아직 더하는 중.. {resp.state}..'
    else:
        return f'완료 >> {resp.result}'


if __name__ == '__main__':
    app.run() 