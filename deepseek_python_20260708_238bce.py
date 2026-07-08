from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the magic square game"""
    return render_template('index.html')

# For Vercel serverless deployment
def handler(request):
    return app(request)

# For local development
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)