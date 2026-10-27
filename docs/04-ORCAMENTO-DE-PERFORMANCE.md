# 04 · Orçamento de performance

O escopo técnico define o piso contratual. Este documento define o **teto
interno**, que é mais apertado — porque orçamento que se persegue no fim do
projeto nunca é atingido.

## 1. Metas contratuais (§ 04 do escopo técnico)

| Métrica | Compromisso assumido |
|---|---|
| PageSpeed Insights, celular | **≥ 85** |
| LCP (maior elemento visível) | **< 2,5 s** |
| Peso da página inicial | **< 1,5 MB** |
| Breakpoints testados | 360 · 768 · 1024 · 1440 px |
| Navegadores | Chrome, Safari, Edge, Firefox — desktop e mobile |
| Tipografia | até 2 famílias, **auto-hospedadas** |
| Imagens | WebP, carregamento sob demanda, redimensionadas por tela |
| Acessibilidade | contraste mínimo AA, alt text, hierarquia de títulos, navegação por teclado |

## 2. Teto interno por arquivo

Alvo: **≤ 600 KB** no carregamento inicial — 40 % do teto contratual. A folga
existe para absorver as fotos que ainda não chegaram.

| Recurso | Teto | Observação |
|---|---|---|
| `index.html` | 40 KB | sem minificar |
| CSS total | 20 KB | arquivo único, sem framework |
| JS total | 15 KB | sem biblioteca; vanilla |
| Fontes | 120 KB · máx. 4 arquivos | 2 famílias × 2 pesos, `woff2`, subset latin-ext |
| Imagem da abertura | 180 KB | WebP, maior derivada |
| Demais imagens, soma | 200 KB | lazy, abaixo da dobra |
| Logos (marca + parceiros) | 40 KB | SVG quando possível |
| **Total inicial** | **≤ 600 KB** | |

### Regras rígidas

- **Zero dependências de terceiros em runtime.** Sem jQuery, GSAP, AOS,
  Bootstrap, Swiper, Font Awesome, Google Fonts via `<link>`, Google Analytics.
  O escopo vendeu "sem plugin e sem bibliotecas pesadas" e a página não coleta
  dados — adicionar rastreio obriga aviso de cookies (§ 05 do escopo).
- **Ícones em SVG inline.** Dos 7 serviços saem no máximo 7 ícones, desenhados
  como `<symbol>` em um único sprite. Nunca uma biblioteca de ícones.
- **Uma fonte por família por peso.** Se um peso não é usado em duas seções
  distintas, não é carregado.
- **`font-display: swap`** e `preload` apenas da fonte do H1.
- **Nenhuma imagem acima da dobra com `loading="lazy"`.** O LCP não pode ser
  adiado. Tudo abaixo da dobra é `lazy` + `decoding="async"`.
- **`width` e `height` explícitos em toda `<img>`.** CLS alvo: **0**.

## 3. Animação — plano Essencial + cortesia declarada

O plano contratado é o **Essencial**: *"animações discretas"* (contrato § 1.3).
Em 27/10 ficou decidido entregar acabamento acima do contratado **como
cortesia declarada ao cliente** (ver [`00-DIAGNOSTICO.md`](00-DIAGNOSTICO.md) § 2).

Isso **amplia o repertório, não o orçamento**. A regra que manda continua sendo
esta seção: toda animação é composta (`transform` + `opacity`), roda a 60 fps
em celular intermediário e desliga em `prefers-reduced-motion`. Animação que
derruba o PageSpeed abaixo de 85 não entra — a meta é contratual e a cortesia
não é.

Liberado pela cortesia:

- Entrada por seção via `IntersectionObserver`, com escalonamento curto
- Transições refinadas em estado (`hover`, `focus`, `active`)
- Elementos gráficos derivados do símbolo da marca, em SVG inline
- Micro-interações em cartões e CTAs

**Continua fora, mesmo com cortesia** — muda prazo, peso ou manutenção:
vídeo na abertura · parallax · scroll scrubbing · partículas · canvas · cursor
customizado · qualquer biblioteca de animação.

O que já cabia no Essencial, sem custo de performance:

- `transition` em `hover`/`focus` de botões e cartões — 150 a 200 ms
- Um `fade`/`rise` curto de entrada por seção, via `IntersectionObserver`
  (~15 linhas de JS), **apenas composto** (`transform` + `opacity`)
- `scroll-behavior: smooth` nas âncoras do menu
- `prefers-reduced-motion: reduce` desligando tudo acima — obrigatório

O que **não** entra: parallax, scroll scrubbing, vídeo de fundo, partículas,
canvas, texto animado letra a letra, cursor customizado.

> Se a direção de arte aprovada exigir qualquer item do Experience, isso é um
> **aditivo contratual** (contrato, § 24: alterações de objeto, preço ou prazo
> só valem por aditivo escrito e assinado), não uma decisão de implementação.

## 4. Verificação

Antes da entrega, com o Playwright MCP já configurado:

1. Screenshot nos 4 breakpoints — 360 / 768 / 1024 / 1440
2. `performance` + `resource timing` da página publicada
3. PageSpeed Insights mobile da URL real na Hostinger, print anexado ao
   relatório de entrega (escopo § 08, entregável 03)
4. `impeccable detect` na pasta `src/`
5. Teste de teclado: `Tab` percorre menu → botões → links do rodapé, com foco visível
6. Contraste AA conferido em todos os pares texto/fundo

## 5. O erro a não repetir

O projeto anterior (AutosFlow) acumulou milhares de imagens derivadas e
arquivos duplicados. A causa não é falta de cuidado — é falta de **limite
numérico**. Então aqui existe um:

> **Teto absoluto de 25 arquivos de imagem em `src/assets/`.**
> Chegou em 25, alguma coisa sai antes de outra entrar.

A regra de derivação está em
[`docs/05-PIPELINE-DE-ASSETS.md`](05-PIPELINE-DE-ASSETS.md).
