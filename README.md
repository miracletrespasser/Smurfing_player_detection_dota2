# Smurfing_player_detection_dota2
Detect smurfing players in dota2 using fuzzy logic approach
User Tutorial:
   Test.py requires python3.9 with fuzzy-expert pacakge installed: https://jdvelasq.github.io/fuzzy-expert/
   smurf_data.json consists of data from 4 smurfing players in 20 specific matches
   normal_data.json consists of data from 72 normal players in those matches
   Following the label in test.py, our data is allocated like this:
   win : the field win in object wl_20
   kda: the field kda in object stats_20
   xp_per_min: the field xp_per_min in object stats_20
   gold_per_min: the field gold_per_min in object stats_20
   hero_damage: the field hero_damage in object stats_20
   
