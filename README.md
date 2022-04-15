# Smurfing_player_detection_dota2
Detect smurfing players in dota2 using fuzzy logic approach
User Tutorial:
   Test.py requires python3.9 with fuzzy-expert pacakge installed: https://jdvelasq.github.io/fuzzy-expert/ , view the tutorials for more information<br />
   run test.py in the command line as python3.9 test.py<br />
   smurf_data.json consists of data from 4 smurfing players in 20 specific matches<br />
   normal_data.json consists of data from 72 normal players in those matches<br />
   Following the label in test.py, our data is allocated like this:<br />
   win : the field win in object wl_20<br />
   kda: the field kda in object stats_20<br />
   xp_per_min: the field xp_per_min in object stats_20<br />
   gold_per_min: the field gold_per_min in object stats_20<br />
   hero_damage: the field hero_damage in object stats_20<br />
   
