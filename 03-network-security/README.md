# Network Security and Traffic Analysis

## Status
Completed packet-analysis lab using a training capture and Wireshark review.

## Objective
Review a sample packet capture to identify normal and suspicious network behavior, document observable facts, and separate evidence from hypotheses.

## Environment and authorization

I used a safe training or lab capture in a controlled environment and reviewed it with Wireshark. The traffic was part of a learning exercise and did not involve any production systems or personal network data. The source capture is documented as a sanitized educational sample.

## Tools used

- Wireshark
- Packet capture file for a small local network exercise
- Basic protocol knowledge for TCP, DNS, and HTTP

## Display filters and observations

I used filters such as:

- `ip.addr == 192.168.1.x` to isolate traffic related to a local host
- `dns` to review domain lookups
- `tcp.flags.syn == 1 && tcp.flags.ack == 0` to inspect connection attempts
- `http` to review application-layer requests and responses

## Evidence and findings

From the capture, I observed the following patterns:

- Several hosts completed a standard TCP three-way handshake before exchanging data.
- DNS queries were present for common internet services, which matches expected web browsing behavior.
- HTTP requests appeared to use typical GET methods for web resources.
- There were repeated connection attempts from a host to a specific destination, which may indicate a failed service attempt or a brief scan pattern.
- Packet timestamps showed the activity occurred in a short time window, which supports a focused burst of network activity instead of random background traffic.

A sample of the evidence is captured in the repository image `Wireshark_captures_packets.png`.

## Analysis

The evidence supports that the network was actively communicating with normal protocol behavior, including DNS and HTTP traffic. The unusual feature was the sequence of repeated connection attempts and short exchanges, which could suggest a system checking for service availability or a misconfigured client. I would not characterize the activity as a confirmed denial-of-service attack without more context such as target volume, response behavior, and host-to-host relationship.

## Alternative explanations

Possible explanations include:

- a service check from a client or monitoring tool
- a brief scan for a listening port on a local host
- an application retry pattern after an earlier timeout

These are plausible alternatives because a single packet snapshot is limited in scope and cannot by itself explain the full intent behind the traffic.

## Recommendations

1. Validate the destination host and whether the repeated connections were expected.
2. Review host logs for failed service attempts or application errors.
3. Confirm whether the source device or application is configured correctly.
4. Apply firewall and host-based filtering to restrict unnecessary inbound or outbound connections.
5. Keep Wireshark capture evidence with timestamps so future investigations can compare against the same traffic pattern.

## Limitations

This analysis is limited by the single packet-capture sample and the lack of full endpoint context. Without system logs or a broader capture window, it is impossible to state with certainty whether the traffic was malicious, misconfigured, or simply a normal application retry.

## References

- Wireshark documentation for TCP, DNS, and HTTP analysis
- Google Cybersecurity Certificate network troubleshooting and packet-analysis coursework

## Lessons learned

This lab reinforced that packet analysis is strongest when findings are tied to observable protocol behavior and clearly labeled as evidence, not assumptions. I learned how easy it is to overstate a conclusion from a small capture, and I also learned the value of using display filters to isolate relevant traffic and explain the reasoning behind an investigation.
