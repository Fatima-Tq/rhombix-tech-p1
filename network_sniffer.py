# Network Sniffer - Rhombix Technologies Task 1
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

PACKET_COUNT = 0

def analyze_packet(packet):
    """Analyze and print packet information"""
    global PACKET_COUNT
    PACKET_COUNT += 1
    
    print("=" * 60)
    print(f"📦 Packet #{PACKET_COUNT}")
    
    if packet.haslayer(IP):
        ip = packet[IP]
        src_ip = ip.src
        dst_ip = ip.dst
        proto = ip.proto
        
        print(f"📤 Source IP: {src_ip}")
        print(f"📥 Destination IP: {dst_ip}")
        
        # Check TCP
        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print(f"🔹 Protocol: TCP")
            print(f"🔹 Source Port: {tcp.sport}")
            print(f"🔹 Dest Port: {tcp.dport}")
            
            # Check for HTTP
            if tcp.dport == 80 or tcp.sport == 80:
                print("🌐 HTTP Traffic Detected!")
                if packet.haslayer(Raw):
                    try:
                        payload = packet[Raw].load.decode('utf-8', errors='ignore')
                        print(f"📝 Payload: {payload[:150]}...")
                    except:
                        pass
        
        # Check UDP
        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print(f"🔹 Protocol: UDP")
            print(f"🔹 Source Port: {udp.sport}")
            print(f"🔹 Dest Port: {udp.dport}")
            
            if udp.dport == 53 or udp.sport == 53:
                print("🌐 DNS Traffic Detected!")
        
        # Check ICMP
        elif packet.haslayer(ICMP):
            icmp = packet[ICMP]
            print(f"🔹 Protocol: ICMP")
            print(f"🔹 Type: {icmp.type}")
            print(f"🔹 Code: {icmp.code}")
        
        else:
            print(f"🔹 Protocol: Other ({proto})")
    
    else:
        print("📡 Non-IP packet")
    
    print("=" * 60)

def start_sniffer():
    """Start the packet sniffer"""
    print("\n" + "=" * 60)
    print("🔍 NETWORK SNIFFER STARTED")
    print("=" * 60)
    print("📌 Capturing packets... Press Ctrl+C to stop")
    print("=" * 60 + "\n")
    
    try:
        sniff(prn=analyze_packet, count=0)
    except PermissionError:
        print("\n❌ ERROR: Please run as Administrator!")
        print("   Right-click Command Prompt → Run as administrator")
    except KeyboardInterrupt:
        print(f"\n\n✅ Sniffer stopped. Captured {PACKET_COUNT} packets.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    start_sniffer()