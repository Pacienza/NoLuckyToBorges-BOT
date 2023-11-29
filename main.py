import random
import discord

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.probabilidade_padrao = 1.0

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # Verificar se a mensagem segue a fórmula XdN
        if 'd' in message.content:
            entrada_usuario = message.content
            resultado_total, resultados_individuais = self.rolar_dados(entrada_usuario, message.author.name)

            if isinstance(resultado_total, int):
                response = f"Rolagem Total: [{resultado_total}] :   |"
                for i, resultado in enumerate(resultados_individuais, start=1):
                    response += f"{resultado} | "
                await message.channel.send(response)
            else:
                await message.channel.send(resultado_total)

    def rolar_dados(self, entrada, nome_usuario):
        probabilidade = self.probabilidade_padrao

        if nome_usuario.lower() == 'necrosamurai':
            probabilidade = 0.7

        try:
            n, x = map(int, entrada.lower().split('d'))

            resultados = [random.randint(1, x) for _ in range(n)]

            resultados_ajustados = [int(resultado * probabilidade) for resultado in resultados]

            resultado_total = sum(resultados_ajustados)

            return resultado_total, resultados_ajustados

        except ValueError:
            return (
                "Entrada inválida. Use o formato XdN, onde X é o número de dados e N é o tipo de dado (4, 6, 8, 10, "
                "12, 20).")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE3OTMxMDA3OTAxMTQ1OTE2Mw.G-fMu0.gxDUl_M1qowadik4USyhBwDadN7GL8_hDzdPP8')



