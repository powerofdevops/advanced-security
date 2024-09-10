# Sample Python Application with Vulnerable Dependency

# Requirements File (requirements.txt)
#
# Flask==0.12.3  # Vulnerable version with known security issues

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
