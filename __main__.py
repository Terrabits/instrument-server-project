from instrument_server.command_line import main


# my app settings
APP_NAME = 'Instrument Server Project'
PLUGINS  = [
    'commands.command1',
    'devices.device1_factory']
DEVICES  = {
    'instr': {
        'type':     'device1',
        'setting1': 'required'}}


if __name__ == '__main__':
    # start my app
    main(APP_NAME, PLUGINS, DEVICES)
