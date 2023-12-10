import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template

# Fratu-Halunga Theodor-Coreneliu => X = 12 , Y = 15

dataframe = pd.read_csv('data.csv')
plotcounter = 0
plots = []


def plot_column(dataframe, column_name, plot_range=None, color='#1f77b4'):
    if plot_range is None:
        plot_range = len(dataframe)

    if plot_range >= 0:
        plot_range_list = range(plot_range)
    else:
        plot_range_list = range(len(dataframe) + plot_range, len(dataframe))

    try:
        plt.plot(plot_range_list, dataframe[column_name][plot_range_list], marker='.', color=color)
        plt.ylabel(column_name)
        plt.title(column_name)
        global plotcounter, plots
        plt.savefig(f"static/plots/Plot{plotcounter}.jpg")
        plots.append(f"plots/Plot{plotcounter}.jpg")
        plotcounter += 1
        plt.show()

    except KeyError:
        print(f"Sorry, {column_name} column does not exist in the provided dataframe")


plot_column(dataframe, "Durata")
plot_column(dataframe, "Puls")
plot_column(dataframe, "MaxPuls")
plot_column(dataframe, "Calorii")

plot_column(dataframe, "Durata", 12, 'red')
plot_column(dataframe, "Puls", 12, 'red')
plot_column(dataframe, "MaxPuls", 12, 'red')
plot_column(dataframe, "Calorii", 12, 'red')

plot_column(dataframe, "Durata", -15, 'green')
plot_column(dataframe, "Puls", -15, 'green')

###################################################################################################

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/entire_span_plots/")
def entire_span_plots():
    return render_template('entire_span_plots.html', plots=plots)


@app.route("/first_X_datapoints/")
def first_X_datapoints():
    return render_template('first_X_datapoints.html', plots=plots)


@app.route("/last_Y_datapoints/")
def last_Y_datapoints():
    return render_template('last_Y_datapoints.html', plots=plots)


app.run()