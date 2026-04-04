#!/usr/bin/env python3
"""
Advanced Packet Sniffer - Entry Point
Author: Your Name
Version: 1.0.0
Description:
    A comprehensive network packet sniffer with filtering, analysis, and logging.
    Supports real-time capture, BPF filtering, and JSON/CSV export.
"""

import argparse
import sys
import os
from src.sniffer import PacketSniffer
from src.logger import Logger


def validate_args(args):
    """Validate CLI arguments."""
    if args.count < 0:
        print("[!] Packet count cannot be negative.")
        sys.exit(1)
    
    if args.output and not (args.output.endswith(".json") or args.output.endswith(".csv")):
        print("[!] Output file must be .json or .csv format.")
        sys.exit(1)
    
    if args.log_level not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
        print("[!] Invalid log level. Use: DEBUG, INFO, WARNING, ERROR")
        sys.exit(1)


def print_banner():
    """Display application banner."""
    banner = r"""
    ╔════════════════════════════════════════════╗
    ║   Advanced Packet Sniffer & Analyzer       ║
    ║   Version 1.0.0                            ║
    ║   Cybersecurity Tool                       ║
    ╚════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """Main execution function."""
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="Advanced Network Packet Sniffer (Cybersecurity Tool)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Capture TCP packets on port 80
  python3 main.py -i eth0 -c 100 -f "tcp port 80" -o packets.json
  
  # Capture DNS traffic
  python3 main.py -i wlan0 -c 50 -f "udp port 53"
  
  # Capture all traffic
  python3 main.py -i eth0 -c 1000 --verbose
  
  # Export to CSV
  python3 main.py -i eth0 -o packets.csv
        """
    )
    
    # Core arguments
    parser.add_argument(
        "-i", "--iface",
        help="Network interface (e.g., eth0, wlan0, en0)",
        default=None,
        type=str
    )
    
    parser.add_argument(
        "-f", "--filter",
        help="BPF filter (e.g., 'tcp port 80', 'udp', 'arp')",
        default=None,
        type=str
    )
    
    parser.add_argument(
        "-c", "--count",
        help="Number of packets to capture (0 = unlimited)",
        type=int,
        default=0
    )
    
    # Output arguments
    parser.add_argument(
        "-o", "--output",
        help="Output file (.json or .csv)",
        default="packets.json",
        type=str
    )
    
    parser.add_argument(
        "-l", "--log-level",
        help="Logging level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        type=str
    )
    
    # Feature flags
    parser.add_argument(
        "-v", "--verbose",
        help="Enable verbose output",
        action="store_true"
    )
    
    parser.add_argument(
        "--no-color",
        help="Disable colored output",
        action="store_true"
    )
    
    parser.add_argument(
        "--live",
        help="Display live packet summary (doesn't save to file)",
        action="store_true"
    )
    
    parser.add_argument(
        "--hex",
        help="Display packet hex dump",
        action="store_true"
    )
    
    parser.add_argument(
        "--stats",
        help="Show packet statistics at the end",
        action="store_true"
    )
    
    args = parser.parse_args()
    validate_args(args)
    
    # Initialize logger
    logger = Logger(level=args.log_level, use_color=not args.no_color)
    
    # Display configuration
    logger.info("=" * 50)
    logger.info("Packet Sniffer Configuration")
    logger.info("=" * 50)
    logger.info(f"Interface    : {args.iface or 'Default (all)'}")
    logger.info(f"Filter       : {args.filter or 'None'}")
    logger.info(f"Count        : {'Unlimited' if args.count == 0 else args.count}")
    logger.info(f"Output File  : {args.output if not args.live else 'Live mode (no save)'}")
    logger.info(f"Verbose      : {args.verbose}")
    logger.info(f"Hex Dump     : {args.hex}")
    logger.info(f"Statistics   : {args.stats}")
    logger.info("=" * 50)
    logger.info("")
    
    # Create sniffer instance
    try:
        sniffer = PacketSniffer(
            interface=args.iface,
            bpf_filter=args.filter,
            packet_count=args.count,
            output_file=args.output if not args.live else None,
            verbose=args.verbose,
            show_hex=args.hex,
            show_stats=args.stats,
            logger=logger
        )
        
        logger.info("Starting packet capture...")
        logger.info("Press Ctrl+C to stop capture\n")
        
        sniffer.start()
        
    except PermissionError:
        logger.error("Permission denied. Run with sudo/admin privileges.")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.warning("\n\nCapture stopped by user.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
