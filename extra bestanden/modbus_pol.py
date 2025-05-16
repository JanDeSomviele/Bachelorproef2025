# modbus_poll.py
import argparse
from pymodbus.client import ModbusTcpClient

def poll_modbus(host, port, unit, count):
    client = ModbusTcpClient(host, port=port)
    if not client.connect():
        print("Fout: Kon geen verbinding maken met Modbus-server.")
        return

    rr = client.read_holding_registers(0, count, unit=unit)
    if rr.isError():
        print(f"Fout bij het lezen van registers: {rr}")
    else:
        print(f"Gelezen waarden: {rr.registers}")

    client.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1', help='Modbus TCP server IP')
    parser.add_argument('--port', type=int, default=5020, help='TCP poort')
    parser.add_argument('--unit', type=int, default=1, help='Modbus unit ID')
    parser.add_argument('--count', type=int, default=10, help='Aantal registers om te lezen')
    args = parser.parse_args()

    poll_modbus(args.host, args.port, args.unit, args.count)

if __name__ == "__main__":
    main()
