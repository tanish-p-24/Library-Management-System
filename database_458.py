# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pes1ug20cs458_project"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS TRAIN(train_no TEXT, train_name TEXT,  train_type TEXT, source TEXT,dst TEXT, avail TEXT)')


def add_data_book(id,name,det,auth,pub,branch,price,quan,avail,rent):
    c.execute('INSERT INTO BOOK(`id`, `bookname`, `bookdetail`, `bookauthor`, `bookpub`, `branch`, `bookprice`, `bookquantity`, `bookava`, `bookrent`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (id,name,det,auth,pub,branch,price,quan,avail,rent))
    mydb.commit()



def add_data_user(id,name,email,password,type):
    c.execute('INSERT INTO USER(`id`, `name`, `email`, `password`, `type`) VALUES (%s,%s,%s,%s,%s)',
              (id,name,email,password,type))
    mydb.commit()


def add_data_issuebook(id,userid,issuename,issue_book,issuetype,days,issuedate,issuereturn,fine):
    c.execute('INSERT INTO ISSUEBOOK(`id`,`userid`,`issuename`,`issuebook`,`issuetype`,`issuedays`,`issuedate`,`issuereturn`,`fine`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (id,userid,issuename,issue_book,issuetype,days,issuedate,issuereturn,fine))
    mydb.commit()

def add_data_requestbook(id,userid,bookid,username,usertype,bookname,days):
    c.execute('INSERT INTO REQUESTBOOK(`id`,`userid`,`bookid`,`username`,`usertype`,`bookname`,`issuedays`) VALUES (%s,%s,%s,%s,%s,%s,%s)',
              (id,userid,bookid,username,usertype,bookname,days))
    mydb.commit()


def view_all_books():
    c.execute('SELECT * FROM BOOK')
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM USER')
    data = c.fetchall()
    return data

def view_issue():
    c.execute('SELECT * FROM ISSUEBOOK')
    data = c.fetchall()
    return data

def view_request():
    c.execute('SELECT * FROM REQUESTBOOK')
    data = c.fetchall()
    return data


def view_only_books():
    c.execute('SELECT bookname FROM BOOK')
    data = c.fetchall()
    return data

def view_only_users():
    c.execute('SELECT name FROM USER')
    data = c.fetchall()
    return data


def get_dealer(train_name):
    c.execute('SELECT * FROM TRAIN WHERE train_name="{}"'.format(train_name))
    data = c.fetchall()
    return data

def get_user(name):
    c.execute('SELECT * FROM USER WHERE name="{}"'.format(name))
    data = c.fetchall()
    return data

def get_book(name):
    c.execute('SELECT * FROM BOOK WHERE bookname="{}"'.format(name))
    data = c.fetchall()
    return data


def edit_book_data(bookname,bookprice,bookquan):
    c.execute("UPDATE BOOK SET bookprice=%s, bookquantity=%s WHERE bookname=%s", (bookprice,bookquan,bookname))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(train_name):
    c.execute('DELETE FROM TRAIN WHERE train_name="{}"'.format(train_name))
    mydb.commit()
