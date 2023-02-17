### Network Activity and Packet Analysis

```bash
pip install scapy==2.4.5
pip install ipython==8.4.0
    # Use ipython as cli
```

```bash
# Enter scapy cli
> scapy
>>> sniff()           # Will capture live packets, Press ctrl + c to exit. 
>>> a = _             # _ is used to get output of last command
>>> a.show()          # to show the packet captured.
>>> sniff(count=20)   # capture only 20 packets
>>> sniff(timeout=10) # capture only for 10 seconds

>>> conf.ifaces        # to get interface details
>>> conf.iface         # to get single interface
>>> sniff(iface="eth0", count=10)       # capture only for specific interface and 10 packets
>>> sniff(timeout=10, filter="src 10.x.x.x")      # filter packets
>>> sniff(timeout=10, filter="dst 10.x.x.x")      # filter packets

>>> l_filter = sniff(lfilter=lambda x: x[ICMP].type == 8, filter="icmp", timeout=10)
>>> l_filter.show()

# prn - allows to run a function for every packets that are captured
>>> prn_cmd = sniff(prn=lambda x: x.sprintf("%IP.src%"), timeout=5)
>>> prn_cmd.show()

# sniffing using the offline parameter - allows to take capture file and import them in scapy
>>> offline_par = sniff(offline="filename.pcap")
>>> offline_par.show()

# saving captures to File with wrpcap
>>> wrpcap("filename.pcap", variable) # variable for example: offline_par

>>> a.summary()
>>> a[0].show()         # look for specific packet

>>> pkt = IP(dst="192.x.x.x/y")/TCP(sport=RandShort(), dport=80, flags="S")
>>> ans,unans = sr(pkt, timeout=10, retry=3, filter="port 80")
>>> ans 
>>> unans 
>>> ans.show()
>>> a.hexdump()
>>> a.filter(lambda x: TCP in x)

# ------
# IP layer
>>> a = IP()
>>> ls(a)
>>> a = IP(src="10.x.x.x", dst="10.x.x.x")
>>> ls(a)
>>> a
>>> a.src 
>>> a.dst 
>>> a.ttl 

# creating a TCP layer on top
>>> a = IP(src="10.x.x.x", dst="10.x.x.x")/TCP()
>>> ls(a)

# Putting ethernet layer
>>> d = Ether()
>>> d

```
