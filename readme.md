
# [Space.io](https://t.me/space_io_bot) ![title](https://img.shields.io/badge/version-%201.3-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
___
###### To test the bot, click on the name
___

Bot on the theme of space, implemented on aiogram (3.x)
###### This's a graduation project in Skillbox
___
### Install
~~~
~ git clone https://gitlab.skillbox.ru/vladimir_kotov_1/python_basic_diploma
~~~
###### In project:

###### 1) Open the file "_DiplomProject/.env_" and fill in the text
~~~python
# Telegram token general-bot (token - BotFather, admin_id - you id profile in Telegram)
token=
admin_id=

# Telegram token log-bot (BotFather)
logger_bot=
~~~
###### 2) Run "main.py"
___
##### Logger - bot
###### It is needed to send critical errors !Dependency: Token, user ID
___
### Opportunities
- Output of a picture with a description from the database
- Output of 3 news posts (parsing)
- Viewing the glossary
- Search for terms from the glossary in messages
- Changing the language of the bot in the settings
- Familiarization with a brief summary of the Solar System
- View a simulation of the solar system
___
### Work
- Editing .js
- Create:
    - General bot: [Space.io](https://t.me/space_io_bot)
    - Helper bot: [Space.io - logger](https://t.me/space_io_logger_bot)
    - WebSite for WebApp: [Simulation Solar system](https://github.com/AstraL13666/Astral13666.github.io)
- Parsing [Astronews](https://www.astronews.ru/)
___
### Bot structure
__config_data__ - _Download tokens for bot_  
__data_base__ - _Вatabase of pictures with a description_  
__handler__ - _Contains handlers for pooling by bot_  
__keyboard__ - _Contains keyboards for by bot_  
__middlewares__ - _Custom kernels helpers_  
__utils__ - _image, text, memory class etc. for the bot_
___
### Technologies used
- Parsing: website, json
- Working with database
- Using API for text translation
___
### Lib
![Python](https://img.shields.io/badge/python-%203.11-%23757575.svg?&style=for-the-badge&logo=python&logoColor=green)
![Aiogram](https://img.shields.io/badge/AioGram-%203.x-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
![BS4](https://img.shields.io/badge/bs4-%204.12-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)  
![Peewee](https://img.shields.io/badge/Peewee-%203.16-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
![DeepTranslator](https://img.shields.io/badge/deep_translator-%201.11%20-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
![Emoji](https://img.shields.io/badge/Emoji-%202.4%20-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)  
![FUA](https://img.shields.io/badge/fake_useragent-%201.1-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
![jmespath](https://img.shields.io/badge/jmespath-%201.0-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
![loguru](https://img.shields.io/badge/loguru-%200.7-%23757575.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
___
![Git](https://img.shields.io/badge/git%20-%23545554.svg?&style=for-the-badge&logo=git&logoColor=white)
![gitlab](https://img.shields.io/badge/gitlab%20-%23545554.svg?&style=for-the-badge&logo=gitlab&logoColor=white)
![markdown](https://img.shields.io/badge/markdown-%23545554.svg?&style=for-the-badge&logo=markdown&logoColor=white)
![telegram](https://img.shields.io/badge/Telegram%20-%23545554.svg?&style=for-the-badge&logo=Telegram&logoColor=white)
![skillbox](https://custom-icon-badges.demolab.com/badge/-Skillbox-%23545554?style=for-the-badge&logoColor=white&logo=repo)
___
![skillbox](https://custom-icon-badges.demolab.com/badge/requirements%20-txt-%23000000.svg?style=for-the-badge&logoColor=white&logo=repo)
- Project:
  - `aiogram (3.0.0rc2)` - the main library for creating a bot
    - `aiohttp (3.8.5)` - lib for asynchronous HTTP requests and web development
    - `aiofiles (23.1.0)` - lib for asynchronous work with files
    - `aiosignal (1.3.1)` - lib for working with operating system signals in asynchronous mode
    - `async-timeout (4.0.3)` - lib that provides asynchronous timeout for operations
    - `magic-filter (1.0.11)` - lib for filtering and processing text data.
    - `pydantic (2.3.0)` - lib for checking and validating data
    - `pydantic_core (2.6.3)` - Internal lib used by pydantic for data validation and validation
  - `beautifulsoup4 (4.12.2)` - library for parsing websites
    - `soupsieve (2.5)` - lib for parsing CSS selectors in HTML and XML documents.
  - `deep-translator (1.11.4)` - lib for translating text
  - `emoji (2.8.0)` - lib for working with emojis in Python
  - `fake-useragent (1.2.1)` - lib for generating random user agents for HTTP requests
  - `jmespath (1.0.1)` - lib for working with JSON-like data structures
  - `loguru (0.7.1)` - lib for simplifying logging in Python
  - `peewee (3.16.3)` - ORM lib for working with databases 
  - `python-dotenv (1.0.0)` lib for loading environment variables
  - `requests (2.31.0)` - lib for sending HTTP requests
    - `urllib3 (2.0.4)` - lib for working with HTTP requests
    - `yarl (1.9.2)` - lib for working with URLs
- Auxiliary lib:
  - `annotated-types (0.5.0)` - lib that provides additional data types for type annotations
  - `attrs (23.1.0)` - lib for creating classes with automatically generated methods
  - `certifi (2023.7.22)` - set of root certificates for authenticating SSL/TLS connections
  - `charset-normalizer (3.2.0)` - lib for normalizing and converting character sets
  - `frozenlist (1.4.0)` - lib that provides an immutable list 
  - `idna (3.4)` - lib for processing and normalization of domain names in Unicode
  - `multidict (6.0.4)` - lib for working with immutable dictionaries
  - `typing_extensions (4.7.1)` - lib that provides extended data types for the `typing` module 
___
  ![update](https://img.shields.io/badge/update%20-1.3-%23000000.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white)
- Fixed a glossary bug
- Fixed a JSON
