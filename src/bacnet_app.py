from collections import deque

from bacpypes.apdu import ReadPropertyRequest, Error, AbortPDU, ReadPropertyACK, WritePropertyRequest, SimpleAckPDU
from bacpypes.app import BIPSimpleApplication
from bacpypes.constructeddata import Array, Any
from bacpypes.core import stop, deferred
from bacpypes.object import get_datatype
from bacpypes.pdu import Address
from bacpypes.primitivedata import Null, Atomic, Integer, Unsigned, Real, CharacterString, OctetString, BitString


class ReadWriteApplication(BIPSimpleApplication):
    def __init__(self, point_list, *args):
        BIPSimpleApplication.__init__(self, *args)

        self._request = None
        self.response_values = []
        self.point_queue = deque(point_list)
        print('self.point_queue', self.point_queue)

    def refresh_points_list(self, point_list):
        self.point_queue = deque(point_list)

    def read_request(self):
        if not self.point_queue:
            stop()
            return
        addr, obj_type, obj_inst, prop_id = self.point_queue.popleft()
        self._request = ReadPropertyRequest(
            objectIdentifier=(obj_type, int(obj_inst)),
            propertyIdentifier=prop_id,
        )
        self._request.pduDestination = Address(addr)
        BIPSimpleApplication.request(self, self._request)

    def write_request(self, *args):
        addr = args[0]
        obj_type = args[1]
        obj_inst = int(args[2])
        prop_id = args[3]
        self._request = WritePropertyRequest(
            objectIdentifier=(obj_type, obj_inst),
            propertyIdentifier=prop_id
        )
        self._request.pduDestination = Address(addr)

        datatype = args[4]
        value = args[5]
        if datatype == 'Integer':
            datatype = Integer
        elif datatype == 'Unsigned':
            datatype = Unsigned
        elif datatype == 'Real':
            datatype = Real
        elif datatype == 'OctetString':
            datatype = OctetString
        elif datatype == 'BitString':
            datatype = BitString
        else:
            datatype = CharacterString

        if (value == 'null'):
            value = Null()
        elif issubclass(datatype, Atomic):
            if datatype is Integer:
                value = int(value)
            elif datatype is Real:
                value = float(value)
            elif datatype is CharacterString or datatype is OctetString:
                value = str(value)
                print(value)
            elif datatype is Unsigned:
                value = int(value)
            value = datatype(value)
        self._request.propertyValue = Any()
        try:
            self._request.propertyValue.cast_in(value)
        except Exception as error:
            print(error)

        BIPSimpleApplication.request(self, self._request)

    def confirmation(self, apdu):
        if isinstance(apdu, Error):
            print(apdu)
            pass

        elif isinstance(apdu, AbortPDU):
            print(apdu)
            pass

        elif isinstance(apdu, SimpleAckPDU):
            print(apdu)
            self.response_values = []
            stop()

        elif (isinstance(self._request, ReadPropertyRequest)) and (isinstance(apdu, ReadPropertyACK)):
            datatype = get_datatype(apdu.objectIdentifier[0], apdu.propertyIdentifier)
            if not datatype:
                raise TypeError("unknown datatype")

            if issubclass(datatype, Array) and (apdu.propertyArrayIndex is not None):
                if apdu.propertyArrayIndex == 0:
                    value = apdu.propertyValue.cast_out(Unsigned)
                else:
                    value = apdu.propertyValue.cast_out(datatype.subtype)
            else:
                value = apdu.propertyValue.cast_out(datatype)

            self.response_values.append(value)
            deferred(self.read_request)
        else:
            pass
