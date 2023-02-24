import pickle

# To save internal data to disk, database, or network

class Person:
    age = 23
    name = 'Mohd Izhar'
    employers = {'LTI' : 2021, 'HPCL': 2020, 'LTIMindtree': 2022}
    skills = ['Cloud', 'Python', 'Linux']
    profile = ('github', 'linkedin')


def serialize(obj):
    # converts passed object to binary object
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f'Serialized object: \n{pickled}\n')
    return pickled


# convert binary object to python object
def deserialize(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized: \n{unpickled}\n')


def deserialize_employers(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized Employers: \n{unpickled.employers}\n')
    

# take python function and save to binary file
def obj_to_file(file, obj):
    # write in binary mode
    with open(file, 'wb') as pf:
        pickle.dump(obj, pf, protocol=pickle.HIGHEST_PROTOCOL)


def file_to_object(file, obj):
    # read file in binary mode
    with open(file, 'rb') as pf:
        obj = pickle.load(pf)
        print(obj)
        return obj


if __name__ == "__main__":
    pickled = serialize(Person())
    deserialize(pickled)
    deserialize_employers(pickled)

    obj = obj_to_file('person.xyz', Person())
    person = file_to_object('person.xyz', obj)
    print(f'Person Name: {person.name}')
