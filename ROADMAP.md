### 🗺️ Development Roadmap — Subota 3.0 (alpha)
Subota 3.0 is being developed using a modular, multi-stage system. Phases 1 and 2 are fully complete, establishing a reliable asynchronous core with essential I/O channels. 
Development is currently focused on **Phase 3**, targeting stability, developer usability, and automation (see ⚙️ **In Progress** status).

#### Legend (Status & Priority)
| Priority | Meaning | Status | Meaning |
| --- | ---| --- | --- |
| 🔴 | Critical – Essential for system operation. | ✅ | Done – Fully implemented. |
| 🟠 | High – Important for stability and core functionality. | ⚙️ | In Progress – Currently under active development. |
| 🟢| Medium – Enhancement, can be postponed. | ⏳ | Plan – Scheduled for future iterations. |

#### Work Plan:
| Phase | Task | Priority | Status | Description|
| --- | --- | --- | --- | --- |
|🟥 1 |Config Manager    |🔴    |✅    |Centralized configuration management using YAML files, ensuring modules fetch settings from a single source.|
|🟥 1 |Health Check    |🔴    |✅    |Pre-startup validation of critical service availability (Redis, PostgreSQL).|
|🟥 1 |Watchdog    |🔴    |✅    |Monitoring of key background processes and automatic restart of failed modules.|
|🟥 1 |Exception Handler    |🔴    |✅    |Centralized exception capturing and structured logging to prevent core crashes.|    
|🟥 1 |Graceful Shutdown    |🔴    |✅    |Correct termination of all running asyncio tasks and closing of DB/Redis connections upon exit signal (SIGTERM/Ctrl+C).|
|🟥 1 |Configuration Validation|🟠|✅|Validating the correctness of configuration parameters at system startup.|
|🟥 1 |Event Logging|🔴|✅|Recording all key system actions, commands, and errors to the system log.|
|🟥 1 |PostgreSQL Storage|🔴|✅|Main asynchronous database connection for long-term data storage.|
|🟥 1 |Secret Manager|🟠|✅|Secure, encrypted storage and retrieval of sensitive credentials (passwords, tokens).|
|🟥 1 |Event Queue (Redis Pub/Sub)|🔴|✅|Core implementation of the Event-Driven Architecture (EDA) for non-blocking task flow.|
|🟧 2 |Voice I/O (Vosk/SileroTTS)|🔴|✅|Integration of Speech Recognition (ASR) and Text-to-Speech (TTS) capabilities.|
|🟧 2 |Network Controller|🟠|✅|Module for checking external network availability and local IP diagnostics.|
|🟧 2 |Telegram Bot|🟢|✅|External interface for sending commands and receiving notifications.|
|🟧 2 |API/UI Authorization|🔴|✅|Implementation of JWT/Token-based authentication for all core interfaces.|
|🟧 2 |Universal Notification System|🔴|✅|Module to standardize message sending across all channels (Telegram, Web, Voice).|
|🟧 2 |Basic Web Interface|🟠|✅|Initial front-end for viewing status, logs, and basic device management.|
|🟧 2 |Scheduler + DB|🟠|✅|Persistent storage and management of delayed and recurring tasks.|
|🟧 2 |API Gateway|🟠|✅|Unified entry point for all system requests, routing to the core event bus.|
|🟨 3 |Notification Center|🟠|✅|Unifies all system notifications into a single, real-time feed for CLI/UI (WebSockets).|
|🟨 3 |Role-Based Access Control (RBAC)|🟢|✅|Dividing users into roles with different access levels to commands and data.|
|🟨 3 |Device Discovery (UPnP/mDNS)|🟢|✅|(Current Focus) Automatic detection and registration of compatible devices using asynchronous network protocols.|
|🟨 3 |Graceful Degradation|🔴|✅|Mechanism to allow the core system to continue functioning despite the failure of non-critical modules.|
|🟨 3 |DB Migrations (Alembic)|🔴|✅|Safe, version-controlled changes to the PostgreSQL database schema.|
|🟨 3 |Time Series Storage|🟠|✅|Collecting and storing metrics (CPU, temperature, load) for system analytics and graphs.|
|🟨 3 |System Health Panel|🟢|✅|Displaying the real-time status and health metrics of all core services in the UI.|
|🟨 3 |Backup/Restore|🟠|✅| Implementation of full backup and recovery procedures for the database and configurations.|
|🟨 3 |Script Versioning|🟢|✅| Storing versions of user scripts, including a "dry run" mode for testing.|
|🟨 3 |Script Debugging|🟢|✅|Tools for step-by-step execution, logging, and tracing of user scripts.|
|🟨 3 |Help System|🟢|✅|(Contextual reference system for available commands and user-created scripts.|
|🟨 3 |Script Descriptions|🟢|✅|(Maintaining documentation and descriptions for all automation scenarios.|
|🛡️ 3.5 | Event Bus Security (Redis HMAC) | 🔴| ⚙️  | Implement digital signature (HMAC-SHA256) for all internal events. |
|🛡️ 3.5 | Secure MQTT Gateway and Android Isolation | 🔴| ⚙️ | Configure TLS, ACLs for MQTT; isolate Android nodes via Termux. |
|🛡️ 3.5 | Zero Trust on MikroTik | 🟠 | ⚙️ | Configure firewall, disable hidden SSID, dynamic device whitelist. |
|🛡️ 3.5 | Layered Authentication (TOTP) | 🟠 | ⚙️ | Implement two-factor authentication for critical commands. |
|🛡️ 3.5 | NLP/LLM Injection Protection | 🟡 | ⚙️ | External Data Sandbox, Hard Prompts, Man-in-the-Loop |
|🛡️ 3.5 | Secure Power Management | 🟡| ⚙️ | Safe Mode, Delayed Shutdown, Loop Reboot Protection. |
|🛡️ 3.5 | USB/Serial Interface Protection | 🟡 | ⚙️ | Discontinue HID, Switch to Serial with Nonce+ACK Protocol, udev rules. |
|🛡️ 3.5 | Intelligent Presence Logic | 🟢| ⚙️ | Multi-Sensor Fusion (Wi-Fi, BT, sensors), EW Protection. |
|🟩 4 | Plugin System | 🟠 | ⏳ | Architecture for external modules with isolation and versioning. |
|🟩 4 | Dialog Context | 🟠 | ⏳| Support for relative commands and action chains. |
|🟩  4 | Debugging Tools and A/B Testing | 🟢| ⏳| Advanced tracing and secure testing of new scripts. |
|🟩  4 | Script Dependency Management | 🟠| ⏳| Isolated venv environments for each script. |
|🟩  4 | Hardware Remote Control (Arduino) | 🟢| ⏳| Physical Interface with Buttons and Security Status Indicator. |
|🟩  4 | Script Templates and Editor | 🟢| ⏳| Generate Standard Scripts via UI with Monaco Editor. |
|🟩  4 | Advanced Device Manager UI | 🟠| ⏳| Control Center for All Devices with Automatic Classification. |
|🟩  4 | Voice Messages in Telegram | 🟢| ⏳| Sending and receiving audio messages via a bot. |
|🟦  5 | LLM Integration (Local) | 🟠| ⏳| Answering complex queries and analyzing using local models. |
|🟦  5 | Update System | 🟠| ⏳| Non-stop kernel and module updates with rollback. |
|🟦  5 | Local API Cache | 🟢| ⏳| Caching external service responses for offline operation. |
|🟦  5 | Sentiment and Emotion Analysis | 🟢| ⏳ Plan | Detecting user sentiment from voice and text. |
|🟦  5 | Pattern Learning | 🟢| ⏳| User habit analysis and automation of routine actions. |
|🟦  5 | Load Forecasting | 🟢| ⏳| CPU/RAM load peak prediction for proactive scaling. |
|🟦  5 | Vector Memory (Semantic Search) | 🟠| ⏳| Storage and retrieval of information by meaning (pgvector or separate DB). |
|🟦  5 | Full Duplex Voice Interaction | 🟢| ⏳| Interrupt mode, continuous dialogue without obvious pauses. |
|🟪  6 | Native Mobile Apps | 🟠| ⏳| Android/iOS clients: Station (Vosk) and Remote (control) modes. |
|🟪  6 | Global notification synchronization | 🟢| ⏳| Synchronize "read" status between all devices. |
|🟪  6 | Vision Language Models (VLM) | 🟡| ⏳| Video stream analysis: recognize people, objects, and situations. |
|🟪  6 | UPS integration | 🟢| ⏳| Automatic graceful shutdown during power outage. |
|🟪  6 | Zigbee/Z-Wave mesh network | 🟡| ⏳| Support for energy-efficient smart home protocols via gateways. | 
|🟪  6 | Initial Setup Wizard | 🟢| ⏳| Step-by-step wizard for new user deployment. |

## 🚀 Strategic Development — Post-3.0 Focus

These tasks represent a long-term development plan aimed at improving **robustness**, **deployment automation**, and **mobile ecosystem** integration, turning Subota 3.0 into a full-fledged product.

### 🛡️ Infrastructure and DevOps

* **Self-Healing Infrastructure (Docker):** Implementation of scripts for auto-restart and health monitoring of Docker containers (e.g., Redis, PostgreSQL) via Docker Compose/Kubernetes mechanisms, ensuring self-healing of the system in case of service failures.
* **First-Run Provisioning Script:** Create a first-run script to automate dependency installation, initial configuration, password generation, and account creation when deploying to a new system.

### 📱 Mobile Ecosystem: Subota Companion App

Native Android app development (**Kotlin, MVVM, Jetpack**) to create an integrated mobile ecosystem.

| Component | Key Purpose | What is it intended to be used for |
| :--- | :--- | :--- |
| **Station Mode** | Turn your old phone into a stationary smart speaker. | **Mobile Development, Foreground Services, WebSocket Audio Streaming** (Vosk-API for Android). |
| **Remote Control Mode** | Personal remote control and secure authenticator. | **JWT authentication, Android Keystore, BiometricPrompt API** (fingerprint/face). |
| **Автоматическое Обнаружение** | **Zero-Configuration** подключение к серверу Subota в локальной сети. | Использование **mDNS/UDP Broadcast** для избавления пользователя от ручного ввода IP-адреса. |
| **Two-Factor Verification** | **Implementation of critical commands** (for example, "arm the house") through confirmation with a **fingerprint** on the user's personal phone, using **WebSocket push** and **RBAC Manager** servers. | Security architecture, critical event handling, asynchronous communication. |
