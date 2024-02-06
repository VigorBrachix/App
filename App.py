from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('applications', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000)