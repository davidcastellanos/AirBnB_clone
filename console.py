#!/usr/bin/env python3
"""
Console prompt hbnb
"""
import cmd



class HBNBCommand(cmd.Cmd):
    """
    Prompt class
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Exit the program
        """
        pass

    def do_quit(self, arg):
        """
        Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
