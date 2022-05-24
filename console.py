#!/usr/bin/python3
"""Console for BanjoAPI"""
""" Switch server from stable to test mode, make tokens in database, etc """
import cmd


class BanjoCommand(cmd.Cmd):
    """Entry point for command interpreter
    """
    prompt = "(Banjo) $"


    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

if __name__ == '__main__':
    BanjoCommand().cmdloop()
