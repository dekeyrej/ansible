# Joe’s Home Lab & Embedded Projects

## 🖥️ Virtualization Infrastructure

**Primary Host:** `Sierra`  
**Platform:** Proxmox-VE  
**Specs:** Ryzen 9 9950X, 128GB DDR5-6000, RTX 2060 (12GB VRAM), PCIe Gen5 & Gen4 NVMe storage, 4 x 1TB SATA SSDs  
**Features:** JetKVM, custom fan curves, headless operation

Migrating from a legacy **Kubernetes cluster of retired hardware** to a consolidated high-performance virtualization environment.

---

## ☁️ Kubernetes & Microservices

### LED Signboard Project
Originally created to display Boston Red Sox scores—evolved into a distributed information display powered by microservices.

- **Architecture:** Multiple implementations across microservices, monoliths, and microcontrollers  
- **Languages:** Python, CircuitPython  
- **Platform:** Kubernetes (MicroK8s), Raspberry Pi + LED Matrix  
- **Data Flow:** Microservices poll external APIs → write to PostgreSQL → notify via Redis pub/sub → update LED client

Microservices:
- `aqi`: Air quality index (OpenWeatherMap)
- `weather`: Current + forecast conditions (OpenWeatherMap)
- `moon`: Astronomical events, moon phase (met.no)
- `mlb` / `nfl`: Game data (ESPN)
- `events`: Family birthdays & anniversaries via k8s ConfigMap
- `mycal`: Google Calendar data (manually scrubbed)

LED Matrix Displays:
- Clock, Wi-Fi QR code, calendar events
- Weather, AQI, moon phase
- MLB/NFL game summaries with live updates
- Uptime display (color-coded)

### Kubernetes Cluster

**Production Cluster (amd64)**  
- 3 x retired PCs  
- MicroK8s, Ceph storage, PostgreSQL, Redis, MQTT, Telegraf, InfluxDB, Grafana, Ollama

**Test Cluster (arm64)**  
- 3 x Raspberry Pi 5s (8GB RAM + NVMe)  
- Ubuntu Server 24.04, Ceph storage, MicroK8s

Supporting tools:
- `apiserver`: Node.js + PostgreSQL + Redis, serves public API  
- `webdisplay`: React SPA, displays microservice data in browser

Utility Libraries:
- `datasource`: Unified DB access for PostgreSQL, MongoDB, SQLite  
- `kubesecrets`: CRUD wrapper for K8s ConfigMaps & Secrets  
- `pages`: Core base classes for service/client logic

---

## 🔧 Microcontroller Projects

### CircuitPython

- **Servo Tester**  
  *Mid-range PWM generator (1500µs) and range testing*  
  - ESP32S2 → RP2040 via Blinka + Adafruit/u2if  
  - ✅ *Complete*

- **IR Remote for Matrix**  
  *Decodes IR commands and routes to matrix system via Redis*  
  - ESP32S3 with TSOP38238 IR receiver  
  - ✅ *Complete*

### C++ / Embedded

- **Battery System Monitor**  
  *Custom energy system display for solar-powered garage*  
  - Custom PCB, sensors, 320x240 touchscreen  
  - MQTT reporting  
  - ✅ *Initial implementation complete*

---

## 📟 Monitoring Projects

- **Freezer AC + Temperature Monitoring**  
  - Pi Zero 2 + PiSugar UPS  
  - Monitors freezer power, door status, ambient/freezer temps  
  - Reports via MQTT  
  - ✅ *Complete*

---

## 🧠 Philosophy

These projects embody a unified ecosystem for local observability, home automation, environmental awareness, and personal dashboarding. Each component is purpose-built but interconnected—built with reuse, automation, and extensibility in mind.

---

## 🚧 What's Next?

With everything consolidated under `Sierra`, future ideas include:
- VM/container orchestrated workflows
- OLED-based smart panel for system stats
- Long-term observability with Grafana Loki + Prometheus
- Possibly a self-documented DevOps homelab as a teaching reference

---

> “Sierra isn’t just a node on the network. It’s the whole mountain.”

```
DrJoesOpus/
├── README.md                        # Top-level overview and project purpose
├── orchestration/
│   ├── README.md                    # Ansible design, Proxmox & Multipass provisioning
│   ├── playbooks.md                 # Description of 00_proxmox.yaml, 04_cluster.yaml, etc.
│   └── inventory_structure.md       # Host vars, groups, cluster layout
├── infrastructure/
│   ├── certificate_authority.md
│   ├── vault.md
│   ├── cloud_init_templates.md
│   └── secrets_management.md
├── cluster_services/
│   ├── microk8s.md
│   ├── microceph.md
│   ├── redis.md
│   └── postgres_kubegres.md
├── microservices/
│   ├── architecture.md              # Microservices overview, Redis pubsub, DB schema
│   ├── aqi.md
│   ├── weather.md
│   ├── moon.md
│   ├── events.md
│   ├── calendar.md
│   ├── mlb.md
│   └── nfl.md
├── displays/
│   ├── LED_signboard.md
│   ├── matrix.md
│   └── MagicMirror2.md
├── hardware_projects/
│   ├── servo_tester.md
│   ├── IR_remote_matrix.md
│   ├── battery_monitor.md
│   └── freezer_monitor.md
├── libraries/
│   ├── datasource.md
│   ├── kubesecrets.md
│   └── pages.md
├── web/
│   ├── apiserver.md
│   └── webdisplay.md
└── future/
    ├── roadmap.md
    ├── lessons_learned.md
    └── publishing_plan.md
```
