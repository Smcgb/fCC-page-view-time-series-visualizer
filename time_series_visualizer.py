import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date", parse_dates=True)

# Clean data
df = df[(df['value'] < np.percentile(df.values, 97.5)) & (df['value'] > np.percentile(df.values, 2.5))]

def draw_line_plot():
    fig, ax = plt.subplots()
    # Draw line plot
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="date", y="value")

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')

    return fig
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar['month_name'] = df_bar.index.strftime('%b')

    month_map = {
        'Jan': 'January',
        'Feb': 'February',
        'Mar': 'March',
        'Apr': 'April',
        'May': 'May',
        'Jun': 'June',
        'Jul': 'July',
        'Aug': 'August',
        'Sep': 'September',
        'Oct': 'October',
        'Nov': 'November',
        'Dec': 'December'
    }

    # Aggregate data
    df_bar = df_bar.groupby(['year', 'month', 'month_name']).mean().reset_index()

    # Sort by month using categorical data type for month names
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_bar['month_name'] = pd.Categorical(df_bar['month_name'], categories=months_order, ordered=True)
    df_bar = df_bar.sort_values('month')

    df_bar ['month_name'] = df_bar ['month_name'].map(month_map)

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(ax=ax, data=df_bar, x="year", y="value", hue="month_name")

    # Set the labels and title
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Monthly Average Page Views per Year')

    plt.legend(title='Months', loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy(deep=True)
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # creates 2 subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
