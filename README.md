📌 Description

This project provides a command-line interface to capture and analyze network packets using customizable filters and output logging. It is designed to demonstrate practical expertise in network security, packet inspection, and tool development.

The tool supports flexible configuration via CLI arguments, allowing users to specify network interfaces, packet filters, capture limits, and output formats.

🚀 Features
📡 Real-time packet capture
⚙️ CLI-based configuration
🔍 BPF filter support (tcp, udp, port-based filtering)
🧾 JSON output logging
🛑 Graceful shutdown handling
🔐 Input validation and error handling
🛠️ Requirements
Python 3.x
Root/Admin privileges (required for packet sniffing)

Install dependencies:

pip install -r requirements.txt
▶️ Usage

Run the tool using:

sudo python main.py [options]
⚙️ Command-Line Arguments
Argument	Description	Example
-i, --iface	Network interface	eth0, wlan0
-f, --filter	BPF filter	tcp, udp, port 80
-c, --count	Number of packets (0 = unlimited)	50
-o, --output	Output JSON file	packets.json
--verbose	Enable verbose output	flag
💡 Example
sudo python main.py --iface eth0 --filter "tcp" --count 100 --output data.json
📊 Sample Output (Console)
[*] Interface   : eth0
[*] Filter      : tcp
[*] Packet Count: 100
[*] Output File : data.json
[*] Verbose     : False

[*] Starting capture...
