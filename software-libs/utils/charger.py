# Codificado por vibras todo esto

import can
import cantools
import time
import sys

DBC_FILE_PATH = "../ter-dbc/charger.dbc"

try:
    db = cantools.database.load_file(DBC_FILE_PATH)
    config_msg_def = db.get_message_by_name("ConfigureCharger")
except FileNotFoundError:
    print(f"Error: Could not find the DBC file at \"{DBC_FILE_PATH}\".")
    print("Please save your DBC text into a file named \"charger.dbc\" in this directory.")
    sys.exit(1)

def send_configure_message(bus, command, **kwargs):
    data_dict = {
        "group": 0,
        "message_type": "Set",
        "command": command
    }

    data_dict.update(kwargs)

    data = config_msg_def.encode(data_dict)

    msg = can.Message(
        arbitration_id=config_msg_def.frame_id,
        data=data,
        is_extended_id=True
    )

    try:
        bus.send(msg)
        print(f"Sent: Command=\"{command}\" with data={kwargs}")
    except can.CanError as e:
        print(f"Failed to send message: {e}")

def main():
    try:
        voltage_limit = int(input("Enter voltage limit in V (e.g. 600): "))
        current_limit = int(input("Enter current limit in mA (e.g. 10000): "))
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return

    try:
        bus = can.interface.Bus(channel="can0", bustype="socketcan")
    except OSError:
        print("Could not open CAN interface. Ensure \"can0\" is up and socketcan is configured.")
        return

    print("\nApplying limits...")
    send_configure_message(bus, command="TargetVoltage", voltage=voltage_limit*1000)

    send_configure_message(bus, command="TargetCurrent", current=current_limit)

    print("\nStarting periodic \"Power On\" loop (Ctrl+C to stop)...")
    try:
        while True:
            send_configure_message(bus, command="Power", power="On")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\nCtrl+C detected! Shutting down charger...")
        send_configure_message(bus, command="Power", power="Off")
        print("Charger turned Off.")

    finally:
        bus.shutdown()

if __name__ == "__main__":
    main()
