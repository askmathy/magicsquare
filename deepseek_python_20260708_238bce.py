from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the magic square game interface"""
    return render_template('index.html')

@app.route('/api/status')
def status():
    """Simple API endpoint for health check"""
    return jsonify({
        'status': 'online',
        'game': 'Magic Square 3x3',
        'version': '1.0.0'
    })

# Vercel requires this handler
def handler(request):
    return app(request)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
