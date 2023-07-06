from pydantic_core._pydantic_core import Url
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from item_price_scraper.data_models import ItemInputInfo, PriceXPaths
from item_price_scraper.spiders.item_price import ItemPriceSpider

i1 = ItemInputInfo(
    name="Vans Old School",
    url=Url("https://eavalyne.lt/p/kedai-vans-old-skool-vn000d3hy28-black-white"),
    price_xpaths=PriceXPaths(
        promotion="//div[@class='final-price promotional']/text()",
        regular="//div[@class='final-price']/text()",
    ),
)

i2 = ItemInputInfo(
    name="Vitamix Explorian E310",
    url=Url(
        (
            "https://www.zaliavalgis.lt/lt/smulkintuvai-blenderiai/vitamix-smulkintuvai-blenderiai"
            "/vitamix-explorian-e310-smulkintuvas-blenderis-juodos-spalvos.html"
        )
    ),
    price_xpaths=PriceXPaths(
        regular="//div[@class='data-rows']//span[@class='price']/text()",
    ),
)

i3 = ItemInputInfo(
    name="New Balance Tevo",
    url=Url("https://eavalyne.lt/p/laisvalaikio-batai-new-balance-mr530zel-pilka"),
    price_xpaths=PriceXPaths(
        promotion="//div[@class='final-price promotional']/text()",
        regular="//div[@class='final-price']/text()",
    ),
)

i4 = ItemInputInfo(
    name="Dyson V11",
    url=Url(
        (
            "https://www.novastar.lt/namu-prieziuros-technika/dulkiu-siurbliai"
            "/dulkiu-siurbliai-sluotos/v11totalclean/dulkiu-siurblys-dyson-v11-total-clean"
        )
    ),
    price_xpaths=PriceXPaths(
        regular="//div[@class='pricing-block__price']//span[@class='price__original']/text()",
    ),
)

if __name__ == "__main__":
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(crawler_or_spidercls=ItemPriceSpider, items=[i1, i2, i3, i4])
    process.start()
