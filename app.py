import traceback
import db
# import mariadb


def hackerLogin():
  while True:
    try:
      alias = input('Enter your alias: ')
      password = input('Enter your password: ')
      conn = db.openConnection()
      if(conn == None):
        print('No connection to database, closing your connection!')
        break
      cursor = db.openCursor(conn)
      if(cursor == None):
        print('Unable to close cursor, Closing DB connection, please retry!')
        db.closeConnection(conn)
        break
      cursor.execute("SELECT h.id FROM hackers h WHERE h.alias = ? AND h.password = ?", [
          alias, password])
      alias_id = cursor.fetchone()
      if(alias_id == None):
        print('Invalid username or password, try again!')
        db.closeAll(cursor, conn)
        continue
    except:
      print('Error with login!')
    db.closeAll(cursor, conn)
    print(alias_id)
    return alias_id


hackerLogin()
