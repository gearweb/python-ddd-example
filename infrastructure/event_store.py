from ksql import KSQLAPI
from ksql.builder import SQLBuilder

client = KSQLAPI('http://localhost:8088')

table_name = 'users'
# columns_type = ['username bigint',
columns_type = ['user_id varchar',
                'username varchar',
                'password varchar',
                'token varchar',
                ]
topic = 'postopic'
value_format='JSON'
key = 'user_id'

client.query(f'drop table {table_name};')
client.query(f'drop stream {table_name};')

client.create_table(table_name=table_name,
                    columns_type=columns_type,
                    topic=topic,
                    value_format=value_format,
                    key=key)

print(client.ksql(f'INSERT INTO {table_name} (username, password, token) VALUES (Piet, sies, my_token);'))

query = client.query('select * from users')
# for item in query: print(item)
print(client.ksql('show tables'))

