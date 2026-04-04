# Advanced Packet Sniffer

A powerful, user-friendly network packet sniffer built with Python and Scapy. Capture, analyze, and export network packets with ease.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## Features

✨ **Core Features**
- Real-time packet capture from any network interface
- Berkeley Packet Filter (BPF) syntax support for advanced filtering
- Multi-format export (JSON, CSV)
- Detailed packet layer analysis (Ethernet, IP, TCP, UDP, ICMP, ARP)
- Hex dump display capability
- Colored terminal output
- Statistics reporting

🔒 **Security Features**
- Protocol-specific packet filtering
- Port-based filtering
- MAC address filtering
- Packet payload inspection

## Requirements

- Python 3.7 or higher
- Linux, macOS, or Windows with Npcap/WinPcap
- Administrator/Root privileges (for packet capture)
- Scapy 2.4.5+

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/packet-sniffer.git
cd packet-sniffer
```

### 2. Install Dependencies

```bash
# On Linux/macOS
pip install -r requirements.txt

# On Windows (with Npcap installed)
pip install -r requirements.txt

# For development
pip install -r requirements.txt
pip install pytest black flake8 mypy
```

### 3. Verify Installation

```bash
python3 main.py --help
```

## Usage

### Basic Capture

```bash
# Capture all packets on default interface
sudo python3 main.py

# Capture TCP packets on port 80
sudo python3 main.py -i eth0 -c 100 -f "tcp port 80"

# Capture DNS traffic
sudo python3 main.py -i wlan0 -c 50 -f "udp port 53" -o dns_packets.json

# Capture ARP traffic
sudo python3 main.py -i eth0 -f "arp" --stats
```

### Advanced Examples

```bash
# Capture with verbose output and hex dump
sudo python3 main.py -i eth0 -c 100 --verbose --hex -o packets.json

# Capture HTTP traffic with statistics
sudo python3 main.py -i eth0 -f "tcp port 80 or tcp port 443" --stats -o http_packets.csv

# Capture ICMP (ping) traffic
sudo python3 main.py -i eth0 -f "icmp" -c 50

# Capture traffic from specific IP
sudo python3 main.py -i eth0 -f "host 192.168.1.100" -o host_traffic.json

# Capture traffic between two hosts
sudo python3 main.py -i eth0 -f "host 192.168.1.100 and host 8.8.8.8" -c 200

# Capture with live display (no file save)
sudo python3 main.py -i eth0 --live --verbose
```

## Command-Line Arguments

```
usage: Advanced Packet Sniffer [-h] [-i IFACE] [-f FILTER] [-c COUNT]
                               [-o OUTPUT] [-l LOG_LEVEL] [-v] 
                               [--no-color] [--live] [--hex] [--stats]

options:
  -h, --help                Show this help message
  -i, --iface IFACE         Network interface (e.g., eth0, wlan0)
  -f, --filter FILTER       BPF filter (e.g., 'tcp port 80', 'udp')
  -c, --count COUNT         Number of packets to capture (default: unlimited)
  -o, --output OUTPUT       Output file (.json or .csv)
  -l, --log-level LEVEL     Logging level (DEBUG, INFO, WARNING, ERROR)
  -v, --verbose             Enable verbose output
  --no-color                Disable colored output
  --live                    Live mode (no file save)
  --hex                     Display hex dump
  --stats                   Show statistics at the end
```

## BPF Filter Examples

```bash
# TCP traffic
-f "tcp"

# UDP traffic
-f "udp"

# HTTP traffic
-f "tcp port 80"

# HTTPS traffic
-f "tcp port 443"

# DNS traffic
-f "udp port 53"

# SSH traffic
-f "tcp port 22"

# ARP traffic
-f "arp"

# ICMP (ping)
-f "icmp"

# Traffic to/from specific IP
-f "host 192.168.1.1"

# Traffic from specific subnet
-f "net 192.168.1.0/24"

# Multiple protocols
-f "tcp port 80 or tcp port 443"

# Exclude traffic
-f "tcp and not port 22"
```

## Output Formats

### JSON Output

```json
[
  {
    "timestamp": "2024-01-15 10:30:45.123456",
    "packet_number": 1,
    "layers": [
      {
        "type": "Ethernet",
        "src_mac": "00:11:22:33:44:55",
        "dst_mac": "ff:ff:ff:ff:ff:ff",
        "proto": 2048
      },
      {
        "type": "IPv4",
        "src_ip": "192.168.1.100",
        "dst_ip": "8.8.8.8",
        "ttl": 64,
        "length": 60,
        "protocol": 6,
        "flags": ""
      },
      {
        "type": "TCP",
        "src_port": 54321,
        "dst_port": 80,
        "flags": "S",
        "seq": 1234567890,
        "ack": 0,
        "window": 65535
      }
    ],
    "summary": "Ether / IP / TCP 192.168.1.100.54321 > 8.8.8.8.80 S"
  }
]
```

### CSV Output

```
packet_number,timestamp,summary,layers_count
1,2024-01-15 10:30:45.123456,Ether / IP / TCP 192.168.1.100.54321 > 8.8.8.8.80 S,4
2,2024-01-15 10:30:45.234567,Ether / IP / TCP 8.8.8.8.80 > 192.168.1.100.54321 SA,4
```

## Project Structure

```
packet-sniffer/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── sniffer.py         # Core sniffer module
│   └── logger.py          # Logging utility
├── tests/
│   ├── __init__.py
│   ├── test_sniffer.py
│   └── test_logger.py
└── docs/
    ├── USAGE.md           # Usage guide
    ├── FILTERS.md         # Filter examples
    └── API.md             # API documentation
```

## Network Interfaces

### Linux
```bash
# List available interfaces
ip link show
# or
ifconfig
```

### macOS
```bash
# List available interfaces
ifconfig
# or
networksetup -listallhardwareports
```

### Windows
```bash
# List available interfaces
ipconfig
```

## Troubleshooting

### Permission Denied
```bash
# Solution: Run with sudo
sudo python3 main.py -i eth0
```

### Interface Not Found
```bash
# Solution: Check available interfaces
ip link show          # Linux
ifconfig             # macOS
ipconfig             # Windows
```

### Scapy Import Error
```bash
# Solution: Reinstall dependencies
pip uninstall scapy
pip install scapy --no-cache-dir
```

### No Packets Captured
- Ensure the interface is correct
- Check if the BPF filter is valid
- Verify network activity exists

## Performance Tips

1. **Limit Packet Count**: Use `-c` flag to limit captures
2. **Use Specific Filters**: Narrow down packets with BPF filters
3. **Avoid Large Files**: Export to JSON/CSV instead of memory
4. **Use Live Mode**: For monitoring without file I/O overhead

## Security Considerations

⚠️ **Important**
- Packet capture requires root/admin privileges
- Only capture on networks you own or have permission to monitor
- Respect privacy laws and regulations (GDPR, CCPA, etc.)
- Do not use for unauthorized network monitoring
- Properly handle captured network data containing sensitive information

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_sniffer.py
```

## Code Quality

```bash
# Format code
black src/ main.py

# Lint code
flake8 src/ main.py

# Type checking
mypy src/ main.py
```

## Changelog

### Version 1.0.0 (2024-01-15)
- Initial release
- Basic packet capture functionality
- JSON/CSV export support
- BPF filtering
- Statistics reporting

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## Author

**Your Name**
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)

## Acknowledgments

- [Scapy](https://scapy.readthedocs.io/) - Packet manipulation library
- [Python](https://www.python.org/) - Programming language
- [Wireshark](https://www.wireshark.org/) - Packet analysis inspiration

## Support

For issues, questions, or suggestions:
1. Open an [GitHub Issue](https://github.com/yourusername/packet-sniffer/issues)
2. Check existing documentation
3. Review closed issues for solutions

## References

- [Scapy Documentation](https://scapy.readthedocs.io/)
- [Berkeley Packet Filter](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter)
- [TCP/IP Protocol Suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)
- [Network Security Best Practices](https://owasp.org/)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
