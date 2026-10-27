# 05 · Pipeline de assets — regra antiduplicação

## 1. O problema que esta regra existe para evitar

No projeto AutosFlow o build inchou com milhares de imagens derivadas e
duplicatas. O mecanismo é sempre o mesmo: cada tentativa de ajuste gera um
arquivo novo, nenhum arquivo velho é apagado, e ninguém sabe mais qual versão a
página realmente usa.

A correção não é "ter cuidado". É tornar a duplicação **impossível por
estrutura**.

## 2. As quatro regras

### Regra 1 — Original nunca se toca

`Connect-Air/` é somente leitura. Nenhum arquivo dela é renomeado, movido,
convertido ou sobrescrito. Nunca.

### Regra 2 — Um original gera no máximo três derivadas

Cada imagem de conteúdo gera exatamente três larguras, e só:

| Derivada | Largura | Uso |
|---|---|---|
| `-480` | 480 px | celular |
| `-960` | 960 px | tablet e notebook |
| `-1600` | 1600 px | desktop e telas densas |

Formato: **WebP, qualidade 72**. Sem AVIF (ganho pequeno, custo de suporte e
mais um arquivo por imagem). Sem fallback JPEG — todos os navegadores do escopo
suportam WebP há anos.

Logotipos e ícones: **SVG, derivada única**. Não geram as três larguras.

### Regra 3 — O nome do arquivo é determinístico

```
<assunto>-<variante>-<largura>.webp
```

`instalacao-vrf-equipe-960.webp` ✅
`instalacao-vrf-equipe-960-final-v2-NOVO.webp` ❌

Sufixos como `final`, `v2`, `novo`, `copy`, `(1)`, `teste`, `ok` são
**proibidos**. Se o nome precisa de uma versão, o arquivo anterior deveria ter
sido apagado.

### Regra 4 — Toda derivada é produzida por script, nunca à mão

A conversão sai de `tools/build-assets.mjs` (criado na fase de
desenvolvimento), que lê de uma pasta de fontes selecionadas e escreve em
`src/assets/`. Regenerar é **destrutivo**: o script limpa o destino antes de
escrever.

Consequência direta: não existe arquivo órfão, porque nada em `src/assets/`
sobrevive sem estar na lista de entrada.

## 3. Tetos

| Limite | Valor |
|---|---|
| Arquivos em `src/assets/` | **≤ 25** |
| Peso de `src/assets/` | **≤ 450 KB** |
| Derivadas por original | **3** (imagens) · **1** (SVG) |

Bater o teto é um sinal de que o layout pede imagens demais, não de que o teto
está errado.

## 4. Registro de assets

Toda imagem publicada tem uma linha aqui. Sem linha, não entra no `src/`.

Derivadas geradas por `tools/build-assets.py` (limpeza destrutiva do destino).
Originais fora do git, refazíveis com `tools/fetch-originals.py`.

| Arquivo final | Origem | Licença | Onde aparece |
|---|---|---|---|
| `duto-1957-{420,840}` | *Pantex Plant Building 12-44-1 Air Ducts*, 1957 | domínio público | porta "Instalar", Splitão |
| `casa-de-maquinas-{420,840}` | *Ventilation ductwork in a mechanical room* | CC BY 2.0 | porta "Manter", Self-contained |
| `chiller-{520,1040,1600}` | *Chiller*, P199 | domínio público | lista de sistemas, contato (sangria) |
| `trocador-aberto-{520,1040}` | *Disassembled chiller heat exchanger*, Rsparks3 | CC0 | Fancoil, escada, retrato circular |
| `controles-1957-{520,1040}` | *Pantex Plant Building 12-44-1 Air Conditioning*, 1957 | domínio público | VRF, Multi Split, escada |
| `exaustao-cozinha-{520,1040}` | *Kitchen Exhaust Fans* | CC0 | Mini VRF, Split Inverter |

**13 arquivos, 440 KB.** O script falha o build se passar de 25 arquivos ou 450 KB.

Todas via Wikimedia Commons, creditadas no rodapé da página. **Nenhuma é
apresentada como foto da Connect-Air** — mostram o mundo do ofício, não a obra
do cliente. Saem assim que as fotos reais chegarem (ver
[`00-DIAGNOSTICO.md`](00-DIAGNOSTICO.md) § 5).

### Descartadas na curadoria

| Imagem | Motivo |
|---|---|
| Técnicos de HVAC (USAF, domínio público) | São militares americanos identificáveis. Um visitante poderia tomá-los pela equipe da Connect-Air. |
| `chiller-plant-scada-system` | Monitores de supervisório: outro mundo visual, não senta na sala escura. |
| `industrial-water-cooling-tower`, `air-conditioning-plant-science` | Céu azul e gramado: claras demais para uma página escura. |
| `double-radial-fan` | Cotas em vermelho e carimbo de data: parece catálogo de oficina. |

## 5. Estado atual dos materiais de marca

### Já disponível e limpo

| Arquivo | Origem | Observação |
|---|---|---|
| `favicon_connect_air.svg` | cliente | **1,2 KB, 4 paths, vetor limpo.** É o símbolo da marca em estado ideal. Usar como favicon **e** como símbolo na página. Copiado para `brand/simbolo-connect-air.svg`. |
| `brand/logo-horizontal.svg` | reconstruído do `.ai` | ✅ **7,6 KB**, dentro do alvo. Ver `brand/README.md`. |

### Precisa de trabalho

| Item | Situação | Encaminhamento |
|---|---|---|
| ~~Lockup horizontal~~ | ✅ **resolvido em 27/10** — reconstruído em **7,6 KB** contra os 62 KB da exportação automática | — |
| `1_logotipo_connect_air.png` | 15478 × 3866 px | Não vai para a web em hipótese alguma. É arquivo de arte. |
| `2_logotipo_connect_air.png` | 8434 × 7085 px | Idem. |
| `img_perfil_connect_air.png` | 4436 × 4437 px | Possível fonte para a imagem Open Graph (1200 × 630). |
| Logos de parceiros (5 PNG) | 720–2000 px, fundo transparente | Derivada única em WebP com **altura normalizada em 80 px**, escala de cinza aplicada por CSS (`filter: grayscale(1)`), não por arquivo. 5 arquivos, ~15 KB somados. |
| `logo_sistema_cft_crt.png` | 1536 × 1536 px, brasão colorido | Derivada única, 160 px. **Mantém cor** — brasão em escala de cinza descaracteriza. |

### Fora do build, em definitivo

| Item | Peso | Decisão |
|---|---|---|
| `saveweb2zip-com-www-waveofunboxing-com-br.zip` | **49 MB** — 209 arquivos, 118 WebP, 25 `woff2`, 6 MP4, HTML de 1 MB | Captura de um site feito em Framer, guardada como **referência visual**. Fica em `Connect-Air/`, ignorada pelo git, **nunca descompactada dentro do projeto**. Serve de exemplo de direção; é também o exemplo exato do peso que este projeto não pode ter. |

## 6. Imagem Open Graph

Um arquivo, 1200 × 630, **≤ 80 KB**, gerado a partir do lockup vertical sobre
fundo `#021D64`. Não entra no teto de 25 porque não é carregado pela página.
