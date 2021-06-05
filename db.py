import mariadb
import dbcreds
import traceback


def openConnection():
  try:
    return mariadb.connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database,
    )

  except:
    print("Error opening connextion to DB!")
    traceback.print_exc()
    return None


def openCursor(conn):
  try:
    return conn.cursor()

  except:
    print("Error opening cursor on DB!")
    traceback.print_exc()
    return None


def closeCursor(cursor):
  if(cursor == None):
    return True
  try:
    cursor.close()
    return True

  except:
    print("Error closing cursor on DB!")
    traceback.print_exc()
    return False


def closeConnection(conn):
  if(conn == None):
    return True
  try:
    conn.close()
    return True

  except:
    print("Error closing connection to DB!")
    traceback.print_exc()
    return False
