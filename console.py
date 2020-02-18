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
        if len(args) is not 0:
            try:
                my_model = eval(arg + "()")
                my_model.save()
                print(my_model.id)
            except:
                print("** class doesn't exist **")
        if len(args) is 0:
            print("** class name missing **")
            return None

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        args = args.split()

        if len(args) is 0:
            print("** class name missing **")
            return None
        if len(args) is not 0:
            try:
                eval(args[0])
            except:
                print("** class doesn't exist **")
                return None
        if len(args) < 2:
            print("** instance id missing **")
            return None

        keys = args[0] + "." + args[1].replace("\"", "")

        if keys in storage.all():
            del storage.all()[keys]
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
