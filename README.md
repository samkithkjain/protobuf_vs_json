# Comparing Protobuf based file storage vs JSON based file storage 

To regenerate python client code:

```bash
python3 -m grpc_tools.protoc \
  --proto_path=. \
  --python_out=. \
  --grpc_python_out=. \
  professor.proto
```
To run python code and view the results 
```bash
python3 main.py
```