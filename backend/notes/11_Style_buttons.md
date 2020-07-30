IT Infrastructure and Cybersecurity
===================================

## Lecture 1

Bandwidth eaters: email/IM/VOIP etc on external network, shared files/printers/databases on internal network.

Real time systems eg voip or video streaming need most protection from latency and congestion, need to guarantee spare bandwidth for them at all times.

## Lecture 2

Application Layer - eg HTTP - individual application
Presentation Layer - e.g. ASCII - encoding
Session Layer - Organising connections
Transport Layer - eg TCP - end to end error checking etc
Network Layer - eg IP - Routing, switching, forwarding addressing
Data Link Layer - Contains MAC and LLC - permissions and error checking
Physical Layer - Cables - low-high transitions of wires etc

IEEE 802.X are all the network standards

Base 5 and base 2 cables:
Coax
terminator - cable - tap for device - cable - terminator
No branches, only taps on main line directly to device

Cat5 is structured cabling, twisted pair
Structured cabling means it can be used for many different things

Cat6 is backwards compatible with cat5, tougher specifications so can reach higher speeds

Virtual networks are good for structured cabling, like containerisation for different usages like phone, fire system etc
Segmenting like this is good for reliability and security

### Important - Limits of unshielded twisted pair cables

Total length of the connection including all patch cables *must* be less that 100m
Comes to 90m to allow 5m on either end for patching
James might set something that can't be done with copper without breaking the limits -> fibre time

Fibre is single-directional, so for a bidirectional link you need double the length for two cables
Multimode fibre is many frequencies, single mode is tiny and extremely high frequencies, much better

## Lecture 3

Every connected device has 48-bit MAC Address

Hubs echo traffic everywhere - dumb
Switches route packets to their destination only - smart
Layer 2 switches are MAC address based, layer 3 can inspect packets - smarter, can learn or be given routes based on IPs for example
Can use layer 2 for small areas and layers 3s to link them to save money

Don't want broadcast domains with more than 250 hosts so broadcasts don't cause congestion
Set up like a tree with redundant routes
Loops in a network can cause feedback loops and congestion

Anything visible from external networks is kept in the de militarised zone, has stricter security

Remember to buy disks for your servers

## Lecture 4

There is a subset of IPv4 addresses that are for private networks (internal) that can be re-used across multiple networks.
There are also multicast addresses that are IPv4 adresses.
IPv4 is 32-bit, IPv6 is 128-bit.

Several classes of network split the IPv4 address into different length sections for netoworks and hosts.
Class C is 192... they have the most networks but the least addresses per network, millions of homes with not many devices each.
Class A is rare and only a few companies have them, they have the most addresses.

Private IP addresses aren't externally accessible, so can be duplicated as long as on separate networks eg 192.168.0.1 or 10.154.63.73.
192.168.0.1/24 means first 24 bits are network, last 8 bits are address so 192.168.0.0 to 192.168.0.255. Subnet mask 255.255.255.0

Traffic on different subnets must go through Layer 3 so you'll need a router (gateway).

65535 TCP ports and 65535 UDP ports (2^16 - 1)
A service will bind to a port e.g. sshd on port 22.

## Lecture 5

User devices better to use dynamic IPs, less work and no understanding needed.
System devices eg printers and servers should be static.
Dynamic IP addresses work by the device broadcasting its MAC to everyone and waiting to be given an IP and configuration.
Dynamic IPs can be done by BootP (old) or DHCP (new).
BootP can be used for network boot so is often built into NICs. DHCP can also respond to BootP.

Dynamic DCHP can give you a lease on an IP address for a certain time, e.g. 2 hours in tower because of lecture length.
Clients can request extensions on the lease.
Dynamic does not work for setting static IP addresses.

Automatic DHCP can set static IPs from the router side rather than the client side. Good for printers etc.
The automatic configurations can be pushed out to clients "updated" every so often, e.g. 10 mins. 
Manual DCHP is where the client makes the rules of static IPs, terrible idea.

Clients might not be able to reach DCHP servers through routers, but routers can have helpers to forward DCHP traffic to the servers.

## Lecture 7

Worst acceptable latency for VOIP is  ms.  Worst acceptable loss is around 1.5%.
QoS marks VOIP packets as important, sent with priority queue so they get treated better across network.
Missing packets can be replaced with silence (Zero), repeat the last packet or try and interpolate inbetween packets.
Faxes can't cope with VOIP because it can be lossy, this is fine beacuse no one should be using fax in current year.
VOIP must allow 999/112 emergency, location is hard to find though.
Can be worth having one or two old-style phones for emergency calls in case of fire etc.

Changeover is best at weekends/holidays etc when usage is lowest.
Lock everyone out while moving data so it can't change.
Email can have temporary downtime but websites etc can't.
Obviously back up data before move.
Keep backup servers in a separate secure location.

Can tag each port on switch as being part of a certain VLAN and then traffic between the switches includes which VLAN each packet is from.
To route between switches can have a router connected to the switch where traffic goes from switch to router on one VLAN and then is sent back but on a different VLAN.

### Create MX records for mail when you make DNS records

### Buy disks and memory for your servers
