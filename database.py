
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