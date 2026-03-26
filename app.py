from flask import Flask, request, jsonify
from model import match_skills

app = Flask(__name__)

@app.route('/')
def home():
    return "SkillSync AI Running"

@app.route('/match', methods=['POST'])
def match():
    data = request.json

    resume = data.get("resume", "")
    job_desc = data.get("job_description", "")

    score = match_skills(resume, job_desc)

    return jsonify({
        "match_score": score,
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)
