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

## Versão 0.1.0 (atual)

| Tela | Comportamento |
| --- | --- |
| Hoje | Título e aviso "Em construção". Cartão com a prévia das cores dos macros (calorias, proteína, carboidrato e gordura) que os anéis e gráficos vão usar. É a tela que abre primeiro |
| Registrar | Título e aviso "Em construção" |
| Histórico | Título e aviso "Em construção" |
| Ajustes | Aparência (Automático, Claro ou Escuro; o automático segue o tema do celular, e a escolha fica salva no aparelho); aviso "Em construção" para o que vem depois; seção "Sobre o app" com o número da versão e o botão "Procurar nova versão"; rodapé com a versão e o crédito "Dados nutricionais: Tabela TACO – NEPA/Unicamp" |

| Área | Comportamento |
| --- | --- |
| Navegação | Barra fixa embaixo com as 4 telas. O título no topo muda conforme a tela |
| Visual | Estilo dashboard, com cartões arredondados. Tema escuro e claro. Cada macro tem uma cor fixa (calorias verde, proteína azul, carboidrato âmbar, gordura rosa), definida num lugar só no `index.html` |
| Celular | Pensado para 390 × 844. Respeita o entalhe e a barra de gestos do iPhone. Pode ser instalado na tela inicial (nome "Macros") |
| Dados salvos | Só a escolha do tema, em `macrotimeline.v1`, no formato `{ "schema": 1, "settings": { "theme": "auto" } }`. Ao salvar, o app mantém o que já existir na chave |
| Versão nova | Ao abrir o app e ao voltar para ele (no máximo a cada 10 min), o app lê a página publicada, sem usar a memória do navegador, e compara o número da versão. Se houver versão mais nova, mostra no topo "Nova versão disponível" com o botão "Atualizar", que recarrega a página nova. Não mexe nos dados salvos. O número fica na constante `APP_VERSION` do `index.html` e precisa mudar a cada versão |

## Limitações conhecidas

- **No iPhone, use o app instalado na Tela de Início.** No Safari comum, o iPhone pode apagar os dados do site depois de 7 dias sem uso.
- Cada aparelho guarda os próprios dados; não há sincronização entre aparelhos.
- O aviso de versão nova só funciona com internet e com o app aberto pelo endereço publicado (não quando o arquivo é aberto direto do computador).
- No app instalado no Android, a tela de abertura usa sempre a cor escura do `manifest.json`, mesmo no tema claro, porque o manifesto aceita uma cor só.

## Fonte de dados

- **Tabela TACO** – Tabela Brasileira de Composição de Alimentos, 4ª edição, NEPA/Unicamp (Núcleo de Estudos e Pesquisas em Alimentação da Universidade Estadual de Campinas). O crédito "Dados nutricionais: Tabela TACO – NEPA/Unicamp" aparece no rodapé de Ajustes. A tabela entra no app numa próxima etapa.
- **Alimentos do usuário**: alimentos que a própria pessoa cadastra, salvos só no aparelho. Entram numa próxima etapa.

## Próximas evoluções

Etapas restantes da v1: dados salvos, tabela de alimentos, registro de refeições, metas, histórico e exportação em CSV.

Depois da v1:
- Registro por foto com IA.
- Gravação direta no Google Drive.

## Histórico

| Versão | Data | Mudança |
| --- | --- | --- |
| 0.1.0 | 07/11/2026 | Esqueleto: 4 telas vazias com navegação, tema claro/escuro/automático, aviso de versão nova, crédito à TACO, instalação na tela inicial |
