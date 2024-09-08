import sqlite3

class DB:
    def save_user(self, chat_id, mono, ssilka, silkal, uzuser):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (chat_id INTEGER, mono TEXT, ssilka TEXT, silkal TEXT, uzuser TEXT)")
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (chat_id, mono, ssilka, silkal, uzuser))
        conn.commit()
        conn.close()