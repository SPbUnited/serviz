"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!vision/ssl_vision_detection.proto"x\n\x11SSL_DetectionBall\x12\x12\n\nconfidence\x18\x01 \x02(\x02\x12\x0c\n\x04area\x18\x02 \x01(\r\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\t\n\x01z\x18\x05 \x01(\x02\x12\x0f\n\x07pixel_x\x18\x06 \x02(\x02\x12\x0f\n\x07pixel_y\x18\x07 \x02(\x02"\x97\x01\n\x12SSL_DetectionRobot\x12\x12\n\nconfidence\x18\x01 \x02(\x02\x12\x10\n\x08robot_id\x18\x02 \x01(\r\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\x13\n\x0borientation\x18\x05 \x01(\x02\x12\x0f\n\x07pixel_x\x18\x06 \x02(\x02\x12\x0f\n\x07pixel_y\x18\x07 \x02(\x02\x12\x0e\n\x06height\x18\x08 \x01(\x02"\xd9\x01\n\x12SSL_DetectionFrame\x12\x14\n\x0cframe_number\x18\x01 \x02(\r\x12\x11\n\tt_capture\x18\x02 \x02(\x01\x12\x0e\n\x06t_sent\x18\x03 \x02(\x01\x12\x11\n\tcamera_id\x18\x04 \x02(\r\x12!\n\x05balls\x18\x05 \x03(\x0b2\x12.SSL_DetectionBall\x12*\n\rrobots_yellow\x18\x06 \x03(\x0b2\x13.SSL_DetectionRobot\x12(\n\x0brobots_blue\x18\x07 \x03(\x0b2\x13.SSL_DetectionRobot')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vision.ssl_vision_detection_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SSL_DETECTIONBALL._serialized_start = 37
    _SSL_DETECTIONBALL._serialized_end = 157
    _SSL_DETECTIONROBOT._serialized_start = 160
    _SSL_DETECTIONROBOT._serialized_end = 311
    _SSL_DETECTIONFRAME._serialized_start = 314
    _SSL_DETECTIONFRAME._serialized_end = 531