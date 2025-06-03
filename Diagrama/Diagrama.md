classDiagram
direction TB
    class Cliente {
	    +String nome
	    +String cpf
	    +String cnh
	    +String telefone
	    +String email
	    +Date data_nascimento
	    +String endereco
	    +String cidade
    }

    class Veiculo {
	    +String placa
	    +String marca
	    +String modelo
	    +Integer ano
	    +String cor
	    +Decimal valor_diaria
	    +CategoriaVeiculo categoria
    }

    class CategoriaVeiculo {
	    +String nome
	    +String descricao
	    +Decimal preco_adicional_diaria
	    +String tipo_de_combustivel
    }

    class Locacao {
	    +Cliente cliente
	    +CarrinhoLocacao carrinholocacao
	    +Funcionario funcionario
	    +DateTime data_hora_retirada
	    +DateTime data_hora_prevista_devolucao
	    +DateTime data_hora_efetiva_devolucao
	    +Decimal valor_total_previsto
	    +String status
    }

    class Funcionario {
	    +String nome
	    +String matricula
	    +String cargo
	    +Date data_admissao
	    +String email_corporativo
    }

    class Seguro {
	    +String tipo
	    +String cobertura
	    +Decimal valor_diario
	    +String franquia
	    +String seguradora
    }

    class Pagamento {
	    +Locacao locacao
	    +String forma_pagamento
	    +Decimal valor
	    +DateTime data_hora_pagamento
	    +String status
    }

    class Acessorios {
        +String nome
        +String descricao
        +Decimal valor_adicional
        +String categoria
    }

    class CarrinhoLocacao {
        +Veiculos veiculos
        +Adicionais adicionais
        +Seguro seguro
        +DateTime data_criacao

    }

    class Adicionais {
        +String nome
        +String descricao
        +Decimal valor_adicional
        +String categoria

    }

    Cliente "1" -- "0..*" Locacao : um para muitos
    Veiculo "1" -- "0..*" CarrinhoLocacao
    Veiculo "1" -- "1" CategoriaVeiculo : um para muitos
    Locacao "1" -- "0..*" Pagamento
    Veiculo "1" -- "0..*" Acessorios : Muitos para Muitos
    Locacao "1" -- "0..*" Funcionario
    Seguro "1" -- "0..*" CarrinhoLocacao
    Locacao "1" -- "0..*" CarrinhoLocacao : Carrinho de compras
    Adicionais "1" -- "0..*" CarrinhoLocacao
