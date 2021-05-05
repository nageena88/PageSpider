import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute('drop table if exists words')
        dll = "CREATE table words (word text PRIMARY KEY not null, usage_count INT DEFAULT 1 not null);"
        cur.execute(dll)
        dll = "create unique INDEX words_word_uindex ON words (word)"
        cur.execute(dll)
    conn.close()


def save_words_to_database(database_path: str, words_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            sql = "select count(word) from words where word ='" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '" + word + "'"
            else:
                sql = "insert into words(word) values('" + word + "')"
            cur.execute(sql)
            # conn.close()
        print('Database save complete!')
