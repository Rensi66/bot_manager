from fastapi import FastAPI
import logging

from app.routers import users


app = FastAPI()


logging.basicConfig(filename='C:/Users/r6999/OneDrive/Рабочий стол/bot_manager_logging.txt', 
                    filemode='w',
                    encoding='utf-8',
                    format='%(asctime)s | %(levelname)8s | %(name)s | %(lineno)d | %(message)s',
                    datefmt='%Y-%m-%d %H-%M-%S')


app.include_router(router=users.router, prefix='/bm')
