#Criador Wget17...esse é meu canal no Youtube: https://www.youtube.com/c/Wget17_oficial/


#Edite esse codigo do seu jeito....ESPERO QUE GOSTE 



#Importe essas pibliotecas se vc não tiver elas


import requests
import telegram
from telegram.ext import Updater, CommandHandler
import json

TOKEN = "AQUI-VAI-SEU-TOKEN"

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher


#ATENÇÃO NAS FUNÇOẼS OU SEJA NAS (def) VOCE PODE COLOCAR SEUS TEXTOS.....VC PODE TIRA OS DIAMANTES TAMBEM CASO QUEIRA!


#função olhar digital
def olhar(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"\n💎Saiba tudo sobre o mundo da Tecnologia e Hacking nesse sites💎 \nhttps://www.tecmundo.com.br/\n \nhttps://olhardigital.com.br/\n")


#Função manda btc
def btc(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"\n💎Saiba o preço do Biticoin (BTC) em tempo real💎 \nhttps://financeone.com.br/criptomoedas/bitcoin-hoje/\n")

#compra md
def comprar(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text=f"\n💎Olá meu nome é Md, sou um bot feito 100% em python\n \nSe você quiser me adquirir, entre em contato com meu braço direito \n \nEspero que você tenha gostado de mim ABRAÇO💎\n")


#gerador
#def gerador(update, context):
   #context.bot.send_message(chat_id=update.effective_chat.id, text=f"💎Gerador de senhas OFF💎")



#Função boa vindas
def Md(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text=f"💎Bem vindo guerreiro(a) Esse são os comandos que temos💎\n \n1-/Md\n \n2-/ajuda\n \n3-/python\n \n5-/cep\n \n6-/comprar\n \n7-/btc\n \n8-/hacker_news\n")

    

#função AJUDA
def ajuda(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text=f"💎Esses são os canais para ajudar você:  ou entre em contato comigo @JoaoFelipeMD💎")

#Função python
def python(update, context):
   context.bot.send_message(chat_id=update.effective_chat.id, text=f"Python é uma linguagem de programação de alto nível: Oque pode ser feito com python:\n Python é uma linguagem poderosa e divertida. Com ela você pode fazer diversas coisas como: Construção de sistemas Web com Django, Flask, Pyramid, etc. Análise de dados, Inteligência Artificial, Machine Learning e etc com Numpy, Pandas, Matplotlib: SAIBA MAIS EM  https://pt.wikipedia.org/wiki/Python\n")


def biticoin(update, context):
    cep=context.args[0]
    
    update.message.reply_text(f'💎Preste atenção no metodo (bid) lá esta acotação certa💎 ')
    try:
        response = requests.get(
            url=f'https://economia.awesomeapi.com.br/last/BTC/'
            
        
            
        
    
        )
        response.raise_for_status()


        message = [
            f'{k}: {v}\n'
            for k, v in response.json().items()
        ]
        update.message.reply_text(''.join(message))
    except Exception as exc:
        update.message.reply_text(f'💎Digite /btc para ver o preço💎')
            


    
    #update.message.reply_text(f'SE VOCÊ FIZER O MAU USO DESSAS INFORMAÇÕES, NÃO NÓS RESPONSABILIZAMOS ')
    #try:
     #  response = requests.get(
       #     url=f'https://viacep.com.br/ws/{cep}/json'
      # # )
      #  response.raise_for_status()


       # message = [
          #  f'{k}: {v}\n'
           # for k, v in response.json().items()
        #]
       # update.message.reply_text(''.join(message))
    #except Exception as exc:
       # update.message.reply_text(f'Cep não encotrado ou errado...o cep tem que ter 8 Número!')
        

    


#CEP...........................................


#função filme
def  busca_movie(update, context):
     movie = ''.join(context.args)
     url_filme = f"http://www.omdbapi.com/?i=tt3896198&apikey=75c5e942&t={movie}&plot=full"
     response = requests.get(url_filme).json()

     if response["Response"] == "True":
         text = (


          f"Filme: {response['Title']}\n"
          f"Data de lançamento: {response['Released']}\n"
          f"Diretor(es): {response['Director']}\n"
          f"Escritor(es): {response['Writer']}\n"
          f"Atores: {response['Actors']}.\n"
          f"Enredo:{response['Plot']}\n"
          f"Genero: {response['Genre']}\n"
          f"Link para o poste do filme: {response['Poster']}\n"
      
        )
     else:
         text = "Desculpe o filme não exite"

     context.bot.send_message(chat_id=update.effective_chat.id, text=text)
 
#dispatcher.add_handler(CommandHandler('cep', busca_cep, pass_args=True));

dispatcher.add_handler(CommandHandler('btc', biticoin, pass_args=True));


olhar_handler = CommandHandler("hacker_news", olhar)
dispatcher.add_handler(olhar_handler)


btc_handler = CommandHandler("btc", btc)
dispatcher.add_handler(btc_handler)


comprar_handler = CommandHandler("comprar", comprar)
dispatcher.add_handler(comprar_handler)


#gerador_handler = CommandHandler("gerador", gerador)
#dispatcher.add_handler(gerador_handler)

python_handler = CommandHandler("python", python)
dispatcher.add_handler(python_handler)


ajuda_handler = CommandHandler("ajuda", ajuda)
dispatcher.add_handler(ajuda_handler)


movie_handler = CommandHandler("filme", busca_movie)
dispatcher.add_handler(movie_handler)

Md_handler = CommandHandler('Md', Md)


dispatcher.add_handler(Md_handler)
dispatcher.add_handler(ajuda_handler)


updater.start_polling()
