# 03 · Copy

Entregável contratual. O escopo § 06 prevê **"PDF com todos os textos da
página, seção por seção"**, aprovado pela Connect-Air nos dias 3–4, **antes do
desenvolvimento**. O contrato (§ 1.1) repete a obrigação.

**Status: análise feita, redação não iniciada** — depende de dados que faltam.

---

## 1. Diagnóstico do material recebido

O cliente enviou `doc_txt_site_connect_air.docx`: 9 tópicos, ~3.400 caracteres.
É material de apoio bem organizado — e não é copy de landing page.

### O que está bom

- Os 9 tópicos cobrem exatamente a arquitetura de seções do escopo. Não falta
  assunto.
- A lista de equipamentos (VRV, VRF, chiller, fancoil, splitão) é ouro para
  público B2B. Deve aparecer com destaque, não escondida.
- PMOC e contratos mensais estão descritos com precisão e são os dois serviços
  de maior valor recorrente.

### O que precisa mudar

**1 · Não existe proposta de valor, existe descrição de empresa.**
Abre com *"A Connect é especializada em soluções de climatização para empresas,
indústrias, comércios, restaurantes e lojas, oferecendo serviços com qualidade,
eficiência e profissionalismo."*

Troque "Connect" por qualquer concorrente e a frase continua verdadeira. O
escopo § 03 pede, para a abertura, "título com a proposta de valor **para
comércio e indústria**" — ou seja, uma frase que só a Connect-Air possa
assinar. Hoje ela não existe no material.

**2 · Adjetivos no lugar de provas.**
"Qualidade", "eficiência", "profissionalismo", "altamente qualificada",
"comprometidos", "responsabilidade", "transparência", "excelência" aparecem
repetidamente. São autoelogios não verificáveis — e o leitor B2B desconta todos
automaticamente.

Em contrapartida, as provas reais que a empresa tem estão subaproveitadas:
15 anos, registro CFT/CRT, NR10, NR35, PCMSO, e clientes como Cacau Show e
Faculdade Oswaldo Cruz. Prova vale mais que adjetivo, sempre.

**3 · O tópico 3 inteiro não diz nada.**
"Qualidade e Compromisso" é 100 % adjetivo. Na página aprovada ele some, e o
espaço vai para números e credenciamentos.

**4 · Faltam os números.**
O escopo § 03 prevê "até 4 números de destaque" na seção Sobre. Temos um:
15 anos. Ver [`01-BRIEFING.md`](01-BRIEFING.md) § 4.

**5 · Nenhuma menção a região de atendimento.**
O escopo pede explicitamente ("quem são, há quanto tempo atuam e **onde
atendem**"). Também é o dado de maior peso para o SEO local e para a marcação
Schema.org de empresa local. Falta.

**6 · Escrito para quem já decidiu.**
O texto fala de serviços. Não fala do problema: equipamento parado em dia de
calor, obra parada, loja sem cliente, risco de multa por falta de PMOC. Quem
busca "manutenção de ar condicionado comercial" às 9 h de uma segunda-feira
está com um problema, não com uma curiosidade.

**7 · Nenhuma chamada para ação.**
O tópico 9 termina em "solicite um orçamento personalizado" — genérico. O
escopo prevê CTA de WhatsApp **com mensagem pronta e identificador próprio por
seção** (§ 05). São 7 CTAs diferentes a escrever.

## 2. Tom a adotar

| Em vez de | Escrever |
|---|---|
| "Soluções em climatização com qualidade e eficiência" | O que acontece, em quanto tempo, para quem |
| "Profissionais altamente qualificados" | "Técnicos com NR10 e NR35, registro CFT/CRT nº ___" |
| "Mais de 15 anos de experiência" | "15 anos climatizando comércio e indústria em São Paulo" |
| "Atendimento especializado" | A região, o prazo de resposta, o horário |

Direto, específico, sem adjetivo que não venha acompanhado de prova.
Segunda pessoa quando for sobre o problema do cliente, primeira quando for
sobre o que a Connect-Air faz.

## 3. Estrutura a redigir

Conforme escopo § 02 e § 03. Cada seção precisa dos campos marcados.

| # | Seção | A escrever | Bloqueios |
|---|---|---|---|
| 01 | Abertura | H1 (proposta de valor, comércio e indústria), subtítulo, prova rápida, 2 CTAs | precisa de § 1.1 e da região |
| 02 | Sobre | 1 parágrafo + 4 números + região | **faltam 3 números e a região** |
| 03 | Serviços | 7 cartões: título + 1 frase + CTA próprio | **falta a priorização** |
| 04 | Manutenção obrigatória | Faixa: a exigência, a quem se aplica, CTA "quero regularizar" | 🔴 **falta a referência legal** |
| 05 | Credenciamentos e parceiros | Legenda explicando o que cada selo significa | 🔴 **falta o nº de registro e a autorização das marcas** |
| 06 | Avaliações | 3 a 6 depoimentos + selo de nota | 🔴 **os depoimentos não foram enviados** |
| 07 | Contato e rodapé | Chamada final, WhatsApp, telefone, e-mail, endereço, Instagram | e-mail provável obtido, a confirmar |
| + | Meta | `<title>` ≤ 60 car., `description` ≤ 155 car., Open Graph | precisa da região |

## 4. Mensagens de WhatsApp

Cada botão abre o WhatsApp com texto pronto identificando a origem (escopo
§ 05). Rascunho, a validar com o cliente:

| Origem | Mensagem |
|---|---|
| Abertura | `Olá! Vim pelo site e quero um orçamento de climatização para minha empresa.` |
| Serviço — instalação | `Olá! Quero um orçamento de instalação de ar-condicionado.` |
| Serviço — manutenção preventiva | `Olá! Tenho interesse em contrato de manutenção preventiva.` |
| Serviço — manutenção corretiva | `Olá! Preciso de manutenção corretiva no meu sistema de climatização.` |
| Serviço — PMOC | `Olá! Preciso de PMOC para a minha edificação.` |
| Faixa de manutenção obrigatória | `Olá! Quero regularizar a manutenção do meu sistema de climatização.` |
| Contato final | `Olá! Quero falar com a Connect-Air sobre climatização.` |

Cada botão recebe `id` próprio para a configuração de conversão no Google Ads
(escopo § 05). Convenção: `wa-abertura`, `wa-servico-instalacao`,
`wa-servico-preventiva`, `wa-servico-corretiva`, `wa-servico-pmoc`,
`wa-manutencao-obrigatoria`, `wa-contato`, `wa-flutuante`.

## 5. Perguntas ao cliente

Sem estas respostas a copy não pode ser escrita:

1. **Região de atendimento** — São Paulo capital? Grande São Paulo? Interior?
2. **Três números** além dos 15 anos — quantos clientes ativos, quantas obras
   entregues, quantos técnicos, prazo de atendimento de emergência?
3. **Priorização dos 7 serviços** — quais 3 trazem mais receita?
4. **Referência legal** da manutenção obrigatória que a empresa quer citar
5. **Número de registro CFT/CRT** e comprovante
6. **E-mail** — confirmar se `connectairarcondicionado@gmail.com` (o da assinatura do contrato) é o e-mail comercial a publicar
7. **Depoimentos do Google** — texto, nome, nota, e a média do perfil
8. **Wolfmann × UTC Engenharia** — qual entra? (ver [`01-BRIEFING.md`](01-BRIEFING.md) § 7)
9. **Autorização de uso das marcas** dos clientes citados
10. **"Connect" ou "Connect-Air"** na copy

---

> Enquanto essas respostas não chegarem, o prazo contratual **não corre**:
> escopo § 06 — *"o prazo conta a partir da conferência completa dos materiais"*.
