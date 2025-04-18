"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#messages_robocup_ssl_geometry.proto" \n\x08Vector2f\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02"e\n\x14SSL_FieldLineSegment\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x15\n\x02p1\x18\x02 \x02(\x0b2\t.Vector2f\x12\x15\n\x02p2\x18\x03 \x02(\x0b2\t.Vector2f\x12\x11\n\tthickness\x18\x04 \x02(\x02"y\n\x13SSL_FieldCicularArc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x19\n\x06center\x18\x02 \x02(\x0b2\t.Vector2f\x12\x0e\n\x06radius\x18\x03 \x02(\x02\x12\n\n\x02a1\x18\x04 \x02(\x02\x12\n\n\x02a2\x18\x05 \x02(\x02\x12\x11\n\tthickness\x18\x06 \x02(\x02"\xd8\x01\n\x15SSL_GeometryFieldSize\x12\x14\n\x0cfield_length\x18\x01 \x02(\x05\x12\x13\n\x0bfield_width\x18\x02 \x02(\x05\x12\x12\n\ngoal_width\x18\x03 \x02(\x05\x12\x12\n\ngoal_depth\x18\x04 \x02(\x05\x12\x16\n\x0eboundary_width\x18\x05 \x02(\x05\x12*\n\x0bfield_lines\x18\x06 \x03(\x0b2\x15.SSL_FieldLineSegment\x12(\n\nfield_arcs\x18\x07 \x03(\x0b2\x14.SSL_FieldCicularArc"\xc9\x02\n\x1dSSL_GeometryCameraCalibration\x12\x11\n\tcamera_id\x18\x01 \x02(\r\x12\x14\n\x0cfocal_length\x18\x02 \x02(\x02\x12\x19\n\x11principal_point_x\x18\x03 \x02(\x02\x12\x19\n\x11principal_point_y\x18\x04 \x02(\x02\x12\x12\n\ndistortion\x18\x05 \x02(\x02\x12\n\n\x02q0\x18\x06 \x02(\x02\x12\n\n\x02q1\x18\x07 \x02(\x02\x12\n\n\x02q2\x18\x08 \x02(\x02\x12\n\n\x02q3\x18\t \x02(\x02\x12\n\n\x02tx\x18\n \x02(\x02\x12\n\n\x02ty\x18\x0b \x02(\x02\x12\n\n\x02tz\x18\x0c \x02(\x02\x12\x1f\n\x17derived_camera_world_tx\x18\r \x01(\x02\x12\x1f\n\x17derived_camera_world_ty\x18\x0e \x01(\x02\x12\x1f\n\x17derived_camera_world_tz\x18\x0f \x01(\x02"h\n\x10SSL_GeometryData\x12%\n\x05field\x18\x01 \x02(\x0b2\x16.SSL_GeometryFieldSize\x12-\n\x05calib\x18\x02 \x03(\x0b2\x1e.SSL_GeometryCameraCalibration')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_robocup_ssl_geometry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VECTOR2F._serialized_start = 39
    _VECTOR2F._serialized_end = 71
    _SSL_FIELDLINESEGMENT._serialized_start = 73
    _SSL_FIELDLINESEGMENT._serialized_end = 174
    _SSL_FIELDCICULARARC._serialized_start = 176
    _SSL_FIELDCICULARARC._serialized_end = 297
    _SSL_GEOMETRYFIELDSIZE._serialized_start = 300
    _SSL_GEOMETRYFIELDSIZE._serialized_end = 516
    _SSL_GEOMETRYCAMERACALIBRATION._serialized_start = 519
    _SSL_GEOMETRYCAMERACALIBRATION._serialized_end = 848
    _SSL_GEOMETRYDATA._serialized_start = 850
    _SSL_GEOMETRYDATA._serialized_end = 954