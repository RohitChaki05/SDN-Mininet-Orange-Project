# SDN-Mininet-Orange-Project
<img width="1357" height="138" alt="SDN3" src="https://github.com/user-attachments/assets/4e3f3c3c-1a64-4ad2-b9d7-4543979aaed9" />
<img width="1600" height="255" alt="SDN2" src="https://github.com/user-attachments/assets/adbf3231-7dbc-49d8-a110-f8d5fc655b65" />
<img width="1600" height="517" alt="SDN1" src="https://github.com/user-attachments/assets/81a2ae40-8297-454f-9ef0-58fd9ad7081f" />
<img width="1214" height="198" alt="SDN5" src="https://github.com/user-attachments/assets/55212539-6031-4b79-8a5e-bbbbec625484" />
<img width="875" height="291" alt="SDN4" src="https://github.com/user-attachments/assets/aa6b223a-d677-4bd3-b8a2-f7f2bee71a36" />
SDN Multi-Switch Flow Table Analyzer (Orange Problem)
1. Problem Statement & ObjectiveObjective: The goal of this project is to implement an SDN-based solution using Mininet and an OpenFlow controller (Ryu) that demonstrates controller-switch interaction and flow rule design.Problem: Managing and monitoring flow rules across multiple switches is critical in SDN. This solution implements a "Learning Switch" logic that dynamically installs flow rules based on network traffic and allows for the analysis of active vs. idle rules using packet statistics.
2. Topology JustificationThe topology consists of:1 Remote Controller (Ryu): Centralized brain managing the control plane.2 Open vSwitch (OVS) Instances: Connected in a linear fashion to simulate multi-hop flow propagation.3 Hosts: Distributed across switches to test inter-switch and intra-switch communication.Justification: This specific "Multi-Switch" setup is required to prove that the controller can handle packet_in events from different datapath IDs (DPIDs) and correctly route traffic through the network fabric.
3. Setup and Execution StepsFollow these steps to replicate the environment:Environment: Ensure Mininet and Ryu are installed on your Ubuntu/Linux system.Run the Topology: Execute the Python script:sudo python3 mytopo.pyRun the Controller: In a separate terminal, start the Ryu application:ryu-manager controller_logic.pyVerification: Use the Mininet CLI to test connectivity:mininet> pingall
4. SDN Logic & Flow Implementation
The controller_logic.py implements the following SDN principles:
Packet_In Handling: The controller captures unknown packets, extracts the source MAC address, and maps it to a specific switch port.
Match-Action Design: Once the destination MAC is learned, the controller installs an Explicit Flow Rule (Match: In_Port + Destination MAC -> Action: Output to learned Port).
Flow Mod: Using OpenFlow v1.3, the controller sends FlowMod messages to the switches to handle future packets at hardware speed.
5. Performance Observation & Analysis
Test Scenario 1: Functional Forwarding (Normal Behavior)Action: Executed pingall in the Mininet CLI.Result: 0% packet loss achieved. This confirms that the controller correctly processed packet_in events for all three hosts across both switches.
Test Scenario 2: Flow Table & Packet Count AnalysisAction: Ran h1 ping -c 5 h3 followed by sudo ovs-ofctl dump-flows s1.Observation:Latency: Average RTT was measured at approximately 0.128ms, indicating efficient rule processing.Packet Counts: The n_packets field in the flow table incremented correctly (showing 5 packets for the ICMP request), proving the switch is using installed rules.
6. References: Mininet Documentation. Ryu SDN Framework OpenFlow Tutorial. Orange Project Student Guidelines.
