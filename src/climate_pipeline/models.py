from pydantic import BaseModel, Field, field_validator

class NamedRef(BaseModel):
    id: str
    value: str

class WorldBankModel(BaseModel):
    countryiso3code: str
    date: int
    country: NamedRef
    indicator: NamedRef
    value: float | None = Field(ge=0)

class MaunaLoaRecord(BaseModel):
    year: int = Field(ge=1900, le=2100)
    month: int = Field(ge=1, le=12)
    decimal_date: float = Field(alias="decimal date")
    average: float = Field(ge=100, le=10000)
    deseasonalized: float = Field(ge=250, le=1000)
    ndays: int = Field(ge=-1, le=31)
    sdev: float = Field(ge=-9.99)
    unc: float = Field(ge=-0.99)

class GistempRecord(BaseModel):
    Year: int = Field(ge=1880,le=2100)
    Jan: float | None = Field(ge=-2,le=4)
    Feb: float | None = Field(ge=-2,le=4)
    Mar: float | None = Field(ge=-2,le=4)
    Apr: float | None = Field(ge=-2,le=4)
    May: float | None = Field(ge=-2,le=4)
    Jun: float | None = Field(ge=-2,le=4)
    Jul: float | None = Field(ge=-2,le=4)
    Aug: float | None = Field(ge=-2,le=4)
    Sep: float | None = Field(ge=-2,le=4)
    Oct: float | None = Field(ge=-2,le=4)
    Nov: float | None = Field(ge=-2,le=4)
    Dec: float | None = Field(ge=-2,le=4)
    JtoD: float | None = Field(ge=-2,le=4,alias="J-D")
    DtoN: float | None = Field(ge=-2,le=4,alias="D-N")
    DJF: float | None = Field(ge=-2,le=4)
    MAM: float | None = Field(ge=-2,le=4)
    JJA: float | None = Field(ge=-2,le=4)
    SON: float | None = Field(ge=-2,le=4)

    @field_validator("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
                     "JtoD", "DtoN", "DJF", "MAM", "JJA", "SON", mode="before")
    @classmethod
    def stars_to_none(cls, v):
        if v == "***":
            return None
        return v

    

    


