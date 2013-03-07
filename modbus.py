#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

class ModbusClass():
    connected=False
    
    def __init__(self, *kwargs):
        self.connect()
    
    def connect(self):
        '''Try to connect to the Modbus client
        (mostely internal)
        '''
        if not self.connected:
            self.client = ModbusClient('192.168.50.238', port=502)
            self.client.connect()
            self.connected=True
    
    def reset_safety(self, callback):
        '''Call this class to reset safety
        :param callback: callback which should be called at the end
        '''
        if not self.connected:
            self.connect()
        #write to bit 8480
        rq = self.client.write_coil(8480, True)
        time.sleep(0.5)
        rq = self.client.write_coil(8480, False)
        callback()
    
    def transfer_array(self, array, callback):
        '''Call this function to move the array to the PLC
        :param array: array which should be transmitted
        :param callback: callback which should be called when finished
        '''
        #check array size
        c=0
        for cube in array:
            c+=1
        if c!= 105:
            print "Array size isn't suitable", c
            return   
        
        lis = array
        
        #write cubes into PLC
        c=0
        for cube in lis:
            #write x
            rq = self.client.write_register(c, cube['x'])
            c+=1
            #write y
            rq = self.client.write_register(c, cube['y'])
            c+=1
            #write z
            rq = self.client.write_register(c, cube['z'])
            c+=1
            #write rot
            rq = self.client.write_register(c, cube['typ'])
            c+=1
            #write type
            rq = self.client.write_register(c, cube['rot'])
            c+=1
            
        callback()

Modbus=ModbusClass()
            