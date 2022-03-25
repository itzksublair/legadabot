import psycopg2
import config
from qstnansw import *

db_connection = psycopg2.connect(config.DB_URI, sslmode="require")
db_object = db_connection.cursor()


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    db_object.execute(f"UPDATE users SET state = '{value}' WHERE id = '{user_id}'")
    db_connection.commit()


# Получаем текущее состояние пользователя
def get_current_state(user_id):
    db_object.execute(f"SELECT state from users WHERE id = '{user_id}'")
    result = db_object.fetchall()
    return str(int(result[0][0]))


# Добавляем текущий ответ пользователя
def add_answer(user_id, сategory, value):
    db_object.execute(f"UPDATE users SET {сategory} = '{value}' WHERE id = '{user_id}'")
    db_connection.commit()


# Получаем сводку с базы данных по вопросу, кол-ву ответов и критерию + возвращаем всё словарями
def get_data_2(num_ans, count_ans, criteria):
    db_object.execute(f"SELECT * FROM users")
    data = db_object.fetchall()
    if criteria == "Пол":
        all_ans_m = {ans: 0 for ans in answers[:count_ans]}
        all_ans_w = {ans: 0 for ans in answers[:count_ans]}
        for user in data:
            if str(user[num_ans + 2]).isdigit():
                if str(user[2]) == 'М':
                    all_ans_m[str(user[num_ans + 2]).strip()] += 1
                elif str(user[2]) == 'Ж':
                    all_ans_w[str(user[num_ans + 2]).strip()] += 1
        return all_ans_m, all_ans_w
    elif criteria == "Возраст":
        all_ans_29 = {ans: 0 for ans in answers[:count_ans]}
        all_ans_30 = {ans: 0 for ans in answers[:count_ans]}
        all_ans_50 = {ans: 0 for ans in answers[:count_ans]}
        for user in data:
            if str(user[num_ans + 2]).strip().isdigit():
                if int(user[3]) <= 29:
                    all_ans_29[str(user[num_ans + 2]).strip()] += 1
                elif 30 <= int(user[3]) <= 50:
                    all_ans_30[str(user[num_ans + 2]).strip()] += 1
                elif int(user[3]) > 50:
                    all_ans_50[str(user[num_ans + 2]).strip()] += 1
        return all_ans_29, all_ans_30, all_ans_50
    elif criteria == "Образование":
        all_ans_1 = {ans: 0 for ans in answers[:count_ans]}
        all_ans_2 = {ans: 0 for ans in answers[:count_ans]}
        all_ans_3 = {ans: 0 for ans in answers[:count_ans]}
        all_ans_4 = {ans: 0 for ans in answers[:count_ans]}
        all_ans_5 = {ans: 0 for ans in answers[:count_ans]}

        for user in data:
            if str(user[num_ans + 2]).strip().isdigit():
                if int(user[5]) == 1:
                    all_ans_1[str(user[num_ans + 2]).strip()] += 1
                elif int(user[5]) == 2:
                    all_ans_2[str(user[num_ans + 2]).strip()] += 1
                elif int(user[5]) == 3:
                    all_ans_3[str(user[num_ans + 2]).strip()] += 1
                elif int(user[5]) == 4:
                    all_ans_4[str(user[num_ans + 2]).strip()] += 1
                elif int(user[5]) == 5:
                    all_ans_5[str(user[num_ans + 2]).strip()] += 1

        return all_ans_1, all_ans_2, all_ans_3, all_ans_4, all_ans_5
