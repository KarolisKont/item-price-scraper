from typing import Optional

from itemloaders.processors import MapCompose, TakeFirst
from price_parser.parser import Price
from scrapy.loader import ItemLoader


def _get_price(price_raw: str) -> Optional[float]:
    return Price.fromstring(price_raw).amount_float


def _get_currency(price_raw: str) -> Optional[str]:
    return Price.fromstring(price_raw).currency


class BaseScrapyItemLoader(ItemLoader):  # type: ignore
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    price_in = MapCompose(str.strip, _get_price)
    price_out = TakeFirst()

    currency_in = MapCompose(str.strip, _get_currency)
    currency_out = TakeFirst()
