CMD_PORT: int = 29001
RTD_PORT: int = 29000


# IO constants
CTRLR_MAX_DIG_IN_BYTES = 8
CTRLR_MAX_AN_IN = 4
CTRLR_MAX_DIG_OUT_BYTES = 8
CTRLR_MAX_AN_OUT = 4

AVAILABLE_AN_IN_INDEX_COUNT = 4
AVAILABLE_AN_OUT_INDEX_COUNT = 4
AVAILABLE_DIG_IN_INDEX_COUNT = 24  # real count
AVAILABLE_DIG_OUT_INDEX_COUNT = 24  # real count

AMPERAGE_VALUES_RANGE = (4, 20)  # мА
VOLTAGE_INPUT_INDEXES_RANGE = 2
VOLTAGE_VALUES_RANGE = (0, 10)  # В

BITS_IN_BYTE = 8

# value according to robot core logics (btw, real amount is 24 in
# [1.2.50.33555456/3] api version)
DIGITAL_IO_INDEX_COUNT = 64

# Log constants
LOGGER_NAME = 'RC_LOGGER'
TAB = '\t'
N_LINE = '\n'
TNL = N_LINE + (TAB * 8) + '   '


# Different constants
CHECK_FREQUENCY_SEC = 0.05
DISABLE = 0
EMPTY_BYTES = b''
ENABLE = 1
IK_N_SOL = 8
JOINTS_COUNT = 6
JOYSTICK_ACCEL_MAX_DEG_SEC = 40
JOYSTICK_ACCEL_MAX_RAD_SEC = 10
JOYSTICK_SPEED_MAX_DEG_SEC = 30
JOYSTICK_SPEED_MAX_RAD_SEC = 0.5
NO_FUNC_ANSWER_VALUE = 0
CTRLR_CMD_PAYLOAD_LENGTH_SIZE = 4
CTRLR_CMD_TYPE_LENGTH = 4
SET_CTRLR_STATE_AWAIT_SEC = 60
SET_MOTION_MODE_AWAIT_SEC = 5
WP_ADD_TIMEOUT = 5
WP_COUNTER_MAX_VALUE = 65535

# Range of positions and orientations in kinematic_state
FKINE_RESPONSE_JOINT_POSITION_SLICE = slice(1, 7)
ORIENTATION_SLICE = slice(3, 6)
POSITION_SLICE = slice(0, 3)

# Validate values
ACCEL_LIMITS = (0, 15)  # м/c^2
BLEND_LIMITS = (0, None)  # м
JOINT_COUNT = 6
JOINT_ACCEL_LIMITS_DEG_SEC = (0, 1500)
JOINT_ACCEL_LIMITS_RAD_SEC = (0, 26.18)
JOINT_SPEED_LIMITS_DEG_SEC = (0, 180)
JOINT_SPEED_LIMITS_RAD_SEC = (0, 3.14)
TCP_POSITION_COUNT = 3
SPEED_LIMITS = (0, 3)  # м/с
POSITION_ORIENTATION_LENGTH = 6
WP_COUNT_LIMITS = (0, None)

# PACK/UNPACK FORMATS
CTRLR_ADD_WP_CMD_PACK_FORMAT = 'i6d6d6d6BB7di0q'
CTRLR_FKINE_CMD_PACK_FORMAT = '6d'
CTRLR_FKINE_CMD_UNPACK_FORMAT = 'i6d'
CTRLR_GET_LAST_POSITION_UNPACK_FORMAT = '6d'
CTRLR_IKINE_CMD_PACK_FORMAT = '6d'
CTRLR_IKINE_CMD_UNPACK_FORMAT = 'i48d'
CTRLR_IO_GET_FUNCTION_UNPACK_VALUES_TYPE = 'i'
CTRLR_IO_SET_FUNCTION_PACK_FORMAT = '1b3xi'
CTRLR_IO_SET_VALUE_PACK_FORMAT = '24B4d'
CTRLR_JOINT_JOG_CMD_PACK_FORMAT = 'i6b2x'
CTRLR_SET_GET_PAYLOAD_PACK_UNPACK_FORMAT = '4d'
CTRLR_SET_MOVE_SCALE_PACK_UNPACK_FORMAT = 'dd'
CTRLR_SET_GET_STATE_PACK_UNPACK_FORMAT = 'i'
CTRLR_SET_GET_TOOL_PACK_UNPACK_FORMAT = '6d'
JOG_CMD_PACK_FORMAT = 'i6B6d6d6d6d'
JOG_CMD_SET_GET_PARAMS_PACK_UNPACK_FORMAT = 'B6B6d6d6d6d'
OMM_ENABLE_DISABLE_PACK_FORMAT = 'B'
CTRLR_CMD_DATA_PACK_UNPACK_FORMAT = 'i'

# GUI
ALLOWED_GUI_ENTRY_SYMBOLS = r'^-?\d*\.?\d*$'
