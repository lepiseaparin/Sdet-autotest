@echo off

:: Путь к python проекта
set PYTHON_PATH=Simbir-testovoe\.venv\Scripts\python.exe

:: Добавление python в PATH
set PATH=%PYTHON_PATH%;%PATH%

:: Путь к виртуальному окружению
call C:\Users\jackp\kulas\Simbir-testovoe\.venv\Scripts\activate.bat

:: Запуск тестов 
pytest --alluredir=./allure-results --maxfail=1 --disable-warnings -v

:: Генерация отчета Allure 
allure serve ./allure-results 2>nul

:: Ожидание завершения, чтобы увидеть результаты в консоли
pause
