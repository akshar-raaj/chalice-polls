from chalice import Chalice

app = Chalice(app_name='polls')


@app.route('/')
def index():
    return {'hello': 'world'}
