import xarray as xr

def correlacao(prev: xr.Dataset, obs: xr.Dataset) -> xr.Dataset:
    """
    Faz a correlação de pearson entre o dado previsto e o observado.
    
    prev: xr.Dataset
        Dataset com os dados de previsão
    obs: xr.Dataset
        Dataset com os dados observados.
    """
    
    corr = xr.corr(prev, obs, dim='time')
    
    return corr