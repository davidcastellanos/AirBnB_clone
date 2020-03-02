![Holberton school logo](https://secure.meetupstatic.com/photos/event/b/c/5/6/highres_475548214.jpeg)
# AirBnB Clone (Hbnb) project repository

This repository contains the files for Holberton's **HBnB project**. It can be used by cloning this repository and executing the console file with "./console". This is the first stage of the project in which we must create a console (command interpeter) to create new instances/objects to interact with our HBNB page.

## Files contained:

Brief description of files contained in project:

[**0-index.html**](./0-index.html) : contains the cmd that will execute the command interpeter for the user.

[**1-index.html**](./AUTHORS): contains the authors that took part in the making of this console. 

[**base_model.py**](models/base_model.py):  defines all common attributes/methods for other classes.

[**amenity.py**](models/amenity.py):  class that inherits from BaseModel and contains the structure to create amenities.

[**city.py**](models/city.py): class that inherits from BaseModel and contains the structure to create cities.

[**place.py**](models/place.py): class that inherits from BaseModel and contains the structure to create places.

[**review.py**](models/review.py): class that inherits from BaseModel and contains the structure to create reviews.

[**state.py**](models/state.py): class that inherits from BaseModel and contains the structure to create states.

[**user.py**](models/user.py): class that inherits from BaseModel and contains the structure to create users.

[**file_storage.py**](models/engine/file_storage.py): class that serializes instances to a JSON file and deserializes JSON file to instances.

README.md: this.

## Example:

```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```

### Contact Info:

Git: [David Castellanos](https://github.com/davidcastellanos)

Twitter: [@davcastellanosp](https://twitter.com/davcastellanosp)
