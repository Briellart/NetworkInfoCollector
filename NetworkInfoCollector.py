import psutil
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from timezonefinder import TimezoneFinder


class Network:
    def __init__(self):
        self.connections = psutil.net_connections(kind='inet')
        self.ip_addresses = []  
        
    def network_ips(self):
        connections = psutil.net_connections(kind='inet')
        ip_addresses = []  
        for conn in connections:
            if conn.raddr:
                ip_addresses.append(conn.raddr[0])  # Añadir la dirección IP remota a la lista
            
            if conn.laddr:
                ip_addresses.append(conn.laddr[0])  # Añadir la dirección IP local a la lista
              
        self.ip_addresses = list(set(ip_addresses))  
        return self.ip_addresses
    
    def get_timezone(self, latitude, longitude):
        tf = TimezoneFinder()
        return tf.timezone_at(lng=longitude, lat=latitude)
    
    def get_info(self):
        connections=psutil.net_connections(kind='inet')
        for conn in connections:
            print(f"[+] Process Name: {psutil.Process(conn.pid).name()}")
            print(f"[+] Process PID: {conn.pid}")
            print(f"[+] Local Address: {conn.laddr}")
            print(f"[+] Remote Address: {conn.raddr if conn.raddr else ''}")
            print(f"[+] Status: {conn.status}\n")
        


if __name__ == '__main__':
    network = Network()
    while True:
        print("\n[+] NETWORK MENU:")
        print("1. Get ALL Network Information")
        print("2. Get information about a specific IP address")
        print("3. Get Unique IP addresses used")
        print("4. Exit")
        opcion = input("Enter an option: ")

        if opcion == '1':
            network.get_info()

        elif opcion == '2': 
            ip = input("Enter the IP address to get information: ")
            response = DbIpCity.get(ip, api_key='free')
            
            print(f"IP: {response.ip_address}")
            print(f"City: {response.city}")
            print(f"Region: {response.region}")
            print(f"Country: {response.country}")
            print(f"Latitude: {response.latitude}")
            print(f"Longitude: {response.longitude}")
            timezone = network.get_timezone(response.latitude, response.longitude)
            print(f"Timezone: {timezone}")
        
        elif opcion == '3':
            print("\n[+] Unique IP addresses Used:")
            ip_addressess = network.network_ips()
            for ip in ip_addressess:
                print(f"Unique IP address: {ip}")
        

        elif opcion == '4':  
            break  
