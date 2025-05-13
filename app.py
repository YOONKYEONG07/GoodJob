from flask import Flask, render_template, request, jsonify
from analyzer import analyze_resume

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

# ✅ 여기 추가
@app.route('/resume')
def resume_page():
    return render_template('resume.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['resume']
    result = analyze_resume(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
