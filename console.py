#!/usr/bin/env python3
"""
Console prompt hbnb
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


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

    def do_all(self, args):
        """
        Display contents
        """
        split = args.split()
        content = []
        if len(args) is 0:
            for key, value in storage.all().items():
                key = key.split('.')
                content.append(str(value))
            print(content)
        elif split[0] in classes:
            for key, value in storage.all().items():
                key = key.split('.')
                if split[0] == key[0]:
                    content.append(str(value))
            print(content)
        else:
            print("** class doesn't exist **")
            return None

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        splits = args.split()

        if not splits:
            print("** class name missing **")
        else:
            if splits[0] not in classes:
                print("** class doesn't exist **")
            elif len(splits) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(splits[0], splits[1])
                if key not in storage.all().keys():
                    print("** no instance found **")
                elif len(splits) == 2:
                    print("** attribute name missing **")
                elif len(splits) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], splits[2], splits[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
