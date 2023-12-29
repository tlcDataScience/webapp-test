from sqlalchemy import create_engine, text

db_connection_string = 'mysql+pymysql://nbkbui5m89g1n6xlqbzg:pscale_pw_7VOp7LslnMC5DNAUUAkyeAqFXfrkbyu56zpKD87EILF@aws.connect.psdb.cloud:3306/joviancareers?charset=utf8mb4'
engine = create_engine(
    db_connection_string,
    connect_args={
        'ssl': {
            'ssl_ca': '/etc/ssl/cert.pem'
        }
    })

def load_jobs_from_db():

    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
    return jobs
    