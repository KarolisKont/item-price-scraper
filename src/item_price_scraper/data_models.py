from typing import Optional

import scrapy
from pydantic import BaseModel, HttpUrl


class PriceXPaths(BaseModel):
    promotion: Optional[str] = None
    regular: str


class ItemInputInfo(BaseModel):
    name: str
    url: HttpUrl
    price_xpaths: PriceXPaths


class ItemOutputInfo(scrapy.Item):  # type: ignore
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
