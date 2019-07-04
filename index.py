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
# HELP baremetal_last_payload_timestamp
# TYPE baremetal_last_payload_timestamp gauge
baremetal_last_payload_timestamp{instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228"} 1.553890342e+09
# HELP baremetal_front_led_panel
# TYPE baremetal_front_led_panel gauge
baremetal_front_led_panel{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Front LED Panel (0x23)"} 0.0
# HELP baremetal_inlet_temp_celsius
# TYPE baremetal_inlet_temp_celsius gauge
baremetal_inlet_temp_celsius{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Inlet Temp (0x5)",status="ok"} 21.0
# HELP baremetal_exhaust_temp_celsius
# TYPE baremetal_exhaust_temp_celsius gauge
baremetal_exhaust_temp_celsius{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Exhaust Temp (0x6)",status="ok"} 36.0
# HELP baremetal_temp_celsius
# TYPE baremetal_temp_celsius gauge
baremetal_temp_celsius{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Temp (0x1)",status="ok"} 44.0
baremetal_temp_celsius{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Temp (0x2)",status="ok"} 43.0
# HELP baremetal_system_unknown
# TYPE baremetal_system_unknown gauge
baremetal_system_unknown{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Unknown (0x8)"} 0.0
# HELP baremetal_current
# TYPE baremetal_current gauge
baremetal_current{entity_id="10.2 (Power Supply)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Current 2 (0x6c)",status="ok"} 0.6
baremetal_current{entity_id="10.1 (Power Supply)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Current 1 (0x6b)",status="ok"} 0.6
# HELP baremetal_pwr_consumption
# TYPE baremetal_pwr_consumption gauge
baremetal_pwr_consumption{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Pwr Consumption (0x76)",status="ok"} 264.0
# HELP baremetal_chassis_mismatch
# TYPE baremetal_chassis_mismatch gauge
baremetal_chassis_mismatch{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Chassis Mismatch (0x37)"} 0.0
# HELP baremetal_tpm_presence
# TYPE baremetal_tpm_presence gauge
baremetal_tpm_presence{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="TPM Presence (0x41)"} 1.0
# HELP baremetal_memory_post_pkg_repair
# TYPE baremetal_memory_post_pkg_repair gauge
baremetal_memory_post_pkg_repair{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="POST Pkg Repair (0x45)"} 1.0
# HELP baremetal_idpt_mem_fail
# TYPE baremetal_idpt_mem_fail gauge
baremetal_idpt_mem_fail{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="iDPT Mem Fail (0x2b)"} 0.0
# HELP baremetal_memory_spared
# TYPE baremetal_memory_spared gauge
baremetal_memory_spared{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Memory Spared (0x11)"} 0.0
# HELP baremetal_memory_mirrored
# TYPE baremetal_memory_mirrored gauge
baremetal_memory_mirrored{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Memory Mirrored (0x12)"} 0.0
# HELP baremetal_memory_ecc_uncorr_err
# TYPE baremetal_memory_ecc_uncorr_err gauge
baremetal_memory_ecc_uncorr_err{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="ECC Uncorr Err (0x2)"} 1.0
# HELP baremetal_memory_b
# TYPE baremetal_memory_b gauge
baremetal_memory_b{entity_id="32.1 (Memory Device)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="B  (0xd6)"} 0.0
# HELP baremetal_memory_a
# TYPE baremetal_memory_a gauge
baremetal_memory_a{entity_id="32.1 (Memory Device)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="A  (0xca)"} 0.0
# HELP baremetal_memory_ecc_corr_err
# TYPE baremetal_memory_ecc_corr_err gauge
baremetal_memory_ecc_corr_err{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="ECC Corr Err (0x1)"} 1.0
# HELP baremetal_power_status
# TYPE baremetal_power_status gauge
baremetal_power_status{entity_id="10.2 (Power Supply)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Status (0x86)"} 0.0
baremetal_power_status{entity_id="10.1 (Power Supply)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Status (0x85)"} 0.0
# HELP baremetal_os_watchdog
# TYPE baremetal_os_watchdog gauge
baremetal_os_watchdog{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="OS Watchdog (0x71)"} 0.0
# HELP baremetal_os_watchdog_time
# TYPE baremetal_os_watchdog_time gauge
baremetal_os_watchdog_time{entity_id="34.1 (BIOS)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="OS Watchdog Time (0x23)"} 0.0
# HELP baremetal_fan_rpm
# TYPE baremetal_fan_rpm gauge
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan4A (0x3b)",status="ok"} 9960.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan1B (0x40)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan8B (0x47)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan3A (0x3a)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan2A (0x39)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan6B (0x45)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan5A (0x3c)",status="ok"} 9720.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan3B (0x42)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan7A (0x3e)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan7B (0x46)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan4B (0x43)",status="ok"} 5880.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan1A (0x38)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan6A (0x3d)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan2B (0x41)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan5B (0x44)",status="ok"} 5640.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan8A (0x3f)",status="ok"} 9240.0
# HELP baremetal_fan_redundancy
# TYPE baremetal_fan_redundancy gauge
baremetal_fan_redundancy{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Fan Redundancy (0x78)"} 0.0
# HELP baremetal_vccio_pg
# TYPE baremetal_vccio_pg gauge
baremetal_vccio_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VCCIO PG (0x34)"} 0.0
baremetal_vccio_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VCCIO PG (0x2a)"} 0.0
# HELP baremetal_voltage
# TYPE baremetal_voltage gauge
baremetal_voltage{entity_id="10.1 (Power Supply)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Voltage 1 (0x6d)",status="ok"} 208.0
baremetal_voltage{entity_id="10.2 (Power Supply)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="Voltage 2 (0x6e)",status="ok"} 208.0
# HELP baremetal_dimm_pg
# TYPE baremetal_dimm_pg gauge
baremetal_dimm_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="DIMM PG (0x7)"} 0.0
# HELP baremetal_ps_pg_fail
# TYPE baremetal_ps_pg_fail gauge
baremetal_ps_pg_fail{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="PS1 PG FAIL (0x9)"} 0.0
baremetal_ps_pg_fail{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="PS2 PG FAIL (0xa)"} 0.0
# HELP baremetal_mem_vpp_pg
# TYPE baremetal_mem_vpp_pg gauge
baremetal_mem_vpp_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM345 VPP PG (0x28)"} 0.0
baremetal_mem_vpp_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM345 VPP PG (0x32)"} 0.0
baremetal_mem_vpp_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM012 VPP PG (0x25)"} 0.0
baremetal_mem_vpp_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM012 VPP PG (0x2f)"} 0.0
# HELP baremetal_mem_vddq_pg
# TYPE baremetal_mem_vddq_pg gauge
baremetal_mem_vddq_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM012 VDDQ PG (0x2e)"} 0.0
baremetal_mem_vddq_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM012 VDDQ PG (0x24)"} 0.0
baremetal_mem_vddq_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM345 VDDQ PG (0x31)"} 0.0
baremetal_mem_vddq_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM345 VDDQ PG (0x27)"} 0.0
# HELP baremetal_vcore_pg
# TYPE baremetal_vcore_pg gauge
baremetal_vcore_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VCORE PG (0x35)"} 0.0
baremetal_vcore_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VCORE PG (0x2b)"} 0.0
# HELP baremetal_mem_vtt_pg
# TYPE baremetal_mem_vtt_pg gauge
baremetal_mem_vtt_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM345 VTT PG (0x29)"} 0.0
baremetal_mem_vtt_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM345 VTT PG (0x33)"} 0.0
baremetal_mem_vtt_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM012 VTT PG (0x26)"} 0.0
baremetal_mem_vtt_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="MEM012 VTT PG (0x30)"} 0.0
# HELP baremetal_pvnn_sw_pg
# TYPE baremetal_pvnn_sw_pg gauge
baremetal_pvnn_sw_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="PVNN SW PG (0x11)"} 0.0
# HELP baremetal_b_pg
# TYPE baremetal_b_pg gauge
baremetal_b_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="3.3V B PG (0x15)"} 0.0
# HELP baremetal_vsbm_sw_pg
# TYPE baremetal_vsbm_sw_pg gauge
baremetal_vsbm_sw_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VSBM SW PG (0x13)"} 0.0
# HELP baremetal_sw_pg
# TYPE baremetal_sw_pg gauge
baremetal_sw_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="2.5V SW PG (0xf)"} 0.0
baremetal_sw_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="5V SW PG (0x10)"} 0.0
baremetal_sw_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="1.8V SW PG (0xe)"} 0.0
# HELP baremetal_vsa_pg
# TYPE baremetal_vsa_pg gauge
baremetal_vsa_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VSA PG (0x37)"} 0.0
baremetal_vsa_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VSA PG (0x2d)"} 0.0
# HELP baremetal_a_pg
# TYPE baremetal_a_pg gauge
baremetal_a_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="3.3V A PG (0x14)"} 0.0
# HELP baremetal_fivr_pg
# TYPE baremetal_fivr_pg gauge
baremetal_fivr_pg{entity_id="3.2 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="FIVR PG (0x36)"} 0.0
baremetal_fivr_pg{entity_id="3.1 (Processor)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="FIVR PG (0x2c)"} 0.0
# HELP baremetal_bp_pg
# TYPE baremetal_bp_pg gauge
baremetal_bp_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="BP0 PG (0xb)"} 0.0
baremetal_bp_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="BP1 PG (0xc)"} 0.0
baremetal_bp_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="BP2 PG (0xd)"} 0.0
# HELP baremetal_vsb_sw_pg
# TYPE baremetal_vsb_sw_pg gauge
baremetal_vsb_sw_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="VSB11 SW PG (0x12)"} 0.0
# HELP baremetal_ndc_pg
# TYPE baremetal_ndc_pg gauge
baremetal_ndc_pg{entity_id="7.1 (System Board)",instance_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",node_name="knilab-master-u9",node_uuid="ac2aa2fd-6e1a-41c8-a114-2084c8705228",sensor_id="NDC PG (0x8)"} 0.0
# HELP baremetal_last_payload_timestamp
# TYPE baremetal_last_payload_timestamp gauge
baremetal_last_payload_timestamp{instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d"} 1.553890522e+09
# HELP baremetal_front_led_panel
# TYPE baremetal_front_led_panel gauge
baremetal_front_led_panel{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Front LED Panel (0x23)"} 0.0
# HELP baremetal_inlet_temp_celsius
# TYPE baremetal_inlet_temp_celsius gauge
baremetal_inlet_temp_celsius{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Inlet Temp (0x5)",status="ok"} 21.0
# HELP baremetal_exhaust_temp_celsius
# TYPE baremetal_exhaust_temp_celsius gauge
baremetal_exhaust_temp_celsius{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Exhaust Temp (0x6)",status="ok"} 36.0
# HELP baremetal_temp_celsius
# TYPE baremetal_temp_celsius gauge
baremetal_temp_celsius{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Temp (0x1)",status="ok"} 44.0
baremetal_temp_celsius{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Temp (0x2)",status="ok"} 43.0
# HELP baremetal_system_unknown
# TYPE baremetal_system_unknown gauge
baremetal_system_unknown{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Unknown (0x8)"} 0.0
# HELP baremetal_current
# TYPE baremetal_current gauge
baremetal_current{entity_id="10.2 (Power Supply)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Current 2 (0x6c)",status="ok"} 0.6
baremetal_current{entity_id="10.1 (Power Supply)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Current 1 (0x6b)",status="ok"} 0.6
# HELP baremetal_pwr_consumption
# TYPE baremetal_pwr_consumption gauge
baremetal_pwr_consumption{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Pwr Consumption (0x76)",status="ok"} 264.0
# HELP baremetal_chassis_mismatch
# TYPE baremetal_chassis_mismatch gauge
baremetal_chassis_mismatch{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Chassis Mismatch (0x37)"} 0.0
# HELP baremetal_tpm_presence
# TYPE baremetal_tpm_presence gauge
baremetal_tpm_presence{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="TPM Presence (0x41)"} 1.0
# HELP baremetal_memory_post_pkg_repair
# TYPE baremetal_memory_post_pkg_repair gauge
baremetal_memory_post_pkg_repair{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="POST Pkg Repair (0x45)"} 1.0
# HELP baremetal_idpt_mem_fail
# TYPE baremetal_idpt_mem_fail gauge
baremetal_idpt_mem_fail{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="iDPT Mem Fail (0x2b)"} 0.0
# HELP baremetal_memory_spared
# TYPE baremetal_memory_spared gauge
baremetal_memory_spared{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Memory Spared (0x11)"} 0.0
# HELP baremetal_memory_mirrored
# TYPE baremetal_memory_mirrored gauge
baremetal_memory_mirrored{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Memory Mirrored (0x12)"} 0.0
# HELP baremetal_memory_ecc_uncorr_err
# TYPE baremetal_memory_ecc_uncorr_err gauge
baremetal_memory_ecc_uncorr_err{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="ECC Uncorr Err (0x2)"} 1.0
# HELP baremetal_memory_b
# TYPE baremetal_memory_b gauge
baremetal_memory_b{entity_id="32.1 (Memory Device)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="B  (0xd6)"} 0.0
# HELP baremetal_memory_a
# TYPE baremetal_memory_a gauge
baremetal_memory_a{entity_id="32.1 (Memory Device)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="A  (0xca)"} 0.0
# HELP baremetal_memory_ecc_corr_err
# TYPE baremetal_memory_ecc_corr_err gauge
baremetal_memory_ecc_corr_err{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="ECC Corr Err (0x1)"} 1.0
# HELP baremetal_power_status
# TYPE baremetal_power_status gauge
baremetal_power_status{entity_id="10.2 (Power Supply)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Status (0x86)"} 0.0
baremetal_power_status{entity_id="10.1 (Power Supply)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Status (0x85)"} 0.0
# HELP baremetal_os_watchdog
# TYPE baremetal_os_watchdog gauge
baremetal_os_watchdog{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="OS Watchdog (0x71)"} 0.0
# HELP baremetal_os_watchdog_time
# TYPE baremetal_os_watchdog_time gauge
baremetal_os_watchdog_time{entity_id="34.1 (BIOS)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="OS Watchdog Time (0x23)"} 0.0
# HELP baremetal_fan_rpm
# TYPE baremetal_fan_rpm gauge
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan4A (0x3b)",status="ok"} 9960.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan1B (0x40)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan8B (0x47)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan3A (0x3a)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan2A (0x39)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan6B (0x45)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan5A (0x3c)",status="ok"} 9720.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan3B (0x42)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan7A (0x3e)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan7B (0x46)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan4B (0x43)",status="ok"} 5880.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan1A (0x38)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan6A (0x3d)",status="ok"} 9360.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan2B (0x41)",status="ok"} 5520.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan5B (0x44)",status="ok"} 5640.0
baremetal_fan_rpm{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan8A (0x3f)",status="ok"} 9240.0
# HELP baremetal_fan_redundancy
# TYPE baremetal_fan_redundancy gauge
baremetal_fan_redundancy{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Fan Redundancy (0x78)"} 0.0
# HELP baremetal_vccio_pg
# TYPE baremetal_vccio_pg gauge
baremetal_vccio_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VCCIO PG (0x34)"} 0.0
baremetal_vccio_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VCCIO PG (0x2a)"} 0.0
# HELP baremetal_voltage
# TYPE baremetal_voltage gauge
baremetal_voltage{entity_id="10.1 (Power Supply)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Voltage 1 (0x6d)",status="ok"} 208.0
baremetal_voltage{entity_id="10.2 (Power Supply)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="Voltage 2 (0x6e)",status="ok"} 208.0
# HELP baremetal_dimm_pg
# TYPE baremetal_dimm_pg gauge
baremetal_dimm_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="DIMM PG (0x7)"} 0.0
# HELP baremetal_ps_pg_fail
# TYPE baremetal_ps_pg_fail gauge
baremetal_ps_pg_fail{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="PS1 PG FAIL (0x9)"} 0.0
baremetal_ps_pg_fail{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="PS2 PG FAIL (0xa)"} 0.0
# HELP baremetal_mem_vpp_pg
# TYPE baremetal_mem_vpp_pg gauge
baremetal_mem_vpp_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM345 VPP PG (0x28)"} 0.0
baremetal_mem_vpp_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM345 VPP PG (0x32)"} 0.0
baremetal_mem_vpp_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM012 VPP PG (0x25)"} 0.0
baremetal_mem_vpp_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM012 VPP PG (0x2f)"} 0.0
# HELP baremetal_mem_vddq_pg
# TYPE baremetal_mem_vddq_pg gauge
baremetal_mem_vddq_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM012 VDDQ PG (0x2e)"} 0.0
baremetal_mem_vddq_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM012 VDDQ PG (0x24)"} 0.0
baremetal_mem_vddq_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM345 VDDQ PG (0x31)"} 0.0
baremetal_mem_vddq_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM345 VDDQ PG (0x27)"} 0.0
# HELP baremetal_vcore_pg
# TYPE baremetal_vcore_pg gauge
baremetal_vcore_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VCORE PG (0x35)"} 0.0
baremetal_vcore_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VCORE PG (0x2b)"} 0.0
# HELP baremetal_mem_vtt_pg
# TYPE baremetal_mem_vtt_pg gauge
baremetal_mem_vtt_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM345 VTT PG (0x29)"} 0.0
baremetal_mem_vtt_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM345 VTT PG (0x33)"} 0.0
baremetal_mem_vtt_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM012 VTT PG (0x26)"} 0.0
baremetal_mem_vtt_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="MEM012 VTT PG (0x30)"} 0.0
# HELP baremetal_pvnn_sw_pg
# TYPE baremetal_pvnn_sw_pg gauge
baremetal_pvnn_sw_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="PVNN SW PG (0x11)"} 0.0
# HELP baremetal_b_pg
# TYPE baremetal_b_pg gauge
baremetal_b_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="3.3V B PG (0x15)"} 0.0
# HELP baremetal_vsbm_sw_pg
# TYPE baremetal_vsbm_sw_pg gauge
baremetal_vsbm_sw_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VSBM SW PG (0x13)"} 0.0
# HELP baremetal_sw_pg
# TYPE baremetal_sw_pg gauge
baremetal_sw_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="2.5V SW PG (0xf)"} 0.0
baremetal_sw_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="5V SW PG (0x10)"} 0.0
baremetal_sw_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="1.8V SW PG (0xe)"} 0.0
# HELP baremetal_vsa_pg
# TYPE baremetal_vsa_pg gauge
baremetal_vsa_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VSA PG (0x37)"} 0.0
baremetal_vsa_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VSA PG (0x2d)"} 0.0
# HELP baremetal_a_pg
# TYPE baremetal_a_pg gauge
baremetal_a_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="3.3V A PG (0x14)"} 0.0
# HELP baremetal_fivr_pg
# TYPE baremetal_fivr_pg gauge
baremetal_fivr_pg{entity_id="3.2 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="FIVR PG (0x36)"} 0.0
baremetal_fivr_pg{entity_id="3.1 (Processor)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="FIVR PG (0x2c)"} 0.0
# HELP baremetal_bp_pg
# TYPE baremetal_bp_pg gauge
baremetal_bp_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="BP0 PG (0xb)"} 0.0
baremetal_bp_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="BP1 PG (0xc)"} 0.0
baremetal_bp_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="BP2 PG (0xd)"} 0.0
# HELP baremetal_vsb_sw_pg
# TYPE baremetal_vsb_sw_pg gauge
baremetal_vsb_sw_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="VSB11 SW PG (0x12)"} 0.0
# HELP baremetal_ndc_pg
# TYPE baremetal_ndc_pg gauge
baremetal_ndc_pg{entity_id="7.1 (System Board)",instance_uuid="6d85703a-565d-469a-96ce-30b6de53079d",node_name="knilab-master-u8",node_uuid="6d85703a-565d-469a-96ce-30b6de53079d",sensor_id="NDC PG (0x8)"} 0.0
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("9100"), debug=True)
