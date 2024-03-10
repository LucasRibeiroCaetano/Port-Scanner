import socket

def scan_ports(ip_address):

    # Display scan options menu
    print("\nScan Options:")
    print("1. Common Ports Scan")
    print("2. Specific Port Scan")
    print("3. Full Scan\n")

    # Get user choice
    choice = input("Enter the number of the desired scan type: ")

    # Perform the selected scan
    if choice == "1":
        common_ports_scan(ip_address)
    elif choice == "2":
        specific_port_scan(ip_address)
    elif choice == "3":
        full_scan(ip_address)
    else:
        print("Invalid choice. Please enter a valid number.")

def common_ports_scan(ip_address):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 443, 445, 993, 995, 3389, 8080]  # Add more ports as needed
    scan_results = []

    for port in common_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                s.connect((ip_address, port))
                scan_results.append((port, "\033[32;1mOpen\033[0m"))
        except (socket.timeout, socket.error):
            scan_results.append((port, "\033[31;1mClosed\033[0m"))

    print(f"\n[ \033[36mINFO\033[0m ] Common Ports Scan Results for IP address {ip_address}:")
    for port, status in scan_results:
        print(f"Port {port}: {status}")

def specific_port_scan(ip_address):
    specific_port = int(input("Enter the specific port to scan: "))
    scan_result = ""

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip_address, specific_port))
            scan_result = "\033[32;1mOpen\033[0m"
    except (socket.timeout, socket.error):
        scan_result = "\033[31;1mClosed\033[0m"

    print(f"\n[ \033[36mINFO\033[0m ] Scan Result for port {specific_port} on IP address {ip_address}: {scan_result}")

def full_scan(ip_address):
    start_port = 1
    end_port = 65535
    scan_results = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((ip_address, port))
                scan_results.append((port, "\033[32;1mOpen\033[0m"))
        except (socket.timeout, socket.error):
            scan_results.append((port, "\033[31;1mClosed\033[0m"))

    print(f"\n[ \033[36mINFO\033[0m ] Full Scan Results for IP address {ip_address} (Ports {start_port}-{end_port}):")
    for port, status in scan_results:
        print(f"Port {port}: {status}")

def main():
    print("\033[34mPort Scanner\033[0m")
    print("Made by: https://github.com/LucasRibeiroCaetano\n")

    # Prompt the user for an IP address
    ip_address = input("Enter IP address: ")

    # Call the function to scan ports using the specified IP address
    scan_ports(ip_address)
    print("\n\n")    
    input()


if __name__ == "__main__":
    main()

