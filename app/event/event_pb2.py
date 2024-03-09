# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65vent.proto\x12\x05\x65vent\"Q\n\x11\x43reateClubRequest\x12\x10\n\x08\x63oach_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\x05\x61\x62out\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_about\" \n\x12\x43reateClubResponse\x12\n\n\x02id\x18\x01 \x01(\t\":\n\x15\x41\x64\x64\x43oachToClubRequest\x12\x10\n\x08\x63oach_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63lub_id\x18\x02 \x01(\t\")\n\x16\x41\x64\x64\x43oachToClubResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"=\n\x18RemoveCoachToClubRequest\x12\x10\n\x08\x63oach_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63lub_id\x18\x02 \x01(\t\",\n\x19RemoveCoachToClubResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"^\n\x11UpdateClubRequest\x12\x0f\n\x07\x63lub_id\x18\x01 \x01(\t\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x61\x62out\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\x08\n\x06_about\"%\n\x12UpdateClubResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"6\n\x11\x44\x65leteClubRequest\x12\x0f\n\x07\x63lub_id\x18\x01 \x01(\t\x12\x10\n\x08\x63oach_id\x18\x02 \x01(\t\"%\n\x12\x44\x65leteClubResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"&\n\x16GetClubIDByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"*\n\x17GetClubIDByNameResponse\x12\x0f\n\x07\x63lub_id\x18\x01 \x01(\t\"$\n\x14GetClubByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x12GetClubByIDRequest\x12\x0f\n\x07\x63lub_id\x18\x01 \x01(\t\"I\n\x0fGetClubResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\x05\x61\x62out\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_about\"2\n\x0fGetClubsRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\",\n\x10GetClubsResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"*\n\x17GetClubCoachesIDRequest\x12\x0f\n\x07\x63lub_id\x18\x01 \x01(\t\",\n\x18GetClubCoachesIDResponse\x12\x10\n\x08\x63oach_id\x18\x01 \x01(\t\"\x8b\x02\n\x18\x43reateCompetitionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x05\x61\x62out\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05price\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x17\n\nprize_pool\x18\x05 \x01(\x02H\x02\x88\x01\x01\x12\x19\n\x0climit_boxers\x18\x06 \x01(\x05H\x03\x88\x01\x01\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12\x0e\n\x06region\x18\x08 \x01(\t\x12\x0c\n\x04\x63ity\x18\t \x01(\t\x12\x14\n\x0corganizer_id\x18\n \x01(\tB\x08\n\x06_aboutB\x08\n\x06_priceB\r\n\x0b_prize_poolB\x0f\n\r_limit_boxers\"\'\n\x19\x43reateCompetitionResponse\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x1c\x41\x64\x64\x42oxerToCompetitionRequest\x12\x10\n\x08\x62oxer_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63ompetition_id\x18\x02 \x01(\t\"0\n\x1d\x41\x64\x64\x42oxerToCompetitionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"K\n\x1fRemoveBoxerToCompetitionRequest\x12\x10\n\x08\x62oxer_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63ompetition_id\x18\x02 \x01(\t\"3\n RemoveBoxerToCompetitionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xd8\x02\n\x18UpdateCompetitionRequest\x12\x16\n\x0e\x63ompetition_id\x18\x01 \x01(\t\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x61\x62out\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05price\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x11\n\x04\x64\x61te\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x17\n\nprize_pool\x18\x06 \x01(\x02H\x04\x88\x01\x01\x12\x19\n\x0climit_boxers\x18\x07 \x01(\x05H\x05\x88\x01\x01\x12\x14\n\x07\x63ountry\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x13\n\x06region\x18\t \x01(\tH\x07\x88\x01\x01\x12\x11\n\x04\x63ity\x18\n \x01(\tH\x08\x88\x01\x01\x42\x07\n\x05_nameB\x08\n\x06_aboutB\x08\n\x06_priceB\x07\n\x05_dateB\r\n\x0b_prize_poolB\x0f\n\r_limit_boxersB\n\n\x08_countryB\t\n\x07_regionB\x07\n\x05_city\",\n\x19UpdateCompetitionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"2\n\x18\x44\x65leteCompetitionRequest\x12\x16\n\x0e\x63ompetition_id\x18\x01 \x01(\t\",\n\x19\x44\x65leteCompetitionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xa5\x02\n\x16GetCompetitionsRequest\x12\x12\n\x05price\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x11\n\x04\x64\x61te\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nprize_pool\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x19\n\x0climit_boxers\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x14\n\x07\x63ountry\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x13\n\x06region\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x11\n\x04\x63ity\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x0c\n\x04page\x18\x08 \x01(\x05\x12\x11\n\tpage_size\x18\t \x01(\x05\x42\x08\n\x06_priceB\x07\n\x05_dateB\r\n\x0b_prize_poolB\x0f\n\r_limit_boxersB\n\n\x08_countryB\t\n\x07_regionB\x07\n\x05_city\"p\n\x17GetCompetitionsResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x0e\n\x06region\x18\x07 \x01(\t\x12\x0c\n\x04\x63ity\x18\x08 \x01(\t\"+\n\x1bGetCompetitionByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"3\n\x19GetCompetitionByIDRequest\x12\x16\n\x0e\x63ompetition_id\x18\x01 \x01(\t\"\xff\x01\n\x16GetCompetitionResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\x05\x61\x62out\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05price\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x17\n\nprize_pool\x18\x06 \x01(\x02H\x02\x88\x01\x01\x12\x19\n\x0climit_boxers\x18\x07 \x01(\x05H\x03\x88\x01\x01\x12\x0f\n\x07\x63ountry\x18\x08 \x01(\t\x12\x0e\n\x06region\x18\t \x01(\t\x12\x0c\n\x04\x63ity\x18\n \x01(\tB\x08\n\x06_aboutB\x08\n\x06_priceB\r\n\x0b_prize_poolB\x0f\n\r_limit_boxers\"d\n\x12\x43reateFightRequest\x12\x16\n\x0e\x63ompetition_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ighter_one\x18\x02 \x01(\t\x12\x13\n\x0b\x66ighter_two\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\"&\n\x13\x43reateFightResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\".\n\x10SetWinnerRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06winner\x18\x02 \x01(\t\"$\n\x11SetWinnerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x1bGetFightsCompetitionRequest\x12\x16\n\x0e\x63ompetition_id\x18\x01 \x01(\t\"m\n\x10GetFightResponse\x12\x11\n\tfights_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ighter_one\x18\x02 \x01(\t\x12\x13\n\x0b\x66ighter_two\x18\x03 \x01(\t\x12\x0e\n\x06winner\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\"u\n\x15GetFightsBoxerRequest\x12\x10\n\x08\x62oxer_id\x18\x01 \x01(\t\x12\x1b\n\x0e\x63ompetition_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04\x64\x61te\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x11\n\x0f_competition_idB\x07\n\x05_date\"(\n\x14GetFightScoreRequest\x12\x10\n\x08\x66ight_id\x18\x01 \x01(\t\"J\n\x15GetFightScoreResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bscore_value\x18\x02 \x01(\t\x12\x10\n\x08judge_id\x18\x03 \x01(\t2\x9a\x0e\n\x05\x45vent\x12\x43\n\nCreateClub\x12\x18.event.CreateClubRequest\x1a\x19.event.CreateClubResponse\"\x00\x12O\n\x0e\x41\x64\x64\x43oachToClub\x12\x1c.event.AddCoachToClubRequest\x1a\x1d.event.AddCoachToClubResponse\"\x00\x12X\n\x11RemoveCoachToClub\x12\x1f.event.RemoveCoachToClubRequest\x1a .event.RemoveCoachToClubResponse\"\x00\x12\x43\n\nUpdateClub\x12\x18.event.UpdateClubRequest\x1a\x19.event.UpdateClubResponse\"\x00\x12\x43\n\nDeleteClub\x12\x18.event.DeleteClubRequest\x1a\x19.event.DeleteClubResponse\"\x00\x12R\n\x0fGetClubIDByName\x12\x1d.event.GetClubIDByNameRequest\x1a\x1e.event.GetClubIDByNameResponse\"\x00\x12\x46\n\rGetClubByName\x12\x1b.event.GetClubByNameRequest\x1a\x16.event.GetClubResponse\"\x00\x12\x42\n\x0bGetClubByID\x12\x19.event.GetClubByIDRequest\x1a\x16.event.GetClubResponse\"\x00\x12?\n\x08GetClubs\x12\x16.event.GetClubsRequest\x1a\x17.event.GetClubsResponse\"\x00\x30\x01\x12W\n\x10GetClubCoachesID\x12\x1e.event.GetClubCoachesIDRequest\x1a\x1f.event.GetClubCoachesIDResponse\"\x00\x30\x01\x12X\n\x11\x43reateCompetition\x12\x1f.event.CreateCompetitionRequest\x1a .event.CreateCompetitionResponse\"\x00\x12\x64\n\x15\x41\x64\x64\x42oxerToCompetition\x12#.event.AddBoxerToCompetitionRequest\x1a$.event.AddBoxerToCompetitionResponse\"\x00\x12m\n\x18RemoveBoxerToCompetition\x12&.event.RemoveBoxerToCompetitionRequest\x1a\'.event.RemoveBoxerToCompetitionResponse\"\x00\x12X\n\x11UpdateCompetition\x12\x1f.event.UpdateCompetitionRequest\x1a .event.UpdateCompetitionResponse\"\x00\x12X\n\x11\x44\x65leteCompetition\x12\x1f.event.DeleteCompetitionRequest\x1a .event.DeleteCompetitionResponse\"\x00\x12T\n\x0fGetCompetitions\x12\x1d.event.GetCompetitionsRequest\x1a\x1e.event.GetCompetitionsResponse\"\x00\x30\x01\x12Y\n\x14GetCompetitionByName\x12 .event.GetCompetitionByIDRequest\x1a\x1d.event.GetCompetitionResponse\"\x00\x12W\n\x12GetCompetitionByID\x12 .event.GetCompetitionByIDRequest\x1a\x1d.event.GetCompetitionResponse\"\x00\x12H\n\x0b\x43reateFight\x12\x19.event.CreateFightRequest\x1a\x1a.event.CreateFightResponse\"\x00(\x01\x12@\n\tSetWinner\x12\x17.event.SetWinnerRequest\x1a\x18.event.SetWinnerResponse\"\x00\x12W\n\x14GetFightsCompetition\x12\".event.GetFightsCompetitionRequest\x1a\x17.event.GetFightResponse\"\x00\x30\x01\x12K\n\x0eGetFightsBoxer\x12\x1c.event.GetFightsBoxerRequest\x1a\x17.event.GetFightResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATECLUBREQUEST']._serialized_start=22
  _globals['_CREATECLUBREQUEST']._serialized_end=103
  _globals['_CREATECLUBRESPONSE']._serialized_start=105
  _globals['_CREATECLUBRESPONSE']._serialized_end=137
  _globals['_ADDCOACHTOCLUBREQUEST']._serialized_start=139
  _globals['_ADDCOACHTOCLUBREQUEST']._serialized_end=197
  _globals['_ADDCOACHTOCLUBRESPONSE']._serialized_start=199
  _globals['_ADDCOACHTOCLUBRESPONSE']._serialized_end=240
  _globals['_REMOVECOACHTOCLUBREQUEST']._serialized_start=242
  _globals['_REMOVECOACHTOCLUBREQUEST']._serialized_end=303
  _globals['_REMOVECOACHTOCLUBRESPONSE']._serialized_start=305
  _globals['_REMOVECOACHTOCLUBRESPONSE']._serialized_end=349
  _globals['_UPDATECLUBREQUEST']._serialized_start=351
  _globals['_UPDATECLUBREQUEST']._serialized_end=445
  _globals['_UPDATECLUBRESPONSE']._serialized_start=447
  _globals['_UPDATECLUBRESPONSE']._serialized_end=484
  _globals['_DELETECLUBREQUEST']._serialized_start=486
  _globals['_DELETECLUBREQUEST']._serialized_end=540
  _globals['_DELETECLUBRESPONSE']._serialized_start=542
  _globals['_DELETECLUBRESPONSE']._serialized_end=579
  _globals['_GETCLUBIDBYNAMEREQUEST']._serialized_start=581
  _globals['_GETCLUBIDBYNAMEREQUEST']._serialized_end=619
  _globals['_GETCLUBIDBYNAMERESPONSE']._serialized_start=621
  _globals['_GETCLUBIDBYNAMERESPONSE']._serialized_end=663
  _globals['_GETCLUBBYNAMEREQUEST']._serialized_start=665
  _globals['_GETCLUBBYNAMEREQUEST']._serialized_end=701
  _globals['_GETCLUBBYIDREQUEST']._serialized_start=703
  _globals['_GETCLUBBYIDREQUEST']._serialized_end=740
  _globals['_GETCLUBRESPONSE']._serialized_start=742
  _globals['_GETCLUBRESPONSE']._serialized_end=815
  _globals['_GETCLUBSREQUEST']._serialized_start=817
  _globals['_GETCLUBSREQUEST']._serialized_end=867
  _globals['_GETCLUBSRESPONSE']._serialized_start=869
  _globals['_GETCLUBSRESPONSE']._serialized_end=913
  _globals['_GETCLUBCOACHESIDREQUEST']._serialized_start=915
  _globals['_GETCLUBCOACHESIDREQUEST']._serialized_end=957
  _globals['_GETCLUBCOACHESIDRESPONSE']._serialized_start=959
  _globals['_GETCLUBCOACHESIDRESPONSE']._serialized_end=1003
  _globals['_CREATECOMPETITIONREQUEST']._serialized_start=1006
  _globals['_CREATECOMPETITIONREQUEST']._serialized_end=1273
  _globals['_CREATECOMPETITIONRESPONSE']._serialized_start=1275
  _globals['_CREATECOMPETITIONRESPONSE']._serialized_end=1314
  _globals['_ADDBOXERTOCOMPETITIONREQUEST']._serialized_start=1316
  _globals['_ADDBOXERTOCOMPETITIONREQUEST']._serialized_end=1388
  _globals['_ADDBOXERTOCOMPETITIONRESPONSE']._serialized_start=1390
  _globals['_ADDBOXERTOCOMPETITIONRESPONSE']._serialized_end=1438
  _globals['_REMOVEBOXERTOCOMPETITIONREQUEST']._serialized_start=1440
  _globals['_REMOVEBOXERTOCOMPETITIONREQUEST']._serialized_end=1515
  _globals['_REMOVEBOXERTOCOMPETITIONRESPONSE']._serialized_start=1517
  _globals['_REMOVEBOXERTOCOMPETITIONRESPONSE']._serialized_end=1568
  _globals['_UPDATECOMPETITIONREQUEST']._serialized_start=1571
  _globals['_UPDATECOMPETITIONREQUEST']._serialized_end=1915
  _globals['_UPDATECOMPETITIONRESPONSE']._serialized_start=1917
  _globals['_UPDATECOMPETITIONRESPONSE']._serialized_end=1961
  _globals['_DELETECOMPETITIONREQUEST']._serialized_start=1963
  _globals['_DELETECOMPETITIONREQUEST']._serialized_end=2013
  _globals['_DELETECOMPETITIONRESPONSE']._serialized_start=2015
  _globals['_DELETECOMPETITIONRESPONSE']._serialized_end=2059
  _globals['_GETCOMPETITIONSREQUEST']._serialized_start=2062
  _globals['_GETCOMPETITIONSREQUEST']._serialized_end=2355
  _globals['_GETCOMPETITIONSRESPONSE']._serialized_start=2357
  _globals['_GETCOMPETITIONSRESPONSE']._serialized_end=2469
  _globals['_GETCOMPETITIONBYNAMEREQUEST']._serialized_start=2471
  _globals['_GETCOMPETITIONBYNAMEREQUEST']._serialized_end=2514
  _globals['_GETCOMPETITIONBYIDREQUEST']._serialized_start=2516
  _globals['_GETCOMPETITIONBYIDREQUEST']._serialized_end=2567
  _globals['_GETCOMPETITIONRESPONSE']._serialized_start=2570
  _globals['_GETCOMPETITIONRESPONSE']._serialized_end=2825
  _globals['_CREATEFIGHTREQUEST']._serialized_start=2827
  _globals['_CREATEFIGHTREQUEST']._serialized_end=2927
  _globals['_CREATEFIGHTRESPONSE']._serialized_start=2929
  _globals['_CREATEFIGHTRESPONSE']._serialized_end=2967
  _globals['_SETWINNERREQUEST']._serialized_start=2969
  _globals['_SETWINNERREQUEST']._serialized_end=3015
  _globals['_SETWINNERRESPONSE']._serialized_start=3017
  _globals['_SETWINNERRESPONSE']._serialized_end=3053
  _globals['_GETFIGHTSCOMPETITIONREQUEST']._serialized_start=3055
  _globals['_GETFIGHTSCOMPETITIONREQUEST']._serialized_end=3108
  _globals['_GETFIGHTRESPONSE']._serialized_start=3110
  _globals['_GETFIGHTRESPONSE']._serialized_end=3219
  _globals['_GETFIGHTSBOXERREQUEST']._serialized_start=3221
  _globals['_GETFIGHTSBOXERREQUEST']._serialized_end=3338
  _globals['_GETFIGHTSCOREREQUEST']._serialized_start=3340
  _globals['_GETFIGHTSCOREREQUEST']._serialized_end=3380
  _globals['_GETFIGHTSCORERESPONSE']._serialized_start=3382
  _globals['_GETFIGHTSCORERESPONSE']._serialized_end=3456
  _globals['_EVENT']._serialized_start=3459
  _globals['_EVENT']._serialized_end=5277
# @@protoc_insertion_point(module_scope)
