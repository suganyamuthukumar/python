import avro
import avro.schema
import happybase
import sys
import os
import json

import io

from avro.datafile import DataFileReader
from avro.io import DatumReader


def get_hbase_avro_decoded_content(schemaFilePath, avroFilePath):
    # connection = happybase.Connection("durahc1nn04-stg.corp.netapp.com")
    # print ("Reading Hbase conent from "+tableName +" Column Name" + columnName + "using key " + rowKey)
    # table = happybase.connection.table(tableName)
    # row = table.row(rowKey)
    # data = row[columnName]


    schema = avro.schema.parse(open(schemaFilePath, 'rb').read())

    bytes_reader = io.BytesIO(open(avroFilePath, 'rb').read())

    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    content = reader.read(decoder)
    print(content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_hbase_avro_decoded_content('C:/willows/AvroFilesToTest/MANIFEST_1.1.avsc', 'C:/willows/AvroFilesToTest/MANIFEST.avro')
    get_hbase_avro_decoded_content('C:/willows/AvroFilesToTest/LOG_FILES_INFO_1.0.avsc', 'C:/willows/AvroFilesToTest/LOG_FILES_INFO.avro')
