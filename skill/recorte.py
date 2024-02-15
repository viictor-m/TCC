import xarray as xr
import geopandas as gpd
import xesmf as xe

from typing import List

def preparar_para_recorte(dataset: xr.Dataset, crs="epsg:4326", xdim="longitude", ydim="latitude") -> xr.Dataset:
    """
    Ajusta o dataset para ter sistema de coordenadas correto para o recorte.
    ----------
    Argumentos:
        dataset: Dataset
            Dataset a ser ajustado.
        crs: str
            Sistema de coordenadas a ser utilizado.
        xdim: str
            Nome da dimensão x.
        ydim: str
            Nome da dimensão y.
    ----------
    Retorna:
        Dataset
    """
    dataset = dataset.assign_coords(lon=(((dataset.lon + 180) % 360) - 180)).sortby(xdim)
    dataset = dataset.rio.set_spatial_dims(x_dim=xdim, y_dim=ydim) 
    dataset = dataset.rio.write_crs(crs)

    return dataset

def recorte(dataset: xr.Dataset, shp: gpd.GeoDataFrame) -> xr.Dataset:
    """
    Recorta o dataset de acordo com o polígono do shapefile.
    ----------
    Argumentos:
        dataset: Dataset
        shp: GeoDataFrame
    """
    shapefile = gpd.GeoDataFrame(shp)
    clip = dataset.rio.clip(shapefile["geometry"],"epsg:4326")

    return clip


def recortar(ds: xr.Dataset, shp: gpd.GeoDataFrame) -> xr.Dataset:
    """
    Recorta o dataset de acordo com o polígono do shapefile.
    ----------
    Argumentos:
        dataset: Dataset
        shp: GeoDataFrame
    """
    
    ds_para_recorte = preparar_para_recorte(ds, xdim='lon', ydim='lat')
    ds_recortado = recorte(ds_para_recorte, shp)
    
    return ds_recortado

def regridder(ds: xr.Dataset, lat: List, lon: List) -> xr.Dataset:
    """ 
    Retorna o dataset com a grade interpolada.
    ------------
    Argumentos:
    
    ds: xr.Dataset
        Dataset a ser interpolado.
    lat: List
        Latitudes a serem utilizadas na interpolação
    lon: List
        Longitudes a serem utilizadas na interpolação
    """
    
    ds_out = xr.Dataset(
    {
        "lat": (["lat"], lat),
        "lon": (["lon"], lon),
    })
    
    regridder = xe.Regridder(ds, ds_out, "bilinear")
    dr_out = regridder(ds)
    
    return dr_out