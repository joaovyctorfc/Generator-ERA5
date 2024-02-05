import cdsapi
import sys
import time

inicio = time.time()

c = cdsapi.Client()

dataInicio = input("Data Início (D/M/Y): ")
dataFim = input("Data Final (D/M/Y): ")

variavel = int(input("Variável: \n 1- TP2M \n 2- TP2M MAX \n 3- TP2M MIN \n 4- DT2M \n\n"))

anoInicio = dataInicio[4:]
mesInicio = dataInicio[2:4]
diaInicio = dataInicio[:2]

anoFim = dataFim[4:]
mesFim = dataFim[2:4]
diaFim = dataFim[:2]

ano = anoInicio
hora = 0
horarios = ["00", "06", "12", "18"]

if variavel == 1:
    print("\n Iniciando download de dados para 2m_temperature...")
    while ano <= anoFim:
        mes = mesInicio
        while mes <= mesFim:
            dia = diaInicio
            while dia <= diaFim:
                hora = 0  # Reiniciar a hora para cada dia
                while hora <= 3:
                    print(f" Baixando dados para {ano}-{mes}-{dia}--{horarios[hora]}:00")
                    c.retrieve(
                        'reanalysis-era5-single-levels',
                        {
                            'product_type': 'reanalysis',
                            'variable': ['2m_temperature'],
                            'year': ano,
                            'month': mes,
                            'day': dia,
                            'time': horarios[hora] + ':00',
                            'area': [-35, -80, -55, 10],  # Coordenadas para América do Sul
                            'format': 'netcdf',
                        },
                        f'ERA5_2m_Temperature_{ano}{mes}{dia}{horarios[hora]}.nc')
                    hora += 1
                dia += 1
            mes += 1
        ano += 1
    print("Download concluído para 2m_temperature.")

elif variavel == 2:
    print("\n Iniciando download de dados para Maximum_2m_temperature_since_previous_post-processing...")
    while ano <= anoFim:
        mes = mesInicio
        while mes <= mesFim:
            dia = diaInicio
            while dia <= diaFim:
                hora = 0  # Reiniciar a hora para cada dia
                while hora <= 3:
                    print(f" Baixando dados para {ano}-{mes}-{dia}--{horarios[hora]}:00")
                    c.retrieve(
                        'reanalysis-era5-single-levels',
                        {
                            'product_type': 'reanalysis',
                            'variable': ['maximum_2m_temperature_since_previous_post_processing'],
                            'year': ano,
                            'month': mes,
                            'day': dia,
                            'time': horarios[hora] + ':00',
                            'area': [-35, -80, -55, 10],  # Coordenadas para América do Sul
                            'format': 'netcdf',
                        },
                        f'ERA5_Maximum_2m_Temperature_{ano}{mes}{dia}{horarios[hora]}.nc')
                    hora += 1
                dia += 1
            mes += 1
        ano += 1
    print("Download concluído para Maximum_2m_Temperature.")

elif variavel == 3:
    print("\n Iniciando download de dados para Minimum 2m temperature since previous post-processing...")
    while ano <= anoFim:
        mes = mesInicio
        while mes <= mesFim:
            dia = diaInicio
            while dia <= diaFim:
                hora = 0  # Reiniciar a hora para cada dia
                while hora <= 3:
                    print(f" Baixando dados para {ano}-{mes}-{dia}--{horarios[hora]}:00")
                    c.retrieve(
                        'reanalysis-era5-single-levels',
                        {
                            'product_type': 'reanalysis',
                            'variable': ['minimum_2m_temperature_since_previous_post_processing'],
                            'year': ano,
                            'month': mes,
                            'day': dia,
                            'time': horarios[hora] + ':00',
                            'area': [-35, -80, -55, 10],  # Coordenadas para América do Sul
                            'format': 'netcdf',
                        },
                        f'ERA5_Minimum_2m_Temperature_{ano}{mes}{dia}{horarios[hora]}.nc')
                    hora += 1
                dia += 1
            mes += 1
        ano += 1
    print("Download concluído para Minimum_2m_Temperature.")

elif variavel == 4:
    print("\n Iniciando download de dados para 2m_Dewpoint_Temperature...")
    while ano <= anoFim:
        mes = mesInicio
        while mes <= mesFim:
            dia = diaInicio
            while dia <= diaFim:
                hora = 0  # Reiniciar a hora para cada dia
                while hora <= 3:
                    print(f" Baixando dados para {ano}-{mes}-{dia}--{horarios[hora]}:00")
                    c.retrieve(
                        'reanalysis-era5-single-levels',
                        {
                            'product_type': 'reanalysis',
                            'variable': ['2m_dewpoint_temperature'],
                            'year': ano,
                            'month': mes,
                            'day': dia,
                            'time': horarios[hora] + ':00',
                            'area': [-35, -80, -55, 10],  # Coordenadas para América do Sul
                            'format': 'netcdf',
                        },
                        f'ERA5_2m_Dewpoint_Temperature_{ano}{mes}{dia}{horarios[hora]}.nc')
                    hora += 1
                dia += 1
            mes += 1
        ano += 1
    print("Download concluído para 2m_Dewpoint_Temperature.")

else:
    print("Variável incorreta!")

fim = time.time()
tempo_total = fim - inicio
print(f"Tempo de execução: {tempo_total} segundos")