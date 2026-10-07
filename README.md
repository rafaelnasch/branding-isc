# branding-isc · a identidade visual do Instituto ISC como skill

**O que é:** a identidade visual do **Instituto ISC · Health & Aesthetics** (Curitiba) e do **Dr. Sharbo Casagrande**, empacotada como uma *skill*. Uma skill é um pacote de instruções e arquivos que o assistente de IA (Claude, Codex ou ChatGPT) carrega sozinho quando o pedido combina com ela.

**O que muda depois de instalar:** você pede o material em português, como pediria a um designer, e ele já sai **no padrão do ISC**. Isso vale para post, carrossel, story, reels, status de WhatsApp, site, proposta, receituário, apresentação, e-mail e impresso, com cor, fontes, marca e tom certos e com as regras de publicidade médica do CFM. Não é preciso explicar nada disso de novo a cada conversa.

> "Faz um carrossel de 6 lâminas do ISC sobre como funciona a primeira consulta."
> "Monta um story no padrão do ISC chamando para agendar a avaliação."
> "Cria uma apresentação de 8 slides do Instituto para uma parceria."

**Ver o manual da marca sem instalar nada:** [rafaelnasch.github.io/branding-isc](https://rafaelnasch.github.io/branding-isc/) (abre em qualquer aparelho).

**Baixar o pacote de instalação (ZIP):** [branding-isc.zip](https://github.com/rafaelnasch/branding-isc/releases/latest/download/branding-isc.zip). O link entrega sempre a versão mais recente.

---

## Sumário

1. [Antes de começar: qual caminho é o seu](#1-antes-de-começar-qual-caminho-é-o-seu)
2. [Instalar no Claude pelo navegador (claude.ai)](#2-instalar-no-claude-pelo-navegador-claudeai)
3. [Instalar no Claude Code](#3-instalar-no-claude-code)
4. [Instalar no Codex](#4-instalar-no-codex)
5. [ChatGPT](#5-chatgpt)
6. [Conferir se funcionou](#6-conferir-se-funcionou)
7. [Como a skill funciona por dentro](#7-como-a-skill-funciona-por-dentro)
8. [Como pedir: o pedido que dá certo](#8-como-pedir-o-pedido-que-dá-certo)
9. [O que você recebe e como finalizar](#9-o-que-você-recebe-e-como-finalizar)
10. [As regras que a skill aplica sozinha](#10-as-regras-que-a-skill-aplica-sozinha)
11. [Atualizar, compartilhar com a equipe e remover](#11-atualizar-compartilhar-com-a-equipe-e-remover)
12. [Problemas comuns](#12-problemas-comuns)
13. [O que vem no repositório](#13-o-que-vem-no-repositório)
14. [Pendências com o Instituto](#14-pendências-com-o-instituto)
15. [Para quem mantém a skill](#15-para-quem-mantém-a-skill)

---

## 1. Antes de começar: qual caminho é o seu

| Você usa | Caminho | Precisa de | Tempo |
|---|---|---|---|
| **Claude no navegador ou no app** (claude.ai) | [Seção 2](#2-instalar-no-claude-pelo-navegador-claudeai): envia o ZIP | Conta Claude (Free, Pro, Max, Team ou Enterprise) e um computador para o envio | 3 minutos |
| **Claude Code** (terminal, VS Code, app de desktop) | [Seção 3](#3-instalar-no-claude-code): um comando | Git instalado | 1 minuto |
| **Codex** (app, CLI ou extensão de IDE) | [Seção 4](#4-instalar-no-codex): um comando | Git instalado | 1 minuto |
| **ChatGPT** | [Seção 5](#5-chatgpt) | Depende do que a sua conta libera | Leia a seção |

**Regra de ouro para o ZIP:** use sempre o link de download acima ou a página de [Releases](https://github.com/rafaelnasch/branding-isc/releases/latest). **Nunca** use o botão verde "Code > Download ZIP" do GitHub. Esse botão baixa o repositório inteiro, com a pasta chamada `branding-isc-main`, e a skill sobe com o nome errado ou grande demais.

---

## 2. Instalar no Claude pelo navegador (claude.ai)

Faça uma vez, no computador. Depois disso a skill fica na sua conta.

**Passo 1 · Ligue a execução de código** (só na primeira vez)
1. Abra [claude.ai](https://claude.ai) e entre na sua conta.
2. Vá em **Configurações** (Settings) > **Capacidades** (Capabilities).
3. Ligue **Execução de código e criação de arquivos** (Code execution and file creation). Sem isso, nenhuma skill funciona.

> Em conta **Team** ou **Enterprise**, quem administra a organização precisa ter liberado skills e execução de código. Se a opção não aparecer, peça ao administrador.

**Passo 2 · Baixe o pacote**
- Clique em [branding-isc.zip](https://github.com/rafaelnasch/branding-isc/releases/latest/download/branding-isc.zip). Ele tem cerca de 6 MB.
- **Não descompacte.** O Claude recebe o ZIP do jeito que ele veio.

**Passo 3 · Envie a skill**
1. No claude.ai, abra **Personalizar** (Customize) > **Skills**.
2. Clique em **+** e depois em **Criar skill** (Create skill).
3. Escolha **Enviar uma skill** (Upload a skill) e selecione o `branding-isc.zip`.
4. A skill `branding-isc` aparece na lista. Confira se a chave ao lado dela está **ligada**.

**Passo 4 · Teste**
- Abra uma **conversa nova** e siga a [seção 6](#6-conferir-se-funcionou).

**Bom saber no navegador:** o que o Claude cria ali sai como **arquivo único** (um HTML com marca, imagens e motores embutidos), porque o artefato não enxerga as outras pastas do pacote. A skill já sabe disso e faz sozinha. Para virar PDF, veja a [seção 9](#9-o-que-você-recebe-e-como-finalizar).

---

## 3. Instalar no Claude Code

Abra o terminal e rode:

```bash
git clone https://github.com/rafaelnasch/branding-isc.git ~/.claude/skills/branding-isc
```

1. Abra uma sessão **nova** do Claude Code.
2. Digite `/branding-isc` para chamar a skill na hora, ou só peça "faz no padrão do ISC", e ela entra sozinha.

No Claude Code o ambiente é completo: a skill grava os arquivos no seu computador, usa as fotos e a marca de `assets/` e exporta PDF direto (`exportar_pdf.py`).

> **Para um projeto só:** se preferir que a skill valha apenas dentro de uma pasta de projeto, clone em `<pasta-do-projeto>/.claude/skills/branding-isc`.

---

## 4. Instalar no Codex

Abra o terminal e rode:

```bash
git clone https://github.com/rafaelnasch/branding-isc.git ~/.agents/skills/branding-isc
```

1. Reinicie o Codex (app, CLI ou extensão de IDE).
2. Digite `/skills` para ver a lista. A skill aparece como **Instituto ISC · Fio de Ouro**, nome dado pelo arquivo `agents/openai.yaml`.
3. Para chamar a skill na hora, escreva `$branding-isc` no começo do pedido. Ou só peça "faz no padrão do ISC", e ela entra sozinha.

> **Versões antigas do Codex** leem `~/.codex/skills/` em vez de `~/.agents/skills/`. Se a skill não aparecer em `/skills`, rode o mesmo comando trocando a pasta de destino.

---

## 5. ChatGPT

O ChatGPT usa o mesmo formato de skill (pasta com `SKILL.md`), e este pacote já traz o arquivo que o ChatGPT e o Codex leem para mostrar nome, ícone e pedido de exemplo (`agents/openai.yaml`).

**O envio de uma skill avulsa pelo ChatGPT web ainda não está documentado pela OpenAI** (consulta de 07/10/2026). Hoje a documentação oficial descreve skills no **Codex** e skills que chegam ao ChatGPT por meio de *plugins*.

- Se o seu ChatGPT mostra **Skills** na barra lateral com a opção de **criar ou enviar** uma skill, envie o mesmo [branding-isc.zip](https://github.com/rafaelnasch/branding-isc/releases/latest/download/branding-isc.zip), sem descompactar. Depois, chame a skill digitando `@` e escolhendo `branding-isc`.
- Se essa opção não aparece na sua conta, use o **claude.ai** ([seção 2](#2-instalar-no-claude-pelo-navegador-claudeai)) ou o **Codex** ([seção 4](#4-instalar-no-codex)), que funcionam hoje.

---

## 6. Conferir se funcionou

Abra uma **conversa nova** (a skill não entra numa conversa que já estava aberta antes da instalação) e peça:

> "No padrão do ISC, faz um post 1080 × 1350 explicando como funciona a primeira consulta."

**Funcionou se vier:**
- [ ] fundo **preto** (Preto ISC) ou **marfim**, nunca branco puro de qualquer jeito;
- [ ] título em serifa (Gilda Display) com **uma única** palavra em itálico: dourada sobre o preto, marrom sobre o marfim;
- [ ] a marca ou o símbolo do ISC **em arquivo** (nunca "ISC" digitado), em ouro só sobre o preto;
- [ ] um único próximo passo, como "Agende sua avaliação";
- [ ] nenhuma promessa de resultado, nenhum superlativo, nenhum emoji na arte.

**Não funcionou se vier** um post genérico, com cores aleatórias ou com "ISC" escrito numa fonte qualquer. Veja a [seção 12](#12-problemas-comuns).

---

## 7. Como a skill funciona por dentro

A skill não fica "lendo tudo" o tempo todo. Ela carrega em camadas, só o que o pedido precisa:

1. **A descrição (sempre carregada).** O assistente vê só o nome `branding-isc` e um parágrafo que diz quando usar a skill: material do ISC ou do Dr. Sharbo, e palavras como "padrão ISC", "marca isc", "post do isc", "dr sharbo" e "sharbo casagrande". É isso que faz a skill entrar sozinha quando o pedido combina.
2. **O `SKILL.md` (quando a skill entra).** Traz as regras travadas: cores e pares de contraste, tipografia, as versões da marca, as cinco leis da casa, a voz, as regras do CFM, as medidas de cada peça, o celular e o PDF.
3. **Os arquivos de apoio (só quando a peça pede):**

| Arquivo | Quando o assistente abre |
|---|---|
| `brand-book.html` | Para copiar o modelo de **documento** (proposta, relatório, página de leitura) e conferir modelos de peça em tamanho real. É o manual completo em 24 seções. |
| `deck-template.html` | Para montar uma **apresentação**: dez tipos de slide em 1440 × 900, navegação por seta e notas na tecla P. |
| `lockup.html` | Para pegar a **marca pronta**, inclusive em *data URI* (a imagem embutida no próprio HTML, usada no navegador), o bloco de identificação médica e a assinatura de e-mail. |
| `iviz.js` | Para desenhar **gráficos** no padrão: barras, linha, anel, funil, número em destaque, linha do tempo. |
| `iforms.js` | Para desenhar as **formas da casa** derivadas do símbolo (fio, ponto, órbita, percurso, camadas), usadas no lugar de foto quando não há foto real. |
| `assets/` | Marca em SVG e PNG, favicon, avatar, **fotos reais** do Instituto já tratadas, formas, ícones e fontes. |
| `autocontido.py` e `exportar_pdf.py` | Para gerar a versão de arquivo único e o PDF (ambientes com terminal: Claude Code e Codex). |

**Por que isso importa para você:** a resposta sai rápida, e as regras entram sempre que o assunto é o ISC, sem você colar instruções.

**Duas marcas, papéis diferentes.** A skill separa o **Instituto ISC** (marca da clínica, vitrine de todo o corpo clínico) do **Dr. Sharbo Casagrande** (marca pessoal do médico, só os procedimentos que ele faz). Ela também conhece as submarcas: **ISC REGEN** (medicina regenerativa, com verde petróleo como cor de apoio), **Benessere** (acupuntura e bem-estar) e **ISC Academy** (educação para médicos, nunca nos perfis de pacientes). Diga quem assina a peça; se você não disser, ela pergunta.

---

## 8. Como pedir: o pedido que dá certo

Um bom pedido tem quatro partes:

| Parte | Exemplos |
|---|---|
| **A peça** | carrossel, post único, story, capa de reels, status de WhatsApp, proposta, receituário, apresentação, e-mail, cartão de visita, página de site |
| **Quem assina** | Instituto ISC · Dr. Sharbo Casagrande · ISC REGEN · Benessere · ISC Academy |
| **O tema e o objetivo** | "explicar como é a primeira consulta", "convidar para agendar a avaliação", "apresentar a médica nova" |
| **Ler ou apresentar** | se vai ser **lido**, a skill faz documento; se vai ser **projetado**, faz apresentação |

**Exemplos prontos para copiar:**

- "No padrão do ISC, carrossel de 6 lâminas para o @instituto.isc explicando a diferença entre gordura localizada e flacidez. Termina convidando para a avaliação."
- "Story do Dr. Sharbo, no padrão ISC, chamando para a consulta de dor no joelho do corredor."
- "Proposta de tratamento em A4 do Instituto ISC para a paciente [nome], com capa preta e miolo marfim. Os valores eu preencho depois."
- "Apresentação de 10 slides do Instituto ISC para uma parceria com academia, com notas do apresentador."
- "Assinatura de e-mail da recepção do Instituto ISC."
- "Status de WhatsApp da Benessere avisando que aceitamos planos de saúde."

**Dicas:**
- A skill já sabe a medida de cada formato (post 1080 × 1350, story 1080 × 1920, A4 etc.). Só diga a medida se for diferente.
- Se faltar dado, ela **não inventa**: CRM, RQE, telefone e valores saem como `[nº]` ou entre colchetes para você preencher.
- Para ajustar, peça em cima do que veio: "troca o título da lâmina 3", "deixa o fundo marfim", "encurta o texto".

---

## 9. O que você recebe e como finalizar

| Ambiente | O que chega | Como finalizar |
|---|---|---|
| **claude.ai** | Um artefato HTML de arquivo único, que você vê na tela e pode baixar | Para imagem: abra o HTML baixado no navegador e tire print da peça. Para PDF: veja abaixo. |
| **Claude Code / Codex** | Arquivos HTML (e PNG ou PDF, se você pedir) gravados na sua pasta | PDF direto: `python3 exportar_pdf.py <arquivo.html>`. Para mandar a alguém: `python3 autocontido.py <arquivo.html>` cria a versão de arquivo único em `dist/`. |

**PDF pelo Chrome (qualquer ambiente):**
1. Abra o HTML no Chrome e espere uns 3 segundos.
2. `Cmd+P` (Mac) ou `Ctrl+P` (Windows) > **Salvar como PDF**.
3. Em **Mais configurações**, ligue **Gráficos de segundo plano**. Sem isso o fundo preto some.
4. Documento: retrato, margens padrão. Apresentação: **Paisagem**, margens **Nenhuma**.

**Antes de publicar qualquer peça**, rode o checklist da seção "Checklist de aprovação" do `SKILL.md` e consiga a **aprovação por escrito**: do Diretor Técnico-Médico para peça do Instituto, do próprio médico para peça do perfil pessoal.

---

## 10. As regras que a skill aplica sozinha

**As cinco leis da casa**
1. **O ouro só brilha sobre preto.** No marfim ou no branco, a marca é preta e o destaque é marrom.
2. **O metal é da marca.** O dourado metálico vive no símbolo e nas letras ISC. Há um elemento metálico por peça, e o resto do ouro é um fio fino, com no máximo 5% da área.
3. **Uma ideia por peça, um itálico por título.** Se falta espaço, corta-se texto, nunca margem.
4. **Foto real, luz quente.** Só o Instituto, a equipe e o trabalho verdadeiro. Banco de imagem, nunca; o letreiro antigo fica fora do quadro.
5. **Critério antes de promessa.** Nenhum resultado prometido, nenhum superlativo, nenhuma técnica proibida, e a identificação médica sempre que o CFM exigir.

**Publicidade médica (CFM)**
- Sem promessa de resultado, superlativo, preço de procedimento, pacote, sorteio, gratuidade ou depoimento sobre resultado.
- Antes e depois só no formato educativo do Manual de Publicidade Médica, nunca em post solto ou anúncio.
- **PMMA e bioplastia** ficam fora de tudo, porque a Resolução CFM 2.461/2026 os proíbe como preenchedor desde 02/06/2026.
- Bloco de identificação médica (nome, CRM e, só quando a peça cita especialidade, o RQE) vai na **legenda** dos posts e dentro da peça apenas em impresso, receituário e rodapé do site.
- Frases aprovadas para o botão: "Agende sua avaliação" · "Fale com a equipe" · "Entenda se é indicado para você" · "Saiba como funciona a consulta".

**A marca:** o logotipo nunca é redesenhado, redigitado, recolorido fora das versões, esticado ou com sombra. É sempre um arquivo de `assets/`. Fundo preto pede a versão em ouro metálico; fundo claro, a preta; foto escura, a branca; bordado e gravação, o ouro chapado. Abaixo de 72 px, entra só o símbolo.

O detalhe completo está no `SKILL.md` e no [manual](https://rafaelnasch.github.io/branding-isc/). Este guia não substitui assessoria jurídica.

---

## 11. Atualizar, compartilhar com a equipe e remover

**Atualizar**
- **claude.ai e ChatGPT:** baixe o [ZIP mais recente](https://github.com/rafaelnasch/branding-isc/releases/latest/download/branding-isc.zip), apague a skill antiga (passos abaixo) e envie a nova.
- **Claude Code:** `cd ~/.claude/skills/branding-isc && git pull`
- **Codex:** `cd ~/.agents/skills/branding-isc && git pull`

As novidades de cada versão ficam na página de [Releases](https://github.com/rafaelnasch/branding-isc/releases).

**Compartilhar com a equipe (claude.ai)**
- Em **Personalizar > Skills**, clique em **...** ao lado da skill > **Compartilhar** e informe nome ou e-mail. Quem recebe pode ligar e usar a skill, mas não pode editar.
- Em conta Team ou Enterprise, **Publicar na organização** coloca a skill na biblioteca de todo o time.

**Desligar ou remover**
- **claude.ai:** em **Personalizar > Skills**, desligue a chave. Para apagar: abra a skill, desligue, clique em **...** > **Excluir**.
- **Claude Code:** `rm -rf ~/.claude/skills/branding-isc`
- **Codex:** `rm -rf ~/.agents/skills/branding-isc`

---

## 12. Problemas comuns

| O que aconteceu | Causa provável | O que fazer |
|---|---|---|
| O envio do ZIP dá erro de **tamanho** | Você baixou pelo botão "Code > Download ZIP" (repositório inteiro) | Baixe o [branding-isc.zip](https://github.com/rafaelnasch/branding-isc/releases/latest/download/branding-isc.zip) do Releases, de cerca de 6 MB |
| Erro de **nome da pasta** ou falta de `SKILL.md` | ZIP descompactado e compactado de novo, ou pasta renomeada | Envie o ZIP original, sem mexer. A pasta de dentro tem de se chamar `branding-isc` |
| A opção **Skills** não aparece no claude.ai | Execução de código desligada, ou bloqueio da organização | Ligue em Configurações > Capacidades; em Team/Enterprise, fale com o administrador |
| O resultado sai **genérico** | A skill está desligada, ou a conversa foi aberta antes da instalação | Confira a chave em Personalizar > Skills, abra uma **conversa nova** e cite "padrão do ISC" no pedido |
| A marca aparece como **"ISC" digitado** ou com cor errada | A skill não carregou | Mesma solução da linha acima. A marca certa vem sempre de arquivo |
| O **PDF** saiu com fundo branco | "Gráficos de segundo plano" desligado | Ligue a opção em Mais configurações na hora de imprimir |
| No Codex a skill **não aparece** em `/skills` | Pasta errada para a sua versão | Clone também em `~/.codex/skills/branding-isc` e reinicie o Codex |
| Apareceu `[nº]` ou colchete na peça | Dado ainda não confirmado pelo Instituto (de propósito) | Preencha com o dado real antes de publicar |

---

## 13. O que vem no repositório

| Arquivo | O que é |
|---|---|
| `SKILL.md` | As regras travadas. É o que o assistente lê quando a skill entra. |
| `brand-book.html` | O manual vivo em 24 seções e o modelo de **documento**. |
| `deck-template.html` | O modelo de **apresentação** (dez tipos de slide, 1440 × 900). |
| `lockup.html` | Marca em arquivo e em data URI, bloco de identificação médica, assinatura de e-mail. |
| `iviz.js` · `iforms.js` | Motores de gráfico e de forma da casa. |
| `autocontido.py` | Gera versões de arquivo único (`dist/`) de qualquer HTML feito com a skill. |
| `exportar_pdf.py` | Exporta documento ou apresentação em PDF (Playwright ou o Chrome instalado). |
| `agents/openai.yaml` | Nome, descrição, ícone e pedido de exemplo no Codex e no ChatGPT. O Claude ignora este arquivo. |
| `dist/` | Versões de arquivo único, prontas para mandar: brand book, apresentação e assinaturas. **Não vai no ZIP.** |
| `assets/` | Marca (horizontal, vertical, símbolo, avatar, favicon; em ouro, preto, branco e ouro chapado), fotos reais, formas, gráficos, destaques, ícones, fontes e o arquivo original do designer. |
| `tools/empacotar_skill.py` | Gera o ZIP de instalação dentro dos limites (ver a seção 15). |

**O que fica fora do ZIP** e continua no [endereço público do manual](https://rafaelnasch.github.io/branding-isc/): o arquivo original do designer, as PNG da marca em resolução de impressão, os ícones em PNG, as capturas do manual e o `dist/`. Dentro do pacote, o manual aponta para esses endereços. Para impressão em gráfica, baixe a PNG grande ou o arquivo original pelo repositório.

---

## 14. Pendências com o Instituto

Enquanto cada uma não se resolve, a skill entrega só a versão permitida e avisa em uma linha:

1. Licença comercial da fonte usada no "ISC" do logotipo.
2. Validação, pelo designer, das versões derivadas (branca, ouro chapado, vertical, símbolo, avatar, favicon).
3. CRM e RQE de cada médico, registro da clínica e Diretor Técnico-Médico.
4. Uso público da leitura "Integrated Systemic Care" e o nome registrado no CRM-PR (o nome principal já é "Instituto ISC").
5. WhatsApp oficial, e-mail institucional, horário, site e domínio.
6. Cores das submarcas e da paleta em reserva do designer.
7. Troca do letreiro e sessão de fotos.
8. Cores de gráfica (CMYK e Pantone).
9. Disponibilidade das fontes no Canva e no editor de vídeo.
10. Missão e valores escritos (resolvida em 27/09/2026; ver 07.8 do manual).
11. Validação regulatória antes de anunciar a medicina regenerativa.
12. Revisão de nome, bio e cadastros dos perfis.

O detalhe de cada uma está na seção 23 do manual.

---

## 15. Para quem mantém a skill

**Gerar o ZIP de uma versão nova**

```bash
python3 tools/empacotar_skill.py
```

O script grava `dist-skill/branding-isc.zip` (fora do git) e **falha** se qualquer limite abaixo estourar. Depois, valide com o validador oficial da especificação e publique:

```bash
# validador oficial (precisa do uv; clone https://github.com/agentskills/agentskills antes)
uvx --from <pasta-do-clone>/skills-ref skills-ref validate .
gh release create vX.Y dist-skill/branding-isc.zip -t "branding-isc vX.Y" --latest
```

**Limites atendidos (conferidos em 07/10/2026)**

| Limite | Regra | Esta skill |
|---|---|---|
| `name` | minúsculas, números e hífen, até 64, igual ao nome da pasta | `branding-isc` (12) |
| `description` | até 1.024 caracteres, sem `<` e `>`; caso de uso e gatilhos no começo | 788 caracteres |
| Campos do frontmatter | só os da especificação | `name` e `description` |
| `SKILL.md` | menos de 500 linhas | 335 linhas |
| Links relativos | todo link do `SKILL.md` aponta para arquivo do pacote | 0 quebrados |
| ZIP | até 30 MB (meta abaixo de 10 MB) | 5,80 MB |
| Descompactado | até 25 MB | 8,10 MB |
| Arquivos | até 400; nenhum acima de 10 MB; nomes só com letras, números, ponto, hífen e sublinhado | 212; o maior é o `brand-book.html` (1,35 MB) |
| Estrutura | uma pasta `branding-isc/` no topo, um só `SKILL.md` | sim |
| Validador oficial | `skills-ref validate` | "Valid skill: branding-isc" no pacote e no repositório |

Os limites de nome, descrição, campos e linhas são os da [especificação Agent Skills](https://agentskills.io/specification). Os de tamanho são as travas do `tools/empacotar_skill.py`, mais rígidas que as dos apps (a ajuda do Claude não publica um número). **Regra para manter:** tudo o que é pesado e não serve para produzir peça fica fora do ZIP e é servido pelo endereço público.

**Navegadores:** Chrome, Edge ou Safari recentes (iOS 16 ou mais novo, Chrome 105 ou mais novo).

---

Marca, símbolo e logotipo são propriedade do **Instituto ISC**. Os motores `iviz.js` e `iforms.js` foram escritos para este sistema. Sistema de identidade organizado com a GrowAI. Fio de Ouro v1 · setembro de 2026.

Fontes das instruções de instalação: [Usar skills no Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) · [Build skills (OpenAI)](https://learn.chatgpt.com/docs/build-skills) · [Especificação Agent Skills](https://agentskills.io/specification).
