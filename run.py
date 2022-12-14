from ingestion.data_ingestion import *
from best_squad.best_squad import *

query = '''

SELECT 
        first_name
        ,second_name
        ,web_name
        ,t1.id_
        ,now_cost
        ,points_per_game
        ,selected_by_percent
        ,team
        ,team_code
        ,total_points
        ,minutes
        ,goals_scored
        ,assists
        ,clean_sheets
        ,goals_conceded
        ,yellow_cards
        ,red_cards
        ,bonus
        ,cost_change_start
        ,cost_change_event
        ,dreamteam_count
        ,selected_by_percent
        ,t2.plural_name_short as player_position
        ,squad_select
        ,squad_min_play
        ,squad_max_play
        ,T1.date_inserted
        ,cast(cast(total_points as decimal(20,2))/cast(now_cost as decimal(20,2)) as decimal(10,2)) 
            AS points_per_cost
        
 
    FROM fantasy_football t1

    INNER JOIN player_types t2
        ON t1.element_type = t2.id_

    where  t1.date_inserted = (SELECT max(date_inserted) from fantasy_football)

    group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27
        

'''

raw_data = execute_query(query)

linear_optimisation = BestPlayers(raw_data)

players = linear_optimisation.return_team()[['web_name']] ## return list of players in best squad

print(players)

