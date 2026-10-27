# 02 · Direção de arte

**Status: fechada em 27/10/2026 e construída.** A direção escolhida foi dealt
pela skill `design-taste-frontend`, não inventada.

| | |
|---|---|
| Direção | **The dark room** — um campo escuro de cima a baixo e, dentro dele, objetos iluminados |
| Seed | `1099997846` · setor `architecture` · tom `technical` |
| Redraws | **1** — a tipografia. O par dealt (Bodoni Moda / Jost) é um didone de revista de moda; a própria folha diz que serve a "luxury property, jewellery, fragrance and fashion". Numa página de manutenção industrial contradiz o tom técnico do brief. Redealt: **Clash Grotesk** |
| Cor | **mantida da marca** (`--keep palette`) |
| Tipografia | Clash Grotesk 400/500, auto-hospedada, 39 KB, acentos conferidos |
| Seções | abertura (duas portas) → serviços (colunas de nomes) → sistemas (foto fixa, lista ativa) → consequência (escada) → empresa (painel, retrato recortado) → credenciamentos (nomes como frase) → contato (cartão sobre foto) → rodapé |

### A ideia

> Nesta página, **os nove sistemas que a Connect-Air mantém funcionando** viram
> **os objetos iluminados na sala escura**.

Todo concorrente diz "soluções em climatização". A Connect-Air pode dizer as
nove máquinas pelo nome: VRV, VRF, Mini VRF, Self-contained, Chiller, Fancoil,
Splitão, Split Inverter, Multi Split Inverter. Para quem especifica, esse
vocabulário é prova.

### A coisa viva

A lista de sistemas. Apontar, focar ou tocar um nome troca a fotografia fixa ao
lado, abre a descrição daquele equipamento e **leva o nome do sistema para
dentro da mensagem do WhatsApp**. Conteúdo real, funciona no polegar, e sem
JavaScript a lista aparece inteira e aberta.

### O retrato recortado

A seção da empresa usa `clip-path: circle()` na fotografia: a esfera do símbolo
da marca vira a máscara. É o único lugar onde a geometria do logotipo aparece
sem ser o logotipo.

---

## Histórico da decisão

O que segue registra como se chegou aqui.

---

## 1. O problema de design

Climatização B2B é um mercado onde praticamente todo site parece o mesmo:
stock photo de split branco em parede branca, azul-ciano em degradê, três
cartões com ícone de floco de neve, "qualidade e compromisso". O visitante não
distingue uma empresa da outra — e, não distinguindo, decide por preço.

A Connect-Air chega com três ativos que a maioria dos concorrentes não tem:

1. **Um símbolo de verdade.** A esfera com fluxos recortados é uma marca
   desenhada, não um clipart. Em vetor limpo, 1,3 KB. Dá para usá-la grande.
2. **Dois azuis com distância real entre si.** `#021D64` e `#0267DB` não são
   duas variações do mesmo tom — um é quase preto-azulado, o outro é saturado e
   elétrico. Isso permite contraste dramático sem introduzir cor nova.
3. **Vocabulário técnico.** Chiller, fancoil, VRF, splitão, PMOC. Para quem
   especifica, essas palavras são prova. A maioria dos concorrentes esconde
   isso atrás de "soluções em climatização".

**A direção tem que fazer a página parecer competência de engenharia, não
simpatia de prestador de serviço.** O público é comércio e indústria: síndico
de prédio comercial, gerente de facilities, engenheiro de manutenção. Essa
pessoa não quer conforto — quer não ser incomodada e não ser multada.

## 2. O que já está decidido pelo contrato

Antes de qualquer discussão estética, estas são restrições, não opiniões:

| Restrição | Origem |
|---|---|
| HTML/CSS/JS estático, sem framework, sem biblioteca pesada | Escopo § 04 |
| Até 2 famílias tipográficas, auto-hospedadas | Escopo § 04 |
| Animações — *discretas* por contrato, **ampliadas por cortesia declarada** em 27/10. Vídeo de abertura continua fora | Contrato § 1.3 · Escopo § 07 · [`00`](00-DIAGNOSTICO.md) § 2 |
| Identidade atual do cliente — sem criar logo ou identidade | Contrato § 3 |
| Fotos: só as que o cliente enviar | Contrato § 3 |
| 7 seções, nesta ordem | Escopo § 02 |
| Contraste mínimo AA | Escopo § 04 |

🔴 **A última restrição é a que mais pesa, e está confirmada:** não há uma
única foto, e o Drive do cliente já foi verificado e esgotado. Ver
[`00-DIAGNOSTICO.md`](00-DIAGNOSTICO.md) § 5.

Isso **reforça a recomendação pela direção B** (§ 3): fundo escuro e geometria
do símbolo como sistema visual é a única das três que sustenta uma página
inteira com pouca ou nenhuma fotografia.

## 3. Três direções candidatas

Nenhuma delas pede vídeo de abertura. Todas cabem em 600 KB. Com a cortesia
declarada (27/10), as três podem usar animação de entrada e transições
refinadas — o teto de performance continua valendo.

### A · **Projeto executivo**
> A página como documento técnico bem desenhado.

Fundo claro, quase branco-papel. Tipografia de engenharia: uma grotesca de
largura estreita para títulos, com números tabulares. Grade visível — linhas
finas de 1 px em `#021D64` a 12 % separando seções, como folha de projeto.
Dados de equipamento apresentados em tabela, não em cartão. O azul elétrico
`#0267DB` entra só em elementos acionáveis e em números.

**Por que funciona:** fala a língua de quem compra. Engenheiro confia em quem
organiza informação como ele organiza.
**Risco:** pode ficar frio se a copy não tiver números — e hoje ela não tem.

### B · **Pressão e fluxo**
> O símbolo da marca vira o sistema visual.

Fundo escuro `#021D64` dominante. Os três fluxos recortados da esfera saem do
logo e viram elemento estrutural: curvas finas em `#0267DB` que atravessam
divisões de seção e emolduram as fotos. Tipografia grande, pouco texto por
tela, muito respiro. Fotos em recorte largo, tratadas com leve dominante azul
para unificar material de qualidade irregular.

**Por que funciona:** é a única direção que usa um ativo que só a Connect-Air
tem. Fundo escuro também é o melhor cenário quando as fotos são poucas — menos
área exposta.
**Risco:** depende das curvas serem executadas com precisão. Curva mal
desenhada em fundo escuro fica amadora na hora.

### C · **Norma e selo**
> Conformidade como argumento central.

Construída em torno da obrigação legal de manutenção. Hierarquia tipográfica
severa, muito espaço em branco, blocos de texto estreitos. CFT/CRT, PMOC e
NR10/NR35 tratados como selos — não escondidos num rodapé, mas apresentados
como a razão de contratar. Cor usada com parcimônia extrema: `#021D64` para
tudo, `#0267DB` só no CTA.

**Por que funciona:** ataca direto o medo do comprador B2B (multa, interdição,
responsabilidade) em vez do desejo (conforto).
**Risco:** ⚠️ **bloqueada até a referência legal chegar.** Construir a página
inteira sobre uma lei que ainda não foi confirmada pelo cliente é
irresponsável. Ver [`01-BRIEFING.md`](01-BRIEFING.md) § 6.

---

### Recomendação

**B · Pressão e fluxo**, com a disciplina informacional de A nas seções de
serviços e equipamentos.

Três razões: usa o único ativo visual exclusivo da marca; fundo escuro é a
estratégia mais segura diante da escassez de fotos; e o contraste entre os dois
azuis da marca entrega impacto sem introduzir cor nova — o que mantém a
identidade do cliente intacta, como o contrato exige.

## 4. Referências — pendente

🔴 **Nenhuma referência real foi coletada ainda.** O Mobbin, que seria a fonte
natural, **exige plano pago** e retornou erro (ver
[`00-DIAGNOSTICO.md`](00-DIAGNOSTICO.md) § 1).

Plano alternativo, a executar na próxima etapa:

1. **Captura de concorrentes reais** com o Playwright MCP — climatização
   corporativa no Brasil e HVAC comercial nos EUA/Europa, para mapear o lugar-
   comum e saber do que fugir.
2. **Referências fora do setor** — engenharia industrial, equipamento técnico,
   infraestrutura. É onde está o vocabulário visual de competência.
3. **A skill `design-taste-frontend`**, que traz direções pesquisadas a partir
   de uma curadoria de sites premiados, substitui parcialmente o Mobbin.
4. A captura do **Wave of Unboxing** guardada em `Connect-Air/` entra como
   referência de acabamento — não de conteúdo nem de peso.

Entregável desta etapa: um painel com 12 a 18 capturas reais, anotadas com o
que se aproveita de cada uma. Registro em
[`reference/REFERENCIAS.md`](../reference/REFERENCIAS.md).

## 5. Tipografia — a decidir

Duas famílias, auto-hospedadas, `woff2`, subset `latin-ext` (a copy tem
*ç*, *ã*, *ê*, *é*). Candidatas por direção:

| Direção | Títulos | Texto |
|---|---|---|
| A | uma grotesca condensada de engenharia | humanista neutra, números tabulares |
| B | uma geométrica de peso alto, caixa alta nos títulos | a mesma família em peso regular |
| C | uma serifada de documento | grotesca neutra |

Decisão só depois da direção aprovada. Máximo 4 arquivos, 120 KB somados.

## 6. Checklist antes de escrever a primeira linha de CSS

- [ ] Direção escolhida e aprovada pelo cliente
- [ ] Painel de referências montado e anotado
- [ ] Fotos recebidas — ou plano B de imagem aprovado
- [ ] Copy aprovada ([`03-COPY.md`](03-COPY.md)) — é entregável contratual e precede o código
- [ ] Famílias tipográficas escolhidas e licença verificada
- [ ] Lockup horizontal reconstruído em SVG ≤ 8 KB
