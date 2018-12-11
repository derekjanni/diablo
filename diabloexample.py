#! /usr/local/bin/python3
import time
import sys
from diablo import Diablo

class App(Diablo):
    def run(self):
        while True:
            print('hi')
            time.sleep(5)

app = App('/tmp/pid.pid')
