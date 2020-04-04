#!/bin/bash
# run in root of project

# python -m pip install grpcio grpcio-tools
DIR=application/grpc_services/pos_service/generated
python -m grpc_tools.protoc -I $(pwd)/protos --python_out=$DIR --grpc_python_out=$DIR $(pwd)/protos/pos.proto

# fixes relative imports and makes it compatible with python 2 and 3
# https://github.com/protocolbuffers/protobuf/issues/1491
2to3 $DIR -w -n

