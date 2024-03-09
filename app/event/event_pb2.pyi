from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateClubRequest(_message.Message):
    __slots__ = ("coach_id", "name", "about")
    COACH_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    coach_id: str
    name: str
    about: str
    def __init__(self, coach_id: _Optional[str] = ..., name: _Optional[str] = ..., about: _Optional[str] = ...) -> None: ...

class CreateClubResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AddCoachToClubRequest(_message.Message):
    __slots__ = ("coach_id", "club_id")
    COACH_ID_FIELD_NUMBER: _ClassVar[int]
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    coach_id: str
    club_id: str
    def __init__(self, coach_id: _Optional[str] = ..., club_id: _Optional[str] = ...) -> None: ...

class AddCoachToClubResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RemoveCoachToClubRequest(_message.Message):
    __slots__ = ("coach_id", "club_id")
    COACH_ID_FIELD_NUMBER: _ClassVar[int]
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    coach_id: str
    club_id: str
    def __init__(self, coach_id: _Optional[str] = ..., club_id: _Optional[str] = ...) -> None: ...

class RemoveCoachToClubResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateClubRequest(_message.Message):
    __slots__ = ("club_id", "name", "about")
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    club_id: str
    name: str
    about: str
    def __init__(self, club_id: _Optional[str] = ..., name: _Optional[str] = ..., about: _Optional[str] = ...) -> None: ...

class UpdateClubResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DeleteClubRequest(_message.Message):
    __slots__ = ("club_id", "coach_id")
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    COACH_ID_FIELD_NUMBER: _ClassVar[int]
    club_id: str
    coach_id: str
    def __init__(self, club_id: _Optional[str] = ..., coach_id: _Optional[str] = ...) -> None: ...

class DeleteClubResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetClubIDByNameRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetClubIDByNameResponse(_message.Message):
    __slots__ = ("club_id",)
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    club_id: str
    def __init__(self, club_id: _Optional[str] = ...) -> None: ...

class GetClubByNameRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetClubByIDRequest(_message.Message):
    __slots__ = ("club_id",)
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    club_id: str
    def __init__(self, club_id: _Optional[str] = ...) -> None: ...

class GetClubResponse(_message.Message):
    __slots__ = ("id", "name", "about")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    about: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., about: _Optional[str] = ...) -> None: ...

class GetClubsRequest(_message.Message):
    __slots__ = ("page", "page_size")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetClubsResponse(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetClubCoachesIDRequest(_message.Message):
    __slots__ = ("club_id",)
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    club_id: str
    def __init__(self, club_id: _Optional[str] = ...) -> None: ...

class GetClubCoachesIDResponse(_message.Message):
    __slots__ = ("coach_id",)
    COACH_ID_FIELD_NUMBER: _ClassVar[int]
    coach_id: str
    def __init__(self, coach_id: _Optional[str] = ...) -> None: ...

class CreateCompetitionRequest(_message.Message):
    __slots__ = ("name", "about", "price", "date", "prize_pool", "limit_boxers", "country", "region", "city", "organizer_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PRIZE_POOL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BOXERS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    about: str
    price: float
    date: str
    prize_pool: float
    limit_boxers: int
    country: str
    region: str
    city: str
    organizer_id: str
    def __init__(self, name: _Optional[str] = ..., about: _Optional[str] = ..., price: _Optional[float] = ..., date: _Optional[str] = ..., prize_pool: _Optional[float] = ..., limit_boxers: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ..., organizer_id: _Optional[str] = ...) -> None: ...

class CreateCompetitionResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AddBoxerToCompetitionRequest(_message.Message):
    __slots__ = ("boxer_id", "competition_id")
    BOXER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    boxer_id: str
    competition_id: str
    def __init__(self, boxer_id: _Optional[str] = ..., competition_id: _Optional[str] = ...) -> None: ...

class AddBoxerToCompetitionResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RemoveBoxerToCompetitionRequest(_message.Message):
    __slots__ = ("boxer_id", "competition_id")
    BOXER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    boxer_id: str
    competition_id: str
    def __init__(self, boxer_id: _Optional[str] = ..., competition_id: _Optional[str] = ...) -> None: ...

class RemoveBoxerToCompetitionResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateCompetitionRequest(_message.Message):
    __slots__ = ("competition_id", "name", "about", "price", "date", "prize_pool", "limit_boxers", "country", "region", "city")
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PRIZE_POOL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BOXERS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    competition_id: str
    name: str
    about: str
    price: float
    date: str
    prize_pool: float
    limit_boxers: int
    country: str
    region: str
    city: str
    def __init__(self, competition_id: _Optional[str] = ..., name: _Optional[str] = ..., about: _Optional[str] = ..., price: _Optional[float] = ..., date: _Optional[str] = ..., prize_pool: _Optional[float] = ..., limit_boxers: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class UpdateCompetitionResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DeleteCompetitionRequest(_message.Message):
    __slots__ = ("competition_id",)
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    competition_id: str
    def __init__(self, competition_id: _Optional[str] = ...) -> None: ...

class DeleteCompetitionResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetCompetitionsRequest(_message.Message):
    __slots__ = ("price", "date", "prize_pool", "limit_boxers", "country", "region", "city", "page", "page_size")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PRIZE_POOL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BOXERS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    price: float
    date: str
    prize_pool: float
    limit_boxers: int
    country: str
    region: str
    city: str
    page: int
    page_size: int
    def __init__(self, price: _Optional[float] = ..., date: _Optional[str] = ..., prize_pool: _Optional[float] = ..., limit_boxers: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetCompetitionsResponse(_message.Message):
    __slots__ = ("id", "name", "date", "country", "region", "city")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    date: str
    country: str
    region: str
    city: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., date: _Optional[str] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class GetCompetitionByNameRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCompetitionByIDRequest(_message.Message):
    __slots__ = ("competition_id",)
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    competition_id: str
    def __init__(self, competition_id: _Optional[str] = ...) -> None: ...

class GetCompetitionResponse(_message.Message):
    __slots__ = ("id", "name", "about", "price", "date", "prize_pool", "limit_boxers", "country", "region", "city")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PRIZE_POOL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BOXERS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    about: str
    price: float
    date: str
    prize_pool: float
    limit_boxers: int
    country: str
    region: str
    city: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., about: _Optional[str] = ..., price: _Optional[float] = ..., date: _Optional[str] = ..., prize_pool: _Optional[float] = ..., limit_boxers: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class CreateFightRequest(_message.Message):
    __slots__ = ("competition_id", "fighter_one", "fighter_two", "date")
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    FIGHTER_ONE_FIELD_NUMBER: _ClassVar[int]
    FIGHTER_TWO_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    competition_id: str
    fighter_one: str
    fighter_two: str
    date: str
    def __init__(self, competition_id: _Optional[str] = ..., fighter_one: _Optional[str] = ..., fighter_two: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class CreateFightResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SetWinnerRequest(_message.Message):
    __slots__ = ("id", "winner")
    ID_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    id: str
    winner: str
    def __init__(self, id: _Optional[str] = ..., winner: _Optional[str] = ...) -> None: ...

class SetWinnerResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetFightsCompetitionRequest(_message.Message):
    __slots__ = ("competition_id",)
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    competition_id: str
    def __init__(self, competition_id: _Optional[str] = ...) -> None: ...

class GetFightResponse(_message.Message):
    __slots__ = ("fights_id", "fighter_one", "fighter_two", "winner", "date")
    FIGHTS_ID_FIELD_NUMBER: _ClassVar[int]
    FIGHTER_ONE_FIELD_NUMBER: _ClassVar[int]
    FIGHTER_TWO_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    fights_id: str
    fighter_one: str
    fighter_two: str
    winner: str
    date: str
    def __init__(self, fights_id: _Optional[str] = ..., fighter_one: _Optional[str] = ..., fighter_two: _Optional[str] = ..., winner: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class GetFightsBoxerRequest(_message.Message):
    __slots__ = ("boxer_id", "competition_id", "date")
    BOXER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPETITION_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    boxer_id: str
    competition_id: str
    date: str
    def __init__(self, boxer_id: _Optional[str] = ..., competition_id: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class GetFightScoreRequest(_message.Message):
    __slots__ = ("fight_id",)
    FIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    fight_id: str
    def __init__(self, fight_id: _Optional[str] = ...) -> None: ...

class GetFightScoreResponse(_message.Message):
    __slots__ = ("id", "score_value", "judge_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    JUDGE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    score_value: str
    judge_id: str
    def __init__(self, id: _Optional[str] = ..., score_value: _Optional[str] = ..., judge_id: _Optional[str] = ...) -> None: ...
