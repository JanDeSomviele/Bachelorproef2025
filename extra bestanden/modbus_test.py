# from pymodbus.client import ModbusTcpClient
# import time

# # === Parameters ===
# MODBUS_IP = '192.168.1.50'  # <-- Vul hier het IP-adres van je apparaat in
# MODBUS_PORT = 502
# UNIT_ID = 1
# REGISTER = 0
# COUNT = 2
# INTERVAL = 5

# client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)
# if client.connect():
#     print(f"Verbonden met {MODBUS_IP}:{MODBUS_PORT}")
#     while True:
#         result = client.read_holding_registers(REGISTER, COUNT, unit=UNIT_ID)
#         if result.isError():
#             print("❌ Fout bij uitlezen!")
#         else:
#             print(f"✅ Registerwaarden: {result.registers}")
#         time.sleep(INTERVAL)
# else:
#     print("❌ Kan geen verbinding maken met Modbus.")

# client.close()

from pymodbus.client import ModbusTcpClient

MODBUS_IP = 'localhost'
MODBUS_PORT = 5020

client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)
connection = client.connect()

if connection:
    result = client.read_holding_registers(1, count=50)
    print(f"Registers uitgelezen: {result.registers}")
    client.close()
else:
    print("❌ Verbinding mislukt")

client.close()