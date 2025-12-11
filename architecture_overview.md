Architecture Overview:

The system is built using a multi-layered, component-based architecture, with each layer responsible for its own functionality:

1. Input Layer: Responsible for receiving information from external sources.
2. Core Processing Layer: The central component where logic, state management, and orchestration of the entire process occurs.
3. Execution Layer: Implements specific tasks and actions initiated by the system.
4. Data Layer: Provides storage, persistence, and data management.
5. Output Layer: Responsible for delivering results and feedback to users or other systems.

---

Detailed Component Structure and Workflow:

1. Input Layer:
  * User Interfaces:
    * CLI (`inputs/comand_line_input.py`, `senders/cli_sender.py`): Interaction via the command line.
    * Telegram Bot (`bots/telegram_bot.py`, `inputs/telegram_input.py`, `senders/telegram_sender.py`): Integration with Telegram for receiving and sending messages.
    * Web UI (`web/`, `senders/web_ui_sender.py`): Browser interface for interaction.
  * Device Adapters (`adapters/device/`):
    * Interface for interacting with virtual (and potentially physical) devices (e.g., virtual_light.py, virtual_thermostat.py).
  * Event Schedulers (`core/scheduler.py`, `core/backup_scheduler.py`):
    * Run scheduled tasks.

2. Core Processing Layer:
  * Intent and NLP Processing:
    * core/nlp_processor.py, core/intent_processor.py, core/simple_intent_mapper.py: Analyze user text or voice to determine intents and extract parameters.
    * core/voice_controller.py, core/vosk_recognizer.py, core/silero_tts_controller.py: Manage speech recognition (STT) and text-to-speech (TTS).
  * Orchestration and Management:
    * core/action_dispatcher.py: Distribute incoming intents and commands to the appropriate modules.
    * core/device_manager.py: Manage device state and actions.
    * core/auth_manager.py, core/rbac_manager.py: User authentication and role management.
    * core/state_manager.py: Maintaining global system state.
    * core/context_manager.py: Dialog context management.
    * core/config_manager.py: Loading and managing configuration (config/system_config.yaml).
    * core/secret_manager.py: Securely storing and managing secrets.
    * core/notification_manager.py: Managing the notification system.
  * Communication:
    * core/redis_event_bus.py: Using Redis for asynchronous message passing between components.

3. Execution Layer:
  * Scripts (`scripts/`):
    * A set of specialized scripts for performing specific tasks:
      * alarm_handler/v1.py (Handling alarms)
      * internet_check/v1.py (Checking internet connection)
      * weather_script/v1.py (Getting weather information)
      * task_scheduler/v1.py (Managing scheduled tasks)
      * And others (e.g., help_script, logger_script).
  * Device Actions:
    * Commands sent via core/device_manager.py to adapters/device/.

4. Data Layer:
  * Databases:
    * core/data_bases/postgres_manager.py / core/data_bases/database.py: The main relational data store (e.g., user data, device status, history).
    * core/data_bases/redis_manager.py: Using Redis for caching, session management, or temporary storage.
  * Database Schema Migrations (`alembic/`):
    * Managing database structure changes.
  * Backups (`backups/`, `backup.sh`, `restore.sh`):
    * Mechanisms for creating and restoring data backups.

5. Output Layer:
  * Response Delivery (`senders/`):
    * cli_sender.py: Generating and sending text responses to the console.
    * telegram_sender.py: Sending messages to Telegram users.
    * voice_sender.py: Generating voice responses (TTS).
    * web_ui_sender.py: Sending updates to the web interface.
  * Notifications (`core/notification_manager.py`):
    * Sending system notifications.

  ---

Workflow Example:

Suppose a user asks the question "What's the weather like today?" via Telegram:

1. Input: The message "What's the weather like today?" is received from the user in Telegram.
2. Input Layer: bots/telegram_bot.py receives the message, inputs/telegram_input.py processes it.
3. Main Processing (NLP/Intent): The message is passed to core/nlp_processor.py and core/intent_processor.py to identify the intent as get_weather.
4. Main Processing (Dispatching): core/action_dispatcher.py receives the get_weather intent.
5. Execution Layer: core/acti
---

[![Схема рабочего процесса](https://mermaid.ink/img/pako:eNqtGNtu2zb0VwgN2JNjR3Yc28JQIIm7NkDSBnXTAlsGgZJoW7BuI6kkblGg64C97IruaX3Zy943FBuwvXS_4PxCf2D7hB2SEnWx3AZdHSAmD8-N504_NtzYI4ZlbG1tnUVuHE39mXUWIRTgZZxyC5FgIbbwJcEIRYB_EmCXhCTiE04xJ7OlhSaHxydHN88iyWcaxBfuHFOO7u8DFUudGcXJHJ0e2rdonCafnhmHEScUu9yPIwSoUUQCdmZ8pmSIz8HRIaDB_48cesOPkpSzjhuHOPLswI-ILUHtZCmOGYk8QuE88G21hoMKt_skIKBDCCzzJdqPuSB2YuDMM6ANu4xpJlOf5AIrfB8S51ToCd9wO0F2QZxOWSfY2-m6WrAtW2ZvrC2z-mH1--q31d9Xz1Z_XD29-hpdfXn1xdWzq6erV6u_xGr1sqLCnocTsCUDUpwtOx45910i9Tj3KU9xAEabzYX6LZRD-JzQMGYc841qTQ5ua73A6eAlWvXSxJ0TLw0IBQQ3pqTDckDdUvvYXaTJGr4jwXYDWU0VWNwSix5Q_vvzd7-iQ-EPdISXhGpBnk-JiikZeNlHeuiUEYpk1E0heKu3yOOyZNRxHaJN0aDbnaMTbSZYIwhS5IOoiKOExiCN-dGsIhGwcgtEQWJnWPGa1Q4llxxV8dyMDUmo_eCHSSCyRFKEOEneYNsHMUSLvoHcSf2lqSoS5NkBp0Eu51ySQuHgNA4a3P4gZosCly1scFA8i_xH66gTH-jj4gJiZ3POGrnXbnCXQgAxUY3A-fomFaj0CtQPPJOlqyJ67LMEc0DWcalKk-3pg7q2Y5lixzNNoXLOVhLW0PdSPi8hY9huQr23v3eQ41HIj014E8jcsgIikzfKPwAbkkteQncV5A0E0Auq-AAooYvqooAdtmSchLbatZc4DKqaEpeSsmwmAZtE34m5P12W0CMB8F3l3DWiWigcxGHIdAiIXRpltMhJq4l_8xwiYT9l2twEHG4TAbUBN7vkPQFFJ6nTmaTOm6vTEDi9fvHTP39-D3pQgk50-l-rUulCUsu4OrAh3Mue0wZoKuku9RNeGEjtUeA7FNNagClUQGJq1amGdICpaKhYfNvQwz3I0M652VTDaEREFfOzpQ3qu4sG3IcEc5WFF2plK9ENqPcxWwjdOHwX_aMB8TYJxEXn8JVzq5wfxbOZFBnIRQ2nZj6V9nvSdYURsz268PkcqULAGqpFhpaFJRiModdfPUf1tv3mEDNN2QFfPEU3L4mbyhi6TmxVHL9Bs41RM97Xdx1jjh3Mahc8gUFiRonOJA-wbInWSbKjWuk4xj4I4DEFWLX-iXQb7zdwUulZZXOAwfWytjORaHCJZvMd-zOVLoXXClAtrkno-K6MbLmSc1R-bSRCLcTrnaQmT807WpbaNkxEwmJqCGJSjlq32byFwGZgHgLrt0REX0bE81dIKHmtYMj9WUDq9qnrubmgqEFX3_QeSYIlysbf-kivkEVFufbIvkaiJ_JmOlkw14jUnNJMIYf4NYrrDe53Sq2psEEZilRzXO9wOdU7dTnt-6H0_Y-_oLspv-5AXHHZBq02-ltLHknJ33wLdUhUdRyA0-l66YPTvRMxgWs02IpIz2p9C0XkgrUQ4W67MQAUtX62wbZsEoU_4SQRddFsq3eBhUKoBmBBIWj1UvMCSrS1dUPidwvSLpB226j-NATbEf-cMIQhFz9PIR3L9L2CXjxKem3RvqH6wy1DeKEy9YgU87ew_wy6XtbTykx2CiY7wGSnXZpF4RGeRqLRq3dlYz_UjPoFI1EO-nCbuShWsrtn2ktGop6iKY1DKJqIlHxS5rZbcNsFbrtt9HFMQ8w5TDKCCagiylMCgULKdIOCbgB0g7aMNTH-YI2vXqUYNeax5iTieqgukYqnW-EL5RnFC54pZd8q6er_6aHklY94Cpjv5FFhaXVYsrzUQjVM9GG1R-o9DKjZbTNEKU5GO-DkDTFjXeEgEPNnuzrPsZXg9fTU7651BJAlHlnwpR5QmU4VFEF0eqhOoArLPQSrAuior0BlUayCRHgLgHqUKphaN5szt1LDfbPnkDwR751MtfzN0chPvyLkqcbNdMvfDE0WzGpKBWpZViwrpiqYUalWwVGeFxm8VIoqh-rYDTBjpbqos6rkQIkzJlMkf0aSMtHUDwLrA3dEdjzSgmk-XhDrAxP3pwOcbbcufI_PrW5yWeMiGkaZybTrjciuZjLEXbLbfRsTks-PFU7Tadd1NSdnMOpvO2_jJGpKmYnXJ0NvRzPp4yHuv_VOJXdkbLY90-niwjROd7e3rkvLjYOYSs3hs3bHkisytl1H_BVXnIq_d2P7vxUN_Ggx4cuAoG2Uk2Ncs5UJtBnAw2yOKcVLq9-SsqM4InVW5vtj1X1_rHrvzspoGTPqe4bFaUpaRggdFout8VgIgTcgjOTQhyxYepguzoyz6AnQJDj6JI7DnAxCYDY3rCkOGOzSBKKWjH0sElujyBJxEKcRN6yd4VDyMKzHxqVhmf2d9k6v2xv1Rn1zsNs14XRpWMNee9Az-93BcDg0h6Y5fNIyHkmpZrs3GG2Ptvvm9mA4Mnu9lgEPGBjpj9Vv7vKn9yf_AU9n_PY?type=png)](https://mermaid.live/edit#pako:eNqtGNtu2zb0VwgN2JNjR3Yc28JQIIm7NkDSBnXTAlsGgZJoW7BuI6kkblGg64C97IruaX3Zy943FBuwvXS_4PxCf2D7hB2SEnWx3AZdHSAmD8-N504_NtzYI4ZlbG1tnUVuHE39mXUWIRTgZZxyC5FgIbbwJcEIRYB_EmCXhCTiE04xJ7OlhSaHxydHN88iyWcaxBfuHFOO7u8DFUudGcXJHJ0e2rdonCafnhmHEScUu9yPIwSoUUQCdmZ8pmSIz8HRIaDB_48cesOPkpSzjhuHOPLswI-ILUHtZCmOGYk8QuE88G21hoMKt_skIKBDCCzzJdqPuSB2YuDMM6ANu4xpJlOf5AIrfB8S51ToCd9wO0F2QZxOWSfY2-m6WrAtW2ZvrC2z-mH1--q31d9Xz1Z_XD29-hpdfXn1xdWzq6erV6u_xGr1sqLCnocTsCUDUpwtOx45910i9Tj3KU9xAEabzYX6LZRD-JzQMGYc841qTQ5ua73A6eAlWvXSxJ0TLw0IBQQ3pqTDckDdUvvYXaTJGr4jwXYDWU0VWNwSix5Q_vvzd7-iQ-EPdISXhGpBnk-JiikZeNlHeuiUEYpk1E0heKu3yOOyZNRxHaJN0aDbnaMTbSZYIwhS5IOoiKOExiCN-dGsIhGwcgtEQWJnWPGa1Q4llxxV8dyMDUmo_eCHSSCyRFKEOEneYNsHMUSLvoHcSf2lqSoS5NkBp0Eu51ySQuHgNA4a3P4gZosCly1scFA8i_xH66gTH-jj4gJiZ3POGrnXbnCXQgAxUY3A-fomFaj0CtQPPJOlqyJ67LMEc0DWcalKk-3pg7q2Y5lixzNNoXLOVhLW0PdSPi8hY9huQr23v3eQ41HIj014E8jcsgIikzfKPwAbkkteQncV5A0E0Auq-AAooYvqooAdtmSchLbatZc4DKqaEpeSsmwmAZtE34m5P12W0CMB8F3l3DWiWigcxGHIdAiIXRpltMhJq4l_8xwiYT9l2twEHG4TAbUBN7vkPQFFJ6nTmaTOm6vTEDi9fvHTP39-D3pQgk50-l-rUulCUsu4OrAh3Mue0wZoKuku9RNeGEjtUeA7FNNagClUQGJq1amGdICpaKhYfNvQwz3I0M652VTDaEREFfOzpQ3qu4sG3IcEc5WFF2plK9ENqPcxWwjdOHwX_aMB8TYJxEXn8JVzq5wfxbOZFBnIRQ2nZj6V9nvSdYURsz268PkcqULAGqpFhpaFJRiModdfPUf1tv3mEDNN2QFfPEU3L4mbyhi6TmxVHL9Bs41RM97Xdx1jjh3Mahc8gUFiRonOJA-wbInWSbKjWuk4xj4I4DEFWLX-iXQb7zdwUulZZXOAwfWytjORaHCJZvMd-zOVLoXXClAtrkno-K6MbLmSc1R-bSRCLcTrnaQmT807WpbaNkxEwmJqCGJSjlq32byFwGZgHgLrt0REX0bE81dIKHmtYMj9WUDq9qnrubmgqEFX3_QeSYIlysbf-kivkEVFufbIvkaiJ_JmOlkw14jUnNJMIYf4NYrrDe53Sq2psEEZilRzXO9wOdU7dTnt-6H0_Y-_oLspv-5AXHHZBq02-ltLHknJ33wLdUhUdRyA0-l66YPTvRMxgWs02IpIz2p9C0XkgrUQ4W67MQAUtX62wbZsEoU_4SQRddFsq3eBhUKoBmBBIWj1UvMCSrS1dUPidwvSLpB226j-NATbEf-cMIQhFz9PIR3L9L2CXjxKem3RvqH6wy1DeKEy9YgU87ew_wy6XtbTykx2CiY7wGSnXZpF4RGeRqLRq3dlYz_UjPoFI1EO-nCbuShWsrtn2ktGop6iKY1DKJqIlHxS5rZbcNsFbrtt9HFMQ8w5TDKCCagiylMCgULKdIOCbgB0g7aMNTH-YI2vXqUYNeax5iTieqgukYqnW-EL5RnFC54pZd8q6er_6aHklY94Cpjv5FFhaXVYsrzUQjVM9GG1R-o9DKjZbTNEKU5GO-DkDTFjXeEgEPNnuzrPsZXg9fTU7651BJAlHlnwpR5QmU4VFEF0eqhOoArLPQSrAuior0BlUayCRHgLgHqUKphaN5szt1LDfbPnkDwR751MtfzN0chPvyLkqcbNdMvfDE0WzGpKBWpZViwrpiqYUalWwVGeFxm8VIoqh-rYDTBjpbqos6rkQIkzJlMkf0aSMtHUDwLrA3dEdjzSgmk-XhDrAxP3pwOcbbcufI_PrW5yWeMiGkaZybTrjciuZjLEXbLbfRsTks-PFU7Tadd1NSdnMOpvO2_jJGpKmYnXJ0NvRzPp4yHuv_VOJXdkbLY90-niwjROd7e3rkvLjYOYSs3hs3bHkisytl1H_BVXnIq_d2P7vxUN_Ggx4cuAoG2Uk2Ncs5UJtBnAw2yOKcVLq9-SsqM4InVW5vtj1X1_rHrvzspoGTPqe4bFaUpaRggdFout8VgIgTcgjOTQhyxYepguzoyz6AnQJDj6JI7DnAxCYDY3rCkOGOzSBKKWjH0sElujyBJxEKcRN6yd4VDyMKzHxqVhmf2d9k6v2xv1Rn1zsNs14XRpWMNee9Az-93BcDg0h6Y5fNIyHkmpZrs3GG2Ptvvm9mA4Mnu9lgEPGBjpj9Vv7vKn9yf_AU9n_PY)
