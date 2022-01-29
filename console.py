#!/usr/bin/env python3
""" Console application to control the Banjo API """

import cmd
from datetime import datetime
import psutil
import os
import signal



class BanjoCommand(cmd.Cmd):
    """ Banjo Console """
    prompt = "(Banjo) "

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def do_test_mode(self, arg=None):
        """Enable/Disable Stable API for testing """
        process_name = "uvicorn"
        pid = None
        if (arg is None or len(arg) < 1):
            print("Enable/Disable Stable API")
            return (False)
        if (arg.split()[0] == "Enable"):
            for proc in psutil.process_iter():
                if process_name in proc.name():
                    pid = proc.pid
            if (pid is None):
                print("Stable API is not Enabled!")
                return (False)
            os.kill(pid, signal.SIGTERM)
        elif (arg.split()[0] == "Disable"):
            print("Test: Restart job /stable api via cron")
        else:
            print("Unknown passed argument")
        return (False)

    def emptyline(self):
        """Overwriting the emptyline method """
        return (False)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return (True)


if __name__ == '__main__':
    """ Main method """
    BanjoCommand().cmdloop()
