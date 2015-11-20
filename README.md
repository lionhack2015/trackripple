What we have right now:

  - scrapping script that returns all the blogs on hypem with a certain set of parameters that we can extract directly from hypem.
  - running empty database instance on AWS

##PRODUCTION ROADMAP

- UI design and development (expand on this further)
- Creating SQL-schema for db and creating necessary tables and relations
- Scrapping all the blog pages from hypem (all 797 entries)
- Writing script for populating __Blogs__ table
- Writing script for retreiving soundcloud links from blog page, running them through Echonest API and pushing results to __Songs__ table
- Associating songs with Genres somehow (we need template echonest patterns for all genres we have)
- Connecting frontend with backend (query for most relevant blogs for uploaded song)

##Thoughts on Blogs table

First bunch of parameters — country and genre: inhereted from aggregated pages under "Blogs" category on hypem
Second bunch - parameters that can be extracted from the individual page about the blog on hypem. EXample: http://hypem.com/blog/all+things+go/552
What we can get from there:
  - # of tracks
  - # of followers (proxy for popularity)
  - recent genres
  - some keywords from the "Latest posts from" section (suggestion: sort by "Most favorites")
