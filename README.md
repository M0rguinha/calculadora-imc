# 🏥 Calculadora de IMC (Índice de Massa Corporal)

Uma calculadora simples, educativa e bem documentada para calcular o Índice de Massa Corporal em Python. Perfeita para iniciantes aprendendo programação!

## 📋 Sobre o IMC

O **Índice de Massa Corporal (IMC)** é uma medida que relaciona peso e altura para avaliar se uma pessoa está em um peso saudável.

### Fórmula
```
IMC = Peso (kg) ÷ Altura² (metros)
```

### Classificações Oficiais

| IMC | Classificação |
|-----|----------------|
| < 18.5 | 🔵 Abaixo do peso |
| 18.5 - 24.9 | 🟢 Peso normal |
| 25.0 - 29.9 | 🟡 Sobrepeso |
| 30.0 - 34.9 | 🟠 Obesidade grau I |
| 35.0 - 39.9 | 🔴 Obesidade grau II |
| ≥ 40.0 | 🔴 Obesidade grau III |

---

## 🚀 Como Usar

### Pré-requisitos
- Python 3.x instalado em seu computador

### Executar a Calculadora

Abra o terminal/PowerShell e execute:

```bash
python calculadora_imc.py
```

### Exemplo de Uso

```
Digite seu peso corporal (kg): 70
Informe sua altura (m): 1.75

========================================
Peso: 70.0 kg
Altura: 1.75 m
IMC: 22.86
Classificação: Peso normal
========================================
```

---

## ✨ Recursos da Calculadora

- ✅ **Validação de entrada** - Rejeita valores negativos ou zero
- ✅ **Tratamento de erros** - Captura entradas não numéricas
- ✅ **6 classificações** - Todas as faixas de IMC cobertas
- ✅ **Interface amigável** - Mensagens claras e bem formatadas
- ✅ **Código comentado** - Fácil de entender e modificar

---

## 📂 Arquivos

```
inicio/
├── README.md                  # Este arquivo
├── calculadora_imc.py         # Versão principal e melhorada 🌟
├── inicio_de_tudo.py          # Versão com as mesmas funcionalidades
└── mine_calculadora.py        # Versão experimental
```

---

## 💻 Código Exemplo

### Versão Simples
```python
peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura ** 2)
print(f"Seu IMC: {imc:.2f}")
```

### Versão com Validação (Recomendada)
Veja o arquivo `calculadora_imc.py` para a implementação completa com:
- Tratamento de exceções
- Validação de valores
- Classificação automática
- Interface melhorada

---

## 🎓 Conceitos de Programação

Este projeto ensina:

1. **Variáveis** - Armazenar peso e altura
2. **Tipos de Dados** - Usar `float` para números decimais
3. **Input/Output** - `input()` e `print()`
4. **Operadores** - Divisão e exponenciação (`**`)
5. **Estruturas Condicionais** - `if/elif/else`
6. **Tratamento de Erros** - `try/except`
7. **String Formatting** - f-strings
8. **Validação de Dados** - Verificar valores válidos

---

## 🔧 Modificações e Expansões

Você pode expandir este projeto adicionando:

### Fácil
- Perguntar se deseja calcular novamente (loop)
- Adicionar cor ao output usando `colorama`
- Salvar resultado em um arquivo `.txt`

### Intermediário
- Interface gráfica com `tkinter`
- Banco de dados para histórico de cálculos
- Calcular múltiplas pessoas

### Avançado
- Aplicação web com Flask
- API REST
- Banco de dados com SQLite

---

## 📝 Exemplo de Expansão Simples

```python
while True:
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        
        if peso <= 0 or altura <= 0:
            print("❌ Valores devem ser positivos!")
            continue
            
        imc = peso / (altura ** 2)
        print(f"Seu IMC: {imc:.2f}\n")
        
        if input("Deseja calcular novamente? (s/n): ").lower() != 's':
            break
            
    except ValueError:
        print("❌ Digite apenas números!\n")
```

---

## ⚠️ Importante

Este é um programa educativo. Para um diagnóstico real de saúde, consulte um profissional médico. O IMC é apenas um indicador e não deve ser usado como diagnóstico único.

---

## 📚 Recursos Externos

- [OMS - Índice de Massa Corporal](https://www.who.int/publications-detail-redirect/2021-guidelines-on-the-management-of-gestational-diabetes-mellitus)
- [Python Official Docs](https://docs.python.org/3/)
- [Python Tutorial - w3schools](https://www.w3schools.com/python/)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar!

---

## 🤝 Contribuições

Quer melhorar este projeto? Faça um fork e envie um Pull Request!

Dúvidas? Abra uma issue no repositório do GitHub!

---

**Criado com ❤️ por M0rguinha**  
**Data**: 2026-08-18  
**Python**: 3.x
