# 00 · Diagnóstico — Connect-Air Landing Page

Levantamento de 27/10/2026, correspondente à **Etapa 1 do escopo técnico**
(Dias 1–2 · Materiais), cujo critério de aceite é *"lista do que foi recebido e
do que falta"*.

**Veredito: o projeto não pode entrar em desenvolvimento ainda.** Há um
conflito de escopo a resolver e seis materiais obrigatórios em falta — um deles
bloqueante para qualquer direção de arte.

---

## 1. Ferramentas — verificação

| Ferramenta | Estado | Observação |
|---|---|---|
| **Playwright MCP** | ✅ funcionando | Testado com navegação real. Descobriu que `connect-air.com.br` está estacionado na Hostinger (§ 4). Escreve em `.playwright-mcp/` — já adicionado ao `.gitignore`. |
| **Impeccable** | ✅ instalado | v. em `scripts/VERSION`, CLI responde, 40 arquivos de referência, hooks ativos em `SessionStart`/`PostToolUse`/`Stop` com consentimento aceito. |
| **Frontend Design** | ✅ instalado | |
| **Web Design Guidelines** | ✅ instalado | |
| **Vercel React Best Practices** | ⚠️ **instalado, mas inaplicável** | O contrato exige HTML/CSS/JS estático, sem framework (§ 4). Não há React neste projeto. Mantida sem uso. |
| **Mobbin** | 🔴 **indisponível** | `Mobbin MCP requires a paid plan.` Era a fonte natural de referências. Plano alternativo em [`reference/REFERENCIAS.md`](../reference/REFERENCIAS.md) § 2. |
| Geradores de imagem (Artlist, Canva, Higgsfield, Magnific) | ⚪ desconectados | Sem impacto: o contrato proíbe produção de imagem (§ 3) e a disciplina do projeto é **não** gerar derivados. |
| `design-taste-frontend` | ✅ disponível | Substituto parcial do Mobbin. |
| Node 22.16 · npm 10.9 · svgo 4.1 | ✅ | |
| PyMuPDF · python-docx · Pillow | ✅ | Usados para extrair todo o material desta análise. |

**Nota:** o diretório não é um repositório git. Recomendo `git init` antes de
qualquer código — sem histórico, a disciplina antiduplicação depende só de
memória.

## 2. 🔴 Conflito central: o que foi vendido × o que está sendo pedido

Este é o achado mais importante do levantamento.

**O contrato assinado e quitado é do plano `Essencial`, R$ 1.300.** O plano
`Experience`, R$ 2.800, foi apresentado na proposta e **não foi contratado**.

A proposta comercial (p. 8–9) e o escopo técnico (§ 07) são explícitos sobre o
que separa os dois:

| Recurso | Essencial | Experience |
|---|---|---|
| Animações | **discretas** | de rolagem e transições |
| **Direção visual autoral** | — | ✅ |
| Abertura especial, com vídeo | — | ✅ |
| Interações personalizadas | — | ✅ |
| Elementos visuais ligados à climatização | — | ✅ |

E o escopo técnico § 07 lista, sob **"Não faz parte deste projeto"**:

> **Recursos da opção Experience** — Vídeo na abertura e animações de rolagem.

O contrato repete em § 3: *"Não fazem parte do objeto: (...) os recursos do
formato Site Institucional Experience."*

### O problema

O pedido desta sessão é *"direção de arte excepcional, design premium"*. Mas
**"direção visual autoral" é literalmente o item que distingue o plano não
contratado**. Executar o Experience dentro do preço do Essencial significa
entregar R$ 1.300 de receita por R$ 2.800 de trabalho — e cria precedente com
o cliente.

### Três saídas

**A · Excelência dentro do Essencial** — *recomendada*
Tipografia, grade, hierarquia, contraste, ritmo e acabamento não custam
quilobytes nem violam o escopo. Uma página pode ser visualmente excepcional com
animações discretas; a maioria das páginas premiadas é. É o caminho de
[`02-DIRECAO-DE-ARTE.md`](02-DIRECAO-DE-ARTE.md).

**B · Aditivo para o Experience**
Se a ambição visual exigir abertura com vídeo e animações de rolagem, isso é
upgrade de plano: **aditivo de R$ 1.300** (a diferença), por escrito e
assinado, conforme contrato § 24. O cliente já viu os dois preços na proposta,
então a conversa é simples.

**C · Cortesia deliberada**
Entregar além do contratado como investimento de portfólio. É uma decisão
comercial legítima — mas tem que ser **consciente e declarada ao cliente como
cortesia**, não silenciosa. Senão vira expectativa para o próximo projeto.

### ✅ Decisão tomada em 27/10/2026 — **C · Cortesia deliberada**

A EBSS entrega acabamento acima do plano Essencial como investimento de
portfólio, **declarando ao cliente que é cortesia**.

Duas consequências operacionais, e as duas importam:

**1 · Tem que ser dito.** Cortesia silenciosa vira expectativa no próximo
orçamento — e destrói a diferença de R$ 1.300 entre os dois planos para todos
os clientes futuros. A mensagem ao Márcio precisa conter, em uma linha:
*"alguns acabamentos visuais acima do plano contratado entram como cortesia
desta primeira entrega."*

**2 · Cortesia é de acabamento, não de escopo.** Permanecem fora, porque
mudam prazo, peso e manutenção — e porque o escopo § 07 as nomeia:
vídeo na abertura · páginas extras · formulários e integrações · gestão de
Google Ads · produção de fotos.

O que a cortesia libera, dentro do orçamento de 600 KB:

- Direção visual autoral de verdade (tipografia, grade, sistema de cor)
- Animações de entrada por seção e transições refinadas — composto, com
  `prefers-reduced-motion`
- Elementos visuais derivados do símbolo da marca
- Micro-interações nos cartões e CTAs

> O orçamento de performance em [`04-ORCAMENTO-DE-PERFORMANCE.md`](04-ORCAMENTO-DE-PERFORMANCE.md)
> **não se flexibiliza por causa da cortesia.** Cortesia que torna a página
> lenta não é cortesia — é descumprimento da meta de PageSpeed ≥ 85, que é
> contratual.

## 3. Material recebido

Pasta `Connect-Air/`, 57 MB, 19 arquivos. **Íntegra e preservada** — nada foi
renomeado, movido ou convertido. Todos os derivados desta análise foram
escritos fora dela.

| Grupo | Conteúdo | Estado |
|---|---|---|
| Contratual | Contrato (docx, pdf, pdf assinado), Proposta v2, Escopo Técnico v1.0 | ✅ completo e coerente |
| Logotipo | 2 PNG, 1 SVG, 1 `.ai`, 1 PDF, 1 imagem de perfil | ✅ excelente |
| Copy | `doc_txt_site_connect_air.docx` — 9 tópicos | ⚠️ material de apoio, não copy |
| Parceiros | 5 PNG | ⚠️ não batem com a lista da copy |
| Credenciamento | `logo_sistema_cft_crt.png` | ⚠️ falta o nº de registro |
| Avaliações | 1 captura de referência + 1 link | ⚠️ link errado, depoimentos ausentes |
| Referência | `saveweb2zip-...-waveofunboxing.zip` — 49 MB | ⚪ referência visual, fora do build |

## 4. Identidade visual — o ponto forte do projeto

Único item do levantamento que está **acima** do esperado.

| | |
|---|---|
| **Cores oficiais** | `#021D64` e `#0267DB` — **escritas na prancha do `.ai`**, não deduzidas de pixel |
| **Símbolo** | Esfera com três fluxos de ar recortados. Vetor limpo, 4 paths, **1,3 KB** em `favicon_connect_air.svg` |
| **Lockups** | Três: vertical, horizontal e selo circular — todos no `.ai` |
| **Assinatura** | *você no clima ideal* |
| **Tipografia** | ❌ não especificada — entra na direção de arte, limite de 2 famílias |

Os dois azuis são o achado útil: `#021D64` é quase preto-azulado e `#0267DB` é
saturado e elétrico. A distância entre eles permite contraste dramático **sem
introduzir cor nova** — o que respeita a restrição contratual de usar a
identidade atual do cliente.

**Ponto de atenção técnico:** os PNG do logo estão em 15478 × 3866 px. A
exportação automática do lockup horizontal do `.ai` para SVG sai com 62 KB
(mesmo após `svgo`), porque a prancha inteira vem junto e só a `viewBox`
recorta. O cabeçalho precisa de uma reconstrução manual, alvo ≤ 8 KB. Tarefa
registrada em [`05-PIPELINE-DE-ASSETS.md`](05-PIPELINE-DE-ASSETS.md) § 5.

**Domínio:** `connect-air.com.br` responde, mas está **estacionado no DNS da
Hostinger**, sem conteúdo e **sem SSL** (`ERR_SSL_PROTOCOL_ERROR` em HTTPS).
Confirma a hospedagem e confirma que o acesso à Hostinger — listado como
"A RECEBER" no escopo — ainda não chegou.

## 5. 🔴 O bloqueio real: não há uma única foto

De todas as pendências, esta é a que impede a direção de arte.

Três fatos que se combinam mal:

1. O escopo § 03 exige **"foto real + texto"** na seção Sobre e **imagem de
   fundo** na abertura.
2. "Produção de fotos e vídeos" está **fora do objeto** (contrato § 3) — *"a
   página usa as fotos enviadas"*.
3. **Zero fotos foram enviadas.**

Sem resolver isso, a página vira texto e ícones sobre fundo colorido. Nenhuma
direção de arte salva uma landing page de serviço técnico sem imagem de
trabalho real.

### Encaminhamentos, em ordem de preferência

**1 · Pedir as fotos** — o caminho certo. Lista mínima em
[`01-BRIEFING.md`](01-BRIEFING.md) § 10: 8 a 12 fotos de instalação, equipamento
acabado, equipe e ambiente pronto. O Márcio quase certamente tem isso no
celular; é questão de pedir com uma lista específica, não com "manda umas fotos".

**2 · ~~Verificar o Drive do cliente~~** — ✅ **feito e esgotado.** A pasta do
Drive citada no documento de textos já havia sido baixada: é a própria
`CONNECT•AIR/`. Não há foto nenhuma lá. A ausência é definitiva até o cliente
enviar.

**3 · Direção de arte que depende menos de foto** — a direção B (fundo escuro,
geometria do símbolo como sistema visual) é a mais resistente à escassez de
imagem. Não substitui as fotos; reduz a área exposta.

**4 · Banco de imagens** — último recurso. Resolve o vazio e custa a
credibilidade: stock photo de climatização é reconhecível, e o público B2B é
justamente quem reconhece. Se for preciso, precisa ser declarado ao cliente e
orçado (licença é responsabilidade da contratada, contrato § 7).

## 6. Pendências — lista consolidada

### 🔴 Bloqueantes

| # | Pendência | Consequência |
|---|---|---|
| 1 | ~~Decisão sobre o conflito Essencial × Experience~~ | ✅ **resolvida em 27/10: cortesia declarada** (§ 2) |
| 2 | **Fotos reais** | Sem elas não há abertura nem seção Sobre |
| 3 | **Referência legal** da manutenção obrigatória | Seção 04 não vai ao ar sem documento (escopo § 03) |
| 4 | **Nº de registro CFT/CRT** + comprovante | Seção 05 não vai ao ar sem comprovante |
| 5 | **Depoimentos do Google** — texto, nome, nota, média | Seção 06 não existe sem eles |
| 6 | **Autorização de uso** das marcas de clientes | Risco jurídico (§ 7) |

### ⚠️ Importantes

| # | Pendência |
|---|---|
| 7 | Região de atendimento — falta no material, é o dado de maior peso para SEO local e Schema.org |
| 8 | Três números de destaque além dos 15 anos (o escopo prevê até 4) |
| 9 | Priorização comercial dos 7 serviços |
| 10 | ~~E-mail de contato~~ — ✅ `connectairarcondicionado@gmail.com`, obtido da trilha de auditoria do contrato assinado. Falta só confirmar que é o e-mail comercial a publicar |
| 11 | Acesso à Hostinger |
| 12 | Wolfmann Construtora (citada, sem logo) × UTC Engenharia (logo, não citada) |
| 13 | "Connect" ou "Connect-Air" na copy |
| 14 | ~~Conferir o Drive do cliente~~ — ✅ encerrado: o Drive **é** a pasta `CONNECT•AIR/`, já baixada. Sem fotos |

## 7. Risco jurídico — logos de clientes

A copy pede exibição de **Cacau Show**, **Faculdade Oswaldo Cruz**, **JTC**,
**YKP** e **Wolfmann** como parceiros, e cinco logotipos vieram na pasta.

Usar marca de terceiro como prova de relacionamento comercial exige
autorização. O contrato (Obrigações da Contratante, § 3) coloca a
responsabilidade na Connect-Air, inclusive quanto a *"credenciamentos,
parcerias e referências legais citadas"* — mas a EBSS deve **pedir a
confirmação por escrito e guardar o aceite por WhatsApp**. Empresas do porte da
Cacau Show costumam ter política formal de uso de marca.

Alternativa segura, se a autorização não vier: citar os segmentos sem as
marcas — "chocolateria nacional", "instituição de ensino superior",
"distribuidora", "construtora". Perde impacto, elimina o risco.

**Observação separada:** o `logo_sistema_cft_crt.png` traz o brasão da
República Federativa do Brasil, que integra a marca do Sistema CFT/CRT. Usar
como indicação de registro está correto. O que não se pode é diagramar de modo
a sugerir endosso governamental — a legenda precisa dizer o que o registro
significa.

## 8. Copy — resumo

Análise completa em [`03-COPY.md`](03-COPY.md).

O material é um bom briefing e não é copy. Cobre os assuntos certos e falha na
execução: abre com descrição genérica em vez de proposta de valor; troca provas
por adjetivos ("qualidade", "eficiência", "profissionalismo", "excelência");
não cita a região; não tem números além dos 15 anos; e não menciona o problema
do cliente — equipamento parado, obra parada, risco de multa.

Ironia útil: a empresa tem provas boas e está usando adjetivos no lugar delas.
15 anos, CFT/CRT, NR10, NR35, Cacau Show, Faculdade Oswaldo Cruz, chiller e
fancoil valem mais que qualquer "altamente qualificada".

## 9. Estrutura criada

```
connect-air-landing-page/
├── .gitignore              # ignora .zip, .playwright-mcp/, tmp/, derivados
├── README.md
├── Connect-Air/            # ORIGINAL — preservado, somente leitura
├── brand/                  # kit curado: 3 arquivos, 12 KB
│   ├── simbolo-connect-air.svg
│   ├── tokens.css
│   └── README.md
├── docs/
│   ├── 00-DIAGNOSTICO.md
│   ├── 01-BRIEFING.md
│   ├── 02-DIRECAO-DE-ARTE.md
│   ├── 03-COPY.md
│   ├── 04-ORCAMENTO-DE-PERFORMANCE.md
│   ├── 05-PIPELINE-DE-ASSETS.md
│   └── 06-ACEITE.md
└── reference/
    └── REFERENCIAS.md
```

## 10. Como o erro do AutosFlow fica impossível aqui

O inchaço anterior não veio de descuido, veio de ausência de limite. Então os
limites estão escritos e são numéricos:

| Mecanismo | Regra |
|---|---|
| Teto de arquivos | **25 imagens** em `src/assets/`, **450 KB** somados |
| Derivação | **3 larguras por original** (480/960/1600), WebP q72. SVG: derivada única |
| Nomenclatura | `assunto-variante-largura.webp`. `final`, `v2`, `novo`, `copy` **proibidos** |
| Geração | Só por script, com limpeza destrutiva do destino → **órfão é impossível** |
| Registro | Imagem sem linha em [`05-PIPELINE-DE-ASSETS.md`](05-PIPELINE-DE-ASSETS.md) não entra |
| Originais | `Connect-Air/` intocada; os PNG de 15478 px **nunca** vão para a web |
| Referência | O `.zip` de 49 MB fica fora do git e nunca é descompactado no projeto |
| Peso total | **≤ 600 KB** inicial — 40 % do teto contratual de 1,5 MB |

## 11. Próximas etapas — para aprovação

| # | Etapa | Depende de | Esforço |
|---|---|---|---|
| ~~1~~ | ~~Decidir o conflito de escopo~~ | ✅ **feito** — cortesia declarada | — |
| **2** | **Enviar ao cliente a lista única de pendências** — as 6 bloqueantes + as 8 importantes, em uma mensagem só. O prazo contratual não corre até isso voltar (escopo § 06) | Você → Márcio | 1 mensagem |
| ~~3~~ | ~~Conferir o Drive do cliente~~ | ✅ **feito** — é a própria pasta `CONNECT•AIR/`, sem fotos | — |
| **4** | **Painel de referências** — ✅ **5 capturas reais feitas e anotadas** em [`reference/REFERENCIAS.md`](../reference/REFERENCIAS.md): Maneng, Daikin, YKP, Trane e Arclima. Faltam 2–3 fora do setor + a skill `design-taste-frontend` | parcial | ~30 min restantes |
| **5** | **Fechar a direção de arte** — escolher entre A, B e C de [`02-DIRECAO-DE-ARTE.md`](02-DIRECAO-DE-ARTE.md), definir as 2 famílias tipográficas, montar uma amostra estática de uma seção para aprovação | Etapas 1 e 4 | ~2 h |
| **6** | **Escrever a copy** e emitir o PDF de aprovação — entregável contratual dos dias 3–4 | Etapa 2 | ~2 h |
| ~~7~~ | ~~Reconstruir o lockup horizontal~~ | ✅ **feito** — 62 KB → **7,6 KB**, conferido contra o original | — |
| **5** | **Direção de arte** | ✅ **fechada e construída** — ver [`02-DIRECAO-DE-ARTE.md`](02-DIRECAO-DE-ARTE.md) | — |
| **8** | **Desenvolvimento** | 🟡 **segunda versão no ar**: https://connect-air.vercel.app | — |

### O que a página tem (revisão de 27/10, tarde)

🔴 **Falha corrigida nesta revisão.** A primeira versão entregou **5 dos 9
tópicos** que o cliente escreveu no `doc_txt_site_connect_air.docx`. Foram
cortados *Qualidade e Compromisso*, *Clientes e Parceiros*, *Por que escolher* e
*Avaliações do Google*, por julgamento próprio: risco de autorização de marcas e
ausência de depoimentos. Os dois receios eram reais; **a resposta certa era
construir e sinalizar, não omitir** — ainda mais com o contrato pondo essa
responsabilidade no cliente.

Hoje os 9 tópicos estão na página:

| Tópico do cliente | Onde está |
|---|---|
| 1 · Nossos Serviços | seção *Nossos serviços*, 7 serviços em 3 frentes |
| 2 · Nossa Experiência | seção *Quinze anos no clima ideal* |
| 3 · Qualidade e Compromisso | segundo parágrafo da mesma seção |
| 4 · Clientes e Parceiros | 5 logos com link, mais a Wolfmann pelo nome |
| 5 · Equipamentos e Sistemas | os 9 sistemas, com a lista viva |
| 6 · Contratos de Manutenção | campo azul *Contratos de manutenção e PMOC* |
| 7 · PMOC | a mesma seção |
| 8 · Por que escolher | os 7 motivos, literais |
| 9 · Entre em Contato | campo azul de contato |
| Avaliações do Google | cartão com link para o perfil |

Mais: 9 botões de WhatsApp com mensagem e `id` próprios, barra fixa com marcação
da seção atual, Schema.org de empresa local, **130 KB acima da dobra** e
**0 FAIL** nos dois detectores em 1440, 768 e 390 px.

### O que ela ainda não tem, e por quê

| Falta | Motivo |
|---|---|
| **Fotos da Connect-Air** | Não enviadas. No lugar, 6 fotografias de acervo (Wikimedia, CC0/PD/BY), creditadas no rodapé e **nunca apresentadas como obra do cliente**. Saem no dia em que as reais chegarem. |
| **Depoimentos nos cartões** (escopo § 06) | A seção existe e leva ao perfil do Google, mas **sem cartões de depoimento**: os textos não foram enviados e prova não se inventa. O link que o cliente mandou é o de *escrever* avaliação, não o de ler. |
| **Citação da lei** na faixa de manutenção | A referência não foi confirmada. O texto fala da obrigação sem citar norma — afirmação jurídica sem documento não vai ao ar. |
| **Autorização das marcas** | Os 5 logos estão na página, como o cliente pediu. **Falta a autorização por escrito** de cada empresa (§ 7). O contrato põe a responsabilidade na Connect-Air, mas a EBSS deve pedir e guardar o aceite. |
| **Wolfmann × UTC** | O logo enviado é da **UTC Óleo e Gás**, não da UTC Engenharia, e a Wolfmann foi citada sem logo. Hoje o logo aparece com o nome certo, sem link, e a Wolfmann entra pelo nome. Falta o cliente confirmar os dois. |
| **Número do registro CFT/CRT** | Não informado. A página diz que há registro, sem número. |
| **Números da seção Sobre** | Só existe um: quinze anos. |
| **Vídeo** | Fora do plano contratado, e 1,5 MB de teto não comporta. |

### Estado em 27/10, fim do levantamento

Etapas 1, 3 e 7 concluídas. Etapa 4 em 70%.

**Achado da etapa 4 que muda o § 5:** a Trane, referência global de HVAC,
**fotografa edifício, não máquina**. Se o Márcio não tiver fotos boas de
equipamento, fotos de *ambiente climatizado pronto* — loja, galpão, hall —
seguem a mesma estratégia e são muito mais fáceis de conseguir. Isso amplia a
chance de destravar o bloqueio das fotos.

A **etapa 2 continua com você** e é a mais urgente: uma mensagem única ao
Márcio com as 6 pendências bloqueantes + as importantes, incluindo a linha
sobre a cortesia (§ 2). Enquanto ela não for enviada, o relógio contratual
segue parado — o que hoje joga a nosso favor, mas não indefinidamente.
