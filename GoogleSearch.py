from scrap import *

class ScrapeGoogle(WebScraper):
    def __init__(self, driver_path, options=None):
            super().__init__(driver_path, options)
    
    def return_list_urls(self, keyword,SiteName):
        try:
            search = keyword.replace(' ', '+')
            url = (f"https://www.google.com/search?q={search}+{SiteName}")
            data = self.scrape_data(url)           
            class_name = 'yuRUbf'
            elements = self.driver.find_elements_by_class_name(class_name)
            list_url = []   
            for element in elements:
                url = element.find_element_by_tag_name('a').get_attribute('href')
                list_url.append(url)
            return list_url
        except Exception as e:
            pass
    
    def find_proper_link(self,keyword,SiteName):
        list_urls = self.return_list_urls(keyword, SiteName)
        for url in list_urls:
            if SiteName in url[:25]:
                return url
        return None



