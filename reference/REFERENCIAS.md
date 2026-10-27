# Referências de direção de arte

**Regra:** este diretório guarda **anotações e capturas leves**, nunca binários
pesados. Teto: **20 arquivos / 2 MB**. Estado atual: **5 arquivos / 528 KB**.
Nada daqui entra no build.

Capturas feitas em 27/10/2026 com Playwright MCP, viewport 1440 × 900,
reduzidas para 1100 px e JPEG q78.

---

## 1. O clichê da categoria — do que fugir

### `05-arclima.jpeg` — Arclima Engenharia
O retrato completo do lugar-comum. **Ciano saturado** (~`#00A0E9`) em barra
superior cheia, botões em pílula, **divisórias em onda**, três cartões
genéricos com borda azul, WhatsApp verde flutuante.

**O problema não é o gosto, é a ausência de argumento:** a página abre sem
nenhum título. Não há proposta de valor, não há frase que diga o que a empresa
faz melhor que a vizinha. O primeiro texto que o visitante lê é "Onde estamos?".

> **Para a Connect-Air:** nada de ciano, nada de onda, nada de pílula. E a
> abertura precisa de uma afirmação, não de um menu.

### `02-daikin.jpeg` — Daikin Brasil
Fabricante, público final. Carrossel com mascote, prêmio ReclameAQUI, degradê
azul-ciano, **banner de cookies cobrindo o próprio título**.

Dois aprendizados por oposição: o carrossel enterra a mensagem principal (o
texto do slide 1 está cortado pelo aviso de privacidade), e o banner de cookies
existe porque há rastreio. **A Connect-Air não terá formulário nem rastreio, e
portanto não terá aviso de cookies** (escopo § 05) — uma tela limpa de saída.

---

## 2. O concorrente que acerta — e o que o separa dos outros

### `01-maneng.jpeg` — Maneng
O melhor da categoria entre os capturados, e por uma razão só: **fotografia
real de equipamento industrial**. Chiller, dutos, tubulação — o visitante vê
porte de operação antes de ler qualquer coisa.

Azul-marinho escuro no topo, laranja só no CTA e no número. Título
`+20 Anos de experiência e clientes satisfeitos`, com o número em cor de
destaque.

**O que aproveitar:** o fundo escuro funciona nesta categoria; o número grande
e colorido dentro do título funciona; a foto de máquina vale mais que qualquer
adjetivo.

**O que não aproveitar:** o título ainda é sobre a empresa ("nossa
experiência"), não sobre o problema do cliente. E "+20 Anos" é o clichê de
abertura do setor — a Connect-Air tem 15 e perderia essa disputa. **Melhor não
entrar nela.**

> ⚠️ Esta captura é a prova mais direta do § 5 do diagnóstico: o que separa a
> Maneng dos outros é exatamente o ativo que a Connect-Air não tem — foto.

---

## 3. O padrão a perseguir

### `03-ykp.jpeg` — YKP Consultoria ★ referência principal
**O próprio cliente já apontou para este site** — a captura
`ideia_avaliacao_google.png` que ele enviou é a seção de avaliações desta
página. Isso é um sinal de alinhamento de gosto que não se deve desperdiçar.

Anatomia da abertura, toda adaptável:

| Elemento | Como está | Tradução para a Connect-Air |
|---|---|---|
| Sobrancelha | `— GESTÃO FISCAL E TRIBUTÁRIA` em caixa alta, com traço | `— CLIMATIZAÇÃO COMERCIAL E INDUSTRIAL` |
| Data | `DESDE 1990` em cinza, pequeno, acima do título | `DESDE 2011` ou `15 ANOS` |
| Título bicolor | Duas linhas escuras + duas em azul de marca | `#021D64` + `#0267DB` — a marca **já tem** os dois tons |
| Dois CTAs | Preenchido + contorno | `Falar no WhatsApp` + `Ver serviços` (exatamente o que o escopo § 03 pede) |
| Fileira de tags | 4 áreas com marcador | VRF · Chiller · Fancoil · PMOC |
| Divisão | Texto à esquerda, foto à direita sangrando | Mesma estrutura — **e usa só uma foto** |

> **O achado útil:** este layout resolve a abertura com **uma única
> fotografia**. Diante da escassez do § 5, isso vale mais que estética.

### `04-trane.jpeg` — Trane Commercial
O topo do mercado global de HVAC. Foto arquitetônica em tela cheia, tipografia
enorme e leve, **um único CTA**, cartões invadindo a borda inferior do hero.

O detalhe que mais importa: **a Trane não fotografa máquina, fotografa
edifício.** O argumento não é o equipamento, é o lugar que ele serve.

> **Consequência prática para o § 5:** se o Márcio não conseguir fotos boas de
> equipamento, **fotos de ambiente climatizado pronto** — loja, restaurante,
> galpão, hall — são mais fáceis de obter e seguem a estratégia da Trane. Isso
> amplia bastante a chance de resolver o bloqueio.

---

## 4. Síntese — o que entra na direção

| Decisão | Vindo de |
|---|---|
| **Fundo escuro**, `#021D64` dominante | Maneng (funciona na categoria) + resolve escassez de foto |
| **Título bicolor** nos dois azuis da marca | YKP |
| **Sobrancelha + marcador de tempo** acima do título | YKP |
| **Dois CTAs** — WhatsApp preenchido, serviços em contorno | YKP + escopo § 03 |
| **Fileira de tags técnicas** (VRF · Chiller · Fancoil · PMOC) | YKP, com o vocabulário do briefing § 3 |
| **Uma foto grande sangrando**, não galeria | YKP + orçamento de performance |
| **Fotografia de ambiente**, não só de máquina | Trane — e é o plano B do § 5 |
| Sem ciano, sem onda, sem pílula, sem carrossel | Arclima e Daikin, por oposição |

Isso confirma a recomendação pela **direção B · Pressão e fluxo**
([`../docs/02-DIRECAO-DE-ARTE.md`](../docs/02-DIRECAO-DE-ARTE.md) § 3), com a
disciplina informacional da direção A nas seções de serviços e equipamentos.

## 5. Ainda a coletar

- [ ] 2 ou 3 referências fora do setor (engenharia industrial, infraestrutura)
      para o tratamento das seções de credenciamento e norma
- [ ] Rodar a skill `design-taste-frontend` como substituta do Mobbin
      (indisponível — exige plano pago)
