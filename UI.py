from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.clock import Clock
from modbus import Modbus
import depot

#load KV file
Builder.load_file('UI.kv')

class SimpleVisu(Widget):
    building=False
    
    def __init__(self,*args,**kwargs):
        super(SimpleVisu,self).__init__(*args,**kwargs)
        #activate cycle checke
        Clock.schedule_interval(self.actualize_building, 1)

    def reset_safety(self):
        '''Reset safety on machine
        '''
        Modbus.reset_safety(callback=self.success)
    
    def move_array(self):
        '''Move the array with all the cubes to the SPS
        '''
        anlage_ = depot.calculate_mazine(depot.depot, depot.demo_anlage)
        Modbus.transfer_array(array=anlage_, callback=self.success)
    
    def build(self, bahn):
        '''Start building
        '''
        if not self.building:
            #Check which
            if bahn==0:
                print "Lager"
                Modbus.transfer_bahn_nr(nr=0)
            elif bahn==1:
                print "Bahn1"
                Modbus.transfer_bahn_nr(nr=1)
            elif bahn==2:
                print "Bahn2"
                Modbus.transfer_bahn_nr(nr=2)
            elif bahn==3:
                print "Bahn3"
                Modbus.transfer_bahn_nr(nr=3)
            elif bahn==4:
                print "Bahn4"
                Modbus.transfer_bahn_nr(nr=4)
            elif bahn==10:
                print "BahnPC"
                Modbus.transfer_bahn_nr(nr=10)
            else:
                print "No suitable Bahn found"
            
        return
    
    def success(self, *kwargs):
        print "Command Done"
    
    def actualize_building(self, *kwargs):
        '''Actualize information about building
        '''
        bahn = Modbus.read_active_bahn()
        if Modbus.machine_is_building():
            self.status_label.text='Machine is building Bahn '+str(bahn)+' ...'
        else:
            self.status_label.text='Ready'

class MyApp(App):
    def build(self):
        return SimpleVisu()

if __name__ == '__main__':
    MyApp().run()