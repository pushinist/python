# multiprocessing - библиотека для работы с процессами
# threading - библиотека для работы с потоками
# Тема лекции - асинхронное программирование
# Асинхронное программирование - контроль за процессом полностью принадлежит программисту, используют, когда
# программа работает долго.
# EventLoop - контролирует, когда процесс запустится, когда он выполнится
# Coroutine - асинхронная функция, субпроцесс, который выполняется после EventLoop
# Futures - объекты, представляющие собой результат выполнения асинхронной операции
# Tasks - запущенная в рамках EventLoop Couroutine'а
import asyncio
import aiohttp

urls = ['http://github.com', 'http://google.com', 'http://yandex.ru']
async def call_url(url):
    print(f'Requesting {url}')
    response = await aiohttp.get(url)
    data = await response.text()
    print(f'{url}:{len(data)}')
    return data


futures = [call_url(url) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))


async def async_func(task_no):
    print(f'Starting task {task_no}')
    await asyncio.sleep(1)
    print(f'Finishing task {task_no}')
async def main():
    taskA = loop.create_task(async_func('taskA'))
    taskB = loop.create_task(async_func('taskB'))
    taskC = loop.create_task(async_func('taskC'))
    await ([taskA, taskB, taskC])

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except:
        pass

# Преимущество асинхнронности - больше производительность, удобство обработки ввода-вывода
# Асинхронное программирование должно применяться в нужном месте в нужное время

# Виртуальное окружение (venv, Virtualenv, pipenv, pyenv, poetry)
# 1. Создаем
# 2. Активируем
# 3. Работаем
# 4. Деактивируем