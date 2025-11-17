# Flashcard Addition Automation

This project automates the process of adding flashcards to a system using data previously organized in an Excel spreadsheet. The script reads the information and inserts data into specific interface fields through automated clicks and typing.

---

## Technologies Used

* Python 3
* openpyxl: for reading Excel spreadsheets
* pyautogui: for automating clicks and typing in the interface

---

## How It Works

The script executes the following steps automatically:

1. Opens the `flashcards_constitucional.xlsx` spreadsheet and accesses the `Flashcards` sheet.
2. For each row, fills in:
   * Front of the flashcard (Front field) with the value from the first column.
   * Back of the flashcard (Back field) with the value from the second column.
   * Flashcard tag (Tag field) with the value from the third column  **only once on the first execution** .
3. After filling in the fields, clicks the add flashcard button.
4. Repeats the process for all flashcards in the spreadsheet, avoiding repeating the tag for all cards.

---

## Setup

1. Keep the Excel spreadsheet updated with flashcard data in the `Flashcards` sheet.
2. Ensure that the flashcard registration system window is open and correctly positioned, with compatible resolution for the coordinates defined in the script.
3. Install the required libraries:

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 my-md relative flex flex-col rounded-lg font-mono text-sm font-normal bg-subtler"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl flex h-0 items-start justify-end md:sticky md:top-[calc(var(--header-height)+var(--size-xs))]"><div class="overflow-hidden rounded-full border-subtlest ring-subtlest divide-subtlest bg-base"><div class="border-subtlest ring-subtlest divide-subtlest bg-subtler"></div></div></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-subtle py-xs px-sm inline-block rounded-br rounded-tl-lg text-xs font-thin">bash</div></div><div><span><code><span><span>pip </span><span class="token token">install</span><span> openpyxl pyautogui
</span></span><span></span></code></span></div></div></div></pre>

4. Run the Python script.

---

## Important Notes

* Click coordinates (`pyautogui.click(x, y)`) are fixed and may need adjustments depending on your screen resolution and layout.
* The script assumes the tag is fixed and will be filled in only once according to the spreadsheet.
* For other uses, it may be necessary to adapt the code to clear or change the tag according to your requirements.
* Using `sleep` or pauses may be necessary if the system takes time to respond between steps.

---

## Spreadsheet Structure

| Column | Description        |
| ------ | ------------------ |
| A      | Front of flashcard |
| B      | Back of flashcard  |
| C      | Flashcard tag      |

---

## Objective

Automate the quick insertion of flashcards, saving time and reducing manual typing errors.

---

## Contact/Contributions

Feel free to suggest improvements or report issues.

# (PT-BR Version) Automação de Adição de Flashcards

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
