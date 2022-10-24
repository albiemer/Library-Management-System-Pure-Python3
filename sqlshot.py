import sqlite3

def sqlquerysearch(mysearch):
    # mainconn() is a connection for sqlite3 database bitcoindb.db
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    # This is to execute to find record from the database using sqlite3
    c.execute("select * from books_table where Title=?",(mysearch,))
    row = c.fetchone()
    conn.rollback()
    # To close database after execute from searchfunction()
    conn.close()
    return row
#print(sqlquerysearch(mysearch))

def sqlqueryinsertrecord():
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    # this is an insert record execute for insert record function
    c.execute("insert into books_table(Isbn, Title, Author, Borrowed, Borrower) values (?,?,?,?,?)", \
              (23, 'mybullshit2', 'albiemer porte', '2:30', 'zeinab'))
    print("\nINSERTED DATA SUCCESSFULLY")
    input()
    conn.commit()
    conn.close()

#sqlqueryinsertrecord()