# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json

from itemadapter import ItemAdapter  # type: ignore

# TODO: create a pipeline that would remove items that don't have prices and
# would log about that.


class ManoScrapyPipeline:
    def open_spider(self, spider):  # type: ignore
        self.file = open("items.jl", "a")

    def close_spider(self, spider):  # type: ignore
        self.file.close()

    def process_item(self, item, spider):  # type: ignore
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
