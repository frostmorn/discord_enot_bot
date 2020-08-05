import time
import lxml.html
import requests
class Crabdance():
  def __init__(self):
    self.time= time.time()
  def read(self):


    data = {
      'mode': 'read',
      'last_time': self.time,
      'read_interval': '5'
    }

    response = requests.post('https://crabdance.pp.ua/app.php/chat/read', data=data)

    message = lxml.html.fromstring(response.content.decode("utf-8")).xpath("//*[class='message']")
    self.time = time.time()
    pass
if __name__ == "__main__":
    crabdance = Crabdance()
    while 1:
      crabdance.read()
      time.sleep(5)