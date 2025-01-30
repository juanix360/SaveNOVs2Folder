# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:24:37 2025

@author: Juan Ortiz
"""

import os
import json
import pandas as pd
import shutil

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#DATOS IMPORTANTE A CAMBIAR

# Usar cadenas sin formato (raw strings)
normalized_path = r"C:\Users\Usuario\Desktop\Juan_Ortiz\Documents LiDAR Maverick\Data_Lidar"

# Usar la ruta normalizada
base_directory = normalized_path

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def move_novb_files(base_directory):
    # Crear un DataFrame para almacenar la relación entre archivos .novb y carpetas
    data = []

    # Recorrer todas las carpetas en el directorio base
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file == 'sessionMetadata.json':
                json_path = os.path.join(root, file)
                with open(json_path, 'r') as f:
                    metadata = json.load(f)
                    novb_name = metadata.get('collectionSystemTrajectoryName')
                    if novb_name:
                        data.append({'novb_name': novb_name, 'folder': root})

    # Crear un DataFrame a partir de la lista de diccionarios
    df = pd.DataFrame(data)

    # Copiar los archivos .novb a sus respectivas carpetas
    for novb_name in df['novb_name'].unique():
        novb_path = os.path.join(base_directory, novb_name)
        if os.path.exists(novb_path):
            for folder in df[df['novb_name'] == novb_name]['folder']:
                destination_path = os.path.join(folder, novb_name)
                if not os.path.exists(destination_path):
                    shutil.copy(novb_path, destination_path)
                    print(f'Copied {novb_name} to {folder}')
                else:
                    print(f'{novb_name} already exists in {folder}')

move_novb_files(base_directory)



