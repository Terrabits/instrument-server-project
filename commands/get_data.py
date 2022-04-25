from instrument_server.commands import BasicCommand


class GetDataCommand(BasicCommand):
    command = 'data?'
    args    = {}

    def code(self, devices, args):
        data = devices['device1'].data
        return str(data).encode()  # bytes


# for import
IS_COMMAND_PLUGIN = True
plugin            = GetDataCommand
