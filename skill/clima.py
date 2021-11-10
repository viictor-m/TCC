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