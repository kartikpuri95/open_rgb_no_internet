from openrgb import OpenRGBClient

import socket
from openrgb.utils import RGBColor


class NoInternet:
    current_color='white'

    def change_rgb_color(self,status):
        print("inside change rgb")
        cli = OpenRGBClient('127.0.0.1', 6742, 'My client!')
        nzxt_smart_light=cli.get_devices_by_name('NZXT Smart Device V2')[0]
        if status:
            self.current_color='white'
            white = RGBColor(255, 255, 255)
            nzxt_smart_light.set_color(white,start=0,end=10,fast=False) 
        else:
            self.current_color='red'
            red = RGBColor(255, 0, 0)
            nzxt_smart_light.set_color(red,start=0,end=10,fast=False)
    def is_connected(self):
        while True:
            try:
                # connect to the host -- tells us if the host is actually
                # reachable
                socket.create_connection(("1.1.1.1", 53))
                print ("internet connect")
                if not self.current_color=='white':
                    self.change_rgb_color(True)
            except OSError:
                print ("internet dc connect")
                if not self.current_color=='red':
                    self.change_rgb_color(False)
                

    
obj=NoInternet()

obj.is_connected()