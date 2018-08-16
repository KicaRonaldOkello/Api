from flask import Flask, jsonify, request
app = Flask(__name__)

empDB = [
    {
        'id':'101',
        'name':'Saraavan Kica',
        'title':'Inspection Engineer'
    },
    {
        'id':'201',
        'name':'Rajukumar Okello',
        'title':'Junior dev'
    }
]

@app.route('/empdb/employee/<empId>', methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId)]
    return jsonify({'emps':usr})

@app.route('/empdb/employee', methods=['POST'])
def createEmp():
    dat = {
        'id':request.json['id'],
        'name':request.json['name'],
        'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>', methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId)]
    if len(em) == 0
        abort(404)

    empDB.remove(em[0])
    return jsonify({'response':'Success'})



if __name__ == '__main__':
    app.run()