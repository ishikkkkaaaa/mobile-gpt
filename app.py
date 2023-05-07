from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# route for handling control commands
@app.route('/rotate')
def rotate():
    cmd = request.args.get('cmd')
    if cmd == 'left':
        # Rotate left code here
        pass
    elif cmd == 'right':
        # Rotate right code here
        pass
    else:
        return 'Invalid command'

if __name__ == '__main__':
    app.run(debug=False)
