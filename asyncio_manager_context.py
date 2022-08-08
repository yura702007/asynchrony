import asyncio


# имитация  асинхронного соединения с некой периферией
async def get_conn(host, port):
    class Conn:

        async def put_data(self):
            print('Отправка данных...')
            await asyncio.sleep(3)
            print('Данные отправлены.')

        async def get_data(self):
            print('Получение данных...')
            await asyncio.sleep(3)
            print('Данные получены.')

        async def close(self):
            print('Завершение соединения...')
            await asyncio.sleep(3)
            print('Соединение закрыто.')

    print('Устанавливаем соединение...')
    await asyncio.sleep(3)
    print('Соединение установленно.')
    return Conn()


class Connection:

    # этот конструктор будет выполнен в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', '4242') as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        # операции отправки и получения данных выполняем конкурентно
        await send_task
        await receive_task


asyncio.run(main())
