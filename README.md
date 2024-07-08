# Script para vídeo golpista com imagem do Dr. Dráuzio Varella

Nesse repositório se encontram o script para pegar os vídeos e as instruções de
como usá-lo, bem como os arquivos obtidos em sua execução.

## O que é

O site
[https://saudeideal.shop/lp-oleo-drz/](https://saudeideal.shop/lp-oleo-drz/)
promove um tratamento falso (golpe) para disfunção erétil utilizando a voz e
vídeo do Dr. Dráuzio Varella. O vídeo promocional foi subido na plataforma
[VTurb.net](https://vturb.com.br/) e foi obtido como prova utilizando este
repositório.

## Arquivos e Pastas

- `script.py`: Script que executa a raspagem;
- `data/`: Diretório onde são guardados os arquivos de vídeo intermediários;
- `list.txt`: Lista com os comandos para o FFMPEG;
- `final.mp4`: Arquivo extraído dos intermediários usando FFMPEG;
- `README.md`: Esta documentação.

## Como reproduzir

> **IMPORTANTE:** este tutorial assume que você tem as ferramentas
> [Python](https://python.org) e [FFMPEG](https://ffmpeg.org/) instaladas.

Primeiramente, exclua todos os arquivos menos o `README.md` e `script.py`. Caso
ainda não tenha a biblioteca `requests` instalada em seu sistema, rode

```bash
pip install requests
```

Execute o script com

```bash
python3 script.py
```

O script irá recriar o arquivo `list.txt` e o diretório `data`, contendo os
fragmentos do vídeo em qualidade 720p. Para concatená-los em um único arquivo
(`final.data`), execute o seguinte comando:

```bash
ffmpeg -f concat -safe 0 -i list.txt -c copy final.mp4
```

## Metodologia

O link presente no arquivo `script.py` foi obtido inspecionando as requisições
de rede no link do golpe acima. O site não permite que você use as ferramentas
de desenvolvedor do modo convencional (botão direito ou F12), mas é possível
abrí-las usando os 3 pontinhos no topo do Google Chrome.

Na aba Network (Rede) das ferramentas de desenvolvedor, podemos ver várias
requisições para arquivos com o formato `segment__{NUMERO}.ts`, como mostrado na
figura abaixo.

[network.png](./network.png)

Realizando na mão uma dessas requisições, podemos ver que um arquivo é baixado.
Clicando nesse arquivo, é possível ver que ele corresponde a um segmento do
vídeo exibido.

O que o script faz é automatizar a obtenção desses arquivos e organizá-los de
modo que o FFMPEG possa juntá-los novamente.
