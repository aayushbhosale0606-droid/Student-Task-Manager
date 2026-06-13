import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="2m4FnyFux21aQ6Z.root",
        password="sQTHbGnSCJMyKY6c",
        database="student_task_manager"
        )
    return connection