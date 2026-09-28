---
name: branding-isc
description: "A identidade visual do Instituto ISC · Health & Aesthetics (Curitiba) no sistema Fio de Ouro v1: Preto ISC e Marfim como campos, o ouro só sobre preto, o metal só na marca, Gilda Display nos títulos com uma palavra em EB Garamond Italic, Montserrat no texto, foto real com luz quente, as cinco leis da casa, o bloco de identificação médica e as regras de publicidade médica do CFM, motores de gráfico (iviz) e de forma (iforms). Use para qualquer material do ISC ou do Dr. Sharbo Casagrande: post, carrossel, story, reels, WhatsApp, site, proposta, receituário, apresentação, e-mail e impresso. Triggers: /branding-isc, branding isc, marca isc, padrão isc, identidade isc, instituto isc, isc instituto, material do isc, post do isc, deck do isc, dr sharbo, sharbo casagrande, fio de ouro."
---

# /branding-isc · A identidade visual do Instituto ISC

Um estilo de casa travado, chamado **Fio de Ouro**. O nome vem do traço vertical dourado do logotipo, que separa o símbolo do nome. O ISC fala como uma revista de medicina bem desenhada: **título sereno em serifa, campo preto ou marfim, o ouro como fio fino e uma única palavra em itálico.** Cada peça explica antes de indicar e nunca promete resultado. Vale para **todo** material do Instituto ISC e do Dr. Sharbo Casagrande: post, carrossel, story, reels, WhatsApp, site, proposta, receituário, apresentação, e-mail, impresso e sinalização.

Palavras-guia: sóbrio, preciso, acolhedor, médico, de alto padrão. Nunca: gritado, brilhante, milagroso, genérico de luxo.

**Abra PRIMEIRO:** [`brand-book.html`](brand-book.html), o estilo documentando a si mesmo em 24 seções, com a marca, as fichas de cor, as escalas, os modelos de peça em tamanho real e as regras do CFM. O `<head>` e a `<style>` dele são o template portátil de **documento**. Para **apresentação**, o esqueleto pronto é [`deck-template.html`](deck-template.html). Os motores vivem em [`iviz.js`](iviz.js) (dados) e [`iforms.js`](iforms.js) (formas). Os snippets da marca, do bloco de identificação e do e-mail estão em [`lockup.html`](lockup.html). Quando a peça parece com esses arquivos, está certa.

---

## Onde a skill roda (e o que muda em cada lugar)

| Ambiente | Onde instalar | O que muda |
|---|---|---|
| **Claude Code** (terminal, VS Code, app de desktop) | `~/.claude/skills/branding-isc` | Nada. Ambiente completo: escreve arquivo, usa `assets/`, exporta PDF. |
| **Codex CLI** | `~/.codex/skills/branding-isc` | Nada. |
| **claude.ai** (navegador e celular) | Settings, Capabilities, Skills (ZIP do Releases) | **O artefato é um arquivo só: não enxerga `assets/` nem os `.js`.** |

**REGRA DO NAVEGADOR (claude.ai):** todo HTML gerado ali é **autocontido**.
1. **Marca:** use os blocos em **data URI** do [`lockup.html`](lockup.html) (bloco 04, ouro; bloco 05, preta; bloco 06, símbolo). Copie o `src` inteiro; nunca digite, resuma ou reconstrua um data URI.
2. **Fotos:** gere o data URI por código a partir do arquivo de `assets/fotos/`, sem alterar a imagem.
3. **Motores:** cole `iviz.js` e `iforms.js` dentro de um `<script>` do próprio arquivo.
4. **Fontes:** continuam pelo link do Google Fonts.
5. **PDF:** entregue o HTML e mande imprimir pelo Chrome (seção "Exportar PDF").

**Para ENVIAR um HTML a alguém**, use sempre a versão autocontida: `python3 autocontido.py <arquivo.html>` grava em `dist/` com imagens, fontes e motores embutidos. As versões prontas do brand book, da apresentação e das assinaturas já estão em `dist/`.

## Cores (TRAVADAS)

O sistema **não tem modo escuro automático**: preto e marfim são escolha editorial. `body` sempre com background explícito e `color-scheme: light`.

**Dois campos.** **Preto ISC** para o que chama atenção (capa, redes, abertura, story). **Marfim** para o que se lê com calma (miolo de carrossel, documento, proposta, receituário, site em leitura longa). Branco puro só em papel de escritório e documento técnico.

| Token | Nome | HEX | Origem | Uso |
|---|---|---|---|---|
| `--preto` | Preto ISC | `#121314` | vetor oficial | campo principal |
| `--ouro` | Ouro ISC | `#D69F56` (antes `#D39A1F`) | tom do meio do degradê do símbolo; **proposta a validar** | chapado só onde o degradê não cabe (impressão em uma cor, ícone pequeno) |
| `--ouro-degrade` | Ouro com degradê | `linear-gradient(120deg,#F1DDC0,#E6C28A 28%,#D69F56 58%,#C3791C)` | pedido do Instituto em 27/09/2026 | **todo dourado sobre preto**: itálico, rótulo, fio, ponto, botão e numeral. Nunca ouro chapado cor de mostarda |
| `--metal` | Ouro metálico | `linear-gradient(135deg,#FFFFFF 0%,#F1DDC0 16%,#E6C28A 34%,#D69F56 54%,#D19644 66%,#C9862E 82%,#C3791C 100%)` | vetor oficial | **só** na marca e no numeral de abertura sobre preto (≥ 96 px) |
| `--champanhe` | Champanhe | `#F1DDC0` | tom do gradiente | texto quente sobre preto |
| `--ouro-claro` | Ouro claro | `#E6C28A` | tom do gradiente | palavra em itálico sobre preto |
| `--cobre` | Cobre | `#C3791C` | ponta do gradiente | detalhe gráfico sobre preto; nunca texto pequeno |
| `--bronze` | Bronze | `#462214` | contorno do vetor | fio e detalhe sobre marfim |
| `--marrom` | Marrom | `#5E3118` | paleta do designer | a ênfase **sobre marfim**: itálico, numeral, link |
| `--branco` | Branco | `#FFFFFF` | vetor oficial | título sobre preto |
| `--branco-quente` | Branco quente | `#F8EEE0` | extensão | texto corrido sobre preto |
| `--marfim` | Marfim | `#F5F0E6` | extensão editorial | o papel |
| `--areia` · `--noite` | Areia · Noite | `#EBE3D3` · `#1B1C1E` | extensão | painel sobre marfim · painel sobre preto |
| `--fumaca` · `--pedra` · `--grafite` | apoio | `#A8A198` · `#6B645B` · `#34312D` | extensão | apoio no preto · apoio no marfim · texto no marfim |
| `--fio-claro` · `--fio-escuro` | fios | `#D9CDB8` · `#2E2D2B` | extensão | linhas de 1 px |

**Pares de leitura (contraste WCAG):** branco/preto 18,6 · champanhe/preto 14,0 · ouro/preto 7,5 · fumaça/preto 7,3 · preto/marfim 16,4 · grafite/marfim 11,4 · marrom/marfim 9,6 · pedra/marfim 5,1 · preto/ouro 7,5. **Proibidos:** ouro sobre marfim (2,2), branco sobre ouro (2,5), branco sobre cobre em texto pequeno (3,5). Texto sobre ouro é sempre Preto ISC.

**Orçamento do ouro (LEI):** ouro chapado mais metal ocupam no máximo **5% da área** da peça e marcam **uma** informação. **Um único elemento metálico por peça** (o símbolo no post, o logotipo no story). Proporção medida no conjunto das peças do mês: Preto 45 · Marfim 35 · Branco e champanhe 10 · Ouro 6 · Marrom 3 · Metal 1.

**Em reserva (não usar sem decisão):** as outras cores do arquivo do designer (marrom escuro `#402C11`, âmbar `#C98302`, `#D7A241`, marinhos `#0B153B` `#03151F` `#032130`, roxo, ouro de gráfica). **ISC REGEN** usa as cores do Instituto (preto, marfim, ouro e cobre), com o verde petróleo `#1D4B48` como cor secundária para uma leve diferença; laranja mais escuro é alternativa em avaliação, não usar ainda. A **Benessere** usa tons de verde como principais (tom a definir). Ambas usam o mesmo logotipo do Instituto. O verde nunca vai na marca-mãe. CMYK e Pantone dependem de prova de gráfica; metal no papel é hot stamping ou ouro chapado, nunca amarelo.

## Tipografia (TRAVADA)

```html
<link href="https://fonts.googleapis.com/css2?family=Gilda+Display&family=EB+Garamond:ital,wght@1,400;1,500&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">
```

| Papel | Fonte | Regras |
|---|---|---|
| Títulos, numerais de seção, números grandes | **Gilda Display 400** | ≥ 28 px na tela da peça (no documento, o intertítulo desce a 23 px no celular). Entrelinha 1,02 a 1,12. Caixa normal. É a serifa gratuita mais próxima do "ISC" do logotipo entre as que acentuam o português corretamente. |
| A palavra de ênfase | **EB Garamond Italic 400** (500 abaixo de 40 px e em vídeo) | **Uma** palavra (ou expressão curta) por título, no mesmo tamanho. Ouro ou ouro claro sobre preto; marrom sobre marfim. Nunca parágrafo em itálico. |
| Texto, rótulo, botão, dado, legenda | **Montserrat** 400 · 500 · 600 | Corpo 400. Rótulo 500 em caixa alta com `letter-spacing:.2em`. Assinatura estilo "INSTITUTO": 400, caixa alta, `.358em`. Nunca Light sobre preto. |

- **Escala do documento (tela/celular):** display 112/52 · título de seção 64/38 · subtítulo 40/28 · intertítulo 28/23 · chamada 21/18 · corpo 17/16 (entrelinha 1,65 a 1,7) · apoio 15 · legenda 13 · rótulo 11. Montserrat só nesses corpos. `font-variant-numeric: lining-nums`.
- **Escala da peça 1080 px** (unidade `--u: calc(100cqw/1080)`): título 96 a 112 (máximo 3 linhas) · subtítulo 56 · chamada e corpo 32 a 36 · rótulo 26 (+0,2 em) · **piso absoluto de 26 px para qualquer texto, inclusive CRM e RQE** (o post aparece a cerca de 36% no celular) · margem 72 · fio 2 a 3.
- **Legenda de reels:** Montserrat 500 branca, 1 a 3 palavras por vez, na altura do peito, sem caixa; a palavra-chave em EB Garamond Italic 500 a 1,2×.
- **Por que não Cormorant Garamond:** a versão do Google Fonts desloca os acentos (é, ú, ê, ô) no navegador. **Por que não The Seasons:** é a fonte do ISC do logotipo, mas o arquivo usado é demo; nunca digite texto nela. Se Gilda ou EB Garamond faltarem numa ferramenta, a alternativa é **Playfair Display** (título e itálico).

## A marca (TRAVADA)

Arquivo oficial: CorelDRAW do designer da marca, 31/08/2026 (`assets/referencia-original/`). A marca é **sempre um arquivo** de `assets/`: nunca redesenhe, redigite "ISC" em fonte, recolora fora das versões, gire, estique, aplique sombra, brilho ou relevo.

| Versão | Arquivo | Status | Fundo |
|---|---|---|---|
| Horizontal ouro metálico | `isc-horizontal-ouro.svg` / `-web.png` / `.png` (e `-ouro-fundo`) | **Oficial** | Preto ISC, Noite, foto escura com sombra de leitura |
| Horizontal preta | `isc-horizontal-preto.*` | **Oficial** | marfim, branco, areia |
| Horizontal branca | `isc-horizontal-branco.*` | Derivada | foto escura, vídeo |
| Ouro chapado | `isc-horizontal-ouro-chapado.*` (e símbolo, vertical) | Derivada | bordado, carimbo, gravação, hot stamping |
| Vertical | `isc-vertical-{ouro,preto,branco,ouro-chapado}.*` | Derivada | espaço estreito e alto |
| Símbolo | `isc-simbolo-{ouro,preto,branco,ouro-chapado}.*` | Derivada | avatar pequeno, rodapé de peça, selo |
| Avatar circular | `isc-avatar.svg` / `isc-avatar-1080.png` | Derivada | só grande (capa de perfil, 1080) |
| Favicon | `isc-favicon.svg` / `-32` `-180` `-512.png` | Derivada | aba do navegador, atalho |

"Derivada" = extraída do vetor oficial sem mexer nas curvas; rotule "aguarda validação do designer" em material de apresentação da marca.

- **Respiro:** x = 2 × o diâmetro de um ponto do símbolo. Na horizontal, x ≈ 6% da largura do logotipo; na vertical, 9%; no símbolo sozinho, 17%.
- **Tamanho mínimo:** horizontal 160 px na tela e 40 mm no impresso; vertical 120 px; símbolo 24 px e 8 mm. Abaixo de 72 px (avatar, lista de conversas, favicon), **só o símbolo**.
- **O ouro metálico só vive sobre preto.** No claro, a marca é preta.
- **Letreiro antigo** ("Instituto Sharbo Casagrande" com monograma cobre) fica fora do quadro em qualquer foto. Os estudos coloridos de avatar feitos em IA não são arte oficial.

## As cinco leis da casa (TRAVADAS)

1. **O ouro só brilha sobre preto.** No marfim ou no branco, a marca é preta e o destaque é marrom. Ouro nunca é texto sobre fundo claro.
2. **O metal é da marca.** O gradiente vive no símbolo, nas letras ISC e no numeral de abertura sobre preto. Um elemento metálico por peça; o resto do ouro é chapado, fino e ocupa no máximo 5% da área.
3. **Uma ideia por peça, um itálico por título.** Se falta espaço, corta-se texto, nunca margem.
4. **Foto real, luz quente.** Só o Instituto, a equipe e o trabalho verdadeiro. Banco de imagem nunca; letreiro antigo fora do quadro.
5. **Critério antes de promessa.** Nenhum resultado prometido, nenhum superlativo, nenhuma técnica proibida (PMMA em lugar nenhum: arte, legenda, hashtag, texto alternativo, post antigo), identificação médica sempre que o CFM exigir.

## Arquitetura de marca

| Marca | Papel | Assina com |
|---|---|---|
| **Instituto ISC** (marca-mãe) | contém todos os serviços da casa; vitrine de todo o corpo clínico; @instituto.isc publica tudo o que se faz no Instituto | logotipo ISC + bloco da clínica |
| **Dr. Sharbo Casagrande** (marca pessoal) | autoridade e alcance; @drsharbo publica só os procedimentos que ele faz | bloco do médico; o ISC entra como "Atende no Instituto ISC" |
| **ISC REGEN** (submarca) | medicina regenerativa: ortobiológicos, medicina esportiva, ortopedia e estética regenerativa; ISC = Integrated Systemic Care | mesmo logotipo; cores do Instituto + verde secundário; validar enquadramento regulatório antes de anunciar |
| **Benessere** (submarca) | clínica de acupuntura, saúde e bem-estar ("bem-estar" em italiano) | mesmo logotipo do ISC; verde como cor principal, tom a definir |
| **ISC Academy** (submarca) | educação médica: cursos feitos no Instituto, do Dr. Sharbo e eventualmente de outros médicos; público médico, nunca nos perfis de pacientes | nome em texto com o arquivo do ISC; assinatura própria a definir |
| **Vitalize ISC** (produto) | acompanhamento presencial de emagrecimento, saúde hormonal e longevidade; pode ter nutrição e treino associados | nome em texto com a marca-mãe; sem logotipo próprio; nome público a validar |
| **ISC HEALTH** (produto) | o mesmo acompanhamento, online | idem; validar formato (telemedicina, sem pacote) |
| **Volupta** (produto) | protocolo de volumização e preenchimento de glúteo | idem; nunca citar PMMA; nome público a validar |

Outros produtos podem entrar e seguem a mesma regra: nome em texto, assinatura do Instituto ISC.

Nunca assinar peça do Instituto como se fosse do médico, nem o contrário. Nome principal em texto corrido, fala e atendimento: **"Instituto ISC"**. "ISC Instituto" é a forma secundária, como o logotipo se lê (seção 02). "ISC" sempre em maiúsculas; "Health & Aesthetics" com &; **Sharbo Casagrande** (nunca Charbo, Casa Grande).

## Voz e tom

Autoridade médica que explica com critério. Acolhimento sem intimidade forçada. Frase curta, verbo concreto, número com fonte. A consulta é sempre o primeiro passo.

- **Diga:** avaliação, indicação, critério, acompanhamento, "a consulta é sempre o primeiro passo", "depende da avaliação".
- **Nunca:** garantido, sem risco, milagre (só em negação), resultado surpreendente, transformação real, tecnologia de ponta, referência em, o melhor, exclusivo, tudo em um só lugar, livre da dor, emagreça rápido, "medicina estética" como especialidade, "especialista" sem RQE.
- **CTAs aprovados:** "Agende sua avaliação" · "Fale com a equipe" · "Entenda se é indicado para você" · "Saiba como funciona a consulta".
- **Pontuação:** zero travessão em título; no máximo uma exclamação; zero emoji na arte (emoji em legenda e WhatsApp é pendência de decisão: até lá, zero).
- **Remarcação e cancelamento (WhatsApp e e-mail):** a mensagem afirma o compromisso ("Seu horário fica reservado para você."). Nunca oferecer remarcar ou desmarcar ("Para remarcar, é só responder", "se não puder vir, avise"); remarcação só quando o paciente pedir (modelo 07 da seção 15).

## Publicidade médica (CFM) · TRAVADA

Base: Resolução CFM 2.336/2023 (em vigor desde 11/03/2024) + Manual de Publicidade Médica CFM/Codame 2024 + Código de Ética Médica (arts. 75 e 111 a 117) + Resolução CFM 2.461/2026 (PMMA proibido como preenchedor desde 02/06/2026) + Resolução CFM 2.454/2026 (IA em peça segue as mesmas regras). Detalhe e fontes na seção 08 do brand book. **Este manual não substitui assessoria jurídica.**

**Bloco de identificação** (mesma fonte, mesmo tamanho, mesma cor em todos os itens; snippet no bloco 08 do `lockup.html`):
- Médico: `Dr. Sharbo Casagrande · MÉDICO · CRM-PR [nº]` e, **só quando a peça citar especialidade**, `[Especialidade] · RQE [nº]`.
- Clínica: `Instituto ISC · Registro CRM-PR [nº] · Diretor Técnico-Médico: [nome] · CRM-PR [nº]`.
- **Onde:** na bio das redes e **no texto da legenda de todo post**, em todas as redes (post, carrossel, story, reels, anúncio). **Nunca dentro da arte de rede social e nunca em tarja no vídeo** (decisão do Instituto em 27/09/2026, diferente da leitura do Manual CFM p. 71-73; confirmar com a Codame). Dentro da peça só em impresso, no rodapé da página inicial do site e no receituário. Na peça 1080, nunca abaixo de 26 px.
- **Números nunca inventados:** use `[nº]` até o Instituto confirmar.

**Essencial:** sem promessa de resultado; sem superlativo; sem preço de procedimento (preço de consulta pode); sem gratuidade, sorteio, pacote ou venda casada; sem depoimento de paciente sobre resultado; sem paciente identificável; nome comercial de aparelho não vira argumento. **Antes e depois:** só no formato educativo do Manual (vídeo ou página do site, com as condições da seção 08.6); nunca post solto, nunca anúncio pago; mama, glúteo e região íntima fora das redes. **PMMA:** fora de tudo o que sai a partir de 02/06/2026, nem para explicar, nem reaproveitado; o publicado antes dessa data pode ficar no ar (parecer jurídico do Instituto). PRP, ozônio, aspirado de medula e células: não anunciar antes de validar a situação regulatória (pendência).

**Quem aprova:** peça do Instituto, o Diretor Técnico-Médico; peça do perfil pessoal, o próprio médico. Nada vai ao ar sem aprovação escrita.

## Fotografia

Só fotos reais do Instituto e da equipe (`assets/fotos/`): cortina de correntes douradas (capa), sala com pendentes âmbar, sala de espera, consultório, sala de atendimento, lounge, retrato do Dr. Sharbo. Cor real com saturação levemente reduzida e sombra quente; monocromático quente só quando as poltronas laranja e verde competirem com o ouro. Texto sobre foto: sombra de Preto ISC subindo da base (receita CSS e Canva na seção 09), nunca caixa colorida. Recorte fechado, sem letreiro antigo, sem suporte de soro, sem corpo exposto. Nunca banco de imagem, nunca retrato com texto gravado. A sessão de fotos (equipe, mãos, atendimento, retratos em fundo preto quente, fachada nova; lente 35 a 50 mm) é pendência.

## Formas e dados

**`iforms.js`**: a ilustração da casa, derivada do logotipo sem imitá-lo. `<div class="forma-svg" data-iforms="orbita"></div>` ou `iforms.orbita(el, opts)`. Formas: `fio` (critério, estrutura), `ponto` (foco, decisão), `orbita` (cuidado contínuo), `elo` (dois pontos ligados pela curva em S: queixa e indicação), `grade` (precisão: o ponto certo entre muitos), `camadas` (cuidado integral), `percurso` (etapas da consulta), `integrado` (áreas que se cruzam), `tempo` (retorno e evolução), `cortina` (o espaço do Instituto), `prancha` (registro, documento). Uma forma por peça, ao lado do texto, nunca atrás. `iforms.svg(nome, opts)` devolve o SVG para colar no Canva.

**`iviz.js`**: gráficos em SVG puro. `<div class="grafico-svg" data-iviz='{"tipo":"barras","rotulos":["Jun","Jul"],"valores":[42,51],"destaque":1}'></div>`. Tipos: `barras`, `barras-h`, `linha`, `composicao`, `anel`, `funil`, `fluxo`, `kpi`, `linha-tempo`, `cota`. Um destaque (ouro no preto, marrom no marfim), o resto neutro; título que já diz a conclusão; fonte e data sempre; dado de exemplo rotulado "Dados ilustrativos". Nunca dado de paciente.

## Ícones

**Lucide** inline em SVG: traço 1,5, pontas arredondadas, 16/20/24 px, cor do texto ou ouro (preto) / marrom (marfim). Nunca emoji, nunca ícone colorido ou 3D, nunca misturar bibliotecas. WhatsApp não existe no Lucide: use `message-circle`. Ícone não substitui palavra em informação médica. Conjunto curado de 24 na seção 11.

## Componentes canônicos

Os nomes de classe são a interface do sistema: **nunca renomeie**. Todos estão na `<style>` do `brand-book.html` e na seção 13.

| Classe | Uso |
|---|---|
| `.sec` + `.sec--preta` / `.sec--marfim` · `.sec-head` · `.folio` | seção com fólio de revista e numeral (metálico no preto, marrom no marfim) |
| `.bloco` > `.bloco-head` (`.bloco-n` + `h3` + `.bloco-apoio`) | subseção numerada NN.1, NN.2 |
| `campo-preto` · `campo-noite` · `campo-marfim` · `campo-branco` · `campo-areia` · `.faixa` | troca de campo num pedaço ou de ponta a ponta |
| `.cols-2` `.cols-3` `.cols-4` `.cols-7-5` `.cols-5-7` `.cols-8-4` `.grade-12` | grades de 12 colunas que empilham no celular |
| `.enf` / `em` no título · `.rotulo` · `.assinatura` · `.lead` · `.legenda` | tipografia |
| `.fio` `.fio-v` `.fio--ouro` · `.ponto` · `.pilula` · `.selo` | motivos da casa |
| `.btn` + variantes (cheio lê o campo: ouro no preto, preto no marfim; `.btn--linha`) | botões, altura mínima 48 |
| `.nota` · `.alerta` | o primeiro `<strong>` vira o rótulo do cartão |
| `.faca` / `.nao-faca` · `.par` · `.nf-grid` > `.nf` | Assim / Não assim · galeria "Não faça" |
| `.cor` · pares de leitura | ficha de cor com contraste calculado |
| `.table-wrap` > `table.consulta` · `.table-wrap.matriz` | tabela que vira cartão no celular · matriz com rolagem local |
| `.kpi-grid` > `.kpi` > `.kpi-num` + `.kpi-rot` | número antes do rótulo |
| `.olho` | olho de revista (citação em EB Garamond Italic sobre fio) |
| `.id-medica` | bloco de identificação médica |
| `.prancha` · `.foto-sombra` | foto com passe-partout e fio · sombra de leitura |
| `.peca` + formato (post 4:5, quadrado, 3:4, story, reels, whats, doc A4/A5, cartão, e-mail, banner) · `.peca--segura` | mockups em escala real com `--u`; áreas seguras de story e reels |
| `.grafico` > `.grafico-svg[data-iviz]` · `.forma` > `.forma-svg[data-iforms]` | motores |
| `.checklist` > `.check-row` | checklist de aprovação |
| deck: `.slide` + `capa` `capa-clara` `secao` `ideia` `stat` `grafico` `compara` `citacao` `passos` `closer` · `aside.notas` | apresentação |

Espaço só na escala de 4 (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). Respiro lateral 48 px no desktop, 32 até 1024, 16 até 640.

## Aplicações (medidas na arte final)

| Peça | Formato | Regra principal |
|---|---|---|
| Carrossel | 1080 × 1350, margem 72 | capa com foto real de tela inteira, véu de Preto ISC (50% no alto, 90% na base), pergunta em branco e itálico champanhe; miolo marfim com numeral marrom; lâmina final com CTA e bloco de identificação; até 12 palavras no título da capa |
| Post único | 1080 × 1350 (4:5) ou 1080 × 1080 | até 15 palavras na arte; o resto vai na legenda |
| Story | 1080 × 1920 | faixas de 250 px no topo e na base livres; tudo importante nos 1420 do meio |
| Capa de reels | 1080 × 1920 | foto de tela inteira com véu; título e rosto dentro do recorte central 1080 × 1350 (feed) |
| Capa de destaque | 1080 × 1080 | ícone próprio de 580 px no degradê dourado, moldura dupla com quatro losangos (70 px da borda), preto com luz no centro; desenho proposto a validar |
| Avatar | símbolo sobre Preto ISC | composição completa só grande |
| Status de WhatsApp | 1080 × 1920 | tipográfico, com bloco de identificação dentro da peça |
| Receituário | A5 148 × 210 mm ou A4 | logo preto sobre branco; bloco do Diretor Técnico em retângulo branco com filete; espaço para carimbo |
| Cartão de visita | 85 × 55 mm (ou 90 × 50) | frente preta com marca ouro chapado; verso marfim com contatos e identificação |
| Proposta de tratamento | A4 | capa preta, miolo marfim; valor só na proposta individual ao paciente, nunca em material publicitário |
| Assinatura de e-mail | tabela de 600 px | compatível com Gmail e Outlook (bloco 13 do `lockup.html`) |
| Site | 12 colunas | hero sobre foto real com sombra de leitura; rodapé com o bloco da clínica; imagem de compartilhamento 1200 × 630 |
| Fachada e sinalização | por fundo | só a marca; aguarda o vetor validado e a troca do letreiro |

Detalhe completo, mockups e textos prontos nas seções 14 a 18.

## Dois formatos de primeira classe

**Documento** (`brand-book.html` é o template): leitura, proposta, relatório, one-pager. Uma coluna de leitura (máximo 680 px de texto), seções numeradas com fólio, sumário depois da introdução, alternância de campos como numa revista.

**Deck** (`deck-template.html`): reunião, palestra, projeção. Canvas 1440 × 900 escalado; `<section class="slide TIPO">` com os dez tipos acima; setas, espaço, Home/End e toque; barra de progresso; contador; **P** abre as notas; **F** tela cheia; `#3` abre o terceiro slide; no celular os slides empilham.

Vai ser **lido** → documento. Vai ser **apresentado** → deck.

## Mobile System v1 (TRAVADO)

Tudo legível e sem corte entre **320 e 430 px**. Breakpoints 1024 e 640 (e 380 para display). Grades empilham; tabelas de consulta viram cartões pelo script `<script data-isc-responsive="v1">` do fim do `brand-book.html` (copie literal); matriz larga com rolagem local sinalizada; `overflow-wrap:anywhere` em texto corrido; mídia com `max-width:100%`; botões de 48 px. **PROIBIDO `overflow-x:hidden` no `html` ou no `body`.**

## Exportar PDF

**Pelo Chrome:** abra o HTML, espere 3 segundos, `Cmd+P`, Salvar como PDF, **Gráficos de segundo plano LIGADO** (sem isso o preto some). Documento em retrato com margens padrão; deck em paisagem com margens nenhuma.

**Automatizado (Playwright):**
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1200, "height": 900})
    pg.goto("file:///caminho/brand-book.html", wait_until="networkidle"); pg.wait_for_timeout(3000)
    pg.emulate_media(media="print")
    pg.pdf(path="brand-book.pdf", format="A4", print_background=True,
           margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"})
    b.close()
```
Deck: viewport 1440 × 900 e `pg.pdf(width="1440px", height="900px", print_background=True, margin=0)`. O script `exportar_pdf.py` da pasta faz os dois. **Nunca use `--print-to-pdf` do Chrome.** No `@media print` o numeral metálico vira `#D69F56` sólido.

## Pendências com o ISC (não resolva por conta própria)

1. Licença comercial da fonte do "ISC" (The Seasons, arquivo demo).
2. Validação das versões derivadas pelo designer.
3. CRM e RQE de cada médico, registro da clínica no CRM-PR e nome do Diretor Técnico-Médico.
4. Uso público da leitura "Integrated Systemic Care" e nome registrado no CRM-PR (o nome principal já é "Instituto ISC").
5. WhatsApp oficial único, e-mail institucional, horário, site e domínio.
6. Tom exato do verde da Benessere, eventual laranja mais escuro de apoio no ISC REGEN e papel das cores em reserva (ISC REGEN, Benessere e ISC Academy já são submarcas do Instituto ISC).
7. Troca do letreiro físico e sessão de fotos.
8. CMYK e Pantone (prova de gráfica).
9. Gilda Display e EB Garamond no Canva e no editor de vídeo.
10. Missão e valores escritos: resolvida em 27/09/2026 (texto oficial em 07.8 do brand book e abaixo).
11. Situação regulatória de PRP, ozônio, aspirado de medula e células antes de anunciar o ISC REGEN.
12. Revisão de nome, bio e cadastros dos perfis para retirar qualquer menção a técnica proibida (o conteúdo publicado antes de 02/06/2026 fica, por parecer jurídico).

Quando uma peça esbarrar numa pendência, entregue a versão permitida (dado em `[nº]`, versão oficial da marca, sem o tema bloqueado) e diga em uma linha qual pendência trava o resto.

## Checklist de aprovação de peça

- [ ] Marca é arquivo oficial, versão certa para o fundo, com respiro e acima do mínimo; abaixo de 72 px, só o símbolo.
- [ ] Só cores da tabela; ouro nunca como texto no claro; um elemento metálico; ouro ≤ 5% da área.
- [ ] Gilda Display no título com **um** itálico em EB Garamond; Montserrat no resto; nenhum texto de peça 1080 abaixo de 26 px.
- [ ] Uma ideia por peça e um único próximo passo, com CTA aprovado.
- [ ] Foto real, luz quente, sem letreiro antigo, sem banco de imagem, sem paciente identificável.
- [ ] Nenhuma promessa, superlativo, preço de procedimento, sorteio, gratuidade ou depoimento de resultado.
- [ ] PMMA em lugar nenhum (arte, legenda, hashtag, alt, post antigo).
- [ ] Bloco de identificação na legenda do post (nunca na arte de rede social; no impresso, dentro da peça); RQE só com especialidade citada; números em `[nº]` se não confirmados.
- [ ] Zero travessão em título, zero emoji na arte, no máximo uma exclamação; "Sharbo Casagrande" com a grafia certa.
- [ ] Contraste AA; texto alternativo em toda imagem.
- [ ] Testado no celular: peça reduzida a 36% ainda se lê; página sem corte de 320 a 430 px.
- [ ] Aprovada por escrito (Diretor Técnico-Médico ou o próprio médico).

## Gotchas (vão te morder)

1. **Uma única `<style>` por arquivo.** Print e gráfico entram nela.
2. **A marca é arquivo, não código.** Se você está escrevendo `<path>` de logotipo, "ISC" em fonte ou data URI de memória, pare: use `assets/` ou o `lockup.html`. Nunca cole o SVG do logotipo no HTML (os ids internos colidem): use `<img>`.
3. **Ouro no marfim tem 2,2:1.** No claro, a ênfase é marrom `#5E3118`.
4. **Cormorant Garamond quebra acento** no navegador. Não use.
5. **`background-clip:text` vaza no PDF do Chromium:** no print o metal vira `#D69F56` sólido.
6. **IDs de SVG únicos** por página (prefixe).
7. **Data URI nunca digitado:** copie o bloco inteiro do `lockup.html`.
8. **CRM e RQE nunca inventados.** `[nº]` até o Instituto confirmar; RQE só com a especialidade citada.
9. **"Medicina estética" não é especialidade** reconhecida: não use como rótulo de médico.
10. **`print_background=True`** ou "Gráficos de segundo plano" ligado, senão o preto some.
11. **Caminho relativo sempre** (`assets/...`); para enviar, `python3 autocontido.py`.

## O que o Fio de Ouro NÃO é

- Não é luxo genérico: nada de mármore falso, brilho, glitter, 3D, folha de ouro simulada.
- Não é ouro espalhado: é um fio, uma palavra, um número.
- Não é gradiente em fundo, botão, moldura ou texto corrido.
- Não é banco de imagem, antes e depois solto ou corpo exposto.
- Não é promessa, superlativo ou "transformação garantida".
- Não é a marca redesenhada, recolorida ou digitada.
- Não é caixa alta longa, travessão em título ou emoji na arte.

---

Marca, símbolo e logotipo são propriedade do Instituto ISC. Sistema de identidade organizado com a GrowAI. Fio de Ouro v1 · setembro de 2026.

## Missão, visão e valores (oficial, 27/09/2026)

Use o texto literal; não parafraseie.

**Missão.** Transformar vidas de maneira integral. Transformar vidas de maneira integral, cuidando do corpo, acolhendo a alma e as emoções e valorizando a dimensão espiritual de pacientes, colaboradores e corpo médico, com amor cristão, excelência e respeito à singularidade de cada pessoa.

**Visão.** Crescer com propósito e excelência. Crescer com propósito e excelência, desenvolvendo continuamente as pessoas e as competências de todo o time, para ampliar nosso alcance e impactar positivamente cada vez mais vidas.

**Valores.**
- Princípios cristãos: Amar a Deus e ao próximo, seguindo o exemplo de Jesus em nossas atitudes e relações.
- Respeito e gentileza: Acolher cada pessoa com dignidade, escuta e sensibilidade.
- Alegria e satisfação: Cultivar um ambiente de gratidão, cooperação e realização no cuidado e no trabalho.
- Sofisticação e elegância: Expressar excelência na atenção aos detalhes, na comunicação e em cada experiência.
- Evolução e estudo contínuos: Aprender, compartilhar conhecimento e aperfeiçoar continuamente nossas práticas.

**Valores cristãos.**
- Amor: Amar a Deus e ao próximo, traduzindo esse amor em cuidado e acolhimento.
- Perdão: Praticar o perdão, favorecendo a reconciliação e relações saudáveis.
- Humildade: Reconhecer nossas limitações e manter a disposição para aprender e servir.
- Fé: Confiar em Deus e agir com responsabilidade, coerência e propósito.
- Esperança: Cultivar confiança nas promessas de Deus e encorajar novos caminhos.
- Paz: Promover o diálogo, a harmonia e a resolução respeitosa dos conflitos.
- Serviço: Servir com generosidade e dedicação, seguindo o exemplo de Jesus.
- Justiça: Agir com equidade, defender a dignidade humana e enfrentar a injustiça.
- Gratidão: Reconhecer as bênçãos de Deus e valorizar a contribuição de cada pessoa.
- Obediência: Orientar nossas escolhas pelos mandamentos de Deus e pelos ensinamentos de Jesus.
- Pureza: Cultivar pureza de coração, de pensamentos e de intenções, cuidando também do corpo.
- Honestidade: Viver com integridade, dizer a verdade e agir com transparência.
- Generosidade: Compartilhar tempo, conhecimento e recursos para ajudar quem precisa.

Versículos do documento: Provérbios 16:3 e Lucas 12:31. Valores cristãos orientam equipe e cultura; em peça pública, só quando o tema for a própria casa, nunca como argumento de venda.
