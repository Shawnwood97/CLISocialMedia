from hacker import Hacker
from exploit import Exploit
import traceback
import db
# import mariadb


# Login funciton, takes inputs and executes the query. Not sure how efficient the BINARY modifier for changing the Collation is to ensure
# Case-Sensitivity is honored, but I figured it was okay for this assignment and may be something alot of students overlook.
# KeyboardInterrupt returns False so I can break out of other loops we are nested inside when in the scope of hackerLogin.
# Don't know if "scope" is the right word as we haven't used it in Python, but that's how I'll refer to it for now!
# ? returns id and alias as a tuple for use in other functions!
# ! Should this be in the Hacker class??????!??!!??!?!?!? hmmmm......
def hackerLogin():
  while True:
    try:
      alias = input('Enter your alias: ')
      password = input('Enter your password: ')
      conn = db.openConnection()
      cursor = db.openCursor(conn)
      cursor.execute("SELECT h.id, h.alias FROM hackers h WHERE h.alias = ? AND BINARY h.password = ?", [
          alias, password])
      id_alias = cursor.fetchall()
      if(len(id_alias) != 1):
        print('Invalid username or password, try again!')
        db.closeAll(cursor, conn)
        continue
    except KeyboardInterrupt:
      print('\n You have exited the app (CTRL + C)')
      return False
    except:
      print('Error with login!')

    db.closeAll(cursor, conn)
    # returns alias and ID in a
    return id_alias


# Logged in options, pretty basic, takes the returned data from the hackerLogin function and uses it, same deal here with the KeyboardInterrupt returning False.
# small if statement to ensure the content is not left empty. Basic excepts.
def loggedInOptions(h_info):
  while True:
    print(f'Thanks for logging in {h_info[0][1]}')
    print('What would you like to do? \n 1: Make an exploit \n 2: See my exploits \n 3: See other hackers exploits \n 4: Logout!')
    try:
      selection = int(input(f'{h_info[0][1]}, Make a selection: '))
      if(selection > 4 or selection <= 0):
        print('Option must be betweet 1 and 4!')
    except KeyboardInterrupt:
      print('\n You have exited the app (CTRL + C)')
      return False
    except ValueError:
      print('You must enter a valid option!')
      continue
    except:
      print('Unknown error with selection!')
      traceback.print_exc()

    if(selection == 1):
      content = input(f'{h_info[0][1]}, Enter the content of your exploit: ')
      conn = db.openConnection()
      cursor = db.openCursor(conn)
      Exploit(h_info[0][0]).createExploit(conn, cursor, content)
      db.closeAll(cursor, conn)
    elif(selection == 2):
      conn = db.openConnection()
      cursor = db.openCursor(conn)

      # calling class function for getting others exploits
      Hacker(h_info[0][1]).getOwnExploits(cursor, h_info[0][0])
    elif(selection == 3):
      conn = db.openConnection()
      cursor = db.openCursor(conn)

      # calling class function for getting others exploits
      Hacker(h_info[0][1]).getOthersExploits(cursor, h_info[0][0])
    elif(selection == 4):
      break

# function for the app as a whole, calls other functions and has some of it's own error checking (if's and excepts).


def app():
  while True:
    #* ----------- Login ----------- *#
    print('Welcome to CLI-Social-Media! \n 1: Login \n 2: Signup \n 3: Quit')
    try:
      selection = int(input('What would you like to do? '))
      if(selection == 1):
        hacker_info = hackerLogin()
        if(hacker_info == False):
          break
        #! interesting that the below works, not sure why, but it does!
        if(loggedInOptions(hacker_info) == False):
          break
      if(selection == 2):
        alias = input('What would you like your alias to be? ')
        password = input('What would you like your password to be? ')
        conn = db.openConnection()
        cursor = db.openCursor(conn)
        Hacker(alias).createHacker(conn, cursor, password)
        db.closeAll(cursor, conn)
      elif(selection == 3):
        print('Quitting App...')
        break
      elif(selection > 2 or selection <= 0):
        print('Please enter a valid selection')
    except KeyboardInterrupt:
      print('\n You have exited the app (CTRL + C)')
      return False
    except ValueError:
      print('Input must be either 1 or 2!')
      traceback.print_exc()
    except:
      print('Error with user input!')
      traceback.print_exc()


app()
