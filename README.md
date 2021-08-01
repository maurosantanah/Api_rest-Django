# Api_rest-Django
# Como testar
 Antes de começar

<a href="https://insomnia.rest/download">  Insomnia </a>

#Pelo Insomnia.

1 - Acesse a<a href="https://powerful-shore-82457.herokuapp.com"> API.</a>

2 - Utilize o Insomnia para realizar as requisições HTTP.

3 - Para consultar os dados de um usuário especifico utilize a url acrescentando o id do usuário no final https://powerful-shore-82457.herokuapp.com com o metodo GET do Insomnia.

4 - Para adicionar dados de um novo usuário, selecione o formato JSON no corpo da requisição do Insomnia, informe os dados e modifique o cabeçalho para o método POST com a url https://powerful-shore-82457.herokuapp.com.

5 - Para editar os dados de um usuário específico, copie o id selecione o formato JSON no corpo da requisição do Insomnia, descreva as alterações e selecione o método PUT com a url https://powerful-shore-82457.herokuapp.com.

6 - Para deletar um produto selecione o metodo DELETE e informe o id do produto a ser deletado ao final da url https://powerful-shore-82457.herokuapp.com .

7 - Ao acessar a url https://powerful-shore-82457.herokuapp.com erão listados os dados de todos os usuários cadastrados.


# Diretamente pelo Navegador.

1 - Acesse o <a href="https://powerful-shore-82457.herokuapp.com/usuarios// "> Usuario </a>

2 - Na página exibida é possível visualizar os dados de todos os usuários inseridos.

3 - Para adicionar mais usuários, basta preencher os campos solicitados e pressionar o botão POST.

4 - Para editar, basta coletar o id do mesmo e adicionar no fina https://powerful-shore-82457.herokuapp.com/usuarios// .Depois é só realizar as alterações e finalizar com POST.

5 - Para deletar os dados de um usuário, colete seu id e selcione a opção DELETE no canto superior direito.

# Como replicar

1- Faça clone do projeto para o seu computador.

 git clone https://github.com/cristianordon/API_Rest-Django-DB
 
 2 - Com o python instalado em sua máquina, vá até o diretorio do projeto clonado e crie um ambiente virtual para o projeto.
 
 stale o virtualenv caso ainda não tenha instalado.
  pip install virtualenv
Crie o seu ambiente virtual.
 virtualenv nome_do_ambiente_virtual
Ative o ambiente virtual.
  nome_do_ambiente_virtual/Scripts/activate
Caso o ambiente virtual tenha sido ativado o nome aparecerá em destaque à frente:

(nome_do_ambiente_virtual) c:/user/user_api(main):
3 - Instale as dependencias do projeto.

  pip install -r requirements.txt
4 - Execute as migrações caso tenha modificado o arquivo models.py.

   python manage.py migrate
5 - Execute a aplicação em sua máquina.

   python manage.py runserver
Com isso, já é possível testar a aplicação em sua máquina.
