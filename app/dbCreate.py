import psycopg2

def createDB(dbName):
    conn = psycopg2.connect(database="postgres", user='postgres', password='postgres123', host='3.109.216.6', port='5432')
    conn.autocommit = True
    cursor = conn.cursor()
    sql = "create database " + dbName + ";"
    try:
        cursor.execute(sql)
        return("<p style='color: green; font-size: 30px;'>{0} database created successfully</p>".format(dbName))
    except:
        return("<p style='color: red; font-size: 30px;'>{0} database already present</p>".format(dbName))
    conn.close()
