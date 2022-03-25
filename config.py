from enum import Enum

BOT_TOKEN = "5185285412:AAHrKwxdQwpLN_kGTGsN2trFPuL6e3HPJ84"  # Токен бота
DB_URI = "postgres://gzojuyakfhtwkn:97755c93ef66fa2be44ca3b15db300ece31297277e914adfd5afaddc6b9920ad@ec2-54-73-178-126.eu-west-1.compute.amazonaws.com:5432/deeoqn4q3gg3am"  # URI для подключания к БД


# Состояния для создания опросника, по которым пользователь следует последовательно
class States(Enum):
    S_QSTN_0 = "0"
    S_QSTN_1 = "1"
    S_QSTN_2 = "2"
    S_QSTN_3 = "3"
    S_QSTN_4 = "4"
    S_QSTN_5 = "5"
    S_QSTN_6 = "6"
    S_QSTN_7 = "7"
    S_QSTN_8 = "8"
    S_QSTN_9 = "9"
    S_CNGR = "10"
    S_LOBBY = "11"
