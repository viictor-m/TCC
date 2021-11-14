# TCC

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")

## :scroll: Descrição do projeto

Análise do skill do modelo CAM 3.1 para as rodadas operacionais de 2012 a 2020.
	

## :warning: Pré-requisitos

- [Python](https://www.python.org/) (obrigatório)
- [Conda](https://docs.conda.io/en/latest/) (recomendado)


## :arrow_forward: Execução

### Como executar

1. Clone este repositório.

```bash
git clone git@github.com:viictor-m/TCC.git
```

2. Acesse o diretório do projeto.
```
cd TCC
```

3. Instale as dependências.

```bash
conda env create -f environment.yaml
```

4. Baixar arquivos utilizados para análise desse repositório.

4.1 Crie uma pasta dados
```bash
mkdir dados
```
4.2 Instalar extensão para utilizar o drive
```
./download-dados.sh instalar
```
4.3 Autenticar entrada no seu drive
```
./download-dados.sh autenticar
```
4.4 Fazer download dos arquivos.
```
./download-dados.sh download
```

#### Ordem dos notebooks

##### Gera imagens das climatologias do GPCC
climatologia.ipynb

##### Gera o skill do CAM a partir da anomalia
skill-cam_anom.ipynb

##### Gera o skill do CAM a partir das previsões brutas
skill-cam_prev.ipynb

##### Gera imagens do skill do CAM
skill-plot.ipynb
