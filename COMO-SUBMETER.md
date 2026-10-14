# Como Submeter o Seu Projeto

Você construiu (ou está construindo) o seu projeto do desafio? Então esta página é para você. Ao submeter, o seu projeto entra na galeria oficial do mês, você se torna um contribuidor deste repositório da Jornada de Dados e o seu trabalho fica visível para toda a comunidade.

## Como funciona

O seu projeto completo vive no **seu** repositório, no seu perfil do GitHub. É lá que está o código, a documentação e todo o histórico do seu trabalho. Isso é proposital: o portfólio é seu e fica com você.

O que você submete aqui é o **cartão do seu projeto**: uma pasta com o seu nome de usuário contendo um README de apresentação e as imagens que quiser. Esse cartão entra na galeria do mês e aponta para o seu repositório completo.

**O texto do cartão é livre.** Escreva do seu jeito, com as seções que fizerem sentido para o seu projeto, com quantas imagens quiser. A gente recomenda um bloco de metadados no topo do arquivo: é dele que sai a sua linha no [mural de projetos](PROJETOS.md).

| O que fica no SEU repositório | O que entra AQUI (galeria) |
|---|---|
| Código completo do projeto | Uma pasta com o seu nome de usuário |
| Toda a documentação (PRD, SPECs, ADRs, arquitetura) | Um README de apresentação (o cartão) |
| Histórico de commits, PRs e evolução | Link para o seu repositório completo |
| CI, validações e proteções que você configurou | Um diagrama ou imagem do seu projeto (opcional, mas recomendado) |

## Passo a passo da submissão

Siga na ordem. O processo inteiro leva uns 20 minutos e é, ele mesmo, uma prática do fluxo de trabalho que o desafio ensina.

1. **Faça um fork deste repositório** para a sua conta, usando o botão Fork no topo da página

2. **Crie uma branch no seu fork** com o padrão `projeto/mes/seu-usuario`. Exemplo: `projeto/2026-08/caiomachado`

3. **Crie a sua pasta** dentro da pasta de projetos do mês correspondente. Exemplo: dentro de `desafio-vendas/projetos/`, crie a pasta `caiomachado`

4. **Publique o seu projeto** no LinkedIn e na comunidade da plataforma, e guarde os dois links para colocar no cartão. É a regra da visibilidade do desafio, e vale fazer antes da submissão justamente para não ficar para depois

5. **Crie o README do seu cartão** dentro da sua pasta, de preferência começando pelo bloco de metadados do exemplo abaixo. Do bloco para baixo, escreva como quiser — inclusive com as imagens que colocar na sua pasta, como um diagrama da arquitetura ou um print do produto funcionando

6. **Faça o commit**. Exemplo: `docs: adiciona projeto de caiomachado ao desafio 2026-08`

7. **Abra o pull request** do seu fork para este repositório, com um título claro e uma breve descrição do seu projeto no corpo. O PR já abre com um modelo, mas ele é só um exemplo: use, adapte ou apague

8. **Aguarde a revisão.** Não tem validação automática: quem olha o seu PR é uma pessoa. Se algo precisar de ajuste, comentamos no PR, como em qualquer revisão de código do mundo real

9. **Merge feito, você está na galeria.** O [mural de projetos](PROJETOS.md) é atualizado em seguida pela manutenção do repositório, com a sua linha montada a partir dos metadados do cartão. Seu nome entra na lista de contribuidores do repositório da Jornada de Dados e seu projeto fica visível para toda a comunidade

## Dicas antes de abrir o PR

Nada disso é conferido automaticamente, são só coisas que ajudam o seu cartão:

- Repositório do projeto público, com o link no cartão
- Um README no seu repositório explicando como rodar o projeto
- Links do LinkedIn e da plataforma apontando para os **posts**, não para o seu perfil
- Pasta com o seu usuário do GitHub, dentro do mês correto
- Só o cartão e as imagens aqui; o código fica no seu repositório
- Nenhum dado real ou informação sensível

## O bloco de metadados

Não é obrigatório, mas é daqui que sai a sua linha no [mural de projetos](PROJETOS.md). Ele vai no topo do arquivo, entre duas linhas de `---`, sem nada antes. Este é só um exemplo: preencha os campos que fizerem sentido. Sem o bloco, o seu projeto ainda entra no mural, só que identificado pelo nome da pasta.

```markdown
---
projeto: Agente de Atendimento do Petshop
autor: Caio Machado
usuario: caiomachado
dominio: Petshop
repositorio: https://github.com/caiomachado/agente-petshop
linkedin: https://www.linkedin.com/posts/caiomachado_meu-projeto-do-desafio-share-7490415422425698304-LuUl
plataforma: https://suajornadadedados.curseduca.pro/m/community/posts/a773a771-9319-4f51-8340-2358d8d9832d
video: https://youtu.be/abcdefghijk
---
```

| Campo | O que é |
|---|---|
| `projeto` | O nome do seu projeto, como aparece no mural |
| `autor` | Seu nome, como você quer ser creditado |
| `usuario` | Seu usuário do GitHub |
| `dominio` | O negócio que você escolheu: petshop, clínica, imobiliária... |
| `repositorio` | Link do seu repositório no GitHub |
| `linkedin` | Link do **post** sobre o projeto |
| `plataforma` | Link do seu post na comunidade |
| `video` | Uma demo em vídeo, se você gravou |

Algumas dicas sobre o bloco:

- O erro mais comum nos links é colar o **perfil** no lugar do **post**. O link do post você consegue no botão de compartilhar da própria publicação
- Se o valor tiver dois-pontos, use aspas: `projeto: "Clínica: agenda e triagem"`, senão o GitHub não mostra o bloco direito
- O botão de compartilhar do LinkedIn cola um `?utm_source=share&...&rcm=...` no fim da URL, e esse `rcm` identifica a conta que copiou o link. Cortar tudo a partir do `?` deixa o seu cartão mais limpo

## Do bloco para baixo, é seu

Não existe modelo obrigatório para o corpo do cartão: escreva como quiser. Se você quer uma sugestão de por onde começar, estes são os assuntos que a comunidade mais procura ler em um cartão:

- O projeto em três linhas: o que o seu agente faz, para quem, que problema resolve
- A arquitetura, de preferência com um diagrama: quantos agentes, o que cada um pode fazer, onde o humano entra
- A stack escolhida, com uma frase sobre o porquê de cada escolha
- O harness que você usou (Claude Code, Codex, Cursor, Kimi...) e como preparou o repositório para ele
- As três decisões de engenharia mais difíceis, com as alternativas que você descartou
- Como você tratou os medos do cliente: o que virou decisão de arquitetura e o que ficou para depois
- O que você aprendeu: o que foi mais difícil, o que faria diferente

Seja generoso na última. É a parte que a comunidade mais lê.

## Regras da galeria

- Um cartão por pessoa por mês. Você pode participar de todos os meses, e quem participa de vários entra no Hall dos Construtores no README principal
- Projetos em qualquer estágio são bem-vindos. Um discovery bem documentado já é uma submissão válida; atualize o cartão via novo PR conforme o projeto evolui
- O cartão deve ser do seu próprio projeto, com um case inventado por você: negócio, cliente e produto com nome próprio
- Seja generoso na seção de aprendizados. É a parte que a comunidade mais lê

## Depois do merge

Projetos na galeria podem ser comentados na live exclusiva para alunos, e os que mais se destacarem aparecem no vídeo de encerramento do mês no canal da Jornada de Dados e nas nossas redes, sempre com os devidos créditos. Compartilhe o seu cartão no LinkedIn marcando a Jornada: a gente adora repostar projeto de aluno.

**Travou em algum passo?** Pergunte na categoria [**Como construir**](https://github.com/suajornadadedados/desafio-jornada/discussions/new?category=como-construir) nas Discussions: alguém já passou por isso, e a resposta serve para quem vier depois. Se o seu PR já está aberto, comente nele mesmo: fica tudo no mesmo lugar.

**Dúvida sobre o desafio em si?** Tanto faz se é sobre *o que* o cliente pediu ou sobre *como* construir: também é na categoria [**Como construir**](https://github.com/suajornadadedados/desafio-jornada/discussions/new?category=como-construir).