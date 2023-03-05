import pymysql
from variables.config import *

class Conection:
    def __init__(self, host: str, user: str, password: str, db_name: str, port: int = 3306) -> None:
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

    async def chek(self, member_id: int) -> bool:
        """return True when member in basa is"""

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                select_all_rows =f"""
                SELECT user_id FROM mahitka.users
                WHERE user_id='{member_id}';

                """

                cursor.execute(select_all_rows)

                rows = cursor.fetchall()
                if rows:
                    return True
                return False
                
        finally:
            self.connection.close()

    async def set_new_member(self, memberId: int, choise: str) -> None:
        """make a new member in data base\n
        ("Bounty-Hunter", "Pirate", "Marine")"""

        self.connection.ping()
        with self.connection.cursor() as cursor:
            update_query =f"""
                INSERT INTO mahitka.users(user_id, point, choise)
                values('{memberId}', 0, '{choise}');
            """

            cursor.execute(update_query)
            self.connection.commit()
                

    async def get_point(self, memberId: int) -> int:
        """return member point"""

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                select_all_rows =f"""
                SELECT point FROM mahitka.users
                WHERE user_id = '{memberId}';

                """

                cursor.execute(select_all_rows)

                rows = cursor.fetchall()
                
                return rows[0]["point"]
                
        finally:
            self.connection.close()

    async def set_point(self, memberId: int, value: int) -> None:
        """sets the level value of a member"""

        self.connection.ping()
        with self.connection.cursor() as cursor:
            update_query =f"""
                UPDATE mahitka.users
                SET point={value}
                WHERE user_id='{memberId}';
            """

            cursor.execute(update_query)
            self.connection.commit()

    async def get_choise(self, memberId: int) -> str:
        """return user choice"""

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                select_all_rows =f"""
                SELECT choise FROM mahitka.users
                WHERE user_id='{memberId}';
                """

                cursor.execute(select_all_rows)

                rows = cursor.fetchall()
                
                return rows[0]["choise"]
                
        finally:
            self.connection.close()

    async def get_top_list(self, offset: int) -> list:
        """
            returns a list of dictionaries from highest score to lowest.\n
            view:\n
            \n
            user_id - Discord user id\n
            point - Number of points (messages)\n
            choise - Choice of path ("Bounty-Hunter", "Pirate", "Marine")
        """

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                select_all_rows = f"""
                SELECT user_id, point, choise FROM mahitka.users
                ORDER BY point DESC
                LIMIT 5
                OFFSET {offset};"""

                cursor.execute(select_all_rows)
                
                rows = cursor.fetchall()

                offset += 5
                return rows
        finally:
            self.connection.close()

    async def reset_user(self, memberId: int) -> None:
        """
            Removes a user from the database
        """

        self.connection.ping()
        with self.connection.cursor() as cursor:
            update_query =f"""
                DELETE FROM mahitka.users WHERE user_id={memberId};
            """

            cursor.execute(update_query)
            self.connection.commit()


if __name__ == "__main__":
    import asyncio
    from time import sleep
    from random import randint

    async def main():
        aboba = Conection(
            host= host,
            user=user,
            password=password,
            db_name=db_name,
            port=3306
        )
    asyncio.run(main())