# Connect-Air · Landing Page

Landing page institucional de página única para a **Connect-Air Climatização**
(Marcio Dias Souza — CNPJ 20.039.416/0001-20), desenvolvida pela **EBSS Mídia**
(Easy Business Negócios Digitais LTDA).

| | |
|---|---|
| Plano contratado | **Site Institucional Essencial** — R$ 1.300, quitado em 26/10/2026 |
| Prazo | 10 a 15 dias úteis a partir da conferência completa dos materiais |
| Stack | HTML5 + CSS3 + JavaScript estático. **Sem framework, sem CMS, sem build pesado** |
| Hospedagem | Hostinger da Connect-Air, domínio `connect-air.com.br` |
| Objetivo de conversão | Pedido de orçamento no WhatsApp |

---

## Estrutura do repositório

```
.
├── Connect-Air/        # MATERIAL ORIGINAL DO CLIENTE — SOMENTE LEITURA
├── docs/               # Documentos de orientação do projeto
├── brand/              # Kit de marca curado (poucos arquivos, derivados controlados)
├── reference/          # Referências de direção de arte (anotações, sem binários pesados)
├── src/                # A página. É isto que vai para a Hostinger
│   ├── index.html
│   └── assets/         # css · js · fonts · img · brand
├── tools/              # geração de assets, com teto verificado no build
└── assets/             # originais das fotos de acervo (fora do git)
```

### Rodar e publicar

```bash
# servir localmente
python3 -m http.server 8080 -d src     # http://localhost:8080

# regerar as imagens (limpa o destino antes de escrever)
python3 tools/fetch-originals.py       # só na 1ª vez: baixa os originais
python3 tools/build-assets.py          # precisa de Pillow — ver nota abaixo

# publicar: basta subir para o GitHub
git push origin main
```

> **Pillow:** `tools/build-assets.py` depende do Pillow. Se o `python3` padrão
> da máquina mudar de versão (aconteceu em 05/11, numa atualização do Homebrew),
> o script para com uma mensagem dizendo qual interpretador usar. Rode com um
> que tenha Pillow, por exemplo `/usr/local/bin/python3 tools/build-assets.py`.

Prévia no ar: **https://connect-air.vercel.app**

### Como a publicação funciona

O repositório está conectado ao Vercel. **Todo push para `main` publica em
produção automaticamente**; push em qualquer outro branch gera uma prévia
própria, com URL separada. Não há build step: o `vercel.json` aponta
`outputDirectory` para `src/` e o Vercel serve os arquivos como estão.

> **Não publique por `vercel deploy`.** Com o git conectado, isso cria um
> deploy paralelo ao fluxo e consome a cota do plano Hobby (100 deploys/dia)
> sem necessidade. O caminho é o push.

Para testar antes de publicar, use um branch:

```bash
git switch -c ajuste-x
git push -u origin ajuste-x      # o Vercel devolve uma URL de prévia
```

### Formulário de contato

O formulário da seção *Entre em contato* não tem servidor: ele posta direto para
o **Web3Forms**, que encaminha a mensagem por e-mail. Para ligá-lo:

1. Em [web3forms.com](https://web3forms.com), gerar uma chave para
   `contato@connect-air.com.br` e confirmar pelo link que chega nessa caixa.
2. Colar a chave no `value` do campo `access_key` em `src/index.html`
   (está comentado, logo acima dos campos).

**Enquanto a chave estiver vazia o formulário não fica quebrado:** o script
troca o rótulo do botão para *Enviar pelo WhatsApp* e a mensagem segue por lá,
já escrita com nome, e-mail, telefone e texto. O visitante lê isso antes de
clicar. Com a chave preenchida, o envio passa a ser por e-mail sem tocar no HTML,
e continua funcionando mesmo com o JavaScript desligado.

> Alternativa, se preferir não depender de serviço externo: a Hostinger roda PHP,
> então um `contato.php` com `mail()` resolveria na hospedagem final — mas não
> funcionaria na prévia do Vercel, que não executa PHP.

A publicação final é na Hostinger da Connect-Air, copiando o conteúdo de `src/`.
Não há etapa de compilação: o que está em `src/` é exatamente o que vai ao ar.

### `Connect-Air/` — não modificar

Pasta entregue pelo cliente em 27/10/2026. **Nenhum arquivo dela deve ser
renomeado, movido, convertido ou sobrescrito.** Todo derivado para a web é
gerado em `brand/` ou `src/assets/`, com a origem registrada em
[`docs/05-PIPELINE-DE-ASSETS.md`](docs/05-PIPELINE-DE-ASSETS.md).

---

## Documentos

| Documento | Para quê |
|---|---|
| [`docs/00-DIAGNOSTICO.md`](docs/00-DIAGNOSTICO.md) | Estado atual, pendências e riscos. **Comece por aqui.** |
| [`docs/01-BRIEFING.md`](docs/01-BRIEFING.md) | Fonte única de verdade: marca, serviços, contatos, parceiros |
| [`docs/02-DIRECAO-DE-ARTE.md`](docs/02-DIRECAO-DE-ARTE.md) | Direção visual — a definir e aprovar antes do código |
| [`docs/03-COPY.md`](docs/03-COPY.md) | Textos da página, entregável contratual para aprovação |
| [`docs/04-ORCAMENTO-DE-PERFORMANCE.md`](docs/04-ORCAMENTO-DE-PERFORMANCE.md) | Limites de peso e velocidade, com teto por arquivo |
| [`docs/05-PIPELINE-DE-ASSETS.md`](docs/05-PIPELINE-DE-ASSETS.md) | Regra antiduplicação de imagens |
| [`docs/06-ACEITE.md`](docs/06-ACEITE.md) | Checklist dos critérios de aceite do escopo técnico |
| [`docs/07-PEDIDO-DE-FOTOS.md`](docs/07-PEDIDO-DE-FOTOS.md) | Mensagem pronta para pedir as fotos ao cliente, e o que cada uma destrava |

## Números atuais

| | |
|---|---|
| Acima da dobra | **130 KB** |
| Página inteira | **664 KB** (teto contratual: 1,5 MB) |
| Imagens | 20 arquivos, 540 KB (teto próprio: 25 arquivos, 560 KB) |
| Tipografia | 1 família, 2 pesos, 39 KB, auto-hospedada |
| Dependências em runtime | **nenhuma** |

## Ferramentas verificadas

Ver [`docs/00-DIAGNOSTICO.md`](docs/00-DIAGNOSTICO.md) § 1.

---

**Regra número um deste projeto:** nenhuma imagem entra em `src/` sem estar
registrada no pipeline de assets. O custo de um arquivo não é o seu tamanho —
é o tamanho multiplicado por todas as cópias que ninguém lembra de apagar.
