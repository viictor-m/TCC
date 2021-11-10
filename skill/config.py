"""Arquivo de configurações do projeto"""

from pathlib import Path

dir_abs = Path(__file__).parent.parent
dir_dados = dir_abs.joinpath('dados')
dir_img = dir_abs.joinpath('img')
dir_shp = dir_abs.joinpath('shp')

dir_dados.mkdir(parents=True, exist_ok=True)
dir_img.mkdir(parents=True, exist_ok=True)
dir_shp.mkdir(parents=True, exist_ok=True)