# Network Port Scanner

A **multithreaded Python port scanner** that detects open ports and identifies common network services on a target host.
This tool demonstrates core **network security concepts**, including socket programming, concurrent scanning, and service identification.

---

## Features

* ⚡ Fast **multithreaded port scanning**
* 🔍 Detects **open TCP ports**
* 🌐 Identifies common services (HTTP, SSH, DNS, etc.)
* 📡 Scans ports **1–1024**
* 🛠 Simple and lightweight security tool

---

## Technologies Used

* **Python**
* **Socket Programming**
* **Multithreading**

---

## Usage

1. Run the scanner:

```
python port_scanner.py
```

2. Enter the target IP address or domain name:

```
scanme.nmap.org
```

---

## Example Output

```
Enter target IP: scanme.nmap.org

Scanning target scanme.nmap.org...

Port 22 OPEN | Service: SSH
Port 53 OPEN | Service: DNS
Port 80 OPEN | Service: HTTP
Port 443 OPEN | Service: HTTPS

Scan completed.
```

---

## Disclaimer

This tool is created **for educational and ethical security testing purposes only**.
Do **not scan networks or systems without proper authorization*
