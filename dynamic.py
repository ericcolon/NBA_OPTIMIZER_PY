import pandas as pd
import numpy as np 


#constants
dk = 'DRAFT_KINGS'

class Site:

	def __init_(self, name = dk)
		self.name = name

	def roster_constr(self):
		if self.name == dk:
			return [
				['PG'],
				['SG'],
				['SF'],
				['PF'],
				['C'],
				['PG','SG'],
				['SF','PF'],
				['PG','SG','SF','PF','C'],
				]

	def salary_cap(self):
		if self.name == dk:
			return 50000

	def value(self,projection,salary):
		if name == dk:
			min_proj, value_mult, min_sal = 18, 4.2, 3000

		return projection - (min_proj + value_mult * (salary - min_sal)/1000)

class Lineup:

	def __init__(self, pg = None, sg = None, sf = None, pf = None, c = None, g = None, f = None, flex = None):
		self.roster = {}
		self.roster['pg'] = pg
		self.roster['sg'] = sg
		self.roster['sf'] = sf
		self.roster['pf'] = pf
		self.roster['c'] = c
		self.roster['g'] = g
		self.roster['f'] = f
		self.roster['flex'] = flex
		

class Pool:
	def __init__(self):
        __pool = pd.DataFrame({})
		__orig_pool = pd.DataFrame({})

	def from_csv(self, site):

		out = pd.read_csv('./projections.csv')[['Name','Projection','Salary','Position','Team']]
		
		out['Value'] = value(site,out['Projection'],out['Salary'])

		for i, roster_spot in enumerate(roster_constr(site)):
			out["isEligibleRosterSpot" + str(i)] = False
			for roster_position in roster_spot:
				out["isEligibleRosterSpot" + str(i)] = np.logical_or(out['Position'].str.contains(roster_position) , out["isEligibleRosterSpot" + str(i)])
		
		out["isExcluded"] = False
		out["isLocked"] = False
		out["isInLineup"] = False
		
		return out

	def dynamic_optimize(self, lineup):
		pass

if __name__ == "__main__":
	player_pool = Pool()

	memoized = {}
