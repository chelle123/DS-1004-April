import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import *
from string import maketrans

'''
revenue weather join header
----------------------
  0)   0	 pickup_datetime
  1)   1	 fare_amount
  2)   2	 surcharge
  3)   3	 tip_amount
  4)   4	 tolls_amount
  5)   5	 total_amount
  6)   6	 tip_percentage
  7)   7	 PRCP
  8)  12	 SNWD
  9)  17	 SNOW
 10)  22	 TMAX
 11)  27	 TMIN
 12)  32	 AWND
 13)  37	 WDF2
 14)  42	 WDF5
 15)  47	 WSF2
 16)  52	 WSF5

'''
def load_data(fname):
# tip_percentage is in unit (%)
	col_names = ['time', 'total_amount', 'tip_percentage', 'PRCP', 'SNWD', 'SNOW', 'TMAX', 'TMIN', 'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5']
	df =  pd.read_csv(fname,index_col = 0, names=col_names)
	df.sort_index(inplace=True)
	return df

def to_filename(title_label,exclude_str):
	save_label = '_'.join(title_label.strip().split(' '))
	for c in exclude_str:
		save_label = save_label.replace(c,"")
	return save_label

def plot_precipitation(df, fig_size, bar_label, line_label, title_label):
	plt.figure()
	bar_df = df[bar_label]
	line_df = df[line_label]
	line_color = 'r'

	if line_label is 'total_amount':
		line_df = line_df/1000000.
		line_color = 'm'

	ax = bar_df.plot(kind='bar',figsize=fig_size);
	ax.set_ylabel("Precipitation (mm)")
	ax.set_xlabel('Week')

	ax2 = line_df.plot(kind='line',color=line_color,secondary_y=True)

	if line_label == 'total_amount':
		ax2.set_ylabel('Dollar (million)')
	else:
		ax2.set_ylabel('Percentage (%)')

	plt.title(title_label)

	save_label = to_filename(title_label,".()")
	plt.savefig(save_label);
	#plt.show()


def plot_temp_max_min(df, vs_label):
	plt.figure()

	if vs_label == 'total_amount':		
		x_df =df[vs_label]/1000000.
		ax2_ylabel = 'Dollar (million)'
		lab = 'Total Revenue'
	else:
		x_df = df[vs_label]
		ax2_ylabel = 'Percentage (%)'
		lab = 'Tip Percentage'

	ax = df[['TMAX','TMIN']].plot(kind = 'line',style = "--")
	
	ax.set_ylabel("Temperature ()")
	ax.set_xlabel('Week')
	ax.legend(['Max Temperature', 'Min Temperature'],loc = (0,0.85))

	temp_diff = df.TMAX-df.TMIN
	#temp_diff.plot(kind = 'line')

	ax2 = x_df.plot(kind='line',secondary_y=True,label=lab )
	ax2.legend(loc = (0.66,0.91))
	ax2.set_ylabel(ax2_ylabel)
	title_label=lab+' Vs. Temperature'
	save_label = to_filename(title_label,".()")
	plt.title(title_label)
	plt.savefig(save_label)

def plot_temperature_difference(df,vs_label):
	plt.figure()
	if vs_label == 'total_amount':		
		x_df =df[vs_label]/1000000.
		ax2_ylabel = 'Dollar (million)'
		lab = 'Total Revenue'
	else:
		x_df = df[vs_label]
		ax2_ylabel = 'Percentage (%)'
		lab = 'Tip Percentage'

	temp_diff = df.TMAX-df.TMIN
	ax = temp_diff.plot(kind = 'line')
	ax.set_xlabel('Week')
	ax.set_ylabel('Temperature ()')
	ax.legend(['Temp Difference'],loc = (0,0.91))

	ax2 = x_df.plot(kind='line',secondary_y=True,label=lab )
	ax2.legend(loc = (0.66,0.91))
	ax2.set_ylabel(ax2_ylabel)

	title_label = lab+' Vs. Temperature Difference'
	save_label = to_filename(title_label,".()")
	plt.title(title_label)
	plt.savefig(save_label)

def plot_wind(df):
	feat_list = ['total_amount','tip_percentage']
	for vs_label in feat_list:	
		if vs_label == 'total_amount':		
			x_df =df[vs_label]/1000000.
			ax2_ylabel = 'Dollar (million)'
			lab = 'Total Revenue'
		else:
			x_df = df[vs_label]
			ax2_ylabel = 'Percentage (%)'
			lab = 'Tip Percentage'

		ax = df[['WDF5','WSF5']].plot(kind = 'bar')
		ax.set_xlabel('Week')
		ax.set_ylabel('WDF')
		ax.legend(loc = (0,0.87))

		ax2 = x_df.plot(kind='line',color = 'm',secondary_y=True,label=lab )
		ax2.legend(loc = (0.66,0.91))
		ax2.set_ylabel(ax2_ylabel)

		title_label = lab+' Vs. Wind Speed'
		save_label = to_filename(title_label,".()")
		plt.title(title_label)
		plt.savefig(save_label)

def analyze_prcp(df):
	total_days = len(df)
	rev_sum= df['total_amount'].sum()
	rain_days = sum(df['PRCP']>50)
	rain_revenue = df[df['PRCP']>50]['total_amount']
	print 1.*rain_days/total_days
	print rain_revenue.sum()/rev_sum


def main():
	rev_weather = load_data('revweather_weekly')
	del rev_weather['tip_percentage']
	#rev_weather.to_csv('rev_weather.csv')

	'''
	#analyze_prcp(rev_weather)
	rev_weather = load_data('revweather_weekly')
	plot_precipitation(rev_weather, (18,10), ['PRCP','SNOW'],
		'total_amount','Total Revenue Vs. Precipitation (Weekly)')
	'''
	
	# tip_weather = load_data('tipweather_weekly')
	# tip_weather.to_csv("tip_weather.csv")
	'''
	plot_precipitation(tip_weather, (18,10), ['PRCP','SNOW'],
		'tip_percentage','Tip Percentage Vs. Precipitation (Weekly)')
	'''
	'''
	plot_temp_max_min(rev_weather, 'total_amount')
	plot_temp_max_min(tip_weather, 'tip_percentage')
	'''
	'''
	plot_temperature_difference(rev_weather, 'total_amount')
	plot_temperature_difference(rev_weather, 'tip_percentage')
	
	plot_wind(rev_weather)
	'''

if __name__ == '__main__':
	main()
