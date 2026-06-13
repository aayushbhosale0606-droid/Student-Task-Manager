import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="4RBUcTRHeYRJodu.root",
        password="2zAR75RiWhGUDdCg",
        database="student_task_manage"
        )
    return connection