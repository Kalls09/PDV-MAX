from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar descontos': True,
        'cadastrar vendedor': True,

    }

class Vendedor(AbstractUserRole):
    available_permissions = { 
        'realizar_venda': True,
    }
