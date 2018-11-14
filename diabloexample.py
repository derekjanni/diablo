import time
import sys
from diablo import Diablo

class App(Diablo):
    def run(self):
        while True:
            print("Howdy!  Gig'em!  Whoop!")
            time.sleep(10)

app = App('/tmp/pid.pid')
