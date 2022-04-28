# Instrument Server Project

This project is an [Instrument Server](https://github.com/Terrabits/instrument-server) template.

## Requirements

-   Python 3.7+
-   instrument-server ~= 2.1.1

## Install

Run `scripts/install` to install `requirements.txt.lock`, a known-good package set.

## Start

Run `scripts/start` to start the application.

## Test

Run `scripts/start &` (bash) or `scripts\start-in-background.bat` (windows) to start the application in the background.

Then run `scripts/client` to connect to the server and send a few test commands.

## Commands

To implement a new command, copy [commands/command1.py](commands/command1.py) to a new file (e.g. `command2.py`), then:

-   change the `command` property
-   change the `args` property
-   change the `code` method
-   edit [**main**.py](__main__.py) to include the new plugin module in the plugins list (see below).

## Devices

To implement a new device type, copy [devices/device1_factory.py](devices/device1_factory.py) to a new file (e.g. `device2_factory.py`), then:

-   change the `type` property
-   change the `open` method
-   change the `close` method
-   edit [**main**.py](__main__.py) to include the new plugin module in the plugins list (see below).

## Main

[**main**.py](__main__.py) contains the application starting point.

Remember to:

-   edit the `PLUGINS` module list to include all `commands/` and `devices/` plugins.
-   edit the `DEVICES` settings to match `devices/` types and the current instrument setup.

## References

-   <https://github.com/Terrabits/instrument-server>
