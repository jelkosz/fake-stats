from flask import Flask
app = Flask(__name__)
@app.route("/metrics")
def hello():
    return """
# HELP node_ipmi_temperature_celsius Temperature sensor reading from ipmitool
# TYPE node_ipmi_temperature_celsius gauge
node_ipmi_temperature_celsius{sensor="Temp"} 42.000000
node_ipmi_temperature_celsius{sensor="Inlet Temp"} 20.000000
node_ipmi_temperature_celsius{sensor="Exhaust Temp"} 36.000000
# HELP node_ipmi_volts Voltage sensor reading from ipmitool
# TYPE node_ipmi_volts gauge
node_ipmi_volts{sensor="Voltage 1"} 208.000000
node_ipmi_volts{sensor="Voltage 2"} 206.000000
# HELP node_ipmi_power_watts Power sensor reading from ipmitool
# TYPE node_ipmi_power_watts gauge
node_ipmi_power_watts{sensor="Pwr Consumption"} 182.000000
# HELP node_ipmi_speed_rpm Fan sensor reading from ipmitool
# TYPE node_ipmi_speed_rpm gauge
node_ipmi_speed_rpm{sensor="Fan1A"} 5520.000000
node_ipmi_speed_rpm{sensor="Fan1B"} 4200.000000
node_ipmi_speed_rpm{sensor="Fan2A"} 5640.000000
node_ipmi_speed_rpm{sensor="Fan2B"} 4080.000000
node_ipmi_speed_rpm{sensor="Fan3A"} 5640.000000
node_ipmi_speed_rpm{sensor="Fan3B"} 4080.000000
node_ipmi_speed_rpm{sensor="Fan4A"} 5400.000000
node_ipmi_speed_rpm{sensor="Fan4B"} 4080.000000
node_ipmi_speed_rpm{sensor="Fan5A"} 5520.000000
node_ipmi_speed_rpm{sensor="Fan5B"} 4080.000000
node_ipmi_speed_rpm{sensor="Fan6A"} 5520.000000
node_ipmi_speed_rpm{sensor="Fan6B"} 4080.000000
node_ipmi_speed_rpm{sensor="Fan7A"} 5520.000000
node_ipmi_speed_rpm{sensor="Fan7B"} 4200.000000
# HELP node_ipmi_status Chassis status sensor reading from ipmitool
# TYPE node_ipmi_status gauge
node_ipmi_status{sensor="Mem Fatal NB CRC"} 0.000000
node_ipmi_status{sensor="QPIRC Warning"} 23.000000
node_ipmi_status{sensor="Chassis Mismatch"} 22.000000
node_ipmi_status{sensor="5V AUX PG"} 0.000000
node_ipmi_status{sensor="NDC PG"} 0.000000
node_ipmi_status{sensor="VGA Cable Pres"} 0.000000
node_ipmi_status{sensor="Fatal PCI SSD Er"} 2.000000
node_ipmi_status{sensor="3.3V PG"} 0.000000
node_ipmi_status{sensor="Mem ECC Warning"} 0.000000
node_ipmi_status{sensor="CMOS Battery"} 0.000000
node_ipmi_status{sensor="Fan Redundancy"} 0.000000
node_ipmi_status{sensor="MRC Warning"} 2.000000
node_ipmi_status{sensor="USB Over-current"} 0.000000
node_ipmi_status{sensor="2.5V AUX PG"} 0.000000
node_ipmi_status{sensor="M01 VDDQ PG"} 0.000000
node_ipmi_status{sensor="Interconnect Err"} 0.000000
node_ipmi_status{sensor="BP1 Presence"} 0.000000
node_ipmi_status{sensor="ECC Corr Err"} 0.000000
node_ipmi_status{sensor="M23 VPP PG"} 0.000000
node_ipmi_status{sensor="M01 VPP PG"} 0.000000
node_ipmi_status{sensor="1.05V PG"} 0.000000
node_ipmi_status{sensor="CPU TDP"} 0.000000
node_ipmi_status{sensor="OS Watchdog Time"} 0.000000
node_ipmi_status{sensor="Cable SAS A0"} 0.000000
node_ipmi_status{sensor="USB Cable Pres"} 0.000000
node_ipmi_status{sensor="M23 VTT PG"} 0.000000
node_ipmi_status{sensor="Mem Overtemp"} 0.000000
node_ipmi_status{sensor="M01 VTT PG"} 0.000000
node_ipmi_status{sensor="LCD Cable Pres"} 0.000000
node_ipmi_status{sensor="FatalPCIErrOnBus"} 2.000000
node_ipmi_status{sensor="BP2 5V PG"} 0.000000
node_ipmi_status{sensor="Intrusion"} 0.000000
node_ipmi_status{sensor="PCI Parity Err"} 94.000000
node_ipmi_status{sensor="1.5V PG"} 0.000000
node_ipmi_status{sensor="Riser 3 Presence"} 0.000000
node_ipmi_status{sensor="POST Err"} 0.000000
node_ipmi_status{sensor="Mem CRC Err"} 0.000000
node_ipmi_status{sensor="DIMM PG"} 0.000000
node_ipmi_status{sensor="VCORE PG"} 0.000000
node_ipmi_status{sensor="Fatal IO Error"} 0.000000
node_ipmi_status{sensor="BP2 Presence"} 0.000000
node_ipmi_status{sensor="A"} 0.000000
node_ipmi_status{sensor="B"} 0.000000
node_ipmi_status{sensor="Memory Added"} 0.000000
node_ipmi_status{sensor="Additional Info"} 0.000000
node_ipmi_status{sensor="Drive 0"} 0.000000
node_ipmi_status{sensor="Status"} 0.000000
node_ipmi_status{sensor="Dedicated NIC"} 0.000000
node_ipmi_status{sensor="vFlash"} 0.000000
node_ipmi_status{sensor="Chipset Err"} 0.000000
node_ipmi_status{sensor="PCIe Slot2"} 0.000000
node_ipmi_status{sensor="PCIe Slot3"} 0.000000
node_ipmi_status{sensor="Signal Cable"} 0.000000
node_ipmi_status{sensor="NonFatalSSDError"} 22.000000
node_ipmi_status{sensor="Memory Removed"} 0.000000
node_ipmi_status{sensor="Riser Config Err"} 0.000000
node_ipmi_status{sensor="VCCIO PG"} 0.000000
node_ipmi_status{sensor="ROMB Battery"} 0.000000
node_ipmi_status{sensor="OS Watchdog"} 0.000000
node_ipmi_status{sensor="CPUMachineCheck"} 2.000000
node_ipmi_status{sensor="Power Optimized"} 0.000000
node_ipmi_status{sensor="M23 VDDQ PG"} 0.000000
node_ipmi_status{sensor="Non Fatal PCI Er"} 0.000000
node_ipmi_status{sensor="NonFatalPCIErBus"} 22.000000
node_ipmi_status{sensor="Cable SAS B0"} 0.000000
node_ipmi_status{sensor="1.5V AUX PG"} 0.000000
node_ipmi_status{sensor="5V SWITCH PG"} 0.000000
node_ipmi_status{sensor="Link Error"} 2.000000
node_ipmi_status{sensor="iDPT Memfail"} 0.000000
node_ipmi_status{sensor="Hdwr version err"} 0.000000
node_ipmi_status{sensor="FIVR PG"} 0.000000
node_ipmi_status{sensor="Presence"} 0.000000
node_ipmi_status{sensor="NonFatalPCIExpEr"} 0.000000
node_ipmi_status{sensor="Link Warning"} 2.000000
node_ipmi_status{sensor="MSR Info Log"} 0.000000
node_ipmi_status{sensor="BP1 5V PG"} 0.000000
node_ipmi_status{sensor="PS2 PG Fail"} 0.000000
node_ipmi_status{sensor="Power Cable"} 0.000000
node_ipmi_status{sensor="Memory Cfg Err"} 0.000000
node_ipmi_status{sensor="Mem Fatal SB CRC"} 0.000000
node_ipmi_status{sensor="PS1 PG Fail"} 0.000000
node_ipmi_status{sensor="Err Reg Pointer"} 0.000000
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("9100"), debug=True)
