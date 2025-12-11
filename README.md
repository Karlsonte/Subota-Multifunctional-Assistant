# ⚙️ Subota: Multifunctional Local Assistant and Automation Platform

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


#### 🔍 Current Work: Automating Device Discovery (DiscoveryManager)

Currently, the **DiscoveryManager** module is being actively developed, which will transform Subota 3.0 from a "manual" system into a **self-configuring platform**.

* **Purpose:** Automatic search, classification and registration of compatible devices in the local network (IoT hubs, smart TVs, printers, etc.).
   * **Implementation:** An advanced asynchronous network stack is used to work with the **SSDP (UPnP)** and **mDNS (ZeroConf)** protocols.
    * **Passive Mode (Listener):** Continuously listens asynchronously for broadcast announcements (`NOTIFY` in SSDP) to instantly react to the appearance of new devices.
    * **Active Mode (Search):** Regular search for devices (`M-SEARCH`) linked to a specific network interface.
* **Integration:** The discovered device is retrieved, its XML description (for UPnP) is parsed to obtain the name/model, and then the information is published to the **Redis Event Bus** (`device_discovered`) for further processing and storage in **PostgreSQL**.

#### 🌐 Asynchronous Device Discovery: DiscoveryManager
[**DiscoveryManager**](/showcase_code/v3_0/discovery_manager_snippet.py)

##### [Raod map](./ROADMAP.md)
