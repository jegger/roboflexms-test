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
    
    def transfer_bahn_nr(self, nr):
        rq = self.client.write_register(532, nr)
        rq = self.client.write_coil(8483, True)
        time.sleep(0.5)
        rq = self.client.write_coil(8483, False)
        print "transfered"
    
    def transfer_array(self, array, callback):
        '''Call this function to move the array to the PLC
        :param array: array which should be transmitted
        :param callback: callback which should be called when finished
        '''
        #check array size
        c=0
        for cube in array:
            c+=1
        if c!= 106:
            print "Array size isn't suitable", c
            return   
        
        lis = array
        
        #write cubes into PLC
        c=0
        for cube in lis:
            print '-', (c/5)+1, cube
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
        
    def machine_is_building(self, *kwargs):
        '''Call this class to get the bool if the machine is working or not
        '''
        rq = self.client.read_coils(8481,1)
        return rq.bits[0]
    
    def read_active_bahn(self, *kwargs):
        rq = self.client.read_holding_registers(533, 1)
        return rq.registers[0]
        
Modbus=ModbusClass()
            