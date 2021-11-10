import xarray as xr

def climatologia(ds: xr.Dataset, start: str, end: str) -> xr.Dataset:
    """
    Retorna a climatologia de acordo com as datas de entrada.
    --------
    Argumentos
    ds: xr.Dataset
        Dataset com dados para gerar climatologia
    start: str
        Data inicial da climatologia
    end: str
        Data final da climatologia
    """
    
    ds_sliced = ds.sel(time=slice(start, end))
    monthly_clim = ds_sliced.groupby('time.month').mean('time')
    
    return monthly_clim


def anomalia(obj: xr.Dataset, clima: xr.Dataset) -> xr.Dataset:
    """
    Retorna a anomalia de acordo com as entradas.
    
    obj: xr.Dataset
        Dataset com os dados em análise
    clima: xr.Dataset
        Dataset com a climatologia desejada.
    """
    
    anomalia = obj.groupby('time.month') - clima.groupby('time.month')
    
    return anomalia


def correlacao(prev: xr.Dataset, obs: xr.Dataset) -> xr.Dataset:
    """
    Faz a correlação de pearson entre o dado previsto e o observado.
    
    prev: xr.Dataset
        Dataset com os dados de previsão
    obs: xr.Dataset
        Dataset com os dados observados.
    """
    
    corr = xr.corr(prev, obs)
    
    return corr