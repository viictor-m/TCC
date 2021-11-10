import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from skill import cmap_ons
from skill import config
import matplotlib.colors as mcolors
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

def geoaxes_format(ax, longitude_interval=2.5):
    """
    Formata eixos com referências geográficas para mapas cartopy, recorte correto e bacias hidrograficas.
    Essa função é usada pela função plot.

    Parâmetros
    ----------
    ax: matplotlib.axes._subplots.AxesSubplot
        Eixo matplotlib a ser formatado como eixo geográfico

    Retorna
    -------
    gl: cartopy.mpl.geoaxes.GeoAxesSubplot
        Eixo geográfico formatado.
    """
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='black', alpha=0.3, linestyle='--')
    gl.top_labels = False
    gl.left_labels = True
    gl.right_labels = False
    gl.ylines = True
    gl.xlines = True
    gl.xlocator = mticker.FixedLocator(np.arange(-90,50,10))
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 11}
    gl.ylabel_style = {'size': 11}

    dir_shp = config.dir_shp
    
    estados_br = cfeature.NaturalEarthFeature(category='cultural', scale='50m', facecolor='none', name='admin_1_states_provinces_shp', alpha=.35)
    ax.add_feature(estados_br, edgecolor='gray')
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.35, edgecolor='gray')

    bacias = ShapelyFeature(Reader(f'{dir_shp}/bacias.shp').geometries(), ccrs.PlateCarree(),
                            linewidth=1.25, facecolor='none',hatch='//', edgecolor='black', alpha=0.7)
    ax.add_feature(bacias)
    return gl


def addcbar(plot, ax, cblabel="", orientation="horizontal", rotation=0, ticks=None):
    """
    Adiciona uma barra de cores a um mapa automaticamente.

    A função adiciona um eixo independente à figura
    Utilizada na função plot.
    """
    # cria um eixo para a colorbar
    cbar = plt.colorbar(plot, orientation=orientation, pad=0.05, ax=ax, shrink=.75, aspect=40, ticks=ticks)
    cbar.ax.tick_params(labelsize=10)
    cbar.set_label(cblabel, fontsize = 11)
    

def plot(ax, dataset, levels=[0, 1, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200], cmap=cmap_ons.ons_cmap):
    """
    Gera o plot dos dados de precipitação.
    ------------
    Argumentos

    ax: matplotlib.axes 
        eixo a ser plotado

    dataset: xarray.DataArray
        dado a ser plotado
    ------------
    Retorna

    ax: matplotlib.axes
        eixo com o plot
    """

    norm = mcolors.BoundaryNorm(levels, cmap_ons.ons_cmap.N, extend='both')

    cont = ax.contourf(dataset.lon, dataset.lat, dataset,
                    norm=norm,
                    levels=levels,
                    cmap=cmap,
                    extend='both',
                    transform=ccrs.PlateCarree())

    gl = geoaxes_format(ax)

    cbar = addcbar(cont, ax, cblabel='mm', orientation='vertical', ticks=levels)
    return ax