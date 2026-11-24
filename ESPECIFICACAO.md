# Especificação: MacroTimeline

Documento de referência do app. Toda evolução deve seguir as regras abaixo e atualizar este arquivo quando o comportamento do app mudar.

## Objetivo

App pessoal para celular que registra a alimentação do dia com foco em macros: calorias, proteína, carboidrato e gordura. O registro é feito por texto, usando a Tabela TACO e alimentos cadastrados pelo próprio usuário.

É usado por duas pessoas: uma no Android (Chrome) e outra no iPhone (Safari, app instalado na Tela de Início). Cada pessoa tem os próprios dados no próprio aparelho.

## Regras que não podem ser quebradas

1. **Nenhum dado pessoal no repositório.** Refeições, fotos, metas, peso, medidas, chaves de API, endereço ou ID de planilha ficam apenas no `localStorage` do aparelho, na chave `macrotimeline.v1`. Nada disso pode aparecer no código, em arquivos de exemplo ou em mensagens de commit.
2. **Chaves de API nunca saem do aparelho**: não vão para o repositório nem para o backup exportado.
3. **Não quebrar dados já salvos.** Se o formato salvo mudar, os dados antigos são migrados, nunca descartados.
4. **Página estática, publicada no GitHub Pages** a partir da branch `main`, sem etapa de build e sem servidor próprio.
5. **Sem bibliotecas externas**, a não ser que o dono peça.
6. **Interface em português do Brasil**, com números no formato brasileiro (vírgula decimal), gramas e kcal.
7. **Crédito à Tabela TACO (NEPA/Unicamp) sempre visível** no app.

## Versão 0.3.0 (atual)

| Tela | Comportamento |
| --- | --- |
| Hoje | Título e aviso "Em construção". Lembrete discreto de backup no topo, com o botão "Exportar backup", quando passa de 7 dias sem backup (ver "Seus dados"). Cartão com a prévia das cores dos macros (calorias, proteína, carboidrato e gordura) que os anéis e gráficos vão usar. É a tela que abre primeiro |
| Registrar | Cartão "Alimentos" com a busca na Tabela TACO e nos alimentos próprios, o botão "+ Meu alimento" e o crédito à TACO; abaixo, aviso "Em construção" para o registro de refeições (ver "Alimentos") |
| Histórico | Título e aviso "Em construção" |
| Ajustes | Aparência (Automático, Claro ou Escuro; o automático segue o tema do celular, e a escolha fica salva no aparelho); aviso "Em construção" para metas e exportação em CSV; seção "Seus dados" (ver abaixo); seção "Sobre o app" com o número da versão e o botão "Procurar nova versão"; rodapé com a versão e o crédito "Dados nutricionais: Tabela TACO – NEPA/Unicamp" |

| Área | Comportamento |
| --- | --- |
| Navegação | Barra fixa embaixo com as 4 telas. O título no topo muda conforme a tela |
| Visual | Estilo dashboard, com cartões arredondados. Tema escuro e claro. Cada macro tem uma cor fixa (calorias verde, proteína azul, carboidrato âmbar, gordura rosa), definida num lugar só no `index.html` |
| Celular | Pensado para 390 × 844. Respeita o entalhe e a barra de gestos do iPhone. Pode ser instalado na tela inicial (nome "Macros") |
| Dados salvos | Tudo em `macrotimeline.v1`, no formato descrito em "Formato dos dados salvos". Quem vinha da versão 0.1.0 tem os dados migrados automaticamente e mantém o tema |
| Seus dados: exportar backup | Gera o arquivo `macrotimeline-backup-AAAA-MM-DD.json` (data do dia). No Android, baixa direto. No iPhone, abre a folha de compartilhamento, onde se escolhe "Salvar em Arquivos". O backup nunca inclui chaves de API nem as informações do aparelho |
| Seus dados: importar backup | Escolhe um arquivo `.json`. O app confere se é um backup do MacroTimeline e se não é de uma versão mais nova do app. Mostra um resumo (data do backup, dias com refeições, alimentos próprios, registros de peso e tema) e pede confirmação antes de substituir os dados. Arquivo inválido mostra uma mensagem e não altera nada. As chaves de API e a data do último backup do aparelho são mantidas |
| Seus dados: apagar todos os dados | Confirmação dupla: aviso e depois digitar "APAGAR". Apaga tudo, inclusive tema e chaves de API; o app volta ao padrão |
| Seus dados: lembrete | Mostra a data do último backup exportado. Quando há dados além do tema e passam mais de 7 dias sem backup (ou 7 dias de uso sem nenhum backup), aparece um lembrete discreto em Ajustes e no topo da tela Hoje |
| Alimentos: busca | Digitar parte do nome procura na TACO e nos alimentos próprios ao mesmo tempo. Não precisa de acento nem maiúscula, e cada palavra digitada só precisa aparecer em algum lugar do nome ("frango grel" acha "Frango, peito, sem pele, grelhado"; "feijao" acha "Feijão"). Resultados em ordem alfabética, no máximo 50; se houver mais, o app pede para refinar a busca. Cada resultado mostra kcal, proteína (P), carboidrato (C), gordura (G) e fibra por 100 g, com vírgula decimal. Os da TACO mostram o número e o grupo da tabela; os próprios levam a etiqueta "meu alimento". Valor sem dado aparece como "—"; alimento sem nenhum dado mostra "Sem dados na TACO". Com a busca vazia, aparece a lista dos alimentos próprios |
| Alimentos: meu alimento | "+ Meu alimento" abre o cadastro: nome, porção do rótulo em gramas (ex.: 30 g) e kcal, proteína, carboidrato e gordura dessa porção (obrigatórios; 0 se o rótulo disser zero), mais fibra (opcional; vazia = sem dado). Aceita vírgula ou ponto. Enquanto digita, mostra o resultado por 100 g. Recusa porção vazia ou acima de 5.000 g, números inválidos e proteína + carboidrato + gordura acima do peso da porção. Tocar num alimento próprio abre a edição, com o botão "Apagar" (pede confirmação) |
| Alimentos: carregamento | A TACO fica no arquivo `dados/taco.json`, carregado ao abrir o app. Se não carregar (sem internet na primeira vez), a busca avisa e tenta de novo ao abrir a tela Registrar. Os alimentos próprios funcionam mesmo sem a TACO |
| Versão nova | Ao abrir o app e ao voltar para ele (no máximo a cada 10 min), o app lê a página publicada, sem usar a memória do navegador, e compara o número da versão. Se houver versão mais nova, mostra no topo "Nova versão disponível" com o botão "Atualizar", que recarrega a página nova. Não mexe nos dados salvos. O número fica na constante `APP_VERSION` do `index.html` e precisa mudar a cada versão |

## Formato dos dados salvos

Chave `macrotimeline.v1` do `localStorage`, com um objeto JSON:

```
{
  "schema": 2,                         // número do formato; sobe quando o formato muda
  "settings":    { "theme": "auto" },  // ajustes: tema "auto", "light" ou "dark"
  "profile":     {},                   // perfil (próximas etapas)
  "goals":       {},                   // metas de calorias e macros (próximas etapas)
  "customFoods": [],                   // alimentos cadastrados pela pessoa (ver abaixo)
  "days":        {},                   // refeições por dia: { "AAAA-MM-DD": { "meals": [] } }
  "weights":     [],                   // registros de peso (próximas etapas)
  "secrets":     {},                   // chaves de API: nunca entram no backup
  "device":      { "createdAt": "...", "lastBackupAt": null }  // só deste aparelho: não entra no backup
}
```

- **Migração:** ao abrir, o app leva dados de formatos antigos para o atual sem descartar nada (`schema` 1, da versão 0.1.0, vira 2 mantendo o tema). Cada nova mudança de formato ganha um passo na função `migrate` do `index.html`.
- **Alimento próprio** (cada item de `customFoods`, desde a versão 0.3.0, sem mudar o `schema`, porque a lista estava sempre vazia antes):
  ```
  { "id": "f...", "nome": "...", "porcaoG": 30,
    "rotulo": { "kcal": 120, "prot": 24, "carb": 2.5, "gord": 1.5, "fibra": null },  // como digitado, para a porção
    "por100": { "kcal": 400, "prot": 80, "carb": 8.33, "gord": 5, "fibra": null },   // convertido para 100 g (2 casas)
    "criadoEm": "...", "alteradoEm": "..." }
  ```
  `null` = sem dado. Itens sem `id` ganham um ao abrir; itens que não têm `nome` e `por100` são mantidos, mas não aparecem na busca.
- Se o aparelho tiver dados de um formato mais novo do que o app entende, o app não grava por cima e pede para atualizar.
- **Arquivo de backup:** `{ "app": "MacroTimeline", "kind": "backup", "exportedAt": "...", "appVersion": "...", "data": { ... } }`. `data` leva só `schema`, `settings`, `profile`, `goals`, `customFoods`, `days` e `weights` (lista fixa no código); campos de ajustes com nome de chave, token ou senha também são removidos.

## Limitações conhecidas

- **No iPhone, use o app instalado na Tela de Início.** No Safari comum, o iPhone pode apagar os dados do site depois de 7 dias sem uso.
- Cada aparelho guarda os próprios dados; não há sincronização entre aparelhos. O backup é a forma de guardar uma cópia ou passar os dados para outro aparelho.
- O app não tem como saber se o arquivo de backup foi mesmo guardado: no Android, a data do último backup é registrada quando o download começa; no iPhone, quando a folha de compartilhamento termina sem ser cancelada.
- A Tabela TACO precisa de internet na primeira vez que o app abre depois de instalado ou atualizado; depois o navegador costuma guardar uma cópia. Ela também não carrega quando o arquivo é aberto direto do computador (sem o endereço publicado).
- O aviso de versão nova só funciona com internet e com o app aberto pelo endereço publicado (não quando o arquivo é aberto direto do computador).
- No app instalado no Android, a tela de abertura usa sempre a cor escura do `manifest.json`, mesmo no tema claro, porque o manifesto aceita uma cor só.

## Fonte de dados

- **Tabela TACO** – Tabela Brasileira de Composição de Alimentos, 4ª edição revisada e ampliada, NEPA/Unicamp (Núcleo de Estudos e Pesquisas em Alimentação da Universidade Estadual de Campinas), 2011. O crédito "Dados nutricionais: Tabela TACO – NEPA/Unicamp" aparece no rodapé de Ajustes e embaixo da busca de alimentos.
  - **Arquivo de origem:** PDF oficial `taco_4_edicao_ampliada_e_revisada.pdf`, baixado em 18/11/2026 de `https://www.nepa.unicamp.br/wp-content/uploads/sites/27/2023/10/taco_4_edicao_ampliada_e_revisada.pdf` (164 páginas, 744.346 bytes, SHA-256 `2002aec5615b5b1395aaa8fa675635bbb7f712c33f278af5e332f1cac8f108c8`). O PDF não fica no repositório.
  - **Como foi gerado:** `ferramentas/gerar_taco.py` lê o texto da Tabela 1 (composição centesimal por 100 g de parte comestível) e grava `dados/taco.json`. Nenhum número foi digitado à mão. Entram os 597 alimentos (nº 1 a 597), com número, nome, grupo, energia (kcal), proteína, carboidrato, lipídios (gordura) e fibra alimentar. Nas 19 linhas com células vazias no PDF, cada valor é posto na coluna certa pela posição na página, e essas linhas foram conferidas uma a uma. Números de nota de rodapé no fim do nome foram retirados ("Cana, aguardente", "Cerveja, pilsen").
  - **Regras:** "Tr" (traço) = 0. "NA" (não aplicável), "\*" ("análises sendo reavaliadas") ou célula vazia = sem dado (`null`), nunca zero. Ficam inteiramente sem dados: leite de vaca integral (458), leite de vaca desnatado UHT (457), iogurte sabor abacaxi (450), coco verde cru (591), sal dietético (516) e sal grosso (517).
  - **Observação:** na TACO, o carboidrato inclui a fibra alimentar (carboidrato total).
  - **Conferência** contra o PDF oficial (Tabela 1, por 100 g):

    | Nº | Alimento | kcal | Proteína | Carboidrato | Gordura | Fibra | Página do PDF |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 3 | Arroz, tipo 1, cozido | 128 | 2,5 | 28,1 | 0,2 | 1,6 | 29 |
    | 561 | Feijão, carioca, cozido | 76 | 4,8 | 13,6 | 0,5 | 8,5 | 65 |
    | 488 | Ovo, de galinha, inteiro, cozido/10minutos | 146 | 13,3 | 0,6 | 9,5 | sem dado (NA) | 59 |
    | 410 | Frango, peito, sem pele, grelhado | 159 | 32,0 | 0,0 | 2,5 | sem dado (NA) | 55 |
    | 182 | Banana, prata, crua | 98 | 1,3 | 26,0 | 0,1 | 2,0 | 39 |

    Também foi conferido que a energia bate, de forma aproximada, com proteína, carboidrato e gordura em todos os alimentos; as poucas diferenças (bebidas alcoólicas, fermento químico, coentro desidratado, feijão tropeiro) estão assim no próprio PDF.
- **Alimentos do usuário**: alimentos que a própria pessoa cadastra pelo rótulo, salvos só no aparelho (em `customFoods`) e incluídos no backup.

## Próximas evoluções

Etapas restantes da v1: registro de refeições (escolher o alimento e informar os gramas), metas, histórico e exportação em CSV.

Depois da v1:
- Registro por foto com IA.
- Gravação direta no Google Drive.

## Histórico

| Versão | Data | Mudança |
| --- | --- | --- |
| 0.1.0 | 07/11/2026 | Esqueleto: 4 telas vazias com navegação, tema claro/escuro/automático, aviso de versão nova, crédito à TACO, instalação na tela inicial |
| 0.2.0 | 11/11/2026 | Base de dados no aparelho (formato versão 2, com espaços para perfil, metas, alimentos próprios, refeições e peso) e migração do tema já salvo; seção "Seus dados" em Ajustes com exportar e importar backup, apagar todos os dados e lembrete de backup após 7 dias |
| 0.3.0 | 24/11/2026 | Lista de alimentos: Tabela TACO 4ª edição (597 alimentos, em `dados/taco.json`, gerada do PDF oficial do NEPA/Unicamp) e cadastro de alimentos próprios pelo rótulo (convertidos para 100 g, com edição e exclusão, incluídos no backup); busca na tela Registrar sem precisar de acento ou maiúscula, em ordem alfabética, até 50 resultados |
