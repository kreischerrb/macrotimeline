# Instruções para o Claude neste repositório

## Contexto
- App pessoal "MacroTimeline", para registrar a alimentação do dia com foco em macros (proteína, carboidrato, gordura e calorias), por texto (foto com IA numa versão futura). Publicado no GitHub Pages a partir da branch `main`.
- Usado por duas pessoas: uma no Android (Chrome) e outra no iPhone (Safari, app instalado na Tela de Início). Cada uma tem os próprios dados no próprio aparelho.
- O dono do repositório não programa e está aprendendo GitHub e Claude Code. Explique as mudanças em português simples, sem jargão desnecessário.
- Leia `ESPECIFICACAO.md` antes de qualquer mudança. As regras de lá valem sobre qualquer pedido.

## Regras obrigatórias
- **Nunca escreva dados pessoais no código**: refeições, fotos, metas, peso, medidas, chaves de API, endereço ou ID da planilha. Esses dados ficam só no localStorage do aparelho (chave `macrotimeline.v1`). A planilha recebe apenas o CSV que a própria pessoa exporta.
- **Chaves de API nunca vão para o repositório** nem para o backup exportado. Ficam só no aparelho, digitadas em Ajustes.
- **Não quebre dados já salvos.** Se mudar o formato salvo, migre os dados antigos em vez de descartá-los.
- Mantenha o app como página estática, sem etapa de build e sem servidor próprio.
- Interface em português do Brasil; números no formato brasileiro (vírgula decimal), gramas e kcal.
- Não adicione bibliotecas externas sem o dono pedir.
- Mantenha visível no app o crédito à Tabela TACO (NEPA/Unicamp).

## Como trabalhar
- Faça mudanças pequenas, uma por vez, em uma branch, e abra um Pull Request para o dono revisar antes do merge.
- Na descrição do PR, diga em linguagem simples o que mudou, como testar no celular e se algo depende de chave de API ou de serviço externo.
- Atualize `ESPECIFICACAO.md` (tabela da versão e histórico) quando o comportamento mudar.
- A cada nova versão, mude também a constante `APP_VERSION` no `index.html` para o mesmo número.
- Teste no navegador em tamanho de celular (cerca de 390 × 844) antes de abrir o PR. Considere também o Safari do iPhone, porque uma das pessoas usa iPhone.
