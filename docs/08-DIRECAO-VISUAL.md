# 08 · Direção visual — a recuperação de 06/11/2026

A refatoração de UX da manhã de 06/11 resolveu um problema real (metade do
conteúdo só aparecia no hover, e no celular não aparecia nunca) e criou outro:
para expor tudo, transformou quatro seções seguidas na mesma forma — rótulo à
esquerda, texto à direita, repetido sete, nove e sete vezes. Este documento
registra o diagnóstico, a direção escolhida e a crítica das duas rodadas.

## O diagnóstico, medido

Comparação entre `c59e01d` (antes da refatoração) e o estado da tarde de 06/11,
com `inspect.mjs` nas duas versões:

| | antes | depois da refatoração |
|---|---|---|
| Palavras | 733 | 1 034 |
| Fotografias | 6 | 4 |
| Telas | 9,5 | 11 |
| Fotografia da abertura | 31% da tela | 31% da tela |
| Títulos | 42 | 41 |

Mais texto, menos imagem, página mais longa. Os três problemas, em ordem de
visibilidade:

1. **Quatro das dez seções tinham a mesma forma.** Serviços (7 blocos),
   Sistemas (9 linhas), Por que escolher (7 itens) e as duas portas gêmeas.
   A regra da casa chama isto de "fileiras de cartões idênticos"; a crítica
   chama de "o template aparecendo".
2. **Cinco telas seguidas sem nenhuma fotografia**, de Serviços até Por que
   escolher. As duas fotos em preto e branco tinham saído na troca para cor
   original e ninguém tinha ocupado o lugar delas.
3. **O azul em vinte e tantos lugares.** Dezesseis links "Pedir orçamento" e
   "Falar sobre isso", todos iguais. Um acento que aparece em toda parte não
   diz mais "aqui".

## A direção

`draw.mjs --sector architecture --keep palette,type --tone technical`,
três opções sorteadas, escolhida **`uneven-photographs`** (semente 42705800):
fotografias em tamanhos e alturas diferentes sobre uma grade que se sente, com
texto pequeno entre elas.

Por que esta e não as outras duas:

- **`name-as-monument`** põe a marca em corpo gigante como arquitetura da
  página. O João já tinha pedido para tirar exatamente isso do rodapé.
- **`dark-room`** faz a página inteira num campo escuro. A identidade da
  Connect-Air é papel branco com campos azuis; um fundo escuro do topo ao pé
  trocaria a marca por outra.
- **`uneven-photographs`** ataca os três problemas de uma vez: devolve o papel
  às fotografias, impede que duas seções vizinhas tenham a mesma forma, e tira
  a riqueza da colocação em vez do ornamento.

**Redesenhos declarados.** A prancha sorteou a abertura "Small name, open sky",
em que a única tipografia grande é o nome da empresa. Isso tiraria da primeira
tela a linha que diz o que a empresa faz — que é o `h1` e o que o visitante de
anúncio precisa ler em cinco segundos. Mantida a abertura existente, com a
fotografia crescendo de 31% para 40% da tela. A prancha também sorteou, para
"A empresa", uma seção de retratos de pessoas: a Connect-Air não tem retratos,
e inventar está fora de questão.

**Paleta e tipografia:** `--keep`. Nada mudou. `#021D64`, `#0267DB` e a Clash
Grotesk são a identidade entregue pelo cliente.

## As composições, uma por seção

Nenhuma palavra se repete em seções vizinhas, que é o teste da passada 9:

| Seção | Forma |
|---|---|
| Abertura | manchete à esquerda, fotografia dominante à direita |
| As duas portas | **par desigual**: instalar grande em sete faixas, manter menor em quatro e 120px mais abaixo |
| Serviços | enunciado largo com a primeira linha recuada, índice empurrado para a direita, fotografia fechando a coluna da esquerda |
| Sistemas | **índice tipográfico em três colunas**, sem caixas e sem fios |
| Manutenção e PMOC | campo azul, a fotografia é a única coisa clara |
| A empresa | fotografia alta ocupando a coluna inteira, história e razões à direita |
| Parceiros | fileira de logos e o selo |
| Avaliações | citação grande à esquerda, as outras duas como texto corrido numa coluna estreita |
| Contato | convite e canais à esquerda, formulário à direita |

"Por que escolher a Connect-Air" deixou de ser seção e virou uma coluna dentro
de "A empresa": a mesma informação, uma repetição a menos.

## As seis fotografias

Todas de acervo público, todas coloridas, todas do mundo do ofício. Nenhuma é
apresentada como obra da Connect-Air.

| Arquivo | O que é | Onde | Licença |
|---|---|---|---|
| `casa-de-maquinas` | casa de máquinas com evaporadora e quadro | abertura | CC BY 2.0 · MTA Capital Construction |
| `chiller` | chiller instalado | porta "preciso instalar" | domínio público · P199 |
| `trocador-aberto` | trocador de calor aberto | porta "preciso manter" | CC0 · Rsparks3 |
| `cobre` | linhas de cobre e unidade na laje | serviços | CC BY 2.0 · MTA Capital Construction |
| `supervisao` | mesa de supervisão com o sinótico da planta | manutenção e PMOC | CC0 · Rsparks3 |
| `solda` | técnico soldando numa casa de máquinas | a empresa | CC BY 2.0 · MTA Capital Construction |

**Saiu:** `kitchen-exhaust-fans` — ferrugem e neve. Numa página que vende
manutenção, lê-se como descuido.

**Rejeitadas depois de olhar:** `rooftop-packaged-units` (bege, céu cinzento,
sem assunto) e `hvac-ductwork-in-the-chiller-plant-room` (canteiro de obra com
lona e entulho).

## Crítica, rodada 2 (depois)

```
Visto em um segundo: a casa de máquinas, grande, com a manchete ao lado.
Ideia: a amplitude que o próprio cliente descreve, "da sala ao hospital",
  e as fotografias do mundo onde o equipamento vive, em tamanhos desiguais.
Coisa viva: cada serviço e cada sistema abre o WhatsApp com a mensagem
  daquele assunto já escrita, e com a origem do anúncio. Fraca para o padrão
  do critério, mas é o que o escopo permite.
Palavras por seção: abertura=split-dominante / portas=par-desigual /
  serviços=enunciado+índice / sistemas=colunas / manutenção=campo-escuro+foto /
  empresa=coluna-de-foto+razões / parceiros=logos / avaliações=citação+coluna /
  contato=faixa+formulário.  Nenhuma repetida em vizinhas.
Notas: design 7,5 · usabilidade 8 · criatividade 6,5 · conteúdo 7,5 → 7,4
Tetos aplicados: a ideia funciona para um concorrente (criatividade ≤ 7);
  não há uma "coisa viva" no sentido forte do critério (criatividade ≤ 7,5).
```

**7,4. Abaixo de 7,5, e fica registrado assim.** O que falta não é composição:

1. **As fotografias não são da Connect-Air.** Enquanto forem de acervo, a página
   mostra o ofício e não a obra do Márcio. É o único item que levaria design e
   conteúdo juntos para cima, e depende das fotos dele — ver
   [`07-PEDIDO-DE-FOTOS.md`](07-PEDIDO-DE-FOTOS.md).
2. **Não há imagem em movimento.** Vídeo é recurso do plano Experience, fora
   deste contrato. O aviso `no-footage` do inspetor fica defendido por escopo.
3. **Não há números próprios.** "Mais de 15 anos" é o único. Obras entregues,
   equipamentos sob contrato e tempo de resposta substituiriam os sete adjetivos
   de "Por que escolher" — e nenhum deles pode ser inventado.

## Medições finais

`lint.mjs` 0 FAIL / 0 WARN · `inspect.mjs` 0 FAIL em 1440, 768 e 390, com um
aviso defendido (`no-footage`). Cinco tamanhos de tipo, uma família.
Transbordo 0 em 360, 390, 768, 1024 e 1440. Nenhum alvo de toque abaixo de
24px. Contraste AA em todos os pares medidos (menor: 4,79 no link de pedido).
Página 741 KB, contra o teto contratual de 1,5 MB.
