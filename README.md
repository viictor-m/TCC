# TCC

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")

## :scroll: Descrição do projeto

Análise do skill do modelo CAM 3.1 para as rodadas operacionais de 2012 a 2020.

## :warning: Pré-requisitos

- [Python](https://www.python.org/) (obrigatório)
- [Conda](https://docs.conda.io/en/latest/) (recomendado)

## :arrow_forward: Execução

### Como executar

1\. Clone este repositório.

```bash
git clone git@github.com:viictor-m/TCC.git
```

2\. Acesse o diretório do projeto.

```bash
cd TCC
```

3\. Instale as dependências.

```bash
conda env create -f requirements.yaml
```

4\. Baixar arquivos utilizados para análise desse repositório.

   4.1\. Crie uma pasta dados

```bash
mkdir dados
```

   4.2\. Instalar extensão para utilizar o drive

```bash
./download-dados.sh instalar
```

   4.3\. Autenticar entrada no seu drive

```bash
./download-dados.sh autenticar
```

   4.4\. Fazer download dos arquivos.

```bash
./download-dados.sh download
```

## :card_index_dividers: Ordem dos notebooks

### 1. Gera imagens das climatologias do GPCC

climatologia.ipynb

### 2. Gera o skill do CAM a partir da anomalia

skill-cam_anom.ipynb

### 3. Gera imagens do skill do CAM

skill-plot.ipynb

### 4. Baixa e gera imagens do skill dos outros centros componentes do NMME

skill-outros_centros-plot.ipynb

### 5. Faz ajuste de escala da previsão e ponderação pelo skill do CAM

cam3-ajuste_vies.ipynb

### 6. Calcula o RMSE da previsão bruta e com ajustes

cam3-rmse.ipynb

### 7. Plota o RMSE e a variação entre previsão bruta e ajustada

cam3-rmse_plot.ipynb
