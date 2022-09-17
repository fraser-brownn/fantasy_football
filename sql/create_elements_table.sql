CREATE TABLE IF NOT EXISTS fantasy_football (
    chance_of_playing_next_round                    decimal(10,4)
    ,chance_of_playing_this_round                   decimal(10,4)
    ,code                                           int
    ,cost_change_event                              int
    ,cost_change_event_fall                         int
    ,cost_change_start                              int
    ,cost_change_start_fall                         int
    ,dreamteam_count                                int
    ,element_type                                   int
    ,ep_next                                        varchar(100)
    ,ep_this                                        varchar(100)
    ,event_points                                   int
    ,first_name                                     varchar(100)
    ,form                                           varchar(100)
    ,id_                                            int
    ,in_dreamteam                                   bool
    ,news                                           varchar(100)
    ,news_added                                     varchar(100)
    ,now_cost                                       int
    ,photo                                          varchar(100)
    ,points_per_game                                varchar(100)
    ,second_name                                    varchar(100)
    ,selected_by_percent                            varchar(100)
    ,special                                        bool
    ,squad_number                                   varchar(100)
    ,status                                         varchar(100)
    ,team                                           int
    ,team_code                                      int
    ,total_points                                   int
    ,transfers_in                                   int
    ,transfers_in_event                             int
    ,transfers_out                                  int
    ,transfers_out_event                            int
    ,value_form                                     varchar(100)
    ,value_season                                   varchar(100)
    ,web_name                                       varchar(100)
    ,minutes                                        int
    ,goals_scored                                   int
    ,assists                                        int
    ,clean_sheets                                   int
    ,goals_conceded                                 int
    ,own_goals                                      int
    ,penalties_saved                                int
    ,penalties_missed                               int
    ,yellow_cards                                   int
    ,red_cards                                      int
    ,saves                                          int
    ,bonus                                          int
    ,bps                                            int
    ,influence                                      varchar(100)
    ,creativity                                     varchar(100)
    ,threat                                         varchar(100)
    ,ict_index                                      varchar(100)
    ,influence_rank                                 int
    ,influence_rank_type                            int
    ,creativity_rank                                int
    ,creativity_rank_type                           int
    ,threat_rank                                    int
    ,threat_rank_type                               int
    ,ict_index_rank                                 int
    ,ict_index_rank_type                            int
    ,corners_and_indirect_freekicks_order           decimal(10,4)
    ,corners_and_indirect_freekicks_text            varchar(100)
    ,direct_freekicks_order                         decimal(10,4)
    ,direct_freekicks_text                          varchar(100)
    ,penalties_order                                decimal(10,4)
    ,penalties_text                                 varchar(100)
    ,date_inserted                                  date);


CREATE TABLE IF NOT EXISTS player_types (

    id_                                             int
    ,plural_name                                    varchar(100)
    ,plural_name_short                              varchar(100)
    ,singular_name                                  varchar(100)
    ,singular_name_short                            varchar(100)
    ,squad_select                                   int
    ,squad_min_play                                 int
    ,squad_max_play                                 int
    ,ui_shirt_specific                              bool
    ,sub_positions_locked                           varchar(100)
    ,element_count                                  int
    ,date_inserted                                  date
);


CREATE TABLE IF NOT EXISTS teams (

    code                                            int
    ,draw                                           int
    ,form                                           VARCHAR(100)
    ,id                                             int
    ,loss                                           int
    ,name_                                          VARCHAR(100)
    ,played                                         int
    ,points                                         int
    ,position                                       int
    ,short_name                                     VARCHAR(100)
    ,strength                                       int
    ,team_division                                  VARCHAR(100)
    ,unavailable                                    bool
    ,win                                            int
    ,strength_overall_home                          int
    ,strength_overall_away                          int
    ,strength_attack_home                           int
    ,strength_attack_away                           int
    ,strength_defence_home                          int
    ,strength_defence_away                          int
    ,pulse_id                                       int
    ,date_inserted                                  date
);


CREATE TABLE IF NOT EXISTS events (


    id                                              int
    ,name_                                          varchar(100)
    ,deadline_time                                  varchar(100)
    ,average_entry_score                            int
    ,finished                                       bool
    ,data_checked                                   bool
    ,highest_scoring_entry                          decimal(10,0)
    ,deadline_time_epoch                            int
    ,deadline_time_game_offset                      int
    ,highest_score                                  decimal(10,0)
    ,is_previous                                    bool
    ,is_current                                     bool
    ,is_next                                        bool
    ,cup_leagues_created                            bool
    ,h2h_ko_matches_created                         bool
    ,most_selected                                  decimal(10,0)
    ,most_transferred_in                            decimal(10,0)
    ,top_element                                    decimal(10,0)
    ,transfers_made                                 int
    ,most_captained                                 decimal(10,0)
    ,most_vice_captained                            decimal(10,0)
    ,date_inserted                                  date
);


