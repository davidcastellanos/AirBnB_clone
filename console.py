#!/usr/bin/env python3
"""
Console prompt hbnb
"""
import cmd
from models import storage
from models.base_model import BaseModel

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

    def do_quit(self, args):
        """
        Exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exit the program
        """
        print()
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if len(args) is 0:
            print("** class name missing **")
            return None
        try:
            my_model = eval(args + "()")
            my_model.save()
            print(my_model.id)
        except:
            print("** class doesn't exist **")

    # def do_show(self, args):
    #     """
    #     Prints the string representation of an instance
    #     based on the class name and id
    #     """
    #     split = args.split()
    #     if len(args) is 0:
    #         print("** class name missing **")
    #         return None
    #     elif len(args) is 1:
    #         print("** instance id missing **")
    #         return None
    #     args = args.split()
    #     keys = args[0] + "." + args[1].replace("\"", "")
    #     if keys in storage.all():
    #         print(storage.all()[keys])
    #     else:
    #         print("** no instance found **")


    # def do_destroy(self, args):
    #     """
    #     Deletes an instance based on the class name and id
    #     """
    #     args = args.split()

    #     if len(args) is 0:
    #         print("** class name missing **")
    #         return None
    #     elif len(args) is not 0:
    #         try:
    #             eval(args[0])
    #         except:
    #             print("** class doesn't exist **")
    #             return None
    #     elif len(args) < 2:
    #         print("** instance id missing **")
    #         return None
    #     else:
    #         keys = args[0] + "." + args[1].replace("\"", "")
    #         if keys in storage.all():
    #             del storage.all()[keys]
    #             storage.save()
    #         else:
    #             print("** no instance found **")

    def do_all(self, args):
        """
        Display contents
        """
        split = args.split()
        if split :
            try:
                eval(split[0])
            except:
                print("** class doesn't exist **")
                return None
        for key, value in storage.all().items():
            if not split:
                print(value)
            else:
                key = key.split('.')
                if split[0] == key[0]:
                    print(value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
