from fastapi import FastAPI

# 1. Создаем объект приложения
app = FastAPI()


# 2. Главная страница
@app.get("/")
async def read_main() -> dict:
    return {"message": "Главная страница"}

# 3. Страница администратора
@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

# 4. Страницы пользователей по параметру пути
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# 5. Страницы пользователей с параметрами в адресной строке
@app.get("/user")
async def read_user_details(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# Запустите сервер командой: uvicorn main:app --reload
# Перейдите по адресу http://127.0.0.1:8000/docs для просмотра интерфейса Swagger.
# Главная страница: URL: http://127.0.0.1:8000/
# Страница администратора: URL: http://127.0.0.1:8000/user/admin
# Пользователь по ID: URL: http://127.0.0.1:8000/user/123
# Пользователь с параметрами строки запроса: URL: http://127.0.0.1:8000/user?username=Иван&age=25