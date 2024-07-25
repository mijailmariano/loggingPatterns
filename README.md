### Documentation

* [Logging Documentation](https://docs.python.org/3/howto/logging.html)

* [Logging Package Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)

#### `Key Terms`

| Term       | Type       | Description |
|------------|------------|-------------|
| **Logger** | Component  | The primary component of the Python logging module. It is responsible for emitting log messages to various handlers. You instantiate a logger object with a name and call methods to emit log messages of different severity levels. |
| **Handler** | Component | Responsible for processing and emitting log messages received from a logger object. It determines how the log message is outputted. The Python logging module has a set of handlers—StreamHandler, FileHandler, SocketHandler, SMTPHandler, SysLogHandler, etc. |
| **Formatter** | Component | Determines how the log message is formatted before the handler outputs it. It takes a message and formats it into a readable form, typically adding attributes such as the logger’s name, the log message’s severity level, the time the log message was created, and the message itself. |
| **Level** | Attribute  | Defines the severity of a log message and helps you identify the severity of a problem. Logging levels include Debug, Info, Warning, Error, and Critical. When a message is logged with a particular level, all messages of the same level or higher severities are recorded. For example, if you log a message with the ERROR level, logs with the ERROR and CRITICAL levels are recorded. |
| **Filter** | Component | An optional component controls which log messages are processed or emitted by a logger. It provides finer granularity by specifying the criteria of each log. |

`Source Credit: ` [Middleware.io Blog](https://middleware.io/blog/python-logging-best-practices/)




| Level     | When It’s Used                                                                                                          |
|-----------|-------------------------------------------------------------------------------------------------------------------------|
| **DEBUG**    | Detailed information, typically of interest only when diagnosing problems.                                              |
| **INFO**     | Confirmation that things are working as expected.                                                                       |
| **WARNING**  | An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected. |
| **ERROR**    | Due to a more serious problem, the software has not been able to perform some function.                                 |
| **CRITICAL** | A serious error, indicating that the program itself may be unable to continue running.                                   |

### `Logging Map `

```mermaid
flowchart TB
    S[".info()\nLog RECORD\nmessage\nlevel\ncreated\nthread\n..."]
    subgraph Messages
        direction TB
        Y['message': 'THE ACTUAL MESSAGE']
        Z['INFO': 'THE ACTUAL MESSAGE']
    end
    A[LOGGER\nLEVEL: DEBUG/INFO/WARNING/ ...\n FILTER\n...]
    B[HANDLER\nLEVEL\nFILTER\n...\nFORMATTER]
    D[HANDLER\nLEVEL\nFILTER\n...\nFORMATTER]
    F[HANDLER\nLEVEL\nFILTER\n...\nFORMATTER]
    A --> B --> C(STDOUT)
    A --> D --> E(FILE)
    A --> F --> G(EMAIL)
    A --> Y
    A --> Z

    

