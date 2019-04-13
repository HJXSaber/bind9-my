
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'POLICY ALGORITHM_POLICY ZONE ALGORITHM DIRECTORY KEYTTL KEY_SIZE ROLL_PERIOD PRE_PUBLISH POST_PUBLISH COVERAGE STANDBY NONE DATESUFFIX KEYTYPE ALGNAME STR QSTRING NUMBER LBRACE RBRACE SEMIpolicylist : init policy\n                      | policylist policyinit :policy : alg_policy\n                  | zone_policy\n                  | named_policyname : STR\n                | KEYTYPE\n                | DATESUFFIXdomain : STR\n                  | QSTRING\n                  | KEYTYPE\n                  | DATESUFFIXnew_policy :alg_policy : ALGORITHM_POLICY ALGNAME new_policy alg_option_group SEMIzone_policy : ZONE domain new_policy policy_option_group SEMInamed_policy : POLICY name new_policy policy_option_group SEMIduration : NUMBERduration : NONEduration : NUMBER DATESUFFIXpolicy_option_group : LBRACE policy_option_list RBRACEpolicy_option_list : policy_option SEMI\n                              | policy_option_list policy_option SEMIpolicy_option : parent_option\n                         | directory_option\n                         | coverage_option\n                         | rollperiod_option\n                         | prepublish_option\n                         | postpublish_option\n                         | keysize_option\n                         | algorithm_option\n                         | keyttl_option\n                         | standby_optionalg_option_group : LBRACE alg_option_list RBRACEalg_option_list : alg_option SEMI\n                           | alg_option_list alg_option SEMIalg_option : coverage_option\n                      | rollperiod_option\n                      | prepublish_option\n                      | postpublish_option\n                      | keyttl_option\n                      | keysize_option\n                      | standby_optionparent_option : POLICY namedirectory_option : DIRECTORY QSTRINGcoverage_option : COVERAGE durationrollperiod_option : ROLL_PERIOD KEYTYPE durationprepublish_option : PRE_PUBLISH KEYTYPE durationpostpublish_option : POST_PUBLISH KEYTYPE durationkeysize_option : KEY_SIZE KEYTYPE NUMBERstandby_option : STANDBY KEYTYPE NUMBERkeyttl_option : KEYTTL durationalgorithm_option : ALGORITHM ALGNAME'
    
_lr_action_items = {'STR':([3,4,40,],[14,19,14,]),'STANDBY':([25,27,42,57,63,80,85,88,],[31,31,31,31,-22,-35,-23,-36,]),'ROLL_PERIOD':([25,27,42,57,63,80,85,88,],[32,32,32,32,-22,-35,-23,-36,]),'NUMBER':([44,45,64,65,66,67,77,],[74,74,81,74,83,74,74,]),'KEY_SIZE':([25,27,42,57,63,80,85,88,],[33,33,33,33,-22,-35,-23,-36,]),'NONE':([44,45,65,67,77,],[73,73,73,73,73,]),'SEMI':([12,13,14,24,26,28,30,34,36,37,38,39,43,47,48,49,50,53,54,55,56,58,59,60,61,68,69,70,71,72,73,74,75,76,78,79,81,82,83,84,86,87,],[-8,-9,-7,29,52,62,63,-29,-31,-30,-25,-33,-32,-26,-28,-27,-24,-40,-42,-43,-41,-37,80,-39,-38,-44,-53,85,-21,-52,-19,-18,-46,-45,-34,88,-51,-47,-50,-48,-20,-49,]),'PRE_PUBLISH':([25,27,42,57,63,80,85,88,],[35,35,35,35,-22,-35,-23,-36,]),'POLICY':([0,1,2,5,7,8,9,10,25,29,42,52,62,63,85,],[-3,3,3,-4,-5,-2,-6,-1,40,-17,40,-16,-15,-22,-23,]),'$end':([1,5,7,8,9,10,29,52,62,],[0,-4,-5,-2,-6,-1,-17,-16,-15,]),'RBRACE':([42,57,63,80,85,88,],[71,78,-22,-35,-23,-36,]),'ALGORITHM':([25,42,63,85,],[41,41,-22,-23,]),'DATESUFFIX':([3,4,40,74,],[13,17,13,86,]),'KEYTTL':([25,27,42,57,63,80,85,88,],[44,44,44,44,-22,-35,-23,-36,]),'COVERAGE':([25,27,42,57,63,80,85,88,],[45,45,45,45,-22,-35,-23,-36,]),'DIRECTORY':([25,42,63,85,],[46,46,-22,-23,]),'LBRACE':([11,12,13,14,15,16,17,18,19,20,21,22,23,],[-14,-8,-9,-7,-14,-12,-13,-11,-10,-14,25,25,27,]),'ZONE':([0,1,2,5,7,8,9,10,29,52,62,],[-3,4,4,-4,-5,-2,-6,-1,-17,-16,-15,]),'ALGORITHM_POLICY':([0,1,2,5,7,8,9,10,29,52,62,],[-3,6,6,-4,-5,-2,-6,-1,-17,-16,-15,]),'KEYTYPE':([3,4,31,32,33,35,40,51,],[12,16,64,65,66,67,12,77,]),'QSTRING':([4,46,],[18,76,]),'ALGNAME':([6,41,],[20,69,]),'POST_PUBLISH':([25,27,42,57,63,80,85,88,],[51,51,51,51,-22,-35,-23,-36,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'domain':([4,],[15,]),'policy_option':([25,42,],[30,70,]),'zone_policy':([1,2,],[7,7,]),'duration':([44,45,65,67,77,],[72,75,82,84,87,]),'postpublish_option':([25,27,42,57,],[34,53,34,53,]),'policylist':([0,],[1,]),'algorithm_option':([25,42,],[36,36,]),'keysize_option':([25,27,42,57,],[37,54,37,54,]),'directory_option':([25,42,],[38,38,]),'init':([0,],[2,]),'standby_option':([25,27,42,57,],[39,55,39,55,]),'policy':([1,2,],[8,10,]),'new_policy':([11,15,20,],[21,22,23,]),'coverage_option':([25,27,42,57,],[47,58,47,58,]),'alg_policy':([1,2,],[5,5,]),'policy_option_list':([25,],[42,]),'keyttl_option':([25,27,42,57,],[43,56,43,56,]),'alg_option_list':([27,],[57,]),'policy_option_group':([21,22,],[24,26,]),'name':([3,40,],[11,68,]),'alg_option_group':([23,],[28,]),'alg_option':([27,57,],[59,79,]),'prepublish_option':([25,27,42,57,],[48,60,48,60,]),'rollperiod_option':([25,27,42,57,],[49,61,49,61,]),'parent_option':([25,42,],[50,50,]),'named_policy':([1,2,],[9,9,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> policylist","S'",1,None,None,None),
  ('policylist -> init policy','policylist',2,'p_policylist','policy.py',523),
  ('policylist -> policylist policy','policylist',2,'p_policylist','policy.py',524),
  ('init -> <empty>','init',0,'p_init','policy.py',528),
  ('policy -> alg_policy','policy',1,'p_policy','policy.py',532),
  ('policy -> zone_policy','policy',1,'p_policy','policy.py',533),
  ('policy -> named_policy','policy',1,'p_policy','policy.py',534),
  ('name -> STR','name',1,'p_name','policy.py',538),
  ('name -> KEYTYPE','name',1,'p_name','policy.py',539),
  ('name -> DATESUFFIX','name',1,'p_name','policy.py',540),
  ('domain -> STR','domain',1,'p_domain','policy.py',545),
  ('domain -> QSTRING','domain',1,'p_domain','policy.py',546),
  ('domain -> KEYTYPE','domain',1,'p_domain','policy.py',547),
  ('domain -> DATESUFFIX','domain',1,'p_domain','policy.py',548),
  ('new_policy -> <empty>','new_policy',0,'p_new_policy','policy.py',555),
  ('alg_policy -> ALGORITHM_POLICY ALGNAME new_policy alg_option_group SEMI','alg_policy',5,'p_alg_policy','policy.py',559),
  ('zone_policy -> ZONE domain new_policy policy_option_group SEMI','zone_policy',5,'p_zone_policy','policy.py',566),
  ('named_policy -> POLICY name new_policy policy_option_group SEMI','named_policy',5,'p_named_policy','policy.py',573),
  ('duration -> NUMBER','duration',1,'p_duration_1','policy.py',579),
  ('duration -> NONE','duration',1,'p_duration_2','policy.py',584),
  ('duration -> NUMBER DATESUFFIX','duration',2,'p_duration_3','policy.py',589),
  ('policy_option_group -> LBRACE policy_option_list RBRACE','policy_option_group',3,'p_policy_option_group','policy.py',608),
  ('policy_option_list -> policy_option SEMI','policy_option_list',2,'p_policy_option_list','policy.py',612),
  ('policy_option_list -> policy_option_list policy_option SEMI','policy_option_list',3,'p_policy_option_list','policy.py',613),
  ('policy_option -> parent_option','policy_option',1,'p_policy_option','policy.py',617),
  ('policy_option -> directory_option','policy_option',1,'p_policy_option','policy.py',618),
  ('policy_option -> coverage_option','policy_option',1,'p_policy_option','policy.py',619),
  ('policy_option -> rollperiod_option','policy_option',1,'p_policy_option','policy.py',620),
  ('policy_option -> prepublish_option','policy_option',1,'p_policy_option','policy.py',621),
  ('policy_option -> postpublish_option','policy_option',1,'p_policy_option','policy.py',622),
  ('policy_option -> keysize_option','policy_option',1,'p_policy_option','policy.py',623),
  ('policy_option -> algorithm_option','policy_option',1,'p_policy_option','policy.py',624),
  ('policy_option -> keyttl_option','policy_option',1,'p_policy_option','policy.py',625),
  ('policy_option -> standby_option','policy_option',1,'p_policy_option','policy.py',626),
  ('alg_option_group -> LBRACE alg_option_list RBRACE','alg_option_group',3,'p_alg_option_group','policy.py',630),
  ('alg_option_list -> alg_option SEMI','alg_option_list',2,'p_alg_option_list','policy.py',634),
  ('alg_option_list -> alg_option_list alg_option SEMI','alg_option_list',3,'p_alg_option_list','policy.py',635),
  ('alg_option -> coverage_option','alg_option',1,'p_alg_option','policy.py',639),
  ('alg_option -> rollperiod_option','alg_option',1,'p_alg_option','policy.py',640),
  ('alg_option -> prepublish_option','alg_option',1,'p_alg_option','policy.py',641),
  ('alg_option -> postpublish_option','alg_option',1,'p_alg_option','policy.py',642),
  ('alg_option -> keyttl_option','alg_option',1,'p_alg_option','policy.py',643),
  ('alg_option -> keysize_option','alg_option',1,'p_alg_option','policy.py',644),
  ('alg_option -> standby_option','alg_option',1,'p_alg_option','policy.py',645),
  ('parent_option -> POLICY name','parent_option',2,'p_parent_option','policy.py',649),
  ('directory_option -> DIRECTORY QSTRING','directory_option',2,'p_directory_option','policy.py',653),
  ('coverage_option -> COVERAGE duration','coverage_option',2,'p_coverage_option','policy.py',657),
  ('rollperiod_option -> ROLL_PERIOD KEYTYPE duration','rollperiod_option',3,'p_rollperiod_option','policy.py',661),
  ('prepublish_option -> PRE_PUBLISH KEYTYPE duration','prepublish_option',3,'p_prepublish_option','policy.py',668),
  ('postpublish_option -> POST_PUBLISH KEYTYPE duration','postpublish_option',3,'p_postpublish_option','policy.py',675),
  ('keysize_option -> KEY_SIZE KEYTYPE NUMBER','keysize_option',3,'p_keysize_option','policy.py',682),
  ('standby_option -> STANDBY KEYTYPE NUMBER','standby_option',3,'p_standby_option','policy.py',689),
  ('keyttl_option -> KEYTTL duration','keyttl_option',2,'p_keyttl_option','policy.py',696),
  ('algorithm_option -> ALGORITHM ALGNAME','algorithm_option',2,'p_algorithm_option','policy.py',700),
]
