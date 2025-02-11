from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Get cookies
    theme = request.cookies.get('theme', 'light')  # Default to light theme
    visit_count = int(request.cookies.get('visit_count', 0))
    username = request.cookies.get('username', 'Guest')

    # Increment visit count
    visit_count += 1

    # Personalize greeting
    greeting = f"Welcome back, {username}!" if username != 'Guest' else "Welcome, Guest!"

    # Prepare response
    response = make_response(render_template('index.html', theme=theme, visit_count=visit_count, greeting=greeting))

    # Set cookies
    response.set_cookie('theme', theme)
    response.set_cookie('visit_count', str(visit_count))
    response.set_cookie('username', username)

    return response

@app.route('/preferences', methods=['POST'])
def preferences():
    # Get form data
    theme = request.form.get('theme', 'light')
    username = request.form.get('username', 'Guest')

    # Prepare response
    response = make_response(render_template('preferences.html', theme=theme, username=username))

    # Set cookies
    response.set_cookie('theme', theme)
    response.set_cookie('username', username)

    return response

if __name__ == '__main__':
    app.run(debug=True)