from mysql import connector
import datetime
class DbConnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Gau@123##",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None
