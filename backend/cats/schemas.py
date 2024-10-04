from pydantic import BaseModel, Field


class SCats(BaseModel):
	name: str = Field(...)
	breed: str = Field(...)
	age: int = Field(..., ge=0)
	color: str = Field(...)
	description: str = Field(...)


class SFilterCats(BaseModel):
    id: int