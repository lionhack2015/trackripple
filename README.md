##What we have right now

  - scrapping script that returns all the blog urls on hypem
  - running empty database instance on AWS

##Algorithm design

- user uploads soundcloud link to his track and specifies three genres he relates his track to;
- link is uploaded to echonest, set of parameters returned;
- these parameters are compared with the parameter benchmarks for three user-specified genres; closest match is defined as a leading genre;
- all blogs are subset to those who write about leading genre;
- we access all the songs from each blog from this subset that are falling into the leading genre category;
  - calculate distance from uploaded song to each of the songs from a certain blog;
  - average the results and store it as a proxy for song conformity with this blog's style;
  - rank current subset of blogs by this average distance to uploaded song ascendingly;
- return top 5 results as the target for song distribution.

__PROBLEM:__ What we gonna call 'distance'? Euclidian distance?

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
