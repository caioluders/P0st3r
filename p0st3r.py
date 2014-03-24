#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: geolado | g3ol4d0
# Email : g3ol4d0[at]gmail.com
# Python 2.7

import urllib , sys , time , argparse , math , sys , time , optparse , os 


def banner() :
   screen = getTerminalSize()
   screen_height = screen[0]
   screen_width = screen[1]
   center_width = screen[1]
   banner_ascii = ["          ,       ",
                   "._  _  __-+- _ ._.",
                   "[_)(_)_)  | (/,[  ",
                   "|                 ",
                   "                  ",
                   "Poster/0.1",
                   "by geolado | g3ol4d0"]

   print("_"*screen_width)    
   for line in banner_ascii :
      print(line.center(center_width))    
   print("_"*screen_width)       

def getTerminalSize():

    line = os.popen('stty size', 'r').read().split()
    line = map(int , line)

    return line 

class poster(object) :
    
   def __init__(self) :
      self.p = []
      self.pd = []
      self.url = args.url
      self.parameters = args.parameters
      self.requests = args.requests
      self.delay = args.delay

   def prepare_parameters(self) :
      print("[i] Preparing post parameters")
      self.p = self.parameters.split(' ')   

      for i in range(len(self.p)) :
        self.pd.append(self.p[i].split(':'))

      self.pd = dict(self.pd)  

   def progress(self , width, percent):
      screen = getTerminalSize()
      screen_height = screen[0]
      screen_width = screen[1]
      center_width = screen[1]
      actual_percent = percent*100/self.requests
      width_percent = actual_percent*(screen_width-11)/100
      fill = (screen_width-11)*"."
      fill = fill.replace(".","#",width_percent)
      sys.stdout.write("\r[i] [{0}] {1}%".format( fill , actual_percent ))
      sys.stdout.flush()

   def post(self) : 
      self.query = urllib.urlencode(self.pd)
      self.f = urllib.urlopen( self.url, self.query )

      self.contents = self.f.read()
      self.f.close()

   def send_post(self) :
      screen = getTerminalSize()
      screen_height = screen[0]
      screen_width = screen[1]
      center_width = screen[1]
      print("[i] Sending requests ... ")
      for i in range(self.requests) :
         sleep(self.delay)
         p.post()
         p.progress(screen_width,i+1)
      print("\n[i] Finish !")   



if __name__ == "__main__":

   banner()

   parser = argparse.ArgumentParser()
   parser.add_argument("-u","--url", help = "URL to request" , metavar= "http://url.com/" ,  required=True)
   parser.add_argument("-p","--parameters", help = "Parameters for $_POST" , metavar = "variable:data", required=True)
   parser.add_argument("-r","--requests", type = int , help="Number of requests", metavar = "x" , required=True)
   parser.add_argument("-d","--delay", type = float , help="Delay ( sec ) for each request", metavar = "x" , default = 0.0)
   args = parser.parse_args()

   p = poster()
   p.prepare_parameters()
   p.send_post()




