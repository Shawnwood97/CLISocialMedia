import traceback
import mariadb


class Hacker:
  def __init__(self, alias, password=None, h_id=None):
    self.alias = alias

  def createHacker(self, conn, cursor, password):
    self.password = password
    if(self.alias == '' or self.password == ''):
      print('Username and password fields must have values!')
      return False
    try:
      cursor.execute("INSERT INTO hackers (alias, password) VALUES (?, ?)", [
          self.alias, self.password])
      conn.commit()
      self.h_id = cursor.lastrowid
      print(f'Hacker {self.alias} Created!')
    except mariadb.IntegrityError:  # ! I know this means more than this one error, but, used this for the example since it is likely the most common issue?!?
      print("Username unavailable")
    except:
      print("Error creating Hacker!")
      traceback.print_exc()

  # get own exploits using execute, fetchall, and a loop to display it prettify it!
  # Should display newest first!
  #! h_id and self.h_id are diff things, h_id comes from the passed value arg, self.h_id is set within this object from the lastrowid of the returned row
  def getOwnExploits(self, cursor, h_id):
    try:
      cursor.execute("SELECT h.alias, e.content FROM hackers h INNER JOIN exploits e ON h.id = e.hacker_id WHERE e.hacker_id = ? ORDER BY e.id DESC", [
          h_id])
      self.h_id = cursor.lastrowid
      results = cursor.fetchall()
      for user, content in results:
        print(f'User: {user} \n Exploit: {content} \n')
    except:
      print("Error getting your exploits!")
      traceback.print_exc()

  # get others exploits using execute, fetchall, and a loop to display it prettify it!
  # Should display newest first!
  def getOthersExploits(self, cursor, h_id):
    try:
      cursor.execute("SELECT h.alias, e.content FROM hackers h INNER JOIN exploits e ON h.id = e.hacker_id WHERE e.hacker_id != ? ORDER BY e.id DESC", [
          h_id])
      results = cursor.fetchall()
      for user, content in results:
        print(f'User: {user} \n Exploit: {content} \n')
    except:
      print("Error getting others exploits!")
      traceback.print_exc()
