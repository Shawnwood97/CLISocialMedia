from exploit import Exploit
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
      cursor.execute("SELECT h.id, h.alias FROM hackers h WHERE h.alias = ? AND h.password = ?", [
          alias, password])
      alias_id = cursor.fetchall()
      if(alias_id == []):
        print('Invalid username or password, try again!')
        db.closeAll(cursor, conn)
        continue
    except:
      print('Error with login!')
    db.closeAll(cursor, conn)
    return alias_id


def loggedInOptions(h_info):
  while True:
    print(f'Thanks for logging in {h_info[0][1]}')
    print('What would you like to do? \n 1: Make an exploit \n 2: See my exploits \n 3: See other hackers exploits \n 4: Logout!')
    selection = int(input(f'{h_info[0][1]}, Make a selection: '))
    if(selection == 1):
      # *make a new exploit!
      conn = db.openConnection()
      if(conn == None):
        print('No connection to database, closing your connection!')
        break
      cursor = db.openCursor(conn)
      if(cursor == None):
        print('Unable to close cursor, Closing DB connection, please retry!')
        db.closeConnection(conn)
        break
      # calling class function to create an exploit
      Exploit(h_info[0][0]).createExploit(conn, cursor, input(
          f'{h_info[0][1]}, Enter the content of your exploit: '))
      db.closeAll(cursor, conn)

    elif(selection == 2):
      conn = db.openConnection()
      if(conn == None):
        print('No connection to database, closing your connection!')
        break
      cursor = db.openCursor(conn)
      if(cursor == None):
        print('Unable to close cursor, Closing DB connection, please retry!')
        db.closeConnection(conn)
        break
        # calling class function for getting others exploits
      Exploit(h_info[0][0]).getOwnExploits(cursor)
    elif(selection == 3):
      conn = db.openConnection()
      if(conn == None):
        print('No connection to database, closing your connection!')
        break
      cursor = db.openCursor(conn)
      if(cursor == None):
        print('Unable to close cursor, Closing DB connection, please retry!')
        db.closeConnection(conn)
        break
        # calling class function for getting others exploits
      Exploit(h_info[0][0]).getOthersExploits(cursor)
    elif(selection == 4):
      break


def app():
  while True:
    #* ----------- Login ----------- *#
    print('Welcome to CLI-Social-Media! \n 1: Login \n 2: Quit')
    try:
      selection = int(input('What would you like to do? '))
      if(selection == 1):
        hacker = hackerLogin()
        loggedInOptions(hacker)

      elif(selection == 2):
        print('Quitting App...')
        break
      elif(selection > 2 or selection <= 0):
        print('Please enter a valid selection')
    except:
      print('Error with user input!')
      traceback.print_exc()


app()
