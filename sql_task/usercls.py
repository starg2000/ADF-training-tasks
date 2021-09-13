import datetime
import json
import mysql.connector
import config
from datetime import date
import logging
logging.basicConfig(filename="box.log", format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

class Userdata:
    '''userdata functions'''
    def __init__(self,idata):
        self.firstname = idata[0]
        self.lastname=idata[1]
        self.dob=idata[2]
        self.gender=idata[3]
        self.nationality=idata[4]
        self.city=idata[5]
        self.state=idata[6]
        self.pin=idata[7]
        self.qualification=idata[8]
        self.salary=idata[9]
        self.pan=idata[10]
        self.reqid=None

    def getconobj(self):
        """connection object"""
        try:
            mydb = mysql.connector.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.database)
            return mydb
        except Exception as error:
            #logging.error(error)
            print(error)

    def creattable(self):
        """table creation"""
        try:
            dbobj=self.getconobj()
            cursor=dbobj.cursor()
            cursor.execute("create table if not exists Request_info( ID int AUTO_INCREMENT primary key, First_Name varchar(50),\
                Last_Name varchar(50), DOB date, Gender char(30), Nationality char(30), Current_City char(30),\
                State char(30), Pincode int(10), Qualification varchar(50), Salary int(10),\
                PAN_Number varchar(20) unique, request_receive_time date)")
            cursor.execute("create table if not exists Response_info( EID int AUTO_INCREMENT primary key,\
                response varchar(100), id int, reason varchar(200), foreign key(id) references request_info(id))")
            dbobj.commit()
            logging.info("tables created successfully")
        except:
            logging.error("creation table error")

    def insertdata(self):
        try:
            dbobj = self.getconobj()
            cursor = dbobj.cursor(prepared=True)
            time = date.today()
            cursor.execute("insert into Request_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
                           (None, self.firstname, self.lastname, self.dob, self.gender,\
                 self.nationality, self.city, self.state, self.pin, self.qualification, self.salary, self.pan, time))
            dbobj.commit()
        except Exception as error:
            logging.error(error)

    def validage(self):
        """validating age"""
        year, month, day = map(int, self.dob.split('-'))
        birthDate = date(year, month, day)
        today = date.today()
        age = today.year - birthDate.year - ((today.month, \
            today.day) < (birthDate.month, birthDate.day))
        if self.gender == 'male':
            if age > 21:
                return True
        if self.gender == 'female':
            if age > 18:
                return True
        return False

    def validnation(self):
        if self.nationality in ['Indian', 'American']:
            return True
        return False

    def validstate(self):
        if self.state in ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam, Bihar', \
            'Chhattisgarh', 'Karnataka', 'Madhya Pradesh', 'Odisha', 'Tamil Nadu', 'Telangana', 'West Bengal']:
            return True
        return False

    def validsalary(self):
        if 10000 < self.salary < 90000:
            return True
        return False

    def insertresponse(self):
        try:
            dbobj = self.getconobj()
            cursor = dbobj.cursor()
            cursor.execute("select id from request_info where PAN_Number = %s",(self.pan,))
            data=cursor.fetchall()
            self.reqid = data[0][0]
            response=''
            reason=''
            if not self.validage():
                reason+='Age not valid '
            if not self.validnation():
                reason+="Invalid nation "
            if not self.validstate():
                reason+="Inavalid state "
            if not self.validsalary():
                reason+="salary not valid "
            if reason == '':
                response+="success"
            else:
                response+="failure"
            cursor.execute("insert into response_info values(%s,%s,%s,%s)",\
                (None, response, self.reqid, reason))
            dbobj.commit()
            js = {"Request_id": self.reqid, "response":response, "reason": reason}
            logging.info(json.dumps(js))
        except Exception as error:
            logging.error(error)

if __name__ == "__main__":
    '''inputs'''
    firstname = input("Firstname:")
    lastname = input("Lastname:")
    dob = input("dob(yyyy-mm-dd):")
    gender = input("gender:")
    nationality = input("nationality:")
    current_city = input("city:")
    state = input("state:")
    pin_code = int(input("pincode:"))
    qualification = input("qualification:")
    salary = int(input("salary:"))
    pan = input("PAN:")
    listin=[firstname,lastname,dob,gender,nationality,current_city,\
                  state,pin_code,qualification,salary,pan]
    obj=Userdata(listin)
    obj.creattable()
    obj.insertdata()
    obj.insertresponse()










