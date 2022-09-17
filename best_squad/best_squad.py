import pandas as pd
import numpy as np
import psycopg2
import psycopg2.extras as extras
from pulp import *

class BestPlayers:
    def __init__(self, df):
        self.df = df
        self.prob= self.create_problem_variable()
        self.decision_variables = []
        self.optimisation_result = self.solve_optimisation_problem()
    

    def create_problem_variable(self):
        self.prob = pulp.LpProblem('FantasyTeam', LpMaximize)
        

    def create_decision_variables(self):
        #self.decision_variables = []
        for rownum, row in self.df.iterrows():
            variable = str('x' + str(rownum))
            variable = pulp.LpVariable(str(variable), lowBound = 0, upBound = 1, cat= 'Integer') #make variables binary
            self.decision_variables.append(variable)
    
    def create_constraints(self, constraint_column, constraint_name, constraint, sign):
        ''' 
        
        Function to create constraints for the constrained optimisation.

        The sign argument can take value '=', '<=', '>=', '>', '<'
        
        
        '''
        constraint_string = ""
        for row_idx, row in self.df.iterrows():
            for idx, player in enumerate(self.decision_variables):
                if row_idx == idx:
                    if constraint_name in ['GKP', 'DEF', 'MID', 'FWD']:
                        if row[constraint_column] == constraint_name:
                            constraint_string += 1*player
                    else :
                        constraint_string += row[constraint_column]*player

        if sign == '=':
            self.prob += (constraint_string == constraint)
        elif sign == '<=':
            self.prob += (constraint_string <= constraint)
        elif sign == '>=':
            self.prob += (constraint_string >= constraint)
        elif sign == '<':
            self.prob += (constraint_string < constraint)
        elif sign == '>':
            self.prob += (constraint_string > constraint)

    def create_objective_function(self):
        total_points = ""
        for rownum, row in self.df.iterrows():
            for i, player in enumerate(self.decision_variables):
                if rownum == i:
                    formula = row['total_points']*player
                    total_points += formula

        self.prob += total_points

    def create_team_constraints(self):
        team_dict= {}
        for team in set(self.df.team):
            team_dict[str(team)]=dict()
            team_dict[str(team)]['avail'] = 3
            team_dict[str(team)]['total'] = ""
            for rownum, row in self.df.iterrows():
                for i, player in enumerate(self.decision_variables):
                    if rownum == i:
                        if row['team'] == team:
                            formula = 1*player
                            team_dict[str(team)]['total'] += formula

            self.prob += (team_dict[str(team)]['total'] <= team_dict[str(team)]['avail'])


    def create_optimisation_problem(self):
        self.create_problem_variable()
        self.create_decision_variables()
        self.create_objective_function()
        constraints = ['GKP', 'DEF', 'MID', 'FWD']
        players_allowed = [2,5,5,3]
        for i, j in zip(constraints, players_allowed):
            self.create_constraints('player_position', i, j, '=')
        self.create_constraints('now_cost', 'cost', 1000, '<=')
        self.create_team_constraints()


    def solve_optimisation_problem(self):
        self.create_optimisation_problem()
        self.prob.writeLP('FantasyTeam.lp')
        optimization_result = self.prob.solve()
        self.optimisation_result = optimization_result 


    def return_team(self):
        self.solve_optimisation_problem()
        variable_name = []
        variable_value = []

        for v in self.prob.variables():
            variable_name.append(v.name)
            variable_value.append(v.varValue)

        data = pd.DataFrame({'variable': variable_name, 'value': variable_value})
        for rownum, row in data.iterrows():
            value = re.findall(r'(\d+)', row['variable'])
            data.loc[rownum, 'variable'] = int(value[0])

        data = data.sort_index()

        #append results
        for rownum, row in self.df.iterrows():
            for results_rownum, results_row in data.iterrows():
                if rownum == results_row['variable']:
                    self.df.loc[rownum, 'decision'] = results_row['value']

        self.df[self.df.decision==1].now_cost.sum() 
        self.df[self.df.decision==1].total_points.sum() 
        best_squad = self.df[self.df.decision==1].sort_values('player_position').head(15)

        ####check constraints hold:
        if max(list(best_squad['team'].value_counts()))>3:
            print('Team Constraint Failed')
        else:
            print('Maximum number of players from one team is 3 or less')

        if best_squad['now_cost'].sum()> 1000:
            print('Cost constraint failed')
        else:
            print('Cost constraint holds')
        
        return best_squad


    

            