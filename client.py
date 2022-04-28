from client import Client


# constants
ADDRESS   = 'localhost'
PORT      = 9000


# connect to server
client = Client(ADDRESS, PORT)

# send command1
response = client.query('command1 3.14159')
print('received:')
print(f"'{response}'")
assert 'response' in response

# close
client.write('quit')
client.close()
