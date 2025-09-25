from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! This is a simple Flask web application deployed via Azure DevOps.'

@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Application is running successfully'}

@app.route('/info')
def app_info():
    return {
        'app': 'Hello World Flask App',
        'version': '1.0.0',
        'environment': os.environ.get('ENVIRONMENT', 'development')
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
