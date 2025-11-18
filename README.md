# trabalho_erp
# ERP de Controle de Estoque  
Sistema simples de gestão de estoque desenvolvido em **Python**, utilizando **MySQL**, **SQLAlchemy**, **Pandas** e **Matplotlib**.  
Permite cadastrar produtos, movimentar estoque, gerar relatórios, visualizar gráficos e aplicar análise **Curva ABC**.

---

## Tecnologias Utilizadas

- **Python 3**
- **SQLAlchemy** (conexão com MySQL)
- **PyMySQL**
- **Pandas** (manipulação de dados)
- **Matplotlib** (gráficos)
- **MySQL** (banco de dados)

---

## Funcionalidades

### 1. Cadastro de Produtos
- Nome, categoria, preço e quantidade inicial
- Registro da data/hora da última movimentação

### 2. Exclusão de Produtos
- Remove produtos pelo ID

### 3. Movimentação de Estoque
- Entrada e saída de mercadorias
- Validação de estoque insuficiente
- Atualização automática da data de movimentação

### 4. Relatório Completo
- Lista todos os produtos do banco
- Exibe dados essenciais
- Aviso automático de **ESTOQUE BAIXO** (< 5)

### 5. Curva ABC
- Calcula valor total por produto
- Classifica em categorias A, B e C conforme relevância econômica

### 6. Comparação entre Categorias
- Soma de quantidade por categoria
- Geração de gráfico de barras

### 7. Dashboard de Estoque
- Gráfico de barras com estoque por produto
- Gráfico de pizza com valor total por categoria

---

## Estrutura do Banco de Dados

Execute no MySQL:

```sql
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco DECIMAL(10,2),
    quantidade INT DEFAULT 0,
    ultima_mov DATETIME
);
