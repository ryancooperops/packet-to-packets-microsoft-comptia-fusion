# Microsoft + CompTIA Fusion Lab

A technical, portfolio-oriented repository that maps CompTIA foundations to Microsoft security,
endpoint, networking, cloud, data/AI, and Dynamics 365 concepts.

> **Purpose:** demonstrate practical integration patterns, not reproduce exam questions or dumps.
> Certification status and exam objectives should always be verified against the official vendor
> documentation before making study or career decisions.

## Tracks

- **Security:** SY0-701 → CAS-005 → SC-900 → SC-401 → MS-102
- **Endpoint & Support:** 220-1201 → 220-1202 → MD-102
- **Networking & Infrastructure:** N10-009 → XK0-006 → MS-700
- **Project / Delivery:** PK0-005 → Microsoft solution delivery concepts
- **Security Analytics:** CS0-003 → SC-401
- **Data & AI:** DY0-001 → AB-250
- **Business Applications:** MB-230 / MB-240 / MB-310 / MB-330 / MB-500 / MB-800

## Repository map

See `docs/ARCHITECTURE.md` for the learning architecture and `docs/EXAM-MAP.md` for the
source links supplied for this repository.

## Technical components

- Python reference implementations for risk scoring, endpoint posture, network segmentation,
  incident prioritization, and AI/data pipeline validation.
- JSON fixtures for repeatable scenarios.
- Unit tests with `pytest`.
- GitHub Actions workflow for automated tests.
- Markdown documentation connecting certification domains to hands-on engineering concepts.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Disclaimer

This is an independent study and engineering portfolio. It is not affiliated with or endorsed
by CompTIA or Microsoft. No real exam questions, dumps, or confidential materials are included.

---

### My Core Learning Tactics:
* **CLI Over Memorization**: Don't just memorize what `traceroute` or `netstat` does—run them on your terminal, break your home local network on purpose, and analyze the output!
* **Think Like a Defender**: For Security+, understanding *how* a threat actor carries out a Credential Stuffing or ARP Poisoning attack makes configuring the defensive control (MFA, Dynamic ARP Inspection) logical and intuitive.
* **Master the Trifecta Synergies**: A+ gives you hardware/OS foundations, Network+ teaches how packets move, and Security+ teaches how to lock those packets down. They build on top of each other seamlessly.

---

## 🎯 Key Technical Domains & Practical Breakdowns

### 1. Network Infrastructure & Troubleshooting (Network+ Focus)
* **OSI Model Layer Isolation**: Pinpointing connectivity issues layer-by-layer (Physical cable checks -> IP routing issues -> Firewall port blocking).
* **Essential Networking Toolkit**:
  * `ping` / `traceroute`: Testing ICMP reachability and hop latency.
  * `nslookup` / `dig`: Querying DNS record types (A, AAAA, CNAME, MX, TXT).
  * `ipconfig` / `ifconfig` / `ip addr`: Checking interface bindings and subnet masks.

### 2. Cybersecurity Controls & Threat Vectors (Security+ Focus)
* **Identity & Access Management (IAM)**: Implementing Zero Trust architecture, Multi-Factor Authentication (MFA), and Least Privilege enforcement.
* **Cryptographic Frameworks**: Public Key Infrastructure (PKI), Symmetric vs. Asymmetric encryption, and TLS 1.3 handshake dynamics.
* **Incident Response & Forensics**: Log aggregation using SIEM tools, memory capture preservation, and chain of custody tracking.

### 3. Systems Hardware & OS Management (A+ Focus)
* **Storage Technologies**: RAID array configurations (RAID 0, 1, 5, 10) balancing performance against fault tolerance.
* **Virtualization & Cloud Fundamentals**: Hypervisor Type 1 (bare-metal) vs. Type 2 (hosted) resource allocation.

---

## 📁 Repository Structure

* `README.md` - Overall hands-on study framework and homelab notes.
* `Security-Plus-SY0-701-Notes.md` - (In Progress) Domain-by-domain breakdown, threat vector analysis, and PBQ practice tips.
* `Network-Plus-N10-008-Notes.md` - (In Progress) Subnetting cheat sheets, routing protocols, and command-line diagnostics.

---

## ⏱️ My Learning & Lab Roadmap

- [x] Set up a VirtualBox sandbox with Kali Linux and Ubuntu Server
- [x] Practice packet inspection using Wireshark display filters (`ip.addr == ...`, `tcp.flags.syn == 1`)
- [ ] Complete 50+ Performance-Based Questions (PBQs) for Security+
- [ ] Document custom firewall rulesets using `iptables` and Windows Defender Firewall

*Thanks for swinging by! Feel free to star ⭐️ this repo if you're also grinding through CompTIA exams or building your IT skills.*
