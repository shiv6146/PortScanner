# PortScanner
A light weight network port scanner that can be customized based on the scanning requirements

Requirements
============
1. Python 3

Usage
=====
1. Run the following command from your terminal or command prompt with Python 3 installed and available in your system path.
2. `python thread_port_scan.py <website-to-be-scanned> <number-of-threads> <starting-port-range> <ending-port-range>`
3. For example `python thread_port_scan.py example.com 20 10 100` command scans the example.com for open ports with 20 threads running simultaneously and for port numbers ranging between 10 and 99 only.
