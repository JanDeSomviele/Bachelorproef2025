# sla dit op als modbus_server.py
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification
import logging

logging.basicConfig()
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [10]*100)  # Holding Registers
)
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'TestVendor'
identity.ProductCode = 'TV'
identity.VendorUrl = 'http://localhost'
identity.ProductName = 'ModbusSim'
identity.ModelName = 'ModbusTest'
identity.MajorMinorRevision = '1.0'

print("✅ Simulatieserver actief op localhost:5020")
StartTcpServer(context, identity=identity, address=("localhost", 5020))
