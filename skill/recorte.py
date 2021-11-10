import xarray as xr
import geopandas as gpd


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