from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Banglore',
        'salary': '100000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Dehli',
        'salary': '1000000' 
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '200000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'USA',  
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                           companyname ="Jovian Careers"
                            )

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)