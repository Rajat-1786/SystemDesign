import json
import os

from convertJsonToObj import convert

# Import the generated Thrift code (replace 'gen.py.company' with your actual module path)
from ttypes import Company

# Import Thrift serializers
from thrift.protocol import TBinaryProtocol,TCompactProtocol
from thrift.transport import TTransport
from thrift.TSerialization import serialize

def read_json_file(file_path):
    # Open the JSON file in read mode
    with open(file_path, 'r') as json_file:
        # Parse the JSON data from the file
        data = json.load(json_file)
    # Return the parsed data
    return data

def binary_encoding_by_cp(data):
    company = convert(data); 
    output_protocol = TCompactProtocol.TCompactProtocol(TTransport.TMemoryBuffer())
    company.write(output_protocol)
    binary_data = output_protocol.trans.getvalue() 
    return binary_data

def binary_encoding_by_bp(data):
    company = convert(data)
    output_protocol = TBinaryProtocol.TBinaryProtocol(TTransport.TMemoryBuffer())
    company.write(output_protocol)
    binary_data = output_protocol.trans.getvalue() 
    return binary_data

def binaryToJsonCp(binary_data):
    # Deserialize the binary data back to a Thrift object
    input_protocol = TCompactProtocol.TCompactProtocol(TTransport.TMemoryBuffer(binary_data))
    new_company = Company()

    new_company.read(input_protocol)
    print(new_company.name)

def binaryToJsonBp(binary_data):
    # Deserialize the binary data back to a Thrift object
    input_protocol = TBinaryProtocol.TBinaryProtocol(TTransport.TMemoryBuffer(binary_data))
    new_company = Company()

    new_company.read(input_protocol)
    print(new_company.name)

def main():
    
    file_path = 'input.json'
    data = read_json_file(file_path)
    # Calculate the size of the original JSON data
    original_json = json.dumps(data)
    original_size = len(original_json.encode('utf-8'))

    binary_data = binary_encoding_by_cp(data)
    serialized_size = len(binary_data)

    binaryToJsonCp(binary_data)



    # Calculate the size of the serialized data
    

    # Compare the sizes and output the results
    print(f"Size of original JSON data: {original_size} bytes")
    print(f"Size of serialized Thrift data: {serialized_size} bytes")
    print(f"Compression ratio: {(original_size - serialized_size) / original_size:.2%}")

if __name__ == "__main__":
    main()
