# 06 · Critérios de aceite

Transcrição operacional do escopo técnico § 06 e § 08. Serve de checklist de
entrega e de base para o relatório final.

## Etapas

| Etapa | Prazo | Entregável | Critério de aceite | Aprova | Status |
|---|---|---|---|---|---|
| 1 | Dias 1–2 | Materiais | Lista do recebido e do que falta; todos os obrigatórios conferidos | EBSS | 🟡 **em andamento** — ver [`00-DIAGNOSTICO.md`](00-DIAGNOSTICO.md) |
| 2 | Dias 3–4 | Textos | PDF com todos os textos, seção por seção; informações técnicas e afirmações conferidas | Connect-Air | ⚪ bloqueado pela etapa 1 |
| 3 | Dias 5–9 | Desenvolvimento | Todas as seções da especificação presentes | EBSS | ⚪ |
| 4 | Dias 10–12 | Prévia | Link de prévia; ajustes aplicados; botões, links e WhatsApp testados | Connect-Air | ⚪ |
| 5 | Dias 13–15 | Publicação | HTTPS ativo, metas de desempenho atingidas, sitemap e robots publicados | EBSS | ⚪ |

> O prazo **conta a partir da conferência completa dos materiais** e fica
> **pausado enquanto uma aprovação está com a Connect-Air**.

**Rodadas de ajuste:** 2 nos textos + 2 na prévia. Cada rodada é uma lista
única, enviada de uma vez. Pedidos fora das rodadas, ou que alterem algo já
aprovado, são orçados à parte.

## Checklist técnico de publicação

### Seções (escopo § 02)
- [ ] 01 Abertura — proposta de valor, menu âncora, 2 CTAs
- [ ] 02 Sobre — foto real, texto, até 4 números
- [ ] 03 Serviços — grade de cartões, CTA por serviço
- [ ] 04 Manutenção obrigatória — faixa em cor de contraste
- [ ] 05 Credenciamentos e parceiros — logos com legenda
- [ ] 06 Avaliações — 3 a 6 cartões + selo de nota + link do perfil
- [ ] 07 Contato e rodapé — WhatsApp, telefone, e-mail, endereço, Instagram
- [ ] Fixos — botão flutuante de WhatsApp, menu fixo no topo

### Técnico (escopo § 04)
- [ ] HTML5 + CSS3 + JS, sem construtor e sem biblioteca pesada
- [ ] Responsivo testado em 360 · 768 · 1024 · 1440
- [ ] Chrome, Safari, Edge e Firefox — desktop e mobile
- [ ] PageSpeed mobile ≥ 85
- [ ] LCP < 2,5 s
- [ ] Página inicial < 1,5 MB
- [ ] Imagens em WebP, lazy, dimensionadas por tela
- [ ] Até 2 famílias tipográficas, auto-hospedadas
- [ ] HTTPS ativo + redirecionamento para versão única do endereço

### Acessibilidade (escopo § 04)
- [ ] Contraste mínimo AA em todos os pares texto/fundo
- [ ] `alt` descritivo em todas as imagens
- [ ] Um único `H1`; `H2`/`H3` em ordem
- [ ] Navegação por teclado com foco visível
- [ ] `prefers-reduced-motion` respeitado

### SEO (escopo § 05)
- [ ] `<title>` ≤ 60 caracteres, com serviço e região
- [ ] `meta description` ≤ 155 caracteres
- [ ] Schema.org `LocalBusiness` — nome, endereço, telefone, região
- [ ] `sitemap.xml`, `robots.txt`, URL canônica
- [ ] Open Graph + favicon
- [ ] Nomes de arquivo de imagem descritivos

### Conversão (escopo § 05)
- [ ] Cada botão de WhatsApp com mensagem pronta identificando a seção
- [ ] Botão flutuante visível em toda a rolagem, mobile e desktop
- [ ] Telefone clicável no celular (`tel:`)
- [ ] Parâmetros `gclid` e UTM preservados sem quebrar
- [ ] `id` próprio em cada botão de WhatsApp (ver [`03-COPY.md`](03-COPY.md) § 4)

### Privacidade (escopo § 05)
- [ ] Sem formulário e sem coleta de dados pessoais
- [ ] Sem ferramenta de rastreio instalada → sem aviso de cookies
- [ ] Se o cliente pedir tag do Google Ads ou Analytics depois, **avisar que o
      aviso de cookies passa a ser recomendado**

## Entrega final (escopo § 08)

- [ ] 01 · Página no ar no domínio da Connect-Air, com HTTPS
- [ ] 02 · Arquivos-fonte em `.zip` — código e imagens otimizadas
- [ ] 03 · Relatório de entrega — resultado do PageSpeed, lista de links e
      botões testados, identificador de cada botão de WhatsApp
- [ ] 04 · URL final pronta para a campanha do Google Ads
- [ ] 05 · Acesso à Hostinger revogado em até 5 dias úteis após a publicação

## Fora do objeto — não fazer sem aditivo

Gestão de Google Ads · criação de logo ou identidade · produção de fotos e
vídeos · páginas extras, blog ou loja · formulários e integrações (CRM, agenda,
e-mail) · manutenção mensal · **recursos do plano Experience: vídeo na abertura
e animações de rolagem**.

> Contrato § 24: alterações de objeto, preço, prazo ou garantias só valem por
> aditivo contratual escrito e assinado.
