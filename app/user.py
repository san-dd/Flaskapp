from app import app

@app.route('/user')
def user():
    return "User page"
