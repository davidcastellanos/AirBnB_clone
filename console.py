#!/usr/bin/env python3
"""
Console prompt hbnb
"""
import cmd
from models import storage
from models.base_model import BaseModel
classes={'BaseModel': BaseModel,}

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

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        splits = args.split()
        if len(splits) is not 0:
            if len(splits) is 1 and splits[0] in classes:
                print("** instance id missing **")
                return None
            else:
                if splits[0] not in classes:
                    print("** class doesn't exist **")
                    return None
                else:
                    keys = splits[0] + "." + splits[1]
                    if keys in storage.all().keys():
                        print(storage.all()[keys])
                        return None
                    else:
                        print("** no instance found **")
                        return None
        else:
            print("** class name missing **")
            return None


    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        splits = args.split()
        if len(splits) is not 0:
            if len(splits) is 1 and splits[0] in classes:
                print("** instance id missing **")
                return None
            else:
                if splits[0] not in classes:
                    print("** class doesn't exist **")
                    return None
                else:
                    keys = splits[0] + "." + splits[1]
                    if keys in storage.all().keys():
                        del storage.all()[keys]
                        storage.save()
                    else:
                        print("** no instance found **")
                        return None
        else:
            print("** class name missing **")
            return None


    # def do_all(self, args):
    #     """
    #     Display contents
    #     """
    #     split = args.split()
    #     if split :
    #         try:
    #             eval(split[0])
    #         except:
    #             print("** class doesn't exist **")
    #             return None
    #     for key, value in storage.all().items():
    #         if not split:
    #             print(value)
    #         else:
    #             key = key.split('.')
    #             if split[0] == key[0]:
    #                 print(value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
