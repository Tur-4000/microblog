from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Вася'}
    return '''
<!DOCTYPE html>
<html>
    <head>
        <title>Домашняя страница - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
