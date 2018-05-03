import pymysql
from flask import redirect, request
from Python_Files.database_config import setDB

@app.route('/signup', methods = ['POST'])
def userLogIn():
    cursor = setDB()
    employee_name = request.form['fullname']
    nameDB = cursor.execute("SELECT employee_name FROM employees\n",
                            "WHERE employee_name = ?", (employee_name))
    if(employee_name == nameDB):
        return redirect('http://localhost:63342/project/employees.html')

    else:
        return redirect('http://localhost:63342/project/index.html')

if __name__ == '__main__':
    userLogIn()