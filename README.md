# Instrument Server Project

This project is an [Instrument Server](https://github.com/Terrabits/instrument-server) template.

## Requirements

-   Python 3.7+
-   instrument-server ~= 2.1.0

## Install

Run `scripts/install` to install `requirements.txt.lock`, a known-good package set.

## Start

Run `scripts/start` to start the application.

## Test

Run `scripts/start &` (bash) or `scripts\start-in-background.bat` (windows) to start the application in the background.

Then run `scripts/client` to connect to the server and send a few test commands.

## Devices and Connection Settings

The device life cycle is handled by Instrument Server.

[devices.yaml](devices.yaml) contains the device connection settings:

```yaml
device1:
  type:         my_device
  initial_data: 'initial data'
```

`type` must reference an available Device Factory type. In this case, the `my_device` type matches `MyDeviceFactory.type`. See the `MyDeviceFactory` section below.

## Plugins List

Instrument Server requires a list of plugins for import. [plugins.yaml](plugins.yaml) contains the plugin list for this project:

```yaml
- devices.my_device_factory
- commands.get_data
- commands.set_data
```

### `MyDeviceFactory`

Instrument Server requires a `DeviceFactory` plugin for each supported device type.

A hypothetical device type, `MyDevice`, is included as a placeholder. The `MyDevice` class definition can be found here:

[devices/my_device.py](devices/my_device.py)

Then, the `MyDeviceFactory` plugins makes device type `my_device` available in Instrument Server and `devices.yaml`.

In [devices.my_device_factory.py](devices.my_device_factory.py):

```python
class MyDeviceFactory(DeviceFactoryBase):
    type = 'my_device'

    def open(self, *, initial_data=b''):
        return MyDevice(initial_data)

    def close(self, device):
        device.close()
```

The keyword arguments for the `MyDeviceFactory.open` method determine the required and default connection settings for the `my_device` type.

The `my_device` type settings are:

```comment
my_device settings:
  initial_data (optional): initial value of MyDevice.data.
                           Default is an empty string `''`.
```

### `GetDataCommand`

This command returns `device1.data` (float).

Syntax: `data?`

In [commands/get_data.py](commands/get_data.py):

```python
class GetDataCommand(BasicCommand):
    command = 'data?'
    args    = {}

    def code(self, devices, args):
        data = devices['device1'].data
        return str(data).encode()  # bytes
```

### `SetDataCommand`

This command sets `device1.data` to a new `float` value.

Syntax: `data <float>`

In [commands/set_data.py](commands/set_data.py):

```python
class SetDataCommand(BasicCommand):
    command = 'data'
    args    = {'data': float}

    def code(self, devices, args):
        devices['device1'].data = args['data']
```

## References

-   <https://github.com/Terrabits/instrument-server>
