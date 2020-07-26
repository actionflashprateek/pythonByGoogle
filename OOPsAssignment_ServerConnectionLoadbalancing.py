#In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.

#To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. For our simulation, each connection creates a random amount of load in the server, between 1 and 10.
#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
        

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]
        

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        total = sum(self.connections.values())
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#
server = Server()
server.add_connection("192.168.1.1")
server.add_connection("192.168.1.2")
server.add_connection("192.168.1.3")
print(server.connections)
print(server.load())
print(server)

server.close_connection("192.168.1.1")
server.close_connection("192.168.1.2")
server.close_connection("192.168.1.3")
print(server.connections)
print(server.load())
print(server)


print("--"*60)


#Alright, we now have a basic implementation of the server class. Let's look at the basic LoadBalancing class. This class will start with only one server available. When a connection gets added, it will randomly select a server to serve that connection, and then pass on the connection to the server. The LoadBalancing class also needs to keep track of the ongoing connections to be able to close them. This is the basic structure:

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()] #Inheritence as a list

    def add_connection1(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        self.ensure_availability()
        server_random = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server_random
        # Add the connection to the server
        server_random.add_connection(connection_id)
        #print(server_random.connections)		

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        self.connections[connection_id].close_connection(connection_id)
        #print(self.connections[connection_id].connections)
        # Remove the connection from the load balancer
        del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        sum = 0
        for item in self.servers:
            sum += item.load()
        return sum / len(self.servers) 

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

l = LoadBalancing()
l.add_connection1("10.1.1.10")
print(l.connections)
print(l.connections["10.1.1.10"].connections)
print(l.avg_load())
#l.close_connection("10.1.1.10")
#print(l.connections["10.1.1.10"].connections)
#print(l.connections)
#print(l.avg_load())
l.servers.append(Server())
print(l.avg_load())
l.close_connection("10.1.1.10")
#print(l.connections["10.1.1.10"].connections)
print(l.servers)
print(l.avg_load())
print("--"*60)
print("--"*60)

suma=0 
for connection in range(20):
    l.add_connection1(connection)
    suma+=l.connections[connection].connections[connection]
    print(l.connections[connection].connections[connection])
print(suma)
print(suma/2)
print(l.avg_load())

print("--"*60)
print("--"*60)

print(l.avg_load())
print(l)
l.add_connection1("10.1.1.20")
print(l.avg_load())
print(l)




"""
>py "final assist.py"
{'192.168.1.1': 5.2042411603880225, '192.168.1.2': 9.785165613170644, '192.168.1.3': 6.859392043443179}
21.848798817001846
21.85%
{}
0
0.00%
------------------------------------------------------------------------------------------------------------------------
{'10.1.1.10': <__main__.Server object at 0x00851358>}
{'10.1.1.10': 10.059921079865596}
10.059921079865596
5.029960539932798
[<__main__.Server object at 0x00851358>, <__main__.Server object at 0x00875250>]
0.0
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
3.7265010363766518
9.904372665575702
7.056090724960833
6.808964974605829
6.601169798719534
10.731711689370766
7.805799650989677
9.400218717364053
7.986690046772482
7.446595735861439
9.3421613403709
1.3139401655025942
9.963937594902918
3.849280542024525
5.586874012336933
6.163441386281985
2.4391110217021064
2.7316064561417166
7.209650138559406
7.744577935068
133.8126956334881
66.90634781674405
66.90634781674402
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
44.60423187782934
[73.74%,60.07%,0.00%]
45.41235896102848
[73.74%,60.07%,2.42%]
"""
