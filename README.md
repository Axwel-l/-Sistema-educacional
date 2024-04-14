#Sistema Educaciona<br>
Breve descrição ou objetivo do projeto.<br>

Documentação: https://docs.google.com/document/d/1l894b6Cls8oUemLG2Rr-GiRjx6chY9aiURKg06vLYy0/edit?usp=sharing

Instalação<br>
1. Clone o repositório<br>

git clone Axwel-l/-Sistema-educacional<br>


2. Crie um ambiente virtual(Não Obrigatorio)<br>
É altamente recomendável usar um ambiente virtual para manter suas dependências Python isoladas. Você pode criar um ambiente virtual usando o venv.<br>
*python -m venv venv<br>

3. Ative o ambiente virtual:<br>
*/venv\Scripts\Activate.ps1<br>

4. Instale as dependências<br>
*pip install -r requirements.txt<br>

<br>
#Configuração<br>
1. Banco de Dados<br>
Edite o arquivo settings.py no diretório sistema e ajuste as configurações do banco de dados de acordo com o que for usar (no caso é o postegres, em que sera necessario intalar as extensões do banco que deseja usar ):<br>

DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.postgresql',<br>
        'NAME': 'escola',<br>
        'USER':'postgres',<br>
        'PASSWORD':'admin',<br>
        'HOST':'localhost',<br>
    }<br>
}

2. Migrar o Banco de Dados<br>
Depois de configurar o banco de dados, você precisa aplicar as migrações:<br>

*python manage.py makemigrations<br>
*python manage.py migrate<br>

Este é um sistema de Direção de uma Escola.<br>
-Incompleto até o momento<br>
