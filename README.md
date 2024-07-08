# Script pra vídeo de golpista

Nesse repositório se encontram o script para pegar os vídeos e as instruções de
como usá-lo, bem como os arquivos obtidos em sua execução.

## O que é

O site [https://saudeideal.shop/lp-oleo-drz/](https://saudeideal.shop/lp-oleo-drz/) promove um tratamento falso (golpe) para disfunção erétil utilizando a voz e vídeo do Dr. Dráuzio Varella. O vídeo promocional foi subido na plataforma [VTurb.net](https://vturb.com.br/) e foi obtido como prova utilizando este repositório. 

## Arquivos e Pastas

- `script.py`: Script que executa a raspagem;
- `data/`: Diretório onde são guardados os arquivos de vídeo intermediários;
- `list.txt`: Lista com os comandos para o FFMPEG;
- `final.mp4`: Arquivo extraído dos intermediários usando FFMPEG;
- `README.md`: Esta documentação.

## Como reproduzir

> **IMPORTANTE:** este tutorial assume que você tem as ferramentas [Python](https://python.org) e [FFMPEG](https://ffmpeg.org/) instaladas.

Primeiramente, exclua todos os arquivos menos o `README.md` e `script.py`. Caso ainda não tenha a biblioteca `requests` instalada em seu sistema, rode

```bash
pip install requests
```

Execute o script com 

```bash
python3 script.py
```

O script irá recriar o arquivo `list.txt` e o diretório `data`, contendo os fragmentos do vídeo em qualidade 720p. Para concatená-los em um único arquivo (`final.data`), execute o seguinte comando:

```bash
ffmpeg -f concat -safe 0 -i list.txt -c copy final.mp4
```
