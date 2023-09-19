import json 
import sys
import professor_pb2 
import professor_pb2_grpc
import os

data = {
    'Professors' : [
        {
            'id' : '1007',
            'name' : 'Sebastein Mosser',
            'YearsOfExp' : '15'
        },
        {
            'id' : '1008',
            'name' : 'Antoine Deza',
            'YearsOfExp' : '20'
        },
        {
            'id' : '1009',
            'name' : 'Neerja Mhaskar',
            'YearsOfExp' : '5'
        }
    ]
}

with open('data.json', "w") as f:
  json.dump(data, f)

profs = professor_pb2.Professors()

prof1 = profs.professors.add()
prof1.id = 1007
prof1.name = 'Sebastein Mosser'
prof1.yearsOfExp = 15

prof2 = profs.professors.add()
prof2.id = 1007
prof2.name = 'Antoine Deza'
prof2.yearsOfExp = 20

prof3 = profs.professors.add()
prof3.id = 1007
prof3.name = 'Neerja Mhaskar'
prof3.yearsOfExp = 5

with open('protobuf.data', "wb") as f:
  f.write(profs.SerializeToString())

with open('data.json') as f:
   dataFromJson = json.load(f)

print('DATA FROM JSON : \n')
print(dataFromJson, '\n')
print('SIZE OF JSON DATA FILE (IN bytes) : ', os.stat('data.json').st_size)

profsFromFile = professor_pb2.Professors()
with open('protobuf.data', 'rb') as f:
    profsFromFile.ParseFromString(f.read())

print('DATA FROM JSON : \n')
print(profsFromFile, '\n')
print('SIZE OF ProtobufEncoded DATA FILE (IN bytes) : ', os.stat('protobuf.data').st_size)
