

import pymysql

# Create a connection object

dbServerName    = "172.17.0.2"

dbUser          = "root"

dbPassword      = "password"

dbName          = "codemenu"

charSet         = "utf8mb4"

cusrorType      = pymysql.cursors.DictCursor


# This connection uses default curser connection returning just row data as a array - goes with loop number1
# con = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName)


# This connection using the cursurcursur dictionary class returning data in a dictionary format with column name as ket and row data - goes with loop number 2
con = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName, charset=charSet,cursorclass=cusrorType)


with con:
    
    cur = con.cursor()
    cur.execute("SELECT * FROM bumble;")

    result = cur.fetchall()
    #print(result)
    #print(result[2]) 
    print(result)

    #loop number 1 - loops through the tuple object
    # for row in result:
        #print(row[0])
        #print(row[1])
        #print(row[2])


    #loop number 2 -  loops through the dictiony object
    for row in result:
        print(row["id"])
        print(row["breed"])
        print(row["age"])

        



    