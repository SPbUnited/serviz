"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import grsim_commands_pb2 as grsim__commands__pb2
from . import grsim_replacement_pb2 as grsim__replacement__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12grsim_packet.proto\x1a\x14grsim_commands.proto\x1a\x17grsim_replacement.proto"Z\n\x0cgrSim_Packet\x12!\n\x08commands\x18\x01 \x01(\x0b2\x0f.grSim_Commands\x12\'\n\x0breplacement\x18\x02 \x01(\x0b2\x12.grSim_Replacement')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grsim_packet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _GRSIM_PACKET._serialized_start = 69
    _GRSIM_PACKET._serialized_end = 159