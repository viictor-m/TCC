import requests
import xarray as xr
from cdo import Cdo
import pendulum

import os
import shutil

from skill import config

dir_dados = config.dir_dados


def download(centro: str, mes: int) -> xr.Dataset:
    
    url = 'https://ftp.cpc.ncep.noaa.gov/International/nmme/binary_monthly/'
    
    date = pendulum.now().set(year=1975, month=mes, day=21).format('MMM')
    
    name = f'{date}IC_{centro}_precip_skill'
    
    sufixes =['.ctl', '.dat']
    
    for sufix in sufixes:
        
        complete_name = f'{name}{sufix}'
        request = requests.get(f'{url}{complete_name}')
        
        with open(complete_name, 'wb') as file:
            file.write(request.content)
        file.close()
    
    cdo = Cdo()
    nc = cdo.import_binary(input=f'{name}.ctl', output=f'{name}.nc', options='-f nc4')
    shutil.move(nc, dir_dados.joinpath('outros_centros').mkdir(exist_ok=True))
        
    for sufix in sufixes:
        complete_name = f'{name}{sufix}'
        os.unlink(complete_name)
    
    return xr.open_dataset(f'{dir_dados}/{name}.nc')