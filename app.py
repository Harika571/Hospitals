#step -1: importing modules
from flask import FLASK,render_template
import sqlite3
#step -2: app creation
app = Flask(__name__)
db_Name = "hospital.db"
#step -3: DB initialization
def init_db():
    conn = sqlite3.connect(db_Name)
    cursor = conn.cursor()
    cursor.execute('''
    create table if not EXISTS users(
    UID Integer Primary key AUTOINCREMENT,
    UNAME Text not NULL,
    Email Text CHECK(Email like  '%@gmail.com'),
    Phone Text not NULL,
    Role  Text DEFAULT 'demo_user',
    Specialization Text default 'NA',
    Experience Integer DEFAULT 2,
    Salary Real DEFAULT 5000
    );
    ''')
    #data seeding `users`
    cursor.execute('SELECT COUNT (*) FROM Users')
    if cursor.fetchone()[0] == 0:

        cursor.execute('''Insert into users(uname, email, phone, Specialization, role)' \
            values('Dhanush', 'DH@gmail.com', 8901239016, 'Cardio and neuro', 'surgeon doctor')
        ''')
        cursor.execute('''Insert into users(uname, email, phone, Specialization, role)' \
         values('Chiranjeevi', 'MStar@gmail.com', 8901239123, 'Physchartist', 'Therapist')
        ''')
        cursor.execute('''Insert into users(uname, email, phone, Specialization, role)' \
             values('Lingaran', 'LM@gmail.com', 8901239023, 'Gynachologist and Anthropedic', 'surgeon doctor')
        ''')
        cursor.execute('''Insert into users(uname, email, phone, Specialization, role)' \
           values('Suresh', 'SH@gmail.com', 8912349016, 'Cardio and neuro', 'surgeon doctor')
        ''')
        conn.commit()
    conn.close()  
#step -4:routing
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect(db_Name)
    cursor = conn.cursor()
    cursor.execute('''
        select * from users;
    ''')
    dataRecord = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', users=dataRecord)

#step -5:run & debug#step -1: importing modules
if __name__ == '__main__':
    init_db()
    app.run(debug=True,port=3000)