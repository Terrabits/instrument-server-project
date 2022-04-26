from instrument_server.command_line import main


# my app settings
APP_NAME = 'my_app'
PLUGINS  = [
    'commands.get_data',
    'commands.set_data',
    'devices.my_device_factory']
DEVICES  = {
    'device1': {
        'type':        'my_device',
        'initial_data': 1.0}}


if __name__ == '__main__':
    # start my app
    main(APP_NAME, PLUGINS, DEVICES)
