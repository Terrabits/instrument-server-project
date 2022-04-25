from client import Client


# constants
ADDRESS   = 'localhost'
PORT      = 9000


# connect
client = Client(ADDRESS, PORT)

# confirm initial data
response     = client.query('data?')
initial_data = float(response)
assert initial_data == 1.0

# set final data
client.write('data 2.0')

# confirm final data
response   = client.query('data?')
final_data = float(response)
assert final_data == 2.0

# close server
client.write('quit')

# close client
client.close()
