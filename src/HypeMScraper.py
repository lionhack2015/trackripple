from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DATA_DIR = "../data/"
    
def scrape_country_url(url):
 
    # Load WebDriver and navigate to the page url.
    # This will open a browser window.
    driver = webdriver.Firefox()
    driver.get(url)
     
    urls = []
 
    # First click on More Blogs button to launch infinite scroll 
    # and then scroll to the end of the table by sending Page Down keypresses to
    # the browser window.
    try:
        driver.find_element_by_id('more-blog-scroll').click()
    except:
        pass

    i = 0
    while i < 100:
        # Find the first element on the page, so we can scroll down using the
        # element object's send_keys() method
        elem = driver.find_element_by_tag_name('a')
        elem.send_keys(Keys.PAGE_DOWN)
        i += 1
        
    # Once the whole table has loaded, grab all the visible links.    
    blog_divs = driver.find_elements_by_class_name('directory-blog')
    for blog in blog_divs:
        link = blog.find_element_by_xpath('.//a')
        urls.append(link.get_attribute('href'))
         
    driver.quit()
           
    return urls

def scrape_countries():
    driver = webdriver.Firefox()
    driver.get('http://hypem.com/blogs')
     
    urls = []
    
    country_containers = driver.find_elements_by_id('directory-countries')
    
    for tag in country_containers:
        links = tag.find_elements_by_xpath('.//li/a')
        for link in links:
            urls.append(link.get_attribute('href'))
        
    driver.quit()

    return urls


def scrape_each_blog(url):
    driver = webdriver.Firefox()
    driver.get(url)

    # blog link
    blog_link = driver.find_elements_by_class_name('visit-blog')[0].find_element_by_xpath('.//a').get_attribute('href')

    # get blog genres
    genres_ul = driver.find_element_by_css_selector(".tags.small")
    genres_list = []
    for tl in genres_ul.find_elements_by_tag_name('li'):
       genres_list.append(tl.text)

    big_nums =  driver.find_elements_by_xpath("//span[@class='big-num']")
    # tracks
    track_num = big_nums[0].text

    # followers
    followers_num = big_nums[1].text

    # recent soundcloud music links
    sc_links = []
    # TODO: resolve this to acutal sound cloud links
    sc_links.append(driver.find_element_by_class_name("icon-sc").get_attribute("href"))
    play = driver.find_element_by_id("playerPlay").click()

    sng_cnt = 0
    while sng_cnt < 100:
        try:
            next = driver.find_element_by_id("playerNext").click()
            sc_links.append(driver.find_element_by_class_name("icon-sc").get_attribute("href"))
            sng_cnt = sng_cnt + 1
        except:
            break

    driver.quit()
    return (blog_link, genres_list, track_num, followers_num, sc_links)


#blg_list_us = scrape_url("http://hypem.com/blogs/country/US")
#scrape_each_blog("http://hypem.com/blog/abduction+radiation/21500")

def persist_in_text_files():
    country_wise_urls = scrape_countries()

    f = open(DATA_DIR+"countrywise_blog_links.txt", "w")
    f_list = open(DATA_DIR+"countrywise_blog_list.txt", "w")
    f_blg = open(DATA_DIR+"blog_features.txt", "w")

    for c_url in country_wise_urls:
        country = c_url.split("/")[-1]
        f_list.write(country+" "+c_url+"\n")

        blog_list = scrape_country_url(c_url)

        # scrape each blog_link for blog characterisitcs
        for bl in blog_list:
            # persist
            f.write(country+" "+bl+"\n")
            blg_id = bl.split("/")[-1]
            (blog_link, genres_list, track_num, followers_num, sc_links) = scrape_each_blog(bl)
            # persist
            f_blg.write(blg_id+" "+'|'.join(genres_list)+
                    " "+track_num+" "+followers_num+" "+'|'.join(sc_links))


    f.close()
    f_list.close()
    f_blg.close()

if __name__ == "__main__":
    persist_in_text_files()




