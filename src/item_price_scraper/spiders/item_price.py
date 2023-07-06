from typing import Any, Generator, List

from scrapy import Spider
from scrapy.http import Request, Response

from item_price_scraper.data_models import ItemInputInfo, ItemOutputInfo, PriceXPaths
from item_price_scraper.item_loaders import BaseScrapyItemLoader


class ItemPriceSpider(Spider):  # type: ignore
    name: str = "item_price"

    def __init__(self, items: List[ItemInputInfo], *args: Any, **kwargs: Any) -> None:
        super(ItemPriceSpider, self).__init__(*args, **kwargs)
        self.items = items

    def start_requests(self) -> Generator[Request, None, None]:
        for item in self.items:
            yield Request(
                url=str(item.url),
                meta={"name": item.name, "price_xpaths": item.price_xpaths},
                callback=self.parse,
            )

    def parse(self, response: Response) -> Generator[Any, None, None]:
        item_loader = BaseScrapyItemLoader(item=ItemOutputInfo(), response=response)
        item_loader.add_value("name", response.meta["name"])
        item_loader.add_value("url", response.url)

        price_xpaths: PriceXPaths = response.meta["price_xpaths"]
        if price_xpaths.promotion:
            item_loader.add_xpath("price", price_xpaths.promotion)
            item_loader.add_xpath("currency", price_xpaths.promotion)

        item_loader.add_xpath("price", price_xpaths.regular)
        item_loader.add_xpath("currency", price_xpaths.regular)

        yield item_loader.load_item()
