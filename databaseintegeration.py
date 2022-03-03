import mysql.connector
def DataUpdate(requirement, mockup, url, timeline, budget, name, email, phone):

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="information"
   )
  mycursor = mydb.cursor()
  sql='INSERT INTO info (requirement, mockup, url, timeline, budget, name, email, phone) VALUES ("{0}","{1}", "{2}","{3}","{4}","{5}","{6}","{7}","{8}");'.format(requirement,mockup,url,timeline,budget,name,email, phone)
  mycursor.execute(sql)
  mydb.commit()