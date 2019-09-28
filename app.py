from datetime import datetime

from chalice import Chalice

from chalicelib.models import Question

app = Chalice(app_name='polls')


@app.route('/polls/questions', methods=['GET', 'POST'])
def questions():
    request = app.current_request
    if request.method == 'POST':
        question_text = request.json_body['question_text']
        pub_date = datetime.strptime(request.json_body['pub_date'], '%Y-%m-%d')
        question = Question(question_text=question_text, pub_date=pub_date)
        question.save()
        rep = {'question_text': question.question_text, 'id': question.id, 'pub_date': question.pub_date.strftime('%Y-%m-%d')}
        return rep
    elif request.method == 'GET':
        questions = Question.select()
        l = []
        for question in questions:
            l.append({'question_text': question.question_text, 'id': question.id, 'pub_date': question.pub_date.strftime('%Y-%m-%d')})
        return l

@app.route('/')
def index():
    return {'hello': 'duniya'}
