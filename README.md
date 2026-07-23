## 📋 Complete README.md (Copy This Whole Thing)

```markdown
# 🔍 Network Packet Sniffer

## A Python-based Network Traffic Analyzer

---

### 📌 Overview

This is a **Network Packet Sniffer** developed as Task 1 for the **Rhombix Technologies Cyber Security Internship**. It captures and analyzes live network traffic, displaying detailed information about each packet including source/destination IPs, protocols, ports, and detects HTTP/DNS traffic.

---

### ✨ Features

- 📦 **Packet Capture** - Real-time network packet sniffing
- 🔍 **Protocol Detection** - Identifies TCP, UDP, and ICMP protocols
- 🌐 **HTTP Detection** - Detects HTTP traffic on port 80
- 🌐 **DNS Detection** - Detects DNS traffic on port 53
- 📊 **Packet Analysis** - Displays source/destination IPs and ports
- 🎯 **Real-time Monitoring** - Live packet capture with continuous updates

---

### 🛠️ Technologies Used

- Python 3.13+
- Scapy Library
- Raw Sockets
- Network Protocol Analysis

---

### 📋 Prerequisites

- ✅ Python 3.13+ installed
- ✅ Administrator/root privileges
- ✅ Scapy library installed
- ✅ Active network connection

---

### 🚀 Installation & Setup

#### 1️⃣ Install Dependencies

```bash
pip install scapy
```

#### 2️⃣ Run the Sniffer (Administrator Required)

**On Windows:**
```bash
# Open Command Prompt as Administrator
python network_sniffer.py
```

**On Linux/macOS:**
```bash
# Run with sudo
sudo python3 network_sniffer.py
```

---

### 📊 Sample Output

```
============================================================
🔍 NETWORK SNIFFER STARTED
============================================================
📌 Capturing packets... Press Ctrl+C to stop
============================================================

============================================================
📦 Packet #1
📤 Source IP: xxxxx
📥 Destination IP: xxxxx
🔹 Protocol: TCP
🔹 Source Port: xxxxx
🔹 Dest Port: 443
============================================================

📦 Packet #2
📤 Source IP: xxxxx
📥 Destination IP:xxxxx
🔹 Protocol: TCP
🔹 Source Port: 54322
🔹 Dest Port: 80
🌐 HTTP Traffic Detected!
============================================================

📦 Packet #3
📤 Source IP: xxxxxxxx
📥 Destination IP:xxxxx
🔹 Protocol: UDP
🔹 Source Port:xxxx
🔹 Dest Port: xx
🌐 DNS Traffic Detected!
============================================================
```

---

### 📁 Project Structure

```
RhombixTechnologies_Tasks/
│
├── network_sniffer.py          # Main sniffer script
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

---

### 🔧 Code Explanation

**Main Components:**

| Component | Function |
|-----------|----------|
| `analyze_packet()` | Processes each captured packet |
| `start_sniffer()` | Initializes the packet sniffer |
| `sniff()` | Scapy function for packet capture |
| `haslayer()` | Checks if packet has specific protocol |

**Protocol Detection:**
```python
if packet.haslayer(TCP):    # TCP Packet
if packet.haslayer(UDP):    # UDP Packet  
if packet.haslayer(ICMP):   # ICMP Packet
if packet.haslayer(Raw):    # Raw payload data
```

---

### ⚠️ Important Notes

- 🛡️ **Run as Administrator/Root** - Required for packet sniffing
- 🔒 **Educational Purpose Only** - Use only on networks you own
- 📡 **Network Interface** - Captures on default interface
- 🎯 **Traffic Volume** - May capture many packets quickly

---

### 🐛 Troubleshooting

| Error | Solution |
|-------|----------|
| `PermissionError` | Run as Administrator |
| `No module named 'scapy'` | Run `pip install scapy` |
| `File not found` | Check file path and name |
| `Python not found` | Install Python and add to PATH |

---


### 🙏 Acknowledgments

- **Rhombix Technologies** for providing this opportunity
- **Scapy Team** for the amazing library
- **Open Source Community** for continuous learning resources

---



<p align="center">
  Made with ❤️ for <strong>Rhombix Technologies</strong> Internship
</p>

<p align="center">
  <img src="https://img.shields.io/badge/-Cyber%20Security-blue" alt="Cyber Security">
  <img src="https://img.shields.io/badge/-Python-success" alt="Python">
  <img src="https://img.shields.io/badge/-Network%20Sniffer-orange" alt="Network Sniffer">
</p>
```




