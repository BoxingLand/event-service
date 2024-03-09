from uuid import UUID

from pydantic import BaseModel


class ClubInfo(BaseModel):
    id: UUID
    name: str

    def to_dict(self):
        d = self.model_dump()
        if self.id:
            d['id'] = str(self.id)
        return d

class Club(BaseModel):
    id: UUID
    name: str
    about: str

    def to_dict(self):
        d = self.model_dump()
        if self.id:
            d['id'] = str(self.id)
        return d
