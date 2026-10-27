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
└── src/                # Código da página (criado na fase de desenvolvimento)
```

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

## Ferramentas verificadas

Ver [`docs/00-DIAGNOSTICO.md`](docs/00-DIAGNOSTICO.md) § 1.

---

**Regra número um deste projeto:** nenhuma imagem entra em `src/` sem estar
registrada no pipeline de assets. O custo de um arquivo não é o seu tamanho —
é o tamanho multiplicado por todas as cópias que ninguém lembra de apagar.
