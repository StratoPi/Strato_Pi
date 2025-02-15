# Modbus.py exclusively relies on this file, no pressure
# This file contains modbus control parameters
import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from modbus_tk.exceptions import ModbusInvalidResponseError

# Setup modbus master/slave communication
WRITE = cst.WRITE_SINGLE_REGISTER
READ = cst.READ_HOLDING_REGISTERS
PORT = '/dev/ttyAMA0'
BAUDRATE = 9600
BYTESIZE = 8
PARITY = 'N'
STOPBITS = 1
XONXOFF = 0

# Register values
MAINS_VOLTAGE = 3207 #0.1V
CTR_W_SPEED = 8601
CTR_W_FREQ = 8501
SET_SPEED = 8602 # RPM
SET_FREQ = 8502 #0.1Hz
SET_TORQ = 8505 #0.1%
STATUS_W_SPEED = 8603
STATUS_W_FREQ = 3201
DRIVE_STATE = 3240
OUTPUT_VEL = 8604 # RPM
OUTPUT_FREQ = 3202 #0.1Hz
MOTOR_TORQ = 3205
MOTOR_CURRENT = 3204
MOTOR_VOLTAGE = 3208 #V
MOTOR_POWER = 3211 #%
DRIVE_THERMAL_STATE = 3209
MOTOR_THERMAL_STATE = 9630
LOGIC_OUTPUTS = 5212
REF_SWITCH = 8411

# Switch Controls
W_TERMINAL = 96
W_MODBUS = 97

# Motors
MOTOR_1 = 1
MOTOR_2 = 2
MOTOR_3 = 3

motors = [MOTOR_1, MOTOR_2, MOTOR_3]
