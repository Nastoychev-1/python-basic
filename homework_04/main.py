"""
 Домашнее задание №4
 Асинхронная работа с сетью и бд

 доработайте функцию main, по вызову которой будет выполняться полный цикл программы
 (добавьте туда выполнение асинхронной функции async_main):
 - создание таблиц (инициализация)
 - загрузка пользователей и постов
     - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
       при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
 - добавление пользователей и постов в базу данных
   (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
 - закрытие соединения с БД
 """
import asyncio
from models import create_tables, User, Post, Session
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data, USERS_DATA_URL, POSTS_DATA_URL
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(session: AsyncSession, data_users) -> list[User]:
    users = [User(name=i.get('name'), username=i.get('username'), email=i.get('email')) for i in data_users]
    session.add_all(users)
    await session.commit()


def main():
    pass


if __name__ == "__main__":
    main()
