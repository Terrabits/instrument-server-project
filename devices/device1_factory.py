from instrument_server.devices import DeviceFactoryBase


class DeviceFactory(DeviceFactoryBase):
    type = 'device1'

    def open(self, *, setting1, setting2='optional'):
        # TODO
        # - create new object
        # - open object with settings
        return object()

    def close(self, device):
        # TODO
        # e.g. device.close()
        pass


# required for
# instrument server plugins
IS_DEVICE_PLUGIN = True
plugin           = DeviceFactory
