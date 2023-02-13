Para iniciar o servidor, basta ir na pasta raiz (Desafio), e digitar "Python manage.py runserver".
Isso ira iniciar o servidor local da API (exemplo: http://127.0.0.1:8000/).
E necessario utilizar um Token de acesso!

Dependencias:
Python,
Django,
Django Rest Framework,
Postgresql.

Configuracoes do Banco:

Nome do Banco: desafio
Usuario: postgres
Senha: postgres
Host: 127.0.0.1
Porta: 5432


URLs de acesso a API:

http://127.0.0.1:8000/clientes/
http://127.0.0.1:8000/produto/
http://127.0.0.1:8000/produto_cliente/
http://127.0.0.1:8000/excel/
http://127.0.0.1:8000/api-token-auth/


Token para teste:
    'Authorization: Token 5a9d9215c9ae38aa7fc612f967046672d04f05c3'


API:

    Clientes:
        - Na parte de Clientes, e possivel visualizar, alterar, cadastrar e excluir clientes, diretamente do Banco de Dados em Postgresql
        - Cada cliente possui um ID unico
        - O campo de email passa por uma pre-validacao
        - Tambem aceita visualizar individualmente cada cliente, usando /id/. Exemplo: http://127.0.0.1:8000/clientes/4/
        Parametros: Email, Cliente

    Produto:
        - Na parte de Produtos favoritos, e possivel visualizar, alterar, cadastrar e excluir os produtos favoritos de cada cliente, 
        diretamente do Banco de Dados em Postgresql
        - O cadastro do produto so e realizado caso exista um cliente cadastrado com o email informado
        - Os produtos sao relacionados a um usuario pelo email. Caso o usuario seja excluido, os produtos favoritos tambem serao
        - Caso o cliente altere seu email, o banco de dados de seus Produtos Favoritos serao associados ao novo email automaticamente
        - A API tambem valida as alteracoes do produto favorito (e nao so a insercao), e so aceita a mudanca caso o produto exista na base de dados
        - E possivel usar o filtro de busca na API ("?search="), filtrando resultados tanto pelo email, quanto pelo produto favorito. Exemplo:
        http://127.0.0.1:8000/produto/?search=teste@teste.com
        Parametros: Email, Produto
    
    Produto_cliente:
        - E uma parte voltada para ajudar o FrontEnd, trazendo as informacoes de cada produto favorito de um cliente, diretamente de outra API
        - Este link e exclusivo para pesquisa, e a unica forma aceita pela pagina e o protocolo GET
        - Para fazer uma busca, e obrigatorio pesquisar por algum email. Caso contrario, a API nao retornara nenhum resultado
        - A API filtra o email informado no banco de dados, e consulta com a API dos produtos, trazendo as informacoes de Titulo, imagem, preco, e caso 
        exista, a de Avaliacao.
        - Para fazer uma busca, digite por exemplo: http://127.0.0.1:8000/produto_cliente/?search=INSIRA_O_EMAIL_AQUI.

    Excel:
        - Ao acessar o link de Excel, e possivel baixar um arquivo em XLSX, contendo todos os dados cadastrados no banco de Produtos Favoritos


Extras:
    - Melhorias de performance aplicados com o Django AutoPrefetchMixIn, reduzindo o impacto na performance ao efetuar buscas
    - Divisao da API em Clientes e Produtos, com apenas 2 campos em cada, visando um impacto menor na performance
    - Opcao para exportar em Excel o Banco de dados de Produtos Favoritos
    - Validacao em tempo real com a API do banco de dados de Produtos (fornecida pelo Labs)
    - E necessario autenticacao para acessar todas os caminhos da API
    - Uma URL (produto_cliente) que fornece uma visao extra, voltada para facilitar o frontend