#!/usr/bin/env python3

"""
Advanced Packet Sniffer - Entry Point

Author: Your Name
Description:
    CLI interface for starting packet capture with filtering,
    logging, and analysis options.
"""

import argparse
import sys
from sniffer import start_sniffing


def validate_args(args):
    """Validate CLI arguments."""
    if args.count < 0:
        print("[!] Packet count cannot be negative.")
        sys.exit(1)

    if args.output and not args.output.endswith(".json"):
        print("[!] Output file must be a .json file.")
        sys.exit(1)


def print_banner():
    banner = r"""
    ============================================
        Advanced Packet Sniffer & Analyzer
    ============================================
    """
    print(banner)


def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="Advanced Packet Sniffer (Cybersecurity Tool)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-i", "--iface",
        help="Network interface (e.g., eth0, wlan0)",
        default=None
    )

    parser.add_argument(
        "-f", "--filter",
        help="BPF filter (e.g., tcp, udp, port 80)",
        default=None
    )

    parser.add_argument(
        "-c", "--count",
        help="Number of packets to capture (0 = unlimited)",
        type=int,
        default=0
    )

    parser.add_argument(
        "-o", "--output",
        help="Output JSON file",
        default="packets.json"
    )

    parser.add_argument(
        "--verbose",
        help="Enable verbose output",
        action="store_true"
    )

    args = parser.parse_args()
    validate_args(args)

    try:
        print(f"[*] Interface   : {args.iface or 'Default'}")
        print(f"[*] Filter      : {args.filter or 'None'}")
        print(f"[*] Packet Count: {'Unlimited' if args.count == 0 else args.count}")
        print(f"[*] Output File : {args.output}")
        print(f"[*] Verbose     : {args.verbose}")
        print("\n[*] Starting capture...\n")

        start_sniffing(
            iface=args.iface,
            bpf_filter=args.filter,
            count=args.count,
            output_file=args.output
        )

    except PermissionError:
        print("[!] Permission denied. Run as root/admin.")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\n[!] Capture stopped by user.")
        sys.exit(0)

    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()