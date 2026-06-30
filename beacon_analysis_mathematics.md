# The Mathematics of C2 Beacon Detection

When a human analyzes network traffic, a 20% randomized jitter on a 60-second beacon interval (resulting in connections firing randomly between 48 and 72 seconds) looks like organic noise. However, when we apply data science and time-series mathematics to the traffic flows, the programmatic rigidity is immediately exposed.

This document breaks down the actual mathematical models and algorithms used by advanced IDS and threat-hunting platforms to unmask command and control (C2) beacons.

## 1. Feature Extraction: The Flow Tuple
Before doing any math, the IDS must group the network traffic. It aggregates raw packets into **Flows** using a 3-tuple or 5-tuple:
*   `[Source IP]` + `[Destination IP]` + `[Destination Port]` (e.g., `192.168.1.50` -> `198.51.100.22:443`).

For every unique tuple, the IDS calculates statistical features over a given time window (e.g., 24 hours). The two most critical features for beacon detection are:
1.  **IAT (Inter-Arrival Time):** The time delta (in milliseconds) between each consecutive connection.
2.  **Payload Size:** The number of bytes sent and received per connection.

## 2. Unmasking Jitter via IAT Standard Deviation
Let $T_{base}$ be the core beacon interval (e.g., 60 seconds). Let $J$ be the jitter percentage (e.g., 10%). 
The formula for the next connection time is:
$$T_{next} = T_{base} + (T_{base} \times Random(-J, J))$$

While $T_{next}$ seems random, it is bounded. If we take thousands of these connections over a 24-hour period, we calculate the **Mean ($\mu$)** and the **Standard Deviation ($\sigma$)** of the IAT.

*   **The Law of Large Numbers:** Over 1,000 connections, the random positive and negative variations cancel each other out. The Mean ($\mu$) of the IAT will mathematically converge to exactly $T_{base}$ (60 seconds).
*   **The Standard Deviation Drop:** Organic human web browsing has a massive standard deviation (ranging from 1 second to 8 hours). A jittered beacon has a mathematically hard-capped standard deviation bounded by the jitter percentage. If an IDS sees a high volume of connections where $\sigma$ is unusually small relative to $\mu$, it flags the tuple as a programmatic beacon.

## 3. Fast Fourier Transforms (FFT)
When attackers use extreme jitter (e.g., 50%) or blend their beacons with legitimate web traffic to manipulate the IAT standard deviation, defenders escalate to frequency-domain mathematics.

The **Fast Fourier Transform (FFT)** takes time-domain data (when connections happen) and converts it into frequency-domain data (the underlying periodic rhythms).
*   Imagine a choir where dozens of people are singing at different pitches. An FFT isolates each individual voice and tells you exactly what frequency they are singing.
*   In network traffic, the "choir" is all the organic web traffic, background syncs, and the hidden C2 beacon. 
*   Even if the beacon is obscured by heavy jitter and background noise, the FFT algorithm will identify the underlying periodicity. When plotted on a graph, the organic traffic forms a low, flat baseline of noise, while the C2 beacon produces a massive, undeniable geometric "spike" exactly at the beacon's base frequency (e.g., 0.016 Hz, which is exactly 1 connection per 60 seconds).

## 4. Payload Variance and The "Heartbeat"
Time isn't the only dimension analyzed. The IDS also maps the standard deviation of the **Payload Size**.

When a C2 agent checks in and has no new commands to process, it simply sends a status ping and receives an empty acknowledgment. 
*   A user browsing a website will download 1MB of images, then 5KB of text, then 50MB of video. The payload variance is massive.
*   A C2 beacon sending an encrypted JSON status block will send exactly 256 bytes out, and receive exactly 128 bytes back, over and over again.

### The Ultimate Metric: The Jitter-Payload Matrix
Advanced threat hunting doesn't rely on just one metric. It cross-references them. 
If an algorithm detects a flow tuple where:
1.  **IAT Standard Deviation** is bounded.
2.  **FFT** shows a distinct frequency spike.
3.  **Payload Size Variance** is near zero.

The system has a 99.9% statistical confidence that the flow is an automated C2 heartbeat, even if the traffic is completely encrypted via TLS.
