import xarray as xr
import xskillscore as xs

def correlacao(prev: xr.DataArray, obs: xr.DataArray) -> xr.DataArray:
    """
    Faz a correlação de pearson entre o dado previsto e o observado.
    
    prev: xr.DataArray
        Dataset com os dados de previsão
    obs: xr.DataArray
        Dataset com os dados observados.
    """
    
    corr = xr.corr(prev, obs, dim='time')
    
    return corr

def rmse(prev:xr.DataArray, obs:xr.DataArray) -> xr.DataArray:
    """
    Calcula a RMSE entre o dado previsto e o observado.
    
    prev: xr.DataArray
        Dados previstos
    obs: xr.DataArray
        Dados observados
    """
    
    rmse = xs.rmse(prev, obs, dim='time')
    
    return rmse