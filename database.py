
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECT_STR']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
       "ssl_ca": "/etc/ssl/cert.pem"
    }
  }                      
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs_list = []
    # loop through list 
    for row in result.all():
      # list of jobs
      jobs_list.append(row._asdict())
    return jobs_list

def load_job_from_db(id, application):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"select * from jobs where id = {id}")   
      )
    rows = result.all()
    if len(rows) == 0:
      return None 
    else:
      return rows[0]._asdict()

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query,
                 job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url']
                )
  #print("type(result):", type(result))
  #result_all = result.all()
  #print("type(result.all):", type(result_all))
  #print("result.all():", result_all)
  # first element in list
  #first_result = result_all[0]
  #print("type first_result:", type(first_result))
  # convert row into dict
  #first_result_dict = result_all[0]._asdict()
  #print("type first_result_dict:", type(first_result_dict))
  #print(first_result_dict)