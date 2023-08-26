
# TG-bot: Space.io

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
# Telegram token general-bot
token=
admin_id=

# Telegram token log-bot
logger_bot=

# Token translate rapid-api
rapid_api=
~~~
###### 2) Run "main.py"
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
![telegram](https://custom-icon-badges.demolab.com/badge/-Skillbox-%23545554?style=for-the-badge&logoColor=white&logo=repo)
