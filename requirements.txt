no terminal:


// PARA RODAR O PROGRAMA

1. " 

cd cadastro_users 

" 

2. " 

python .\manage.py runserver 

" 


// PARA RESETAR IDs E COMEÇAR NOVOS TESTES

1. " 

python manage.py shell 

"

2. "   

from django.db import connection
from app_cadastro_users.models import Usuario  

# Apaga todos os registros
Usuario.objects.all().delete()

# Reseta o autoincremento
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='app_cadastro_users_usuario';")

"    
