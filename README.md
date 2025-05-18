# Leitor de Notas Fiscais

# Sobre

O presente projeto tem como objetivo ler dados de notas fiscais e enviar os dados do produto para uma planilha do Google docs. A ideia é ler a descrição do item e seu respectivo valor
e jogar isso pra uma planilha onde será possível manipular esse dados.

# Instalação e Configuração

Para instalar as dependências do projeto basta executar o seguinte comando:

`$ pip install -r requirements.txt`

É necessário também configurar duas variáveis no script, _sheetId_ e _googleDocsAcessKey_.

<h1>
  <img alt="img_codigo" title="img_codigo" src="/img/img_codigo.png">  
</h1>

A variável _sheetId_ pode ser obtida a partir da url da planilha do google docs:

<h1>
  <img alt="img_planilha" title="img_planilha" src="/img/img_url_planilha.png">  
</h1>

Ja o _googleDocsAcessKey_ é o caminho do arquivo que serve como acesso a api de comunicação com o google docs . Por ser um pouco mais extenso fica um video que ensina como obter o arquivo.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/w533wJuilao/0.jpg)](https://www.youtube.com/watch?v=w533wJuilao)

Após baixá-lo basta colocá-lo na pasta do projeto e adicionar seu nome a variável. Com a configuração pronta agora basta lançar os dados das notas fiscais na sua planilha.

# Funcionamento

Para que seja possível ler os dados das suas notas fiscais, basta obter as urls das notas fiscais eletrônicas. Essa url pode ser obtida no QR Code que vem impresso na nota fiscal física:

<h1>
  <img alt="img_nota_fiscal" title="img_nota_fiscal" src="/img/img_nota_fiscal.png">  
</h1>

Ao ler essa nota fiscal você obtem essa url. Em posse desa url basta colocá-las no arquivo `notas.txt` e executar o script da seguinte maneira:

`$ python3 sheetWriter.py`

Ao executar o script a sua planilha será atualizada com os dados da nota fiscal.

<h1>
  <img alt="img_planilha_preenchida" title="img_planilha_preenchida" src="/img/img_planilha_preenchida.png">  
</h1>
