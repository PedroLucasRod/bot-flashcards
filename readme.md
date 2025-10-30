# Automação de Adição de Flashcards

Este projeto automatiza o processo de adição de flashcards em um sistema, utilizando dados previamente organizados em uma planilha Excel. O script lê as informações e insere os dados em campos específicos da interface através de cliques e digitação automatizados.

---

## Tecnologias utilizadas

- Python 3
- openpyxl: para leitura da planilha Excel
- pyautogui: para automação dos cliques e escrita na interface

---

## Como funciona

O script executa os seguintes passos de forma automática:

1. Abre a planilha `flashcards_constitucional.xlsx` e acessa a aba `Flashcards`.
2. Para cada linha, preenche:
   - Frente do flashcard (campo Front) com o valor da primeira coluna.
   - Verso do flashcard (campo Back) com o valor da segunda coluna.
   - Tag do flashcard (campo Tag) com o valor da terceira coluna **apenas uma vez na primeira execução**.
3. Após preencher os campos, clica no botão de adicionar flashcard.
4. Repete o processo para todos os flashcards da planilha, evitando repetir a tag em todos.

---

## Configuração

1. Mantenha a planilha Excel atualizada com os dados dos flashcards na aba `Flashcards`.
2. Assegure-se de que a janela do sistema para cadastro dos flashcards esteja aberta e posicionada corretamente, com resolução compatível para as coordenadas definidas no script.
3. Instale as bibliotecas necessárias:				pip install openpyxl pyautogui
4. Execute o script Python.

---

## Observações importantes

- As coordenadas de clique (`pyautogui.click(x, y)`) são fixas e podem precisar de ajustes dependendo da resolução e disposição da sua tela.
- O script assume que a tag é fixa e será preenchida apenas uma vez conforme a planilha.
- Para outros usos, poderá ser necessário adaptar o código para limpar ou alterar a tag conforme seus requisitos.
- O uso de `sleep` ou pausas pode ser necessário caso o sistema demore para responder entre passos.

---

## Estrutura da planilha

| Coluna | Descrição         |
| ------ | ------------------- |
| A      | Frente do flashcard |
| B      | Verso do flashcard  |
| C      | Tag do flashcard    |

---

## Objetivo

Automatizar a inserção rápida de flashcards, economizando tempo e reduzindo erros de digitação manual.

---

## Contato/Contribuições

Sintam-se à vontade para sugerir melhorias ou reportar problemas.
