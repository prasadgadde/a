import gtk
import pandas as pd
from pandas import Series as s
from pandas import DataFrame as df
import numpy as np
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

class PyApp(gtk.Window):

	data = pd.read_csv("Crimes_commited_ipc2.csv")
	combobox_district = gtk.ComboBox()	
	combobox_year = gtk.ComboBox()
	combobox_state = gtk.ComboBox()
	combobox_crime = gtk.ComboBox()
	combobox_state1 = gtk.ComboBox()
	combobox_state2 = gtk.ComboBox()
	combobox_yearc = gtk.ComboBox()
	button_show_graph = gtk.Button("Show Graph")
	compare_button = gtk.Button("Compare")
	filtered_data = df()

	store_dist = gtk.ListStore(str)

	def __init__(self):
		super(PyApp, self).__init__()

		self.set_title("Crimes in India")
		self.set_size_request(700, 500)
		#self.set_icon_from_file("/home/prasadgadde/BigData/Project/icon.png")

		# Set window background image
		pixbuf = gtk.gdk.pixbuf_new_from_file("vector-grunge-texture-background.jpg")
		pixmap, mask = pixbuf.render_pixmap_and_mask()
		width, height = pixmap.get_size()
		#del pixbuf
		self.set_app_paintable(gtk.TRUE)
		self.resize(width, height)
		self.realize()
		self.window.set_back_pixmap(pixmap, gtk.FALSE)
		#del pixmap

		nb = gtk.Notebook()
		nb.set_tab_pos(gtk.POS_TOP)
		vbox = gtk.VBox(False, 5)

		vb = gtk.VBox()
		hbox = gtk.HBox(True, 3)
		hlabelsbox = gtk.HBox(True, 120)
		hbuttonbox = gtk.HBox(True, 10)

		# Horizontal box for labels
		label_state = gtk.Label("State")
		label_district = gtk.Label("District")
		label_year = gtk.Label("Year")
		label_crime = gtk.Label("Crime")

		hlabelsbox.pack_start(label_state, True, True, 10)
		hlabelsbox.pack_start(label_district, True, True, 10)
		hlabelsbox.pack_start(label_year, True, True, 10)
		hlabelsbox.pack_start(label_crime, True, True, 10)

		valign = gtk.Alignment(0.25, 0.10, 0, 0)
		valign1 = gtk.Alignment(0, 1, 0, 0)
		valign2 = gtk.Alignment(0, 0, 1, 0)
		
		store = gtk.ListStore(str)
		cell = gtk.CellRendererText()
		self.combobox_state.pack_start(cell)
		self.combobox_state.set_title("States")
		self.combobox_state.add_attribute(cell, 'text', 0)

		hbox.pack_start(self.combobox_state, True, True, 10)

		store.append (["ANDHRA PRADESH"])
		store.append (["ARUNACHAL PRADESH"])
		store.append (["ASSAM"])
		store.append (["BIHAR"])
		store.append (["GOA"])
		store.append (["GUJARAT"])
		store.append (["HARYANA"])
		store.append (["HIMACHAL PRADESH"])
		store.append (["JAMMU & KASHMIR"])
		store.append (["JHARKHAND"])
		store.append (["KARNATAKA"])
		store.append (["KERALA"])
		store.append (["MADHYA PRADESH"])
		store.append (["MAHARASHTRA"])
		store.append (["MANIPUR"])
		store.append (["MEGHALAYA"])
		store.append (["MIZORAM"])
		store.append (["NAGALAND"])
		store.append (["ODISHA"])
		store.append (["MIZORAM"])
		store.append (["PUNJAB"])
		store.append (["RAJASTHAN"])
		store.append (["TAMIL NADU"])
		store.append (["TRIPURA"])
		store.append (["UTTAR PRADESH"])
		store.append (["UTTARAKHAND"])
		store.append (["WEST BENGAL"])
		store.append (["A & N ISLANDS"])
		store.append (["CHANDIGARH"])
		store.append (["D & N HAVELI"])
		store.append (["DAMAN & DIU"])
		store.append (["DELHI UT"])
		store.append (["LAKSHADWEEP"])
		store.append (["PUDUCHERRY"])
		
		self.combobox_state.set_model(store)
		self.combobox_state.connect('changed', self.on_changed)
		self.combobox_state.set_active(0)

		self.store_dist = gtk.ListStore(str)
		cell_dist = gtk.CellRendererText()
		self.combobox_district.pack_start(cell_dist)
		self.combobox_district.add_attribute(cell_dist, 'text', 0)
		self.combobox_district.connect('changed', self.on_changed_district)
		hbox.pack_start(self.combobox_district, True, True, 10)

		
		#Year dropbox
		
		store_year = gtk.ListStore(str)
		cell_year = gtk.CellRendererText()
		self.combobox_year.pack_start(cell_year)
		self.combobox_year.add_attribute(cell_year, 'text', 0)

		hbox.pack_start(self.combobox_year, True, True, 10)

		district = self.data[(self.data['STATEorUT']=='ANDHRA PRADESH') |  (self.data['STATEorUT']=='Andhra Pradesh')].filter(items=['STATE/UT','DISTRICT','YEAR'])
		year=s(district['YEAR']).unique().tolist()
		store_year.append(["All"])
		for i in year:
			store_year.append([i])
		
		self.combobox_year.set_model(store_year)
		#combobox.connect('changed', self.on_changed)
		self.combobox_year.set_active(0)
		self.combobox_year.connect('changed', self.on_changed_year)

		# Crime dropbox
		
		store_crime = gtk.ListStore(str)
		cell_crime = gtk.CellRendererText()
		self.combobox_crime.pack_start(cell_crime)
		self.combobox_crime.add_attribute(cell_crime, 'text', 0)
		self.combobox_crime.connect('changed', self.on_changed_crime)

		hbox.pack_start(self.combobox_crime, True, True, 10)

		store_crime.append (["MURDER"])
		store_crime.append (["RAPE"])
		store_crime.append (["KIDNAPPING"])
		store_crime.append (["RIOTS"])
		store_crime.append (["ROBBERY"])
		store_crime.append (["BURGLARY"])
		store_crime.append (["DOWRY DEATHS"])
		store_crime.append (["TOTAL IPC CRIMES"])
		self.combobox_crime.set_model(store_crime)
		#combobox.connect('changed', self.on_changed)
		self.combobox_crime.set_active(0)		

		valign.add(hbox)
		valign1.add(hlabelsbox)
		
		button_disp_data = gtk.Button("Display Data")

		button_disp_data.connect("clicked", self.display_data)
		self.button_show_graph.connect("clicked", self.display_graph)

		self.button_show_graph.set_sensitive(False)

		hbuttonbox.pack_start(button_disp_data, True, True, 10)
		hbuttonbox.pack_start(self.button_show_graph, True, True, 10)
		valign2.add(hbuttonbox)
		vbox.pack_start(valign1)
		vbox.pack_start(valign)
		vbox.pack_start(valign2)
		
		nb.append_page(vbox)
		nb.set_tab_label_text(vbox, "District wise crimes")

		# Code for 2nd TAB

		state1lbl = gtk.Label("State 1")
		state2lbl = gtk.Label("State 2")
		
		
		
		self.compare_button.connect("clicked", self.compare_states)
		self.compare_button.set_sensitive(False)

		table = gtk.Table(8,4,True)
		table.set_col_spacings(7)

		states = ["ANDHRA PRADESH", "ARUNACHAL PRADESH", "ASSAM", "BIHAR","CHHATTISGARH", "GOA","GUJARAT","HARYANA","HIMACHAL PRADESH", "JAMMU & KASHMIR", "JHARKHAND", "KARNATAKA", "KERALA", "MADHYA PRADESH", "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA", "PUNJAB", "RAJASTHAN", "SIKKIM", "TAMIL NADU", "TRIPURA", "UTTAR PRADESH", "UTTARAKHAND", "WEST BENGAL","A & N ISLANDS", "CHANDIGARH", "D & N HAVELI", "DAMAN & DIU", "DELHI UT", "LAKSHADWEEP", "PUDUCHERRY"]
		storestate1 = gtk.ListStore(str)
		cellstate1 = gtk.CellRendererText()
		self.combobox_state1.pack_start(cellstate1)
		self.combobox_state1.add_attribute(cellstate1, 'text', 0)
		self.combobox_state1.set_active(0)
		for i in states:
			storestate1.append([i])
		self.combobox_state1.set_model(storestate1)
		

		storestate2 = gtk.ListStore(str)
		cellstate2 = gtk.CellRendererText()
		self.combobox_state2.pack_start(cellstate2)
		self.combobox_state2.add_attribute(cellstate2, 'text', 0)
		self.combobox_state2.set_active(0)
		for i in states:
			storestate2.append([i])
		self.combobox_state2.set_model(storestate2)

		store_yearc = gtk.ListStore(str)
		cell_yearc = gtk.CellRendererText()		
		self.combobox_yearc.pack_start(cell_yearc)
		self.combobox_yearc.add_attribute(cell_yearc, 'text', 0)
		self.combobox_yearc.set_active(0)

		for i in year:
			store_yearc.append([i])
		self.combobox_yearc.set_model(store_yearc)

		self.combobox_state1.connect('changed', self.on_changed_state1)
		self.combobox_state2.connect('changed', self.on_changed_state2)
		self.combobox_yearc.connect('changed', self.on_changed_yearc)


		table.attach(state1lbl, 0, 1, 3, 4)
		table.attach(state2lbl, 2, 3, 3, 4)
		table.attach(self.combobox_state1, 0, 1, 4, 5,xpadding = 8, ypadding=9)
		table.attach(self.combobox_state2, 2, 3, 4, 5,xpadding = 8, ypadding=9)
		table.attach(self.combobox_yearc, 1, 2, 4, 5,xpadding = 8, ypadding=9)
		table.attach(self.compare_button, 1, 2, 6, 7, xpadding = 8, ypadding=9)
		
		nb.append_page(table)
		nb.set_tab_label_text(table, "Comparison of states")

		tv = gtk.TextView()
		nb.append_page(tv)
		nb.set_tab_label_text(tv, "About")
		
		self.add(nb)
		
		self.connect("destroy", gtk.main_quit)		
		self.show_all()

	def on_changed_state1(self, widget):
		if(widget.get_active_text() == self.combobox_state2.get_active_text()):
			self.compare_button.set_sensitive(False)
		else:
			self.compare_button.set_sensitive(True)
		return

	def on_changed_state2(self, widget):
		if(widget.get_active_text() == self.combobox_state1.get_active_text()):
			self.compare_button.set_sensitive(False)
		else:
			self.compare_button.set_sensitive(True)
		return

	def on_changed_yearc(self, widget):
		return

	def on_changed(self, widget):
		#data = pd.read_csv("/home/prasadgadde/BigData/Project/crime-in-india/crime/01_District_wise_crimes_committed_IPC_2013.csv"	
		district = s(self.data[self.data['STATEorUT']==widget.get_active_text()].filter(items=['DISTRICT'])['DISTRICT']).unique().tolist()
		self.store_dist.clear()
		self.store_dist.append(["All"])
		for i in district:
			self.store_dist.append([i])

		self.combobox_district.set_model(self.store_dist)
		#combobox.connect('changed', self.on_changed)
		self.combobox_district.set_active(0)


	def display_data(self, widget):
		#print self.combobox_state.get_active_text(), self.combobox_year.get_active_text(), self.combobox_district.get_active_text(), self.combobox_crime.get_active_text()
		#filtered_data = self.data[((self.data['STATE.UT']==self.combobox_state.get_active_text()) & (self.data['DISTRICT']==self.combobox_district.get_active_text()) & (self.data['YEAR']==self.combobox_year.get_active_text()))].filter(items=['STATE/UT','DISTRICT','YEAR', self.combobox_crime.get_active_text()])

		dialog = gtk.Dialog("My dialog",
		self,
		gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
		(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
		dialog.set_size_request(400,700)
		
		liststore = gtk.ListStore(str, str, str, str)

		treeview = gtk.TreeView(liststore)

		tvcolumn = gtk.TreeViewColumn("STATE/UT")
		tvcolumn1 = gtk.TreeViewColumn("DISTRICT")
		tvcolumn2 = gtk.TreeViewColumn("YEAR")
		tvcolumn3 = gtk.TreeViewColumn(self.combobox_crime.get_active_text())
		
		for i in self.filtered_data.values.tolist():
			liststore.append(i)	
		#liststore.append(['Open', gtk.STOCK_OPEN, 'Open a File', True])
	
		treeview.append_column(tvcolumn)
		treeview.append_column(tvcolumn1)
		treeview.append_column(tvcolumn2)
		treeview.append_column(tvcolumn3)

		cell = gtk.CellRendererText()
		cell1 = gtk.CellRendererText()
		cell2 = gtk.CellRendererText()
		cell3 = gtk.CellRendererText()
		
		cell.set_property('cell-background', 'yellow')
		cell1.set_property('cell-background', 'cyan')
		cell2.set_property('cell-background', 'pink')
		cell3.set_property('cell-background', 'red')

		tvcolumn.pack_start(cell, False)
		tvcolumn1.pack_start(cell1, True)
		tvcolumn2.pack_start(cell2, True)
		tvcolumn3.pack_start(cell3, True)

		tvcolumn.set_attributes(cell, text = 0)
		tvcolumn1.set_attributes(cell1, text = 1)
		tvcolumn2.set_attributes(cell2, text = 2)
		tvcolumn3.set_attributes(cell3, text = 3)

		scrolled_window = gtk.ScrolledWindow()
		scrolled_window.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
		scrolled_window.add(treeview)
		scrolled_window.set_border_width(10)
		#scrolled_window.set_min_content_height(200)

		scrolled_window.add(treeview)

		
		treeview.set_search_column(0)
		dialog.vbox.add(scrolled_window)
		treeview.show()
		scrolled_window.show()
		res = dialog.run()
		dialog.destroy()
		
		return

	def display_graph(self, widget):
		dialog = gtk.Dialog("My dialog",
		self,
		gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
		(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
		dialog.set_size_request(1300,500)

		# Crime name filter
		if " " not in self.combobox_crime.get_active_text():
			crime = self.combobox_crime.get_active_text()
		else:
			crime = ".".join(self.combobox_crime.get_active_text().split(" "))

		

		fig = Figure(figsize=(12, 10), dpi=100)

		sales = [{'Groups':'0-9', 'Counts':38},
				{'Groups':'10-19', 'Counts':41},
				{'Groups':'20-29', 'Counts':77},
				{'Groups':'30-39', 'Counts':73},
				{'Groups':'40-49', 'Counts':77}]
		df = pd.DataFrame(sales)

		ax = fig.add_subplot(111)

		if (self.combobox_year.get_active_text() == "All" and self.combobox_district.get_active_text() != "All"):
			
			self.filtered_data = self.filtered_data.reset_index(drop=True)
			ypos = np.arange(len(self.filtered_data['YEAR'].tolist()))
			p1 = ax.bar(ypos, self.filtered_data[crime], width=0.6, color='r')

			ax.set_title(crime.lower() +'s in ' + self.combobox_district.get_active_text() +'  - Yearwise')
			ax.set_xticks(ypos+0.3)
			ax.set_xticklabels(self.filtered_data.YEAR)
		elif (self.combobox_district.get_active_text() == "All" and self.combobox_year.get_active_text() != "All"):
			fd_total_removed = self.filtered_data[self.filtered_data.DISTRICT != 'TOTAL']
			ypos = np.arange(len(fd_total_removed['DISTRICT'].tolist()))
			
			p1 = ax.bar(ypos, fd_total_removed[crime], width=0.3, color='r')
			fontx = {'fontsize': 7,
 					'fontweight': 2,
 					'verticalalignment': 'center',
 					'horizontalalignment': 'center'}

			ax.set_title(crime + 's in ' + self.combobox_state.get_active_text() + '(' +self.combobox_state.get_active_text()+' )' + '  - Districtwise')
			ax.set_xticks(ypos+0.15)
			ax.set_xticklabels(fd_total_removed.DISTRICT, fontdict=fontx)
		else:
			print(df.index)
			p1 = ax.bar(df.index, df.Counts, width=0.8, color='r')


			ax.set_title('Scores by group and gender')
			ax.set_xticks(df.index+0.4)
			ax.set_xticklabels(df.Groups)

		canvas = FigureCanvas(fig)  # a gtk.DrawingArea
		canvas.set_size_request(800, 600)
		dialog.vbox.pack_start(canvas)
		toolbar = NavigationToolbar(canvas, dialog)
		dialog.vbox.pack_start(toolbar, False, False)
		canvas.show()
		dialog.run()
		dialog.destroy()
		return

	def on_changed_district(self, widget):
		if(self.combobox_year.get_active_text() != 'All'):		
			intyear = int(self.combobox_year.get_active_text())

		# Check crime field
		if " " not in self.combobox_crime.get_active_text():
			crime = self.combobox_crime.get_active_text()
		else:
			crime = ".".join(self.combobox_crime.get_active_text().split(" "))

		if(self.combobox_district.get_active_text() == 'All' and self.combobox_year.get_active_text() == 'All'):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text()').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
			self.button_show_graph.set_sensitive(False)
		elif(self.combobox_district.get_active_text() == 'All'):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
			self.button_show_graph.set_sensitive(True)
		elif (self.combobox_year.get_active_text() == "All"):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and DISTRICT == @self.combobox_district.get_active_text()').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
			self.button_show_graph.set_sensitive(True)	
		else:
			self.button_show_graph.set_sensitive(False)
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and DISTRICT == @self.combobox_district.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
				
		return

	def on_changed_year(self, widget):
		if(self.combobox_year.get_active_text() != 'All'):		
			intyear = int(self.combobox_year.get_active_text())

		# Check crime field
		if " " not in self.combobox_crime.get_active_text():
			crime = self.combobox_crime.get_active_text()
		else:
			crime = ".".join(self.combobox_crime.get_active_text().split(" "))

		if(self.combobox_district.get_active_text() == 'All' and self.combobox_year.get_active_text() == 'All'):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text()').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
			self.button_show_graph.set_sensitive(False)
		elif(self.combobox_district.get_active_text() == 'All'):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
			self.button_show_graph.set_sensitive(True)
		elif (self.combobox_year.get_active_text() == "All"):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and DISTRICT == @self.combobox_district.get_active_text()').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
			self.button_show_graph.set_sensitive(True)	
		else:
			self.button_show_graph.set_sensitive(False)
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and DISTRICT == @self.combobox_district.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
				
		return

	def on_changed_crime(self, widget):
		if(self.combobox_year.get_active_text() != 'All'):		
			intyear = int(self.combobox_year.get_active_text())

		# Check crime field
		if " " not in self.combobox_crime.get_active_text():
			crime = self.combobox_crime.get_active_text()
		else:
			crime = ".".join(self.combobox_crime.get_active_text().split(" "))

		if(self.combobox_district.get_active_text() == 'All' and self.combobox_year.get_active_text() == 'All'):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text()').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
		elif(self.combobox_district.get_active_text() == 'All'):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
		elif (self.combobox_year.get_active_text() == "All"):
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and DISTRICT == @self.combobox_district.get_active_text()').filter(items=['STATEorUT','DISTRICT','YEAR', crime])	
		else:
			self.filtered_data = self.data.query('STATEorUT == @self.combobox_state.get_active_text() and DISTRICT == @self.combobox_district.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT','DISTRICT','YEAR', crime])
		return

	def compare_states(self, widget):
		crimes = ["MURDER", "RAPE", "KIDNAPPING.ABDUCTION", "RIOTS", "ROBBERY", "BURGLARY", "DOWRY.DEATHS"]
		intyear = int(self.combobox_yearc.get_active_text()) 
		state1_data = self.data.query('STATEorUT == @self.combobox_state1.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT', 'DISTRICT', 'YEAR', crimes[0], crimes[1],crimes[2],crimes[3],crimes[4],crimes[5],crimes[6]])[self.data.DISTRICT == 'TOTAL']
		state2_data = self.data.query('STATEorUT == @self.combobox_state2.get_active_text() and YEAR == @intyear').filter(items=['STATEorUT', 'DISTRICT', 'YEAR', crimes[0], crimes[1],crimes[2],crimes[3],crimes[4],crimes[5],crimes[6]])[self.data.DISTRICT == 'TOTAL']
		print(state1_data.iloc[0]['MURDER'])

		state1_total = [state1_data.iloc[0][crimes[0]],state1_data.iloc[0][crimes[1]],state1_data.iloc[0][crimes[2]],state1_data.iloc[0][crimes[3]],state1_data.iloc[0][crimes[4]],state1_data.iloc[0][crimes[5]],state1_data.iloc[0][crimes[6]]]
		state2_total = [state2_data.iloc[0][crimes[0]],state2_data.iloc[0][crimes[1]],state2_data.iloc[0][crimes[2]],state2_data.iloc[0][crimes[3]],state2_data.iloc[0][crimes[4]],state2_data.iloc[0][crimes[5]],state2_data.iloc[0][crimes[6]]]
		print(state1_total)

		dialog = gtk.Dialog("My dialog",
		self,
		gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
		(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
		fig = Figure(figsize=(5, 4), dpi=100)
		dialog.set_size_request(1300,500)
		ax = fig.add_subplot(111)
		ypos = np.arange(len(crimes))
		print(ypos)
		p1 = ax.bar(ypos-0.4, state1_total, width=0.4, color='r', align='center')
		p2 = ax.bar(ypos, state2_total, width=0.4, color='b', align='center')

		ax.set_title("Comparison of " + self.combobox_state1.get_active_text() + " and " + self.combobox_state2.get_active_text())
		ax.set_xticks(ypos-0.2)
		ax.set_xticklabels(crimes)
		ax.set_ylabel('Total Crimes')
		ax.legend((p1[0], p2[0]), (self.combobox_state1.get_active_text(), self.combobox_state2.get_active_text()))

		canvas = FigureCanvas(fig)  # a gtk.DrawingArea
		canvas.set_size_request(800, 600)
		dialog.vbox.pack_start(canvas)
		toolbar = NavigationToolbar(canvas, dialog)
		dialog.vbox.pack_start(toolbar, False, False)
		canvas.show()
		dialog.run()
		dialog.destroy()
		
		return		

PyApp()
gtk.main()

