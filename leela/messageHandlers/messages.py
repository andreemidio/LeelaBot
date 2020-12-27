def echo(update, context):
    pass

def welcome(update, context, new_member):
    #user_id = new_member.id
    #user_name = new_member.username
    #mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    #print(bool(user_id))
    from telegram.parsemode import ParseMode
    if new_member.first_name != 'leelabot':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                            text= 'Olá, ' + str(new_member.first_name) + '!' +
                                            'Seja bem vindo à Comunidade Dev4.0!\n' +
                                            '\nLeia as regras na descrição do grupo!' +
                                            '\n\nTemos <s>tequila</s> artigos semanalmente em nosso blog: https://dev4lab.github.io' +
                                            '\n\nConheça nosso repositório de conteúdo gratuito: https://github.com/dev4lab/tutoriais-tecnologia',
                                            parse_mode=ParseMode.HTML)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Olá, pessoal! Meu nome é Leela. Estou aqui para ajudar!")


def goodbye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Saiu e não pagou nem uma uma cerveja pra nós!")


def empty_message(update, context):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            return welcome(update, context, new_member)
        
    elif update.message.left_chat_member is not None:        
        return goodbye(update, context)