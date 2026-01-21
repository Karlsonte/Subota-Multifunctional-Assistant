# ⚙️ Subota: Multifunctional Local Assistant and Automation Platform [Alpha Version]
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)
![Asyncio](https://img.shields.io/badge/Core-Asyncio-4D88FE?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Event%20Bus-Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Status](https://img.shields.io/badge/Status-Alpha%20%2F%20In%20Dev-orange?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-40%2B%20Pytest-green?style=flat-square)
![License](https://img.shields.io/github/license/Karlsonte/Subota-Multifunctional-Assistant?style=flat-square)

### 🚀 Introduction and Motivation

The Subota project is inspired by the idea of ​​creating a **maximally autonomous, locally controlled assistant** that serves not only as a voice interface but also as a centralized platform for automation and security.

**The idea is based on the concept of "Servitor"**: a highly specialized, reliable and fully controllable system capable of performing a wide range of tasks - from simple information ("What time is it?") to multi-level monitoring and home security (Computer Vision, Smart Home, Scripts).

### 🎯 Key Goal of the Project

#### "Jarvis... Sometimes you gotta run, before you can walk" - Tony Stark (Iron Man 2008)

Create a **private, extensible, and fault-tolerant ecosystem** where all data processing and management logic is executed **strictly locally**.

The main emphasis is on:

1.  **Data Sovereignty:** The user retains full control over data and functionality.
2.  **Modular Architecture:** Ensuring easy addition of new features and system resilience to failures.
3.  **Multi-Channel Interaction:** Support for voice control, Telegram, Web/REST API.

## 💾 2. Historical Context and Iterations (Subota 1.0 & 2.0)

The Subota project went through two prototype iterations, which became a critical foundation for the design of the current asynchronous platform (3.0). These prototypes demonstrated both the potential of the idea and the architectural limitations of a synchronous, monolithic approach.

<p><br></p>

### Subota 1.0 (Jarvis_1.0) — NLP and System Integration

**Technologies:** Python (Synchronous), Vosk, Scikit-learn (Logistic Regression/Count Vectorizer), pyttsx3, psutil.

**Key Achievements and Demonstrated Skills:**

* **Custom NLP/NLU (Natural Language):** Implemented a custom query processing script based on **Logistic Regression** and **Count Vectorizer** to classify intents by key phrases (`data_set`).
* **Voice Computing (Critical Module):** Developed the `numbers_text_to_int` (NL to Math) module, which allowed for complex mathematical calculations to be performed on **Vosk** (as text), including handling of **fractional numbers** and **operator precedence** (e.g. $2+3\cdot4$).
* **Low-Level OS Integration:** Implemented volume control (`pycaw`), system monitoring (`psutil`) and OS command execution (`subprocess`), which provided basic functionality for "smart" PC management.
* **Speech Processing:** Used **Vosk** for speech recognition and **pyttsx3/SileroTTS** (in later versions) for synthesis.

#### 💡 **Main Lesson 1.0:**

The synchronous architecture and reliance on a phrase-based classifier **prevented the system from scaling easily** (adding new features) and led to blocking while waiting for I/O operations (for example, when accessing external APIs or starting long-running processes). This became the direct trigger for the transition to the asynchronous and modular design of 3.0.

#### 🖼️ **Code Demo**
* [numbers_text_to_int.py](./showcase_code/v1_0/numbers_text_to_int.py)

<p><br></p>

### Subota 2.0 – Computer Vision, LLM and a Modular Approach

<figure align="center">
    <img src="./subota_v2.0.png" alt="Subota 2.0 Graph" width="700" />
 <figcaption style="text-align: center; font-size: 0.9em; color: #555;">
     Made with <a href="http://www.gitvizz.com" target="_blank">GitWizz</a>
 </figcaption>
    <p><br></p>
</figure>

**Main Idea:** Recognizing the need for a **flexible, non-rigidly programmed system** with controlled freedom of action. The project became a step towards creating a **"smart" assistant** and moving from a monolith to a plug-in architecture.

**Technologies:** Python, **Computer Vision (OpenCV, YOLOv8, cv2)**, **LLM Integration (llama_cpp)**, **Multithreading (threading)**, SileroTTS, Vosk.

**Key Achievements and Demonstrated Skills:**

* **Computer Vision (CV):** Successfully implemented the `protocol_watch_dog.py` security protocol, which uses **YOLOv8** to detect motion, people, and potentially dangerous situations.
    * **Example:** Implemented real-time object detection, event binding to the camera and sending notifications.
* **Модульная Архитектура (Плагины):** Проект был разделен на модули с использованием классов **Plugin** и **EventHandler**, что продемонстрировало переход к **слабосвязанному дизайну** (даже в рамках синхронного ядра).
* **Notification and Integration System:** A multi-channel notification system has been implemented (Telegram: text only, Email: photo with timestamp) when a CV event is detected.
* **First Experience with LLM:** Connecting the local **LLaMA** model via `llama_cpp` for a more "fluent" response to complex queries (despite the speed limitations due to the lack of a GPU, experience with LLM has been gained).
* **Custom NLP classifier:** A custom model for user intent recognition has been trained but not implemented.

#### 💡 **Main Lesson 2.0:**

The introduction of CV and LLM dramatically increased the requirements for **parallel data processing**. Using standard `threading` and a synchronous core to simultaneously run LLM, CV, and voice control threads led to performance and resource management issues. It became clear that high-load and I/O-dependent tasks required **a complete transition to an asynchronous model (`asyncio`)** and an event-driven core.

#### 🖼️ **Code Demo**
* [plugin.py](./showcase_code/v2_0/plugin.py)
* [protocol_watch_dog.py](./showcase_code/v2_0/protocol_watch_dog.py)

<p><br></p>

### Subota 3.0 (alpha) — Asynchronous Event-based Core and Digital Butler

<figure align="center">
    <img src="./subota_3.0.png" alt="Subota 2.0 Graph" width="700" />
 <figcaption style="text-align: center; font-size: 0.9em; color: #555;">
     Made with <a href="http://www.gitvizz.com" target="_blank">GitWizz</a>
 </figcaption>
    <p><br></p>
</figure>

**Key Idea:** Create a fully **asynchronous, modular, and fault-tolerant** core for performing digital butler tasks, monitoring, and managing devices in real time. Addressing the scalability and reliability issues inherent in versions 1.0 and 2.0.

**Architecture:** Fully **asynchronous (asyncio)**, **event-driven** architecture (EDA) using **Redis Event Bus** as the central message bus. The system utilizes a microservices approach (FastAPI, Uvicorn) and containerization (Docker: Redis, PostgreSQL).

**Technologies (Key Aspects):**

* **Asynchronous Stack:** Python **asyncio**, **FastAPI** (API Gateway, WebSockets), **Uvicorn**, **aioredis**, **asyncpg**.
* **Condition and Storage:** **PostgreSQL** (long memory), **Redis** (ContextManager, EventBus), **Alembic** (database migrations).
* **Reliability/DevOps:** **TaskWatcher** (process monitoring), **HealthChecker**, **Graceful Shutdown**, **MetricsCollector** (collecting CPU, RAM, Latency), **Docker** (containerization of services), **Backup/Restore** scripts.
* **Interaction:** **Voice Input/Output** (Vosk/SileroTTS), **Telegram Bot**, **WebUI** (Bootstrap/FontAwesome), **API Gateway** (JWT Auth).
* **Safety:** **AuthManager** (JWT), **RBACManager** (access rights), **SecretManager**.
* **Code Quality:** Full-fledged **Unit and Integration Testing (Pytest)** — 200+ tests.

#### 🎯 Key Professional Achievements in 3.0:

1.  **Building a Fault-Tolerant Engine (EDA):** Implementation of Redis Event Bus, which isolates failures in handlers and provides **reliable data transfer** between modules (IntentProcessor, ScriptRunner, Senders).
2.  **Full Monitoring and Management System:** Implementation of **TaskWatcher** and **MetricsCollector**, which collect real-time process load and status data and store it in PostgreSQL. This forms the basis for the Health Dashboard.
3.  **Unified Command and Notification Interface:** Unifies all input/output channels (Voice, CLI, Telegram, WebUI) via **SessionManager** and **NotificationManager**. The Assistant responds to the source of the command.
5.  **Comprehensive Security:** Implementation of **RBACManager** and **AuthManager** (JWT, permissions) to control access to API and UI functions, which is key for a home management project.
6.  **Testability:** Building a comprehensive testing framework using `pytest-asyncio` to test critical components (Authentication, EventBus, Scheduler).

### 🖼️ **Code Demo**
[**RBAC Manager**](./showcase_code/v3_0/rbac_manager.py)

##### 🌐 Asynchronous Device Discovery: DiscoveryManager
[**DiscoveryManager**](/showcase_code/v3_0/discovery_manager_snippet.py)

#### 🔍 Current Work: 🛡️ Stage 3.5 — Security Hardening ⚡
The current development phase is fundamentally strengthening the system according to Zero Trust principles.

With the basic functionality complete, it's time to transform Subota from a "smart assistant" into a "secure fortress." This phase is dedicated to systematically eliminating vulnerabilities identified during the security audit and implementing multi-layered protection.

##### 🎯 Key goals of this phase:
- Access control: Every device and user must prove their right to perform every action.
- Data integrity: No event in the system can be tampered with or intercepted.
- Risk isolation: A hack of one component should not compromise the entire system.
- Fault tolerance: The system must fail safely and protect data in the event of any failure.

##### 🔐 Key Focus Areas:
###### 🔴 Critical Priority — Security Foundation:
- Trusted Event Bus: Implementing HMAC signatures for all messages in Redis. Any event without a valid digital signature is ignored by the kernel.
- Secure Network Perimeter: Configuring Zero Trust on MikroTik — new devices on the network are automatically quarantined until manually approved.
- Secure Data Gateway: MQTT broker with TLS, strict ACLs, and a validator bridge that verifies and signs data from IoT devices before transmitting it to the kernel.

###### 🟠 High Priority — Interface Security:
- Depth-based Authentication: Implementing two-factor authentication (TOTP/Google Authenticator) for critical commands in Telegram and voice control.
- NLP/LLM injection protection: Sandboxing for external data processing, strict system prompts, and mandatory "man-in-the-loop" confirmation for commands generated from parsing.
- Hardware security: Transition from vulnerable HID emulation to a secure serial protocol with nonce and handshake for all DIY devices (Arduino, ESP).

###### 🟡 Medium priority — Intelligent protection:
- Smart presence logic: Multi-Sensor Fusion — the system determines whether the owner is home based on a combination of indicators (Wi-Fi, Bluetooth, motion sensors), rather than a single indicator.
- Anti-EW filter: Protects geolocation scenarios from GPS spoofing and electronic jamming.
- Fail-safe states: Clearly defined system behavior scenarios in the event of loss of connection to sensors, the internet, or a critical server battery drain.

###### 🟢 Low Priority — Technical Debt:
- Docker Hardening: Isolate containers on separate networks, run as unprivileged users, limit resources.
- Secret Management Refactoring: Move the master key from configuration files to hardware storage (SD card with a physical lock switch).

#### [Raod map](./ROADMAP.md)
#### [Architecture overview](./architecture_overview.md)
