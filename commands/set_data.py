from instrument_server.commands import BasicCommand


class SetDataCommand(BasicCommand):
    command = 'data'
    args    = {'data': float}

    def code(self, devices, args):
        devices['device1'].data = args['data']


# for import
IS_COMMAND_PLUGIN = True
plugin            = SetDataCommand
