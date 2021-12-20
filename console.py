#!/usr/bin/env python3
# Console application to control the Banjo API
import cmd
from datetime import datetime

class BanjoCommand(cmd.Cmd):
    """ Banjo Console """
    prompt = "(Banjo) "

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
