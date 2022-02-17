'''
This program plot some graphs about CO2 effects on climate changing using matplotlib.

Author: Andrea Tomatis
'''

import matplotlib.pyplot as plt 
import csv



def plotEmissionsByYear(emissions):
    fig, (ax1) = plt.subplots(1, 1)

    ax1.set_title('Emissions by Year and Type')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('emissions (tons (MLN))')

    xaxis = []
    y1axis = []
    y2axis = []
    y3axis = []
    y4axis = []
    y5axis = []
    y6axis = []

    for key, value in emissions.items():
        xaxis.append(key)
        
        y1axis.append(value[0])
        y2axis.append(value[1])
        y3axis.append(value[2])
        y4axis.append(value[3])
        y5axis.append(value[4]) 
        y6axis.append(value[5])
        
    ax1.plot(xaxis, y1axis, '-y', label='Total Emission')
    ax1.plot(xaxis, y2axis, '-r', label='Gas Fuel')
    ax1.plot(xaxis, y3axis, '-m', label='Liquid Fuel')
    ax1.plot(xaxis, y4axis, '-c', label='Solid Fuel')
    ax1.plot(xaxis, y5axis, '-g', label='Cement')
    ax1.plot(xaxis, y6axis, '-b', label='Gas Flaring')
    ax1.legend()
    plt.savefig('./emissionByYear.png')



def plotEmissionPerPopulation(emissions, worldPopulation):
    fig, (ax1) = plt.subplots(1, 1)
    xaxis = []
    yaxis = []

    for key,value in emissions.items():
        if key < 1951:
            continue
        xaxis.append(value[0])
    
    for key, value in worldPopulation.items():
        yaxis.append(value)

    
    ax1.set_title('Emission Per World population')
    ax1.set_xlabel('total emissions (tons (MLN))')
    ax1.set_ylabel('world population (MLR)')
    ax1.plot(xaxis, yaxis, 'ob')
    plt.savefig('./emissionPerPopulation.png')



def plotTotalEmissionComparations(emissions, temperatures):
    fig, (ax1,ax2) = plt.subplots(2, 1)

    ax1.set_title('Total Emissions and Temperatures Comparation')
    ax1.set_xlabel('emissions (tons (MLN))')
    ax1.set_ylabel('temperature variance (°C)')

    ax2.set_title('Emissions Per Capita and Temperatures Comparation')
    ax2.set_xlabel('emissions per capita (tons (MLN))')
    ax2.set_ylabel('temperature variance (°C)')

    xaxis = []
    yaxis = []
    x2axis = []

    for key,value in emissions.items():
        if key < 1950:
            continue
        xaxis.append(value[0])
        x2axis.append(value[-1])
    
    for key,value in temperatures.items():
        if key < 1950:
            continue
        yaxis.append(value)
    
    ax1.plot(xaxis, yaxis[:-7], 'oc')
    ax2.plot(x2axis, yaxis[:-7], 'or')
    


def plotPopulationGrowth(worldPopulation):
    fig, (ax1) = plt.subplots(1,1)

    ax1.set_title('Population Growth')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Population (MLR)')
    
    xaxis, yaxis = [], []
    for key, value in worldPopulation.items():
        xaxis.append(key)
        yaxis.append(value)
    
    ax1.plot(xaxis, yaxis, '4--g', label='world population growth since 1951')
    ax1.legend()
    plt.savefig('./populationGrowth')



def plotTotalEmissionPerCapita(emissions):
    fig, (ax) = plt.subplots(1, 1)
    xaxis = []
    yaxis = []

    ax.set_title('Total Emissions and Emission Per Capita Comparation')
    ax.set_xlabel('total emissions (tons (MLN))')
    ax.set_ylabel('emissions per capita (tons (MLN))')
    
    for key,value in emissions.items():
        if key < 1950:
            continue
        xaxis.append(value[0])
        yaxis.append(value[-1])
    
    ax.plot(xaxis, yaxis, 'Hy')
    plt.savefig('./totalEmissionPerCapita.png')
    


def plotTemperatureByYear(temperature):
    fig, (ax) = plt.subplots(1,1)
    ax.set_title('Temperature by Year (1880-2020)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (°C)')

    xaxis = []
    yaxis = []

    for key, value in temperature.items():
        xaxis.append(key)
        yaxis.append(value)

    ax.plot(xaxis, yaxis, 'h-b')
    plt.savefig('./temperaturesByYear.png')




def main():

    emissions = {}
    temperatures = {}
    worldPopulation = {}

    data_emissions = open("./CO2_emissions.csv")
    data_emissions_reader = csv.reader(data_emissions, delimiter=',')

    data_temperature = open("./Temperature_Anomaly.csv")
    data_temperature_reader = csv.reader(data_temperature, delimiter=',')

    data_population = open("./worldPopulation.csv")
    data_population_reader = csv.reader(data_population, delimiter=',')

    for i in range(5):
        next(data_temperature_reader)
    next(data_emissions_reader)

    for row in data_temperature_reader:
        temperatures[int(row[0])] = float(row[1])

    for row in data_emissions_reader:
        if int(row[0]) < 1880:
            continue
        if row[-1] == '':
            row[-1] = '-1'
        emissions[int(row[0])] = [float(row[i]) for i in range(1, len(row))]
    
    for row in data_population_reader:
        worldPopulation[int(row[0])] = int(row[1])
    
    worldPopulation = dict(reversed(list(worldPopulation.items())))

    plotEmissionsByYear(emissions)
    plotEmissionPerPopulation(emissions, worldPopulation)
    plotTotalEmissionComparations(emissions, temperatures)
    plotPopulationGrowth(worldPopulation)
    plotTemperatureByYear(temperatures)
    plotTotalEmissionPerCapita(emissions)


if __name__ == '__main__':
    main()
