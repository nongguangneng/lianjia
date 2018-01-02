from lianjia.items import HouseItem


class MyPipeline(object):

    def process_item(self, item, spider):
        print(item)