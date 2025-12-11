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
|🟥 1    |Config Manager    |🔴    |✅    |Centralized configuration management using YAML files, ensuring modules fetch settings from a single source.|
|🟥 1    |Health Check    |🔴    |✅    |Pre-startup validation of critical service availability (Redis, PostgreSQL).|
|🟥 1    |Watchdog    |🔴    |✅    |Monitoring of key background processes and automatic restart of failed modules.|
|🟥 1    |Exception Handler    |🔴    |✅    |Centralized exception capturing and structured logging to prevent core crashes.|    
|🟥 1    |Graceful Shutdown    |🔴    |✅    |Correct termination of all running asyncio tasks and closing of DB/Redis connections upon exit signal (SIGTERM/Ctrl+C).|
|🟥 1|Configuration Validation|🟠|✅|Validating the correctness of configuration parameters at system startup.|
|🟥 1|Event Logging|🔴|✅|Recording all key system actions, commands, and errors to the system log.|
|🟥 1|PostgreSQL Storage|🔴|✅|Main asynchronous database connection for long-term data storage.|
|🟥 1|Secret Manager|🟠|✅|Secure, encrypted storage and retrieval of sensitive credentials (passwords, tokens).|
|🟥 1|Event Queue (Redis Pub/Sub)|🔴|✅|Core implementation of the Event-Driven Architecture (EDA) for non-blocking task flow.|
|🟧 2|Voice I/O (Vosk/SileroTTS)|🔴|✅|Integration of Speech Recognition (ASR) and Text-to-Speech (TTS) capabilities.|
|🟧 2|Network Controller|🟠|✅|Module for checking external network availability and local IP diagnostics.|
|🟧 2|Telegram Bot|🟢|✅|External interface for sending commands and receiving notifications.|
|🟧 2|API/UI Authorization|🔴|✅|Implementation of JWT/Token-based authentication for all core interfaces.|
|🟧 2|Universal Notification System|🔴|✅|Module to standardize message sending across all channels (Telegram, Web, Voice).|
|🟧 2|Basic Web Interface|🟠|✅|Initial front-end for viewing status, logs, and basic device management.|
|🟧 2|Scheduler + DB|🟠|✅|Persistent storage and management of delayed and recurring tasks.|
|🟧 2|API Gateway|🟠|✅|Unified entry point for all system requests, routing to the core event bus.|
|🟨 3|Notification Center|🟠|✅|Unifies all system notifications into a single, real-time feed for CLI/UI (WebSockets).|
|🟨 3|Role-Based Access Control (RBAC)|🟢|✅|Dividing users into roles with different access levels to commands and data.|
|🟨 3|Device Discovery (UPnP/mDNS)|🟢|⚙️|(Current Focus) Automatic detection and registration of compatible devices using asynchronous network protocols.|
|🟨 3|Graceful Degradation|🔴|✅|Mechanism to allow the core system to continue functioning despite the failure of non-critical modules.|
|🟨 3|DB Migrations (Alembic)|🔴|✅|Safe, version-controlled changes to the PostgreSQL database schema.|
|🟨 3|Time Series Storage|🟠|✅|Collecting and storing metrics (CPU, temperature, load) for system analytics and graphs.|
|🟨 3|System Health Panel|🟢|✅|Displaying the real-time status and health metrics of all core services in the UI.|
|🟨 3|Backup/Restore|🟠|⚙️|(In Progress) Implementation of full backup and recovery procedures for the database and configurations.|
|🟨 3|Script Versioning|🟢|⚙️|(In Progress) Storing versions of user scripts, including a "dry run" mode for testing.|
|🟨 3|Script Debugging|🟢|⚙️|(In Progress) Tools for step-by-step execution, logging, and tracing of user scripts.|
|🟨 3|Help System|🟢|⚙️|(In Progress) Contextual reference system for available commands and user-created scripts.|
|🟨 3|Script Descriptions|🟢|⚙️|(In Progress) Maintaining documentation and descriptions for all automation scenarios.|
|🟩 4|Plugin System|🟠|⏳|Design and implementation of an external interface for adding modules without core modification.|
|🟩 4|Dialog Context|🟠|⏳|Advanced NLP to understand relative commands and maintain context across sequential interactions.|
|🟩 4|A/B Testing|🟢|⏳|Ability to test new versions of automation scripts on a small user group before full deployment.|
|🟩 4|Multi-user Support|🟠|⏳|Different user profiles, permissions, and personalized contexts.|
|🟩 4|Script Templates|🟢|⏳|UI-driven generation of common automation scenarios.|
|🟦 5|LLM Integration|🟠|⏳|Integration with a locally run Large Language Model for complex queries and information analysis.|
|🟦 5|Update System|🟠|⏳|Automated, near-zero-downtime update procedures for the core and modules.|
|🟦 5|Resource Optimization|🟢|⏳|Automated balancing of CPU/memory loads across workers.|
|🟦 5|ML/AI Integration|🟠|⏳|Predictive capabilities based on time-series metrics and user habit analysis.|
|🟦 5|Voice/Biometric Auth|🟢|⏳|Biometric verification (voice print) for critical security commands.|

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
