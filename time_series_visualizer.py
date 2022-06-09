import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])
df = df.set_index('date')

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize =(24, 10))
    plt.plot(df, color = 'red', linewidth = 1)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = pd.to_datetime(df.index)
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df_bar = (df.groupby(['Year', 'Month'])['value'].mean()).unstack()

    # Draw bar plot
    fig = df_bar.plot(legend = True, kind = 'bar', xlabel ="Years", ylabel = "Average Page Views", figsize=(15,10)).figure
    plt.legend(title ="Months", labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.sort_values(by='Month')

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    ax1 = plt.subplot(1, 2, 1)
    sns.boxplot(x="year", y="value", data = df_box).set(title = "Year-wise Box Plot (Trend)", xlabel="Year", ylabel= "Page Views")

    ax2 = plt.subplot(1, 2, 2)
    sns.boxplot(x="month", y = "value", data = df_box).set(title = "Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel= "Page Views")






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
