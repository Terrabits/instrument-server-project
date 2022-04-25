from .my_device                   import MyDevice
from instrument_server.devices    import DeviceFactoryBase


class MyDeviceFactory(DeviceFactoryBase):
    type = 'my_device'

    def open(self, *, initial_data=b''):
        return MyDevice(initial_data)

    def close(self, my_device):
        my_device.close()


# for import
IS_DEVICE_PLUGIN = True
plugin           = MyDeviceFactory
