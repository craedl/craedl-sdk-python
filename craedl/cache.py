import sqlite3

class Cache():

    db_conn = None
    db_cursor = None

    def close(self):
        self.db_conn.close()

    def open(self, path):
        self.db_conn = sqlite3.connect(path)
        self.db_cursor = self.db_conn.cursor()

        # create table if it does not already exist
        self.db_cursor.execute('''
            SELECT count(name)
            FROM sqlite_master
            WHERE type='table'
                AND name='dirs'
        ''')
        if self.db_cursor.fetchone()[0] != 1:
            self.db_cursor.execute('''
                CREATE TABLE dirs (
                    complete bit,
                    hash varchar(40) NOT NULL,
                    path varchar(1024) NOT NULL UNIQUE
                )
            ''')

    def start_upload(self, dir_path, dir_hash):
        try:
            self.db_cursor.execute('''
                INSERT INTO dirs VALUES (
                    ?,
                    ?,
                    ?
                )
            ''', (
                0,
                dir_hash,
                dir_path,
            ))
            self.db_conn.commit()
        except sqlite3.IntegrityError:
            self.db_cursor.execute('''
                UPDATE dirs
                SET complete=0, hash=?
                WHERE path=?
            ''', (
                dir_hash,
                dir_path
            ))
            self.db_conn.commit()

    def finish_upload(self, dir_path, dir_hash):
        self.db_cursor.execute('''
            UPDATE dirs
            SET complete=1
            WHERE hash=?
                AND path=?
        ''', (
            dir_hash,
            dir_path
        ))
        self.db_conn.commit()

    def check_upload(self, dir_path, dir_hash):
        self.db_cursor.execute('''
            SELECT count(hash)
            FROM dirs
            WHERE hash=?
                AND path=?
                AND complete=1
        ''', (
            dir_hash,
            dir_path
        ))
        if self.db_cursor.fetchone()[0] == 1:
            return True
        return False
