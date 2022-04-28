from instrument_server.commands import BasicCommand


class Command(BasicCommand):
    command = 'command1'
    args    = {'arg1': float}

    def code(self, devices, args):
        instr = devices['instr']
        arg1  = args['arg1']

        # TODO
        print(f'command1(arg1={arg1}) executed', flush=True)

        return b'response for client (optional)'


# required for
# instrument server plugins
IS_COMMAND_PLUGIN = True
plugin            = Command
