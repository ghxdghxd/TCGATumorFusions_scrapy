# -*- coding: utf-8 -*-
import scrapy
from TumorFusions.items import TumorfusionsItem

class TumorfusionsSpiderSpider(scrapy.Spider):
    name = 'TumorFusions_spider'
    allowed_domains = ['tumorfusions.org']
    cancer_list = ['BRCA', 'COAD', 'ESCA', "GBM", "KIRC", "LIHC", "LUAD", "OV", "PRAD", "STAD", "THCA", "UCEC",
                   'ACC', "BLCA", "CESC", "CHOL", "DLBC", "HNSC", "KICH", "KIRP", "LAML", "LGG", "LUSC", "MESO", "PAAD",
                   "PCPG", "READ", "SARC", "SKCM", "TGCT", "THYM", "UCS", "UVM"]
    start_urls = ["https://tumorfusions.org/Fusions!cancerType?cancerType=" +
                  str(x) for x in cancer_list]  # 入口url
    def parse(self, response):
        # table_list = response.xpath('//div[@id="Content Box Content"]/div[6]/section/table[2]/tbody/tr')
        table_list = response.xpath('//*[@id="fusions"]/tbody/tr')
        # print(table_list[1::2])
        for t_item in table_list:
            table_item = TumorfusionsItem()
            table_item['Cancer'] = t_item.xpath(".//td[1]//text()").extract_first()
            table_item['TCGA_sampleID'] = t_item.xpath(".//td[2]//text()").extract_first()
            table_item['FusionPair'] = t_item.xpath(".//td[3]//text()").extract_first()
            table_item['E_value'] = t_item.xpath(".//td[4]//text()").extract_first()
            table_item['Tier'] = t_item.xpath(".//td[5]//text()").extract_first()
            table_item['Frame'] = t_item.xpath(".//td[6]//text()").extract_first()
            table_item['phosphorylation'] = t_item.xpath(".//td[7]//text()").extract_first()
            table_item['ubiquitination'] = t_item.xpath(".//td[8]//text()").extract_first()
            table_item['WGS'] = t_item.xpath(".//td[9]//text()").extract_first()
            # print(table_item)
            yield table_item
