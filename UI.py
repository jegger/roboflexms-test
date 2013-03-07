from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from modbus import Modbus
import depot

#load KV file
Builder.load_file('UI.kv')

class SimpleVisu(Widget):
    building=False

    def reset_safety(self):
        '''Reset safety on machine
        '''
        Modbus.reset_safety(callback=self.success)
    
    def move_array(self):
        '''Move the array with all the cubes to the SPS
        '''
        
        Modbus.transfer_array(array=depot.depot, callback=self.success)
    
    def build(self, bahn):
        '''Start building
        '''
        if not self.building:
            #Check which bahn it is
            if bahn==0:
                print "Lager"
            elif bahn==1:
                print "Bahn1"
            elif bahn==2:
                print "Bahn2"
            elif bahn==3:
                print "Bahn3"
            else:
                print "No suitable bahn found"
            self.building=True
        return
    
    def success(self, *kwargs):
        print "Done"

class MyApp(App):
    def build(self):
        return SimpleVisu()

if __name__ == '__main__':
    MyApp().run()