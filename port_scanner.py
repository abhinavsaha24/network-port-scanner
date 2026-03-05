import socket
import threading
from queue import Queue

target = input("Enter target IP: ")

print(f"\nScanning target {target}...\n")

port_queue = Queue()

# Common port-service mapping
services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def scan_port():
    while not port_queue.empty():
        port = port_queue.get()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            service = services.get(port, "Unknown")
            print(f"Port {port} OPEN | Service: {service}")

        s.close()
        port_queue.task_done()

for port in range(1,1025):
    port_queue.put(port)

for _ in range(100):
    thread = threading.Thread(target=scan_port)
    thread.daemon = True
    thread.start()

port_queue.join()

print("\nScan completed.")