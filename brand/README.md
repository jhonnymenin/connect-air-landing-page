# Kit de marca — curado

Poucos arquivos, de propósito. Os originais ficam em `Connect-Air/` e não se tocam.

| Arquivo | Origem | Peso |
|---|---|---|
| `logo-horizontal.svg` | reconstruído do vetor de `logotipo_connect_air.ai` | **7,6 KB** |
| `simbolo-connect-air.svg` | cópia fiel de `favicon_connect_air.svg` | 1,2 KB |
| `tokens.css` | cores escritas na prancha do `.ai` | <1 KB |

## Sobre o `logo-horizontal.svg`

A exportação automática do `.ai` saía com **62 KB**, porque a prancha inteira
(os três lockups) vinha junto e só a `viewBox` recortava. Foi reconstruído:
extraídas as 43 formas da faixa do lockup horizontal, remontadas em dois paths
contínuos — um por cor oficial — com coordenadas em escala reduzida.

As duas linhas que ladeiam *você no clima ideal* não existem como vetor no
`.ai`: são objetos de degradê (`shading`), que não saem na extração. Foram
refeitas como dois `<rect>` com `linearGradient`, posicionados por medição
sobre o render do original.

Conferido pixel a pixel contra o original. **62 KB → 7,6 KB, sem perda visível.**

## Ainda falta

Nada. As derivadas raster só serão geradas depois da direção de arte
aprovada — derivar cedo é como nasce a duplicação.
