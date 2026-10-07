# branding-isc

**A identidade visual do Instituto ISC · Health & Aesthetics, empacotada como uma Skill do Claude.** Sistema Fio de Ouro v1.

Instale uma vez e peça o material em português. O Claude passa a produzir post, carrossel, story, reels, WhatsApp, site, proposta, receituário, apresentação, e-mail e impresso **já no padrão do ISC**: cor certa, fonte certa, marca certa, tom certo e as regras de publicidade médica do CFM, sem você precisar explicar nada disso de novo.

> "Faz um carrossel de 6 lâminas do ISC sobre como funciona a primeira consulta."
> "Monta um story no padrão do ISC chamando para agendar a avaliação."
> "Cria uma apresentação de 8 slides do Instituto para uma parceria."

**Ver o brand book no navegador:** [rafaelnasch.github.io/branding-isc](https://rafaelnasch.github.io/branding-isc/) (abre em qualquer aparelho, sem instalar nada).

---

## O que vem na caixa

| Arquivo | O que é |
|---|---|
| `SKILL.md` | O estilo inteiro, travado: cores, tipografia, a marca, as cinco leis, voz, publicidade médica, medidas de cada peça, celular e PDF. É o que o Claude lê. |
| `brand-book.html` | **Abra primeiro.** O manual vivo em 24 seções, com modelos de peça em tamanho real, e o template pronto de **documento**. |
| `deck-template.html` | O esqueleto de **apresentação**: dez tipos de slide em 1440 × 900, navegação por seta, notas na tecla **P**. |
| `lockup.html` | Os snippets prontos: marca em arquivo e em data URI, símbolo e avatar, favicon, bloco de identificação médica, fio de ouro, título com itálico, respiro e assinatura de e-mail. |
| `iviz.js` | Motor de gráficos em SVG puro: barras, ranking, linha, composição, anel, funil, fluxo, número em destaque, linha do tempo e cota. |
| `iforms.js` | Motor de formas da casa, derivadas do símbolo: fio, ponto, órbita, elo, grade, camadas, percurso, integrado, tempo, cortina e prancha. |
| `dist/` | **Para enviar a alguém.** Versões de arquivo único (imagens, fontes e motores embutidos): `brand-book-isc.html`, `apresentacao-isc.html` e `assinaturas-isc.html`. Abrem sozinhas no e-mail, WhatsApp, Drive e celular. |
| `autocontido.py` | Gera o `dist/` de novo: `python3 autocontido.py`. Também transforma qualquer HTML novo feito com a skill: `python3 autocontido.py meu-material.html`. |
| `exportar_pdf.py` | Exporta documento ou apresentação em PDF com o Playwright. |
| `agents/openai.yaml` | Nome, descrição, ícone e pedido de exemplo da skill no Codex e no ChatGPT (o Claude ignora). |
| `tools/empacotar_skill.py` | Gera o ZIP do Releases dentro dos limites e falha se algum estourar. |
| `assets/` | A marca em SVG e PNG (horizontal, vertical, símbolo, avatar e favicon, em ouro, preto, branco e ouro chapado), as fotos reais do Instituto já tratadas (`fotos/`), as fontes (`fontes/`) e o arquivo original do designer (`referencia-original/`). |

## Instalar

O nome da pasta tem que ser exatamente `branding-isc`, com o `SKILL.md` dentro. A mesma pasta serve ao Claude, ao Codex e ao ChatGPT: segue o padrão aberto [Agent Skills](https://agentskills.io/specification).

### Claude Code (terminal, VS Code, app de desktop)

```bash
git clone https://github.com/rafaelnasch/branding-isc.git ~/.claude/skills/branding-isc
```

Abra uma sessão nova e digite `/branding-isc`, ou simplesmente peça "faz no padrão do ISC". Para atualizar:

```bash
cd ~/.claude/skills/branding-isc && git pull
```

### Codex (CLI, extensão de IDE e app de desktop)

```bash
git clone https://github.com/rafaelnasch/branding-isc.git ~/.agents/skills/branding-isc
```

O Codex lê `~/.agents/skills/`; versões anteriores leem `~/.codex/skills/` (mesmo comando, trocando a pasta). O `agents/openai.yaml` dá o nome, a descrição, o ícone e o pedido de exemplo que aparecem na lista de skills. Para atualizar: `cd ~/.agents/skills/branding-isc && git pull`.

### claude.ai (navegador e celular) e ChatGPT

1. Baixe o pacote pronto na página de **[Releases](https://github.com/rafaelnasch/branding-isc/releases/latest)**: o arquivo `branding-isc.zip`.
2. No claude.ai, vá em **Configurações, Capacidades, Skills** e envie o ZIP. No ChatGPT, envie o mesmo ZIP onde o app oferecer Skills; o caminho do menu muda conforme a versão do app.

> Use o ZIP do Releases, **não** o "Code, Download ZIP" do GitHub: aquele vem com o nome da pasta trocado (`branding-isc-main`), traz o repositório inteiro (com o `dist/` e o arquivo original do designer) e a skill sobe com o nome errado.

O pacote leva `SKILL.md`, `agents/openai.yaml`, o manual, os modelos, os motores, os scripts, a marca (SVG, PNG web, favicon, avatar, imagem de compartilhamento), as fotos reais, formas, gráficos, destaques, grades, ícones em SVG e as fontes. **Ficam fora do ZIP** e continuam no endereço público [rafaelnasch.github.io/branding-isc](https://rafaelnasch.github.io/branding-isc/): o arquivo original do designer, as PNG da marca em resolução de impressão, os ícones em PNG, as capturas do manual e o `dist/`. Dentro do pacote, o manual aponta para essas URLs. No navegador o material sai como arquivo único, com a marca em data URI do `lockup.html` e os motores embutidos; só o PDF muda: a skill entrega o HTML e você imprime pelo Chrome (instruções abaixo).

**Gerar o pacote** (para subir num Release novo): `python3 tools/empacotar_skill.py` grava `dist-skill/branding-isc.zip` (fora do git) e falha se algum limite abaixo estourar.

### Limites atendidos (conferidos em 07/10/2026)

| Limite | Regra | Esta skill |
|---|---|---|
| `name` | minúsculas, números e hífen, até 64, igual ao nome da pasta | `branding-isc` (12) |
| `description` | até 1.024 caracteres, sem `<` e `>`; caso de uso e gatilhos no começo | 788 caracteres |
| Campos do frontmatter | só os da especificação | `name` e `description` |
| `SKILL.md` | menos de 500 linhas | 335 linhas |
| Links relativos | todo link do `SKILL.md` aponta para arquivo do pacote | 0 quebrados |
| ZIP | até 30 MB (meta 10 MB) | 5,80 MB |
| Descompactado | até 25 MB | 8,10 MB |
| Arquivos | até 400; nenhum acima de 10 MB; nomes só com letras, números, ponto, hífen e sublinhado | 212; o maior é o `brand-book.html` (1,35 MB) |
| Estrutura | uma pasta `branding-isc/` no topo, um só `SKILL.md` | sim |
| Validador oficial | `skills-ref validate` (agentskills/agentskills) | "Valid skill: branding-isc" no pacote e no repositório |

Os limites de nome, descrição, campos e linhas são os da [especificação Agent Skills](https://agentskills.io/specification); os de tamanho são as travas do `tools/empacotar_skill.py`, mais rígidas que as dos apps.

## O primeiro teste

Abra uma conversa nova e peça:

> "Faz um post 1080 × 1350 no padrão do ISC sobre a primeira consulta."

Se vier campo preto (ou marfim), título em serifa com **uma** palavra em itálico dourado, a marca ou o símbolo em ouro só sobre o preto, um único próximo passo ("Agende sua avaliação") e nenhuma promessa de resultado, está funcionando. Se vier um post genérico, a skill não carregou: feche e abra o Claude de novo e confira se a pasta se chama exatamente `branding-isc` e tem o `SKILL.md` dentro.

## Usar

- **"faz no padrão do ISC"** já aciona a skill;
- diga **qual peça** (carrossel, post, story, reels, status de WhatsApp, proposta, receituário, apresentação, e-mail, cartão) e **o tema**: a skill já sabe a medida de cada formato;
- diga se é para **ler** (documento) ou para **apresentar** (deck);
- os números de CRM e RQE saem como `[nº]` até o Instituto confirmar: preencha antes de publicar;
- para **PDF**: abra o HTML no Chrome, espere uns 3 segundos, `Cmd+P`, **Salvar como PDF** e, em "Mais configurações", ligue **Gráficos de segundo plano**. Sem isso o fundo preto some. Apresentação: layout **Paisagem**, margens **Nenhuma**.

## As cinco leis da casa

1. **O ouro só brilha sobre preto.** No marfim ou no branco, a marca é preta e o destaque é marrom.
2. **O metal é da marca.** O dourado metálico vive no símbolo e nas letras ISC. Um elemento metálico por peça; o resto do ouro é um fio fino, no máximo 5% da área.
3. **Uma ideia por peça, um itálico por título.** Se falta espaço, corta-se texto, nunca margem.
4. **Foto real, luz quente.** Só o Instituto, a equipe e o trabalho verdadeiro. Banco de imagem nunca.
5. **Critério antes de promessa.** Nenhum resultado prometido, nenhum superlativo, nenhuma técnica proibida, e a identificação médica sempre que o CFM exigir.

## A marca

O logotipo do ISC **nunca** é redesenhado, redigitado, recolorido fora das versões ou vetorizado por conta própria. É sempre um dos arquivos de `assets/`. Fundo preto pede a versão em ouro metálico; fundo claro pede a preta; foto escura pede a branca; bordado, carimbo e gravação pedem o ouro chapado. Abaixo de 72 px (avatar, lista de conversas, favicon) entra só o símbolo. Respiro, tamanhos mínimos e os erros proibidos estão no `SKILL.md` e na seção 01 do brand book.

## Pendências com o ISC

Até cada uma ser resolvida, a skill entrega só a versão permitida:

1. Licença comercial da fonte usada no "ISC" do logotipo.
2. Validação, pelo designer, das versões derivadas (branca, ouro chapado, vertical, símbolo, avatar, favicon).
3. CRM e RQE de cada médico, registro da clínica e Diretor Técnico-Médico.
4. Uso público da leitura "Integrated Systemic Care" e nome registrado no CRM-PR (o nome principal já é "Instituto ISC").
5. WhatsApp oficial, e-mail institucional, horário, site e domínio.
6. Cores das submarcas e da paleta em reserva do designer.
7. Troca do letreiro e sessão de fotos.
8. Cores de gráfica (CMYK e Pantone).
9. Disponibilidade das fontes no Canva e no editor de vídeo.
10. Missão e valores escritos (resolvida em 27/09/2026, ver 07.8).
11. Validação regulatória antes de anunciar a medicina regenerativa.
12. Revisão de nome, bio e cadastros dos perfis.

Detalhe de cada uma na seção 23 do brand book.

## Navegador

Chrome, Edge ou Safari recentes (iOS 16 ou mais novo, Chrome 105 ou mais novo).

---

Marca, símbolo e logotipo são propriedade do **Instituto ISC**. Os motores `iviz.js` e `iforms.js` foram escritos para este sistema. Sistema de identidade organizado com a GrowAI. Fio de Ouro v1 · setembro de 2026.
