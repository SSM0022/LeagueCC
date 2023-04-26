# LeagueCC
Video Demo: [Youtube](https://youtu.be/wqEeGAJKwHM)

This is a Python project that allows you to find all the crowd control (CC) spells in a live League of Legends game.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries](#libraries)
- [Credits](#credits)
- [License](#license)

---
# Requirements
To use this project, you will need to have:

* Python 3.6 or higher installed on your computer
* Riot Games API key
---

# Installation
I recommend using the program from within a [virtual environment](https://docs.python.org/3/library/venv.html).
1.  Clone or download this repository to your local machine.
2.  Store the Riot API key in an environment variable:
    ```
    export API_KEY=API_KEY 
    ```
3.  Install the required packages by running the following command:
    ```
    pip install -r requirements.txt
    ```
---

# Usage

To use this project, run the following command in the project directory:

```
python LeagueCC/main.py
```

Follow the command-line prompt to enter the summoner name of the player whose game you want to analyze.
The program will then retrieve the active game information for the given summoner name, find the champion names for all players in the active game, and print the name and description of any crowd control (CC) spells in each champion's spell list.

---
# Libraries
These are the libraries used within the project and their dependencies:


> `black: Used for code formatting and ensuring consistent style throughout the codebase.`
```
        click: Used for command-line interface (CLI) creation and management.
        mypy-extensions: Used for extending the type hints in Python code.
        packaging: Used for package version management and distribution.
        pathspec: Used for pattern matching on file paths.
        platformdirs: Used for handling platform-specific directories and file paths.
        tomli: Used for reading configuration files in the TOML format.
```

> `pytest: Used for writing and running unit tests for the codebase.`
```
        exceptiongroup: Used for handling exceptions in groups and logging them.
        iniconfig: Used for reading configuration files in the INI format.
        packaging: Used for package version management and distribution.
        pluggy: Used for creating and managing plugins in Python applications.
        tomli: Used for reading configuration files in the TOML format.
```  

> `requests: Used for making HTTP requests to APIs.`
```
        certifi: Used for HTTPS certificate validation when making API requests.
        charset-normalizer: Used for character encoding normalization to handle different character sets in API responses.
        idna: Used for handling Internationalized Domain Names (IDN) in API requests.
        urllib3: Used for handling HTTP connections and making API requests.
```

---
# Credits
This project was created by [SSM0022](https://github.com/SSM0022). The functions used in this project were inspired by the Riot Games API and adapted for this project.

---
# License
LeagueCC is licensed under the MIT License - see the LICENSE file for details.


