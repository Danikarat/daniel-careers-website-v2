from flask import Flask, jsonify, render_template, send_from_directory
from database import engine
from sqlalchemy import text
app = Flask(__name__)


def load_jobs_from_db():
  conn = engine.connect()
  with conn:
    result = conn.execute(text("select * from jobs"))
    
    jobs = []
    for row in result.all():
        jobs.append(dict(row))
    return jobs    
    

@app.route('/')
def hello_world():
  jobs = load_jobs_from_db
  return render_template('home.html',
                         jobs= jobs,
                        )
  
  
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

@app.route('/images/<path:filename>')
def serve_image(filename):
  return send_from_directory('static', filename)

if __name__ =="__main__":
  app.run(host = '0.0.0.0', debug=True)