#Sistema Educaciona
Breve descrição ou objetivo do projeto.

Instalação
1. Clone o repositório

git clone Axwel-l/-Sistema-educacional


2. Crie um ambiente virtual(Não Obrigatorio)
É altamente recomendável usar um ambiente virtual para manter suas dependências Python isoladas. Você pode criar um ambiente virtual usando o venv.
*python -m venv venv

3. Ative o ambiente virtual:
*/venv\Scripts\Activate.ps1

4. Instale as dependências
*pip install -r requirements.txt


##Configuração
1. Banco de Dados
Edite o arquivo settings.py no diretório sistema e ajuste as configurações do banco de dados de acordo com o que for usar (no caso é o postegres, em que sera necessario intalar as extensões do banco que deseja usar ):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'escola',
        'USER':'postgres',
        'PASSWORD':'admin',
        'HOST':'localhost',
    }
}

2. Migrar o Banco de Dados
Depois de configurar o banco de dados, você precisa aplicar as migrações:

*python manage.py makemigrations
*python manage.py migrate

Este é um sistema de Direção de uma Escola.
-Incompleto até o momento
