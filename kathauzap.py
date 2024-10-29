# Passo 1: Titulo- Kathauzap
# Passo 2: Iniciar chat
        #Popup/modal/alerta
        # titulo: Bem Vindo
        # Campo de Texto: Escreva seu nome no chat
        # Botão: Entrar no chat
        # Sumir com o Titulo e o botao inicial
        # Fechar o popup
        # Criar o chat(com a mensagem  de "nome do usuario entrou no chat")
        # Embaixo do chat
        #  campo de texto: Digite sua mensagem
        # botao de enviar
        # vai aparecer a mensagem no chat com o nome do usuario
        # pabllo: coe galera
        
import flet as ft

# Criar a funçao principal do seu sistema

def main(pagina):
    # Criar alguma coisa
    # Criar o titulo
    titulo = ft.Text("KathauZap")
    
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel) # Criar tunel de comunicaçao
    
    titulo_janela = ft.Text("Bem vindo")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no Chat")
    
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        # enviar a mensagem no chat
           # usuario : mensagem
        
        
        # enviar mensagem no tunel
        pagina.pubsub.send_all(texto) # enviar a mensagem no tunel
           
        #limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()
           
    texto_mensagem = ft.TextField(label="Digite Sua Mensagem", on_submit = enviar_mensagem)    
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column()
    
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    def entrar_chat(evento):
        # Sumir com o Titulo e o botao inicial
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        # Fechar o popup
        janela.open = False
        # Criar o chat
        pagina.add(chat)
        #  campo de texto: Digite sua mensagem e enviar
        pagina.add(linha_mensagem)
    
        # vai aparecer a mensagem no chat com o nome do usuario
        # com a mensagem  de "nome do usuario entrou no chat")
        
        texto_entrar_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrar_chat)
        
        pagina.update()
    
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click= entrar_chat)
    
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])
    
    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
        
        
        
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    
    # Colocar alguma coisa na pagina
    # Adicionar o titulo na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar o seu sistema

ft.app(main, view=ft.WEB_BROWSER)